import re
import os
ROOT=os.environ.get('FF_ROOT') or os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
SRC=os.path.join(ROOT,'src','home.html')
TRAINING={'rider-training','training','horse-rider-development','lessons'}

def chrome(current=None,cta_href='/contact-us',cta_text=None,cta_external=False):
    g=open(SRC,encoding='utf-8').read()
    head=g[:g.index('<div class="ff">')].rstrip()
    header=re.search(r'<header class="site-header" id="top">.*?</header>',g,re.S).group(0)
    footer=re.search(r'<footer class="site-footer">.*?</footer>',g,re.S).group(0)
    script=re.search(r'<script>.*?</script>',g,re.S).group(0)
    track=g[g.index('</script>')+len('</script>'):].strip()
    header=header.replace('href="#top" aria-label="Forecast Farms, back to top"','href="/" aria-label="Forecast Farms home"')
    ext=' target="_blank" rel="noopener"' if cta_external else ''
    header=header.replace('href="#evaluation"',f'href="{cta_href}"{ext}')
    if cta_text:
        header=header.replace('>Schedule an Evaluation Lesson</a>',f'>{cta_text}</a>').replace('>Schedule an Evaluation</a>',f'>{cta_text}</a>')
    footer=footer.replace('href="#top"','href="/"')
    footer=footer.replace('href="#evaluation"',f'href="{cta_href}"{ext}')
    if current:
        a=f'<a href="/{current}">'
        if current in TRAINING:
            header=header.replace('class="nav-drop"','class="nav-drop is-current"',1)
        header=header.replace(a,f'<a href="/{current}" aria-current="page">')
        footer=footer.replace(a,f'<a href="/{current}" aria-current="page">')
    bad=[h for h in re.findall(r'href="(#[^"]*)"',header+footer) if h!=cta_href]
    assert not bad,(current,bad)
    return head,header,footer,script,track

PAGE_JS='''<script>
(()=>{
const HOME='/';
if(HOME!=='/'){document.querySelectorAll('.ff a[href^="/#"]').forEach(a=>a.setAttribute('href',HOME+a.getAttribute('href').slice(1)));document.querySelectorAll('.ff a[href="/"]').forEach(a=>a.setAttribute('href',HOME));}
})();
</script>'''

LIB_CSS='''
.ff .tri{display:grid;gap:2.5rem 3rem}
.ff .tri>*{min-width:0;padding-top:1.5rem;border-top:1px solid var(--line-strong)}
.ff .tri h3{margin-bottom:.75rem;font-size:clamp(1.5rem,1.3rem + .6vw,1.85rem)}
.ff .tri p{color:var(--fg-soft)}
@media (min-width:900px){.ff .tri{grid-template-columns:repeat(3,minmax(0,1fr))}.ff .tri--2{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ff .split{display:grid;gap:2.5rem 5rem;align-items:start}
.ff .split>*{min-width:0}
.ff .split h2{margin-bottom:1.25rem}
@media (min-width:960px){.ff .split{grid-template-columns:minmax(0,5fr) minmax(0,6fr)}}
.ff .ticks li{position:relative;padding:.9rem 0 .9rem 2rem;border-top:1px solid var(--line);color:var(--fg)}
.ff .ticks li:last-child{border-bottom:1px solid var(--line)}
.ff .ticks li::before{content:"";position:absolute;left:.1rem;top:1.25rem;width:.75rem;height:.4rem;border-left:2px solid var(--accent);border-bottom:2px solid var(--accent);transform:rotate(-45deg)}
.ff .ticks li span{display:block;font-size:.925rem;color:var(--fg-soft);margin-top:.15rem}
.ff .quote-solo blockquote p{font:italic 350 clamp(1.8rem,1.3rem + 2vw,3rem)/1.18 var(--serif);letter-spacing:-.01em;text-wrap:balance;max-width:30ch;color:var(--fg)}
.ff .quote-solo figcaption{margin-top:1.75rem;display:flex;flex-wrap:wrap;gap:.25rem 1rem;align-items:baseline}
.ff .faq-list{border-bottom:1px solid var(--line)}
.ff .faq-list details{border-top:1px solid var(--line)}
.ff .faq-list summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:baseline;gap:1.5rem;padding:1.2rem 0;font:400 clamp(1.15rem,1.05rem + .35vw,1.35rem)/1.35 var(--serif);color:var(--fg)}
.ff .faq-list summary::-webkit-details-marker{display:none}
.ff .faq-list summary::after{content:"+";flex:none;font:300 1.5rem/1 var(--sans);color:var(--accent)}
.ff .faq-list details[open] summary::after{content:"\\2212"}
.ff .faq-list summary:hover{color:var(--accent)}
.ff .faq-list details p{max-width:40em;padding-bottom:1.35rem;color:var(--fg-soft);line-height:1.7}
.ff .faq-list details a,.ff .lede a{color:var(--accent);text-underline-offset:3px}
.ff .cta-band .wrap{display:grid;gap:1.75rem 4rem;align-items:end}
.ff .cta-band h2{max-width:16ch}
.ff .cta-band p{color:var(--band-soft);max-width:32em;margin-top:1rem}
.ff .cta-actions{display:flex;flex-wrap:wrap;gap:.75rem}
.ff .cta-band .btn{background:var(--band-fg);border-color:var(--band-fg);color:var(--band)}
.ff .cta-band .btn:hover{background:transparent;color:var(--band-fg)}
.ff .cta-band .btn-ghost{background:transparent;color:var(--band-fg);border-color:var(--band-line)}
.ff .cta-band .btn-ghost:hover{border-color:var(--band-fg)}
@media (min-width:900px){.ff .cta-band .wrap{grid-template-columns:minmax(0,1fr) auto}}
.ff .sm{min-width:0;display:flex;flex-direction:column;gap:.6rem}
.ff .sm .ph{aspect-ratio:4/5;margin-bottom:.5rem}
.ff .sm-type,.ff .sm .sm-type{font:600 .7rem/1.35 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--saddle)}
.ff .sm h3{font-size:1.6rem}
.ff .sm p{font-size:.925rem;color:var(--fg-soft)}
'''

HOSTILE='<style>body{margin:0;font-family:Times;color:red}h2{color:blue}p{font-size:22px}.c-section{padding:40px 15px}.c-row{max-width:1170px;margin:0 auto;padding:0 15px}.c-el{overflow:hidden}</style>'

def assemble(head,css,header,body,footer,script,track,extra_js=PAGE_JS):
    return f'''{head.replace('</style>',css+'</style>')}
<div class="ff">
<a class="skip" href="#main">Skip to content</a>

{header}

{body}

{footer}
</div>

{script}
{extra_js}
{track}
'''

def write(fname,preview,title,page,test):
    open(fname,'w',encoding='utf-8').write(page)
