#!/usr/bin/env python3
"""Build the Forecast Farms website.

Outputs:
  ghl/   one paste-ready file per page for GoHighLevel Custom Code elements
  docs/  the demo website served by GitHub Pages

Run:  python build.py
"""
import json, os, re, shutil, struct, sys, runpy, tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, BUILD = os.path.join(ROOT, 'src'), os.path.join(ROOT, 'src', 'build')
GHL, DOCS, IMAGES, ARCHIVE = (os.path.join(ROOT, d) for d in ('ghl', 'docs', 'images', 'archive'))

V1_BAR = ('<div style="position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:9999;'
          'display:flex;flex-wrap:wrap;justify-content:center;gap:6px 14px;align-items:center;'
          'padding:10px 18px;background:#341C32;color:#EFEDEC;font:500 14px/1.3 system-ui,sans-serif;'
          'border-radius:999px;box-shadow:0 10px 30px rgba(0,0,0,.25);max-width:calc(100% - 32px)">'
          'Original design (v1)<a href="../{page}" style="color:#F3E2F5">See the new design &rarr;</a></div>')

# (path, builder output, page title, meta description)
PAGES = [
    ('', None, 'Forecast Farms | Hunter, Jumper & Equitation Training in Marshall, VA',
     'Individualized Hunter, Jumper and Equitation training for junior and adult riders and their horses in Marshall, Virginia.'),
    ('contact-us', 'forecast-farms-evaluation-ghl.html', 'Schedule an Evaluation Lesson | Forecast Farms',
     'Every new rider and horse starts with an evaluation lesson. Request yours at Forecast Farms in Marshall, Virginia.'),
    ('rider-training', 'forecast-farms-rider-training-ghl.html', 'Rider Training | Hunter, Jumper & Equitation Lessons, Marshall VA',
     'Private and semi-private Hunter, Jumper and Equitation lessons for junior and adult riders, on your own horse or one of our schoolmasters.'),
    ('training', 'forecast-farms-horse-training-ghl.html', 'Horse Training | Forecast Farms, Marshall VA',
     'Correct, consistent schooling for young, green and experienced horses and ponies, from the trainer who also coaches you.'),
    ('horse-rider-development', 'forecast-farms-horse-rider-ghl.html', 'Horse + Rider Development | Forecast Farms',
     'One plan for horse and rider: lessons, training rides and season goals for pairs with competition goals.'),
    ('lessons', 'forecast-farms-junior-riding-club-ghl.html', 'Junior Riding Club, Ages 4–7 | Forecast Farms',
     'Safe, structured, confidence-building lessons for riders ages 4 to 7, with a level-by-level curriculum.'),
    ('sales', 'forecast-farms-sales-ghl.html', 'Horses for Sale & Lease | Forecast Farms',
     'Horse search, sales, leasing and consignment from Forecast Farms in Marshall, Virginia.'),
    ('about-us', 'forecast-farms-about-ghl.html', 'About Forecast Farms | Family-Owned Training in Marshall, VA',
     'Family-owned Hunter, Jumper and Equitation training on Atoka Road in Marshall, Virginia, led by trainer Denise Finch.'),
    ('privacy-policy', 'forecast-farms-privacy-ghl.html', 'Privacy Policy | Forecast Farms',
     'How Forecast Farms collects, uses and protects the information you share through forecastfarms.com.'),
    ('terms-and-conditions', 'forecast-farms-terms-ghl.html', 'Terms & Conditions | Forecast Farms',
     'The terms that apply when you use forecastfarms.com.'),
]
BUILDERS = ['legal_build.py', 'eval_build.py', 'rider_build.py', 'pages_build.py']

# Phone-sized copies of each photo in images/ (NAME-800.jpg etc.), served with srcset.
CARD_PHOTOS = ('schoolmaster-', 'denise-')
WIDTHS = {'hero': (800, 1200), 'card': (600, 900)}
SIZES = {'hero': '(min-width: 960px) 55vw, 100vw', 'card': '(min-width: 960px) 40vw, 100vw'}
GHL_URLS = os.path.join(IMAGES, 'ghl-urls.json')

# Where GitHub Pages serves the demo. Change to '/' if a custom domain is added.
DEMO_BASE = '/forecast-farms-website/'

NOT_FOUND = '''<main id="main">
<section class="section" aria-labelledby="nf-title">
  <div class="wrap">
    <p class="eyebrow">Page not found</p>
    <h1 id="nf-title" style="font-size:clamp(2.6rem,1.8rem + 3vw,4.25rem);line-height:1.04;letter-spacing:-.02em;font-weight:350;max-width:14ch">This page <em>isn’t here.</em></h1>
    <p class="lede" style="margin-top:1.25rem">The page you’re looking for may have moved. Start from the homepage, or schedule an evaluation lesson.</p>
    <div class="hero-ctas">
      <a class="btn" href="index.html">Go to the Homepage</a>
      <a class="btn btn-ghost" href="contact-us.html">Schedule an Evaluation</a>
    </div>
  </div>
</section>
</main>'''

