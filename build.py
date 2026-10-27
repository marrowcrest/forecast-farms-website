#!/usr/bin/env python3
"""Build the Forecast Farms website.

Outputs:
  ghl/   one paste-ready file per page for GoHighLevel Custom Code elements
  docs/  the demo website served by GitHub Pages

Run:  python build.py
"""
import os, re, shutil, sys, runpy, tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, BUILD = os.path.join(ROOT, 'src'), os.path.join(ROOT, 'src', 'build')
GHL, DOCS, IMAGES = (os.path.join(ROOT, d) for d in ('ghl', 'docs', 'images'))

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

FORM_LIVE = 'Thank you. Your request is in, and we will be in touch to schedule your evaluation lesson.'
FORM_DEMO = ('Thank you. This is a preview site, so requests are not sent yet. '
             'To schedule now, call (540) 274-1541 or email info@forecastfarms.com.')


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
            shutil.copy(src, os.path.join(GHL, name))
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
    if os.path.isdir(IMAGES):
        shutil.copytree(IMAGES, os.path.join(DOCS, 'images'),
                        ignore=shutil.ignore_patterns('.gitkeep', 'README*'))
    open(os.path.join(DOCS, '.nojekyll'), 'w').close()


if __name__ == '__main__':
    build_ghl()
    build_docs()
    print(f'Built {len(PAGES)} pages into ghl/ and docs/')
