import re,sys,os
sys.path.insert(0,os.path.dirname(__file__))
from legal_copy import PRIVACY,TERMS,PHONE,EMAIL,UPDATED
os.chdir(os.environ['FF_OUT'])
from ffchrome import chrome
_h,header,footer,script,track=chrome()
head=_h

css='''
.ff .legal-hero{background:var(--bg-lilac);padding-block:clamp(3.25rem,2.25rem + 4vw,6rem) clamp(2.75rem,2rem + 3vw,4.5rem)}
.ff .legal-hero h1{font-size:clamp(2.6rem,1.8rem + 3vw,4.25rem);line-height:1.04;letter-spacing:-.02em;font-weight:350;max-width:14ch}
.ff .legal-hero .lede{margin-top:1.25rem}
.ff .legal-meta{display:flex;flex-wrap:wrap;gap:.5rem 1.75rem;margin-top:1.5rem;font-size:.875rem;color:var(--fg-soft)}
.ff .legal-meta strong{color:var(--fg);font-weight:600}
.ff .glance{display:grid;gap:1rem;margin-top:2.5rem}
.ff .glance li{padding:1.1rem 1.25rem;background:var(--surface);border-top:2px solid var(--accent);border-radius:2px;font-size:.95rem;line-height:1.55;color:var(--fg)}
.ff .glance-title{margin-top:2.75rem;font:600 .7rem/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--saddle)}
.ff .glance-title+.glance{margin-top:.9rem}
@media (min-width:900px){.ff .glance{grid-template-columns:repeat(3,minmax(0,1fr))}}
.ff .section.legal{padding-top:clamp(3rem,2rem + 3vw,5rem)}
.ff .legal-grid{display:grid;gap:2rem 5rem}
.ff .legal-grid>*{min-width:0}
@media (min-width:1000px){.ff .legal-grid{grid-template-columns:15rem minmax(0,1fr)}}
.ff .toc{align-self:start}
@media (min-width:1000px){.ff .toc{position:sticky;top:calc(72px + 2rem)}}
.ff .toc summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;padding:.9rem 1rem;background:var(--surface);border:1px solid var(--line);border-radius:2px;font:600 .7rem/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--saddle)}
.ff .toc summary::-webkit-details-marker{display:none}
.ff .toc summary::after{content:"+";font:400 1.25rem/1 var(--sans);letter-spacing:0;color:var(--fg-soft)}
.ff .toc details[open] summary::after{content:"\\2212"}
.ff .toc ol{counter-reset:toc;margin-top:.75rem}
.ff .toc li{counter-increment:toc}
.ff .toc a{display:grid;grid-template-columns:1.9rem minmax(0,1fr);padding:.5rem 0;border-top:1px solid var(--line);font-size:.9rem;line-height:1.4;text-decoration:none;color:var(--fg-soft);transition:color .2s}
.ff .toc li:first-child a{border-top:0}
.ff .toc a::before{content:counter(toc);color:var(--muted);font-variant-numeric:tabular-nums}
.ff .toc a:hover,.ff .toc a.is-current{color:var(--accent)}
.ff .toc a.is-current::before{color:var(--accent)}
@media (min-width:1000px){.ff .toc summary{pointer-events:none;padding:0 0 .5rem;background:none;border:0;border-bottom:1px solid var(--line-strong);border-radius:0}.ff .toc summary::after{display:none}}
.ff .legal-body{max-width:44rem}
.ff .legal-body>section{padding-block:2.25rem;border-top:1px solid var(--line);scroll-margin-top:96px}
.ff .legal-body>section:first-child{padding-top:0;border-top:0}
.ff .legal-body h2{display:flex;align-items:baseline;gap:.85rem;margin-bottom:1rem;font-size:clamp(1.5rem,1.3rem + .7vw,1.9rem)}
.ff .legal-body h2 .n{flex:none;min-width:1.6rem;font:500 .9rem/1 var(--sans);color:var(--accent);font-variant-numeric:tabular-nums}
.ff .legal-body p,.ff .legal-body li{color:var(--fg-soft);line-height:1.75}
.ff .legal-body p+p,.ff .legal-body ul+p,.ff .legal-body p+ul{margin-top:1rem}
.ff .legal-body ul{display:grid;gap:.45rem}
.ff .legal-body ul li{position:relative;padding-left:1.4rem}
.ff .legal-body ul li::before{content:"";position:absolute;left:.15rem;top:.72em;width:.4rem;height:.4rem;border-radius:50%;background:var(--accent)}
.ff .legal-body strong{color:var(--fg);font-weight:600}
.ff .legal-body a{color:var(--accent);text-decoration:underline;text-underline-offset:3px;overflow-wrap:anywhere}
.ff .legal-body .callout{margin-top:1.25rem;padding:1.1rem 1.25rem;background:var(--bg-lilac);border-left:2px solid var(--accent);color:var(--fg)}
.ff .legal-contact{margin-top:.5rem;padding:clamp(1.5rem,3vw,2.25rem);background:var(--surface);border-radius:2px}
.ff .legal-contact h2{margin-bottom:.4rem}
.ff .legal-contact>p{color:var(--fg-soft)}
.ff .legal-contact dl{margin-top:1.25rem;border-bottom:1px solid var(--line)}
.ff .legal-contact dl>div{display:grid;grid-template-columns:5.5rem minmax(0,1fr);gap:1rem;padding-block:.75rem;border-top:1px solid var(--line)}
.ff .legal-contact dt{font:600 .7rem/1.7 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--fg-soft)}
.ff .legal-contact dd{color:var(--fg)}
.ff .legal-contact dd a{color:var(--fg);text-decoration-color:var(--line-strong);text-underline-offset:4px;overflow-wrap:anywhere}
.ff .foot-base a[aria-current="page"]{color:var(--foot-fg)}
'''
assert head.count('</style>')==1
head_l=head.replace('</style>',css+'</style>')