FORM_LIVE = 'Thank you. Your request is in, and we will be in touch to schedule your evaluation lesson.'
FORM_DEMO = ('Thank you. This is a preview site, so requests are not sent yet. '
             'To schedule now, call (540) 274-1541 or email info@forecastfarms.com.')


def jpeg_width(path):
    data = open(path, 'rb').read()
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        if data[i + 1] in (0xC0, 0xC1, 0xC2):
            return struct.unpack('>H', data[i + 7:i + 9])[0]
        i += 2 + struct.unpack('>H', data[i + 2:i + 4])[0]
    return None


def kind(name):
    return 'card' if name.startswith(CARD_PHOTOS) else 'hero'


def masters():
    if not os.path.isdir(IMAGES):
        return []
    return sorted(f[:-4] for f in os.listdir(IMAGES)
                  if f.endswith('.jpg') and not re.search(r'-\d+\.jpg$', f))


def make_sizes():
    """Create missing phone-sized copies. Needs Pillow; without it pages fall back to the full-size photo."""
    try:
        from PIL import Image
    except ImportError:
        return
    for name in masters():
        src = os.path.join(IMAGES, name + '.jpg')
        for w in WIDTHS[kind(name)]:
            out = os.path.join(IMAGES, f'{name}-{w}.jpg')
            if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
                continue
            im = Image.open(src).convert('RGB')
            if im.width <= w:
                continue
            im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(
                out, 'JPEG', quality=78, optimize=True, progressive=True)


# GHL's own image service (used by the GHL site builder) resizes and converts photos in GHL Media.
GHL_IMG = 'https://images.leadconnectorhq.com/image/f_webp/q_80/r_{w}/u_{url}'
GHL_WIDTHS = {'hero': (800, 1200, 1600), 'card': (600, 900, 1200)}
# Homepage photos already in GHL Media, by media id: how wide each one shows.
CDN_SIZES = {
    '6adcc7799c1511d5b99c0f59': SIZES['hero'],
    '6adcc77936aa4a07e89fa346': '(min-width: 900px) 30vw, (min-width: 700px) 45vw, 100vw',
    '6adcc7799c1511d5b99c0f50': '(min-width: 900px) 30vw, (min-width: 700px) 45vw, 100vw',
    '6adcc779d542268bb4fef806': '(min-width: 900px) 30vw, (min-width: 700px) 45vw, 100vw',
    '6adc546bd542268bb4f4f358': '(min-width: 960px) 45vw, 100vw',
    '6aded14d736386d0dcd54e14': '100vw',
}
# If a smaller copy fails to load, drop srcset so the browser falls back to the original photo.
SAFE_ONERROR = 'onerror="if(this.srcset){this.removeAttribute(\'srcset\')}else{this.remove()}"'


def ghl_set(url, widths):
    return ', '.join(f'{GHL_IMG.format(w=w, url=url)} {w}w' for w in widths)


def responsive(html):
    """Add srcset to photos: local phone-sized copies for images/, GHL's image service for GHL Media.
    If images/ghl-urls.json maps a photo to its GHL Media URL, that URL is used instead of the local file."""
    urls = json.load(open(GHL_URLS, encoding='utf-8')) if os.path.exists(GHL_URLS) else {}

    def fix(m):
        tag = m.group(0)
        s = re.search(r' src="([^"]+)"', tag)
        if not s or ' srcset=' in tag:
            return tag
        src = s.group(1)
        local = re.fullmatch(r'images/([a-z0-9-]+)\.jpg', src)
        if local:
            name = local.group(1)
            k, mapped = kind(name), urls.get(name + '.jpg')
            sizes = SIZES[k]
            if mapped and 'filesafe.space' in mapped:
                new_src, sets = mapped, ghl_set(mapped, GHL_WIDTHS[k])
            else:
                full = os.path.join(IMAGES, name + '.jpg')
                files = [f'{name}-{w}.jpg' for w in WIDTHS[k] if os.path.exists(os.path.join(IMAGES, f'{name}-{w}.jpg'))]
                if not os.path.exists(full) or not files:
                    return tag
                pairs = [(f, f.rsplit('-', 1)[1][:-4]) for f in files] + [(name + '.jpg', jpeg_width(full))]
                sets = ', '.join(f'{urls.get(f) or "images/" + f} {w}w' for f, w in pairs)
                new_src = mapped or src
        elif 'assets.cdn.filesafe.space/' in src:
            mid = re.search(r'/media/([a-z0-9]+)\.', src)
            sizes = CDN_SIZES.get(mid.group(1) if mid else '', '100vw')
            new_src, sets = src, ghl_set(src, GHL_WIDTHS['hero'])
        else:
            return tag
        tag = tag.replace(f' src="{src}"', f' src="{new_src}" srcset="{sets}" sizes="{sizes}"', 1)
        return tag.replace('onerror="this.remove()"', SAFE_ONERROR)

    return re.sub(r'<img\b[^>]*>', fix, html)


def build_ghl():
    out = tempfile.mkdtemp(prefix='ff-build-')
    os.environ['FF_ROOT'], os.environ['FF_OUT'] = ROOT, out
    sys.path.insert(0, BUILD)
    try:
        for b in BUILDERS:
            runpy.run_path(os.path.join(BUILD, b), run_name='__main__')
        shutil.rmtree(GHL, ignore_errors=True)
        os.makedirs(GHL)
        for path, made, *_ in PAGES:
            name = (path or 'home') + '.html'
            src = os.path.join(SRC, 'home.html') if made is None else os.path.join(out, made)
            html = open(src, encoding='utf-8').read()
            open(os.path.join(GHL, name), 'w', encoding='utf-8').write(responsive(html))
    finally:
        shutil.rmtree(out, ignore_errors=True)


def demo_links(html):
    def repl(m):
        slug, rest = m.group(1), m.group(2) or ''
        return f'href="{(slug or "index") + ".html"}{rest}"'
    return re.sub(r'href="/([a-z0-9-]*)([?#][^"]*)?"', repl, html)


def build_docs():
    shutil.rmtree(DOCS, ignore_errors=True)
    os.makedirs(DOCS)
    for path, _, title, desc in PAGES:
        g = open(os.path.join(GHL, (path or 'home') + '.html'), encoding='utf-8').read()
        i = g.index('<div class="ff">')
        head, body = g[:i].strip(), g[i:]
        body = re.sub(r'\s*<!-- Paste your GHL External Tracking script.*?-->\s*', '\n', body)
        body = demo_links(body).replace(FORM_LIVE, FORM_DEMO)
        head = demo_links(head)
        doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<style>html,body{{margin:0;padding:0;background:#EEEDEC}}</style>
{head}
</head>
<body>
{body.strip()}
</body>
</html>
'''
        open(os.path.join(DOCS, (path or 'index') + '.html'), 'w', encoding='utf-8').write(doc)
    home = open(os.path.join(DOCS, 'index.html'), encoding='utf-8').read()
    nf = re.sub(r'<main id="main">.*?</main>', lambda m: NOT_FOUND, home, count=1, flags=re.S)
    nf = re.sub(r'<title>.*?</title>', '<title>Page Not Found | Forecast Farms</title>', nf, count=1)
    nf = nf.replace('href="#evaluation"', 'href="contact-us.html"').replace('href="#top"', 'href="index.html"').replace('href="#main"', 'href="index.html"')
    nf = nf.replace('<head>', f'<head>\n<base href="{DEMO_BASE}">', 1)
    open(os.path.join(DOCS, '404.html'), 'w', encoding='utf-8').write(nf)
    if os.path.isdir(IMAGES):
        shutil.copytree(IMAGES, os.path.join(DOCS, 'images'),
                        ignore=shutil.ignore_patterns('.gitkeep', 'README*', '*.json'))
    build_archive()
    open(os.path.join(DOCS, '.nojekyll'), 'w').close()


def build_archive():
    """Publish frozen earlier designs from archive/<version>/ at docs/<version>/, with a bar linking back."""
    if not os.path.isdir(ARCHIVE):
        return
    for ver in sorted(os.listdir(ARCHIVE)):
        src = os.path.join(ARCHIVE, ver)
        if not os.path.isdir(src):
            continue
        out = os.path.join(DOCS, ver)
        os.makedirs(out)
        for name in sorted(os.listdir(src)):
            if not name.endswith('.html'):
                continue
            doc = open(os.path.join(src, name), encoding='utf-8').read()
            doc = re.sub(r'<title>', f'<title>[{ver}] ', doc, count=1)
            doc = doc.replace('<body>', '<body>\n' + V1_BAR.format(page=name).replace('(v1)', f'({ver})'), 1)
            open(os.path.join(out, name), 'w', encoding='utf-8').write(doc)


if __name__ == '__main__':
    make_sizes()
    build_ghl()
    build_docs()
    print(f'Built {len(PAGES)} pages into ghl/ and docs/')