legal_js='''<script>
(()=>{
const HOME='/';
if(HOME!=='/'){document.querySelectorAll('.ff a[href^="/#"]').forEach(a=>a.setAttribute('href',HOME+a.getAttribute('href').slice(1)));document.querySelectorAll('.ff a[href="/"]').forEach(a=>a.setAttribute('href',HOME));}
const d=document.querySelector('.ff .toc details');if(!d)return;
const wide=window.matchMedia('(min-width:1000px)');
const fit=()=>{if(wide.matches)d.open=true;};fit();
if(wide.addEventListener)wide.addEventListener('change',fit);
d.addEventListener('click',e=>{if(e.target.closest('a')&&!wide.matches)d.open=false;});
const links=[...d.querySelectorAll('a')],secs=links.map(a=>document.getElementById(a.getAttribute('href').slice(1))).filter(Boolean);
if(!('IntersectionObserver' in window)||!secs.length)return;
const io=new IntersectionObserver(es=>{es.forEach(en=>{if(en.isIntersecting){links.forEach(a=>a.classList.toggle('is-current',a.getAttribute('href')==='#'+en.target.id));}});},{rootMargin:'-100px 0px -65% 0px'});
secs.forEach(s=>io.observe(s));
})();
</script>'''

def page(doc):
    secs=doc['sections']
    toc='\n'.join(f'            <li><a href="#{sid}">{t}</a></li>' for sid,t,_ in secs+[('contact','Contact us','')])
    body='\n'.join(f'''        <section id="{sid}" aria-labelledby="{sid}-h">
          <h2 id="{sid}-h"><span class="n">{i:02d}</span>{t}</h2>
          {html}
        </section>''' for i,(sid,t,html) in enumerate(secs,1))
    n=len(secs)+1
    glance='\n'.join(f'      <li>{x}</li>' for x in doc['glance'])
    foot=footer.replace(f'<a href="/{doc["slug"]}">',f'<a href="/{doc["slug"]}" aria-current="page">')
    return f'''{head_l}
<div class="ff">
<a class="skip" href="#main">Skip to content</a>

{header}

<main id="main">
<section class="legal-hero" aria-labelledby="legal-title">
  <div class="wrap">
    <p class="eyebrow">Legal</p>
    <h1 id="legal-title">{doc['title']}</h1>
    <p class="lede">{doc['lede']}</p>
    <p class="legal-meta"><span><strong>Last updated</strong> {UPDATED}</span><span><strong>Applies to</strong> forecastfarms.com</span></p>
    <p class="glance-title">At a glance</p>
    <ul class="glance">
{glance}
    </ul>
  </div>
</section>

<section class="section legal" aria-label="{doc['title']} details">
  <div class="wrap legal-grid">
    <nav class="toc" aria-label="On this page">
      <details>
        <summary>On this page</summary>
        <ol>
{toc}
        </ol>
      </details>
    </nav>
    <div class="legal-body">
{body}
        <section id="contact" aria-labelledby="contact-h">
          <div class="legal-contact">
            <h2 id="contact-h"><span class="n">{n:02d}</span>Contact us</h2>
            <p>{doc['contact_title']} Get in touch and we will respond as soon as we can.</p>
            <dl>
              <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
              <div><dt>Phone</dt><dd><a href="tel:+15402741541">{PHONE}</a></dd></div>
              <div><dt>Mail</dt><dd>Forecast Farms Inc.<br>2497 Atoka Road, Marshall, VA 20115</dd></div>
            </dl>
          </div>
        </section>
    </div>
  </div>
</section>
</main>

{foot}
</div>

{script}
{legal_js}
{track}
'''

out={}
for doc,fn in [(PRIVACY,'forecast-farms-privacy-ghl.html'),(TERMS,'forecast-farms-terms-ghl.html')]:
    p=page(doc);open(fn,'w',encoding='utf-8').write(p);out[fn]=p
print('built',list(out))
