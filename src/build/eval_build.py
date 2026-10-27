import re,os
os.chdir(os.environ['FF_OUT'])
from ffchrome import chrome
g=open(os.path.join(os.environ['FF_ROOT'],'src','home.html'),encoding='utf-8').read()
form=re.search(r'<form class="eval-form".*?</form>',g,re.S).group(0)
head,header,footer,script,track=chrome(current='contact-us',cta_href='#request')

sms='''        <div class="field field--full field--check">
          <input id="f-sms" name="sms_consent" type="checkbox" value="Yes">
          <label for="f-sms">Yes, Forecast Farms may text me about my evaluation request and scheduling. Message frequency varies. Message and data rates may apply. Reply STOP to opt out, HELP for help.</label>
        </div>
      </div>
      <div class="form-foot">'''
a='''      </div>
      <div class="form-foot">'''
form=form if 'f-sms' in form else form.replace(a,sms)
a='''        <p class="form-status"'''
form=form if 'form-legal' in form else form.replace(a,'''        <p class="form-legal">By submitting this form, you agree to our <a href="/terms-and-conditions">Terms</a> and <a href="/privacy-policy">Privacy Policy</a>. Texting consent is optional and is not a condition of any purchase.</p>
'''+a)

css='''
.ff .ev-steps{display:grid;gap:2.5rem 3rem}
.ff .ev-step{min-width:0;padding-top:1.5rem;border-top:1px solid var(--line-strong)}
.ff .ev-step .n{display:grid;place-items:center;width:2.25rem;height:2.25rem;margin-bottom:1.25rem;border-radius:50%;background:var(--accent);color:var(--on-accent);font:500 1.05rem/1 var(--serif)}
.ff .ev-step .when{margin-bottom:.5rem;font:600 .7rem/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--saddle)}
.ff .ev-step h3{margin-bottom:.75rem;font-size:clamp(1.5rem,1.3rem + .6vw,1.85rem)}
.ff .ev-step p{color:var(--fg-soft)}
@media (min-width:900px){.ff .ev-steps{grid-template-columns:repeat(3,minmax(0,1fr))}}
.ff .ev-cols{display:grid;gap:2.75rem 3rem}
.ff .ev-col{min-width:0;padding-top:1.5rem;border-top:2px solid var(--accent)}
.ff .ev-col--bring{border-top-color:var(--saddle)}
.ff .ev-col h3{font-size:1.6rem}
.ff .ev-col .ev-note{margin-top:.3rem;font-size:.875rem;color:var(--fg-soft)}
.ff .ev-col ul{margin-top:1.1rem}
.ff .ev-col li{position:relative;padding:.7rem 0 .7rem 1.6rem;border-bottom:1px solid var(--line);font-size:.95rem;line-height:1.5}
.ff .ev-col li::before{content:"";position:absolute;left:.15rem;top:1.18rem;width:.45rem;height:.45rem;border-radius:50%;background:var(--accent)}
.ff .ev-col--bring li::before{width:.7rem;height:.38rem;top:1.05rem;left:0;border-radius:0;background:none;border-left:2px solid var(--saddle);border-bottom:2px solid var(--saddle);transform:rotate(-45deg)}
@media (min-width:900px){.ff .ev-cols{grid-template-columns:repeat(3,minmax(0,1fr))}}
.ff .field.field--check{display:flex;align-items:flex-start;gap:.75rem;grid-column:1/-1}
.ff .field.field--check input{flex:none;width:1.15rem;height:1.15rem;min-height:0;margin:.2rem 0 0;padding:0;accent-color:var(--accent)}
.ff .field.field--check label{font-size:.85rem;font-weight:400;line-height:1.55;letter-spacing:0;color:var(--fg-soft)}
.ff .form-legal{font-size:.8rem;line-height:1.55;color:var(--fg-soft)}
.ff .form-legal a{color:var(--accent);text-underline-offset:3px}
.ff .faq-grid{display:grid;gap:3rem 5rem;align-items:start}
.ff .faq-grid>*{min-width:0}
@media (min-width:1000px){.ff .faq-grid{grid-template-columns:minmax(0,7fr) minmax(0,4fr)}}
.ff .faq h2{margin-bottom:2rem}
.ff .faq-list{border-bottom:1px solid var(--line)}
.ff .faq-list details{border-top:1px solid var(--line)}
.ff .faq-list summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:baseline;gap:1.5rem;padding:1.2rem 0;font:400 clamp(1.15rem,1.05rem + .35vw,1.35rem)/1.35 var(--serif);color:var(--fg)}
.ff .faq-list summary::-webkit-details-marker{display:none}
.ff .faq-list summary::after{content:"+";flex:none;font:300 1.5rem/1 var(--sans);color:var(--accent)}
.ff .faq-list details[open] summary::after{content:"\\2212"}
.ff .faq-list summary:hover{color:var(--accent)}
.ff .faq-list details p{max-width:38em;padding-bottom:1.35rem;color:var(--fg-soft);line-height:1.7}
.ff .faq-list details a{color:var(--accent);text-underline-offset:3px}
.ff .ev-visit{padding:clamp(1.5rem,3vw,2.25rem);background:var(--surface);border-radius:2px}
.ff .ev-visit h3{font-size:1.6rem;margin-bottom:.5rem}
.ff .ev-visit>p{color:var(--fg-soft);font-size:.95rem}
.ff .ev-visit dl{margin-top:1.25rem;border-bottom:1px solid var(--line)}
.ff .ev-visit dl>div{display:grid;grid-template-columns:5.5rem minmax(0,1fr);gap:1rem;padding-block:.75rem;border-top:1px solid var(--line)}
.ff .ev-visit dt{font:600 .7rem/1.7 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--fg-soft)}
.ff .ev-visit dd{font-size:.95rem;color:var(--fg)}
.ff .ev-visit dd a{color:var(--fg);text-decoration-color:var(--line-strong);text-underline-offset:4px;overflow-wrap:anywhere}
.ff .ev-visit .link-arrow{margin-top:1.5rem}
'''
head_e=head.replace('</style>',css+'</style>')

page_js='''<script>
(()=>{
const HOME='/';
if(HOME!=='/'){document.querySelectorAll('.ff a[href^="/#"]').forEach(a=>a.setAttribute('href',HOME+a.getAttribute('href').slice(1)));document.querySelectorAll('.ff a[href="/"]').forEach(a=>a.setAttribute('href',HOME));}
const map={'rider-training':'Rider Training','horse-training':'Horse Training','horse-rider-development':'Horse + Rider Development','horse-search':'Horse search, sales or leasing','junior-riding-club':'Junior Riding Club (ages 4–7)'};
let v=null;try{v=new URLSearchParams(location.search).get('interest');}catch(e){}
const sel=document.getElementById('f-interest');
if(v&&sel&&map[v])sel.value=map[v];
})();
</script>'''

MAP='https://www.google.com/maps/search/?api=1&query=2497+Atoka+Rd+Marshall+VA+20115'
body=f'''<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <p class="eyebrow">Evaluation lesson</p>
    <h1 id="hero-title">Start with an <em>evaluation lesson.</em></h1>
    <p class="hero-text">Every new rider and horse at Forecast Farms begins here. In one lesson, Denise sees where you are, talks through your goals, and recommends the training that fits you and your horse.</p>
    <div class="hero-ctas">
      <a class="btn" href="#request">Request an Evaluation</a>
      <a class="btn btn-ghost" href="tel:+15402741541">Call (540) 274-1541</a>
    </div>
    <ul class="hero-facts">
      <li><strong>One lesson</strong> to assess rider and horse</li>
      <li><strong>Your horse</strong> or one of our schoolmasters</li>
      <li><strong>A clear plan</strong> pathway, schedule and goals</li>
    </ul>
  </div>
  <figure class="ph ph--hero hero-media">
    <img src="images/evaluation-lesson.jpg" alt="Trainer watching a rider during an evaluation lesson" fetchpriority="high" onerror="this.remove()">
    <div class="ph-note" aria-hidden="true"><span>Hero photograph</span>Evaluation lesson, trainer at the rail</div>
  </figure>
</section>

<section id="how" class="section paper" aria-labelledby="how-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">How it works</p>
        <h2 id="how-title">From request to plan, <em>in three steps.</em></h2>
      </div>
      <p class="lede">The evaluation is a working lesson. You ride, Denise watches closely, and you hear plainly what she sees.</p>
    </header>
    <ol class="ev-steps">
      <li class="ev-step">
        <span class="n" aria-hidden="true">1</span>
        <p class="when">Before</p>
        <h3>Send your request</h3>
        <p>Tell us about the rider, the horse and your goals. We follow up to schedule a time, answer your questions and, if you are bringing your own horse, arrange the ship-in.</p>
      </li>
      <li class="ev-step">
        <span class="n" aria-hidden="true">2</span>
        <p class="when">During</p>
        <h3>Ride with Denise</h3>
        <p>Denise assesses position, balance and effectiveness on the flat and, when it suits the rider, over fences. With your own horse, she also looks at the horse’s training and way of going.</p>
      </li>
      <li class="ev-step">
        <span class="n" aria-hidden="true">3</span>
        <p class="when">After</p>
        <h3>Leave with a plan</h3>
        <p>You hear what is working and what needs attention, then get a recommended pathway, a lesson and training schedule, and first goals for the season.</p>
      </li>
    </ol>
  </div>
</section>

<section id="prepare" class="section lilac" aria-labelledby="prep-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Preparing for your lesson</p>
        <h2 id="prep-title">What we look at, and <em>what to bring.</em></h2>
      </div>
      <p class="lede">Knowing what Denise is watching for helps you get the most from the lesson.</p>
    </header>
    <div class="ev-cols">
      <div class="ev-col">
        <h3>The rider</h3>
        <ul>
          <li>Position and security in the saddle</li>
          <li>Balance and rhythm at the walk, trot and canter</li>
          <li>Clear, consistent use of the aids</li>
          <li>Jumping position and eye for a distance, if jumping</li>
          <li>Riding history, goals and show experience</li>
        </ul>
      </div>
      <div class="ev-col">
        <h3>Your horse</h3>
        <p class="ev-note">If you bring your own</p>
        <ul>
          <li>Rhythm, straightness and way of going</li>
          <li>Response to the aids and adjustability</li>
          <li>Jumping form and attitude over fences</li>
          <li>Fitness, soundness and tack fit</li>
          <li>Training history and show record</li>
        </ul>
      </div>
      <div class="ev-col ev-col--bring">
        <h3>What to bring</h3>
        <ul>
          <li>A properly fitted, ASTM/SEI-certified riding helmet</li>
          <li>Boots with a heel, and breeches or riding tights</li>
          <li>Gloves, if you usually ride in them</li>
          <li>For a ship-in: a current negative Coggins and vaccination records</li>
          <li>Your horse’s tack, fitted and in good repair</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="request" class="section band" aria-labelledby="eval-title">
  <div class="wrap eval-grid">
    <div class="eval-copy">
      <p class="eyebrow">Request an evaluation</p>
      <h2 id="eval-title">Tell us about the rider <em>and the horse.</em></h2>
      <p>The more we know before you arrive, the more useful your first lesson will be. We follow up to schedule a time and answer any questions.</p>
      <dl class="eval-facts">
        <div><dt>Riders</dt><dd>Junior and adult riders</dd></div>
        <div><dt>Horse</dt><dd>Your own, a ship-in, or one of our schoolmasters</dd></div>
        <div><dt>Outcome</dt><dd>A recommended pathway and training schedule</dd></div>
      </dl>
      <div class="contact">
        <p><span>Call</span><a href="tel:+15402741541">(540) 274-1541</a></p>
        <p><span>Email</span><a href="mailto:info@forecastfarms.com">info@forecastfarms.com</a></p>
        <p><span>Visit</span>2497 Atoka Road, Marshall, VA 20115</p>
      </div>
    </div>
    {form}
  </div>
</section>

<section id="faq" class="section paper" aria-labelledby="faq-title">
  <div class="wrap faq-grid">
    <div class="faq">
      <p class="eyebrow">Questions</p>
      <h2 id="faq-title">Before you book</h2>
      <div class="faq-list">
        <details>
          <summary>Do I need my own horse?</summary>
          <p>No. Riders train on their own horse, ship in for lessons, or ride one of our experienced schoolmasters. Tell us in your request and we will plan the lesson around it.</p>
        </details>
        <details>
          <summary>What level should I be?</summary>
          <p>We train junior and adult riders who want to ride consistently and progress, from riders building a solid foundation to riders preparing for the show ring. The evaluation shows us where to start. Riders ages 4 to 7 begin in our <a href="/lessons">Junior Riding Club</a>.</p>
        </details>
        <details>
          <summary>I want training for my horse. How does that start?</summary>
          <p>The same way. Choose Horse Training in the form and tell us about your horse’s age, experience and goals. We will arrange the best way to assess the horse.</p>
        </details>
        <details>
          <summary>How much does the evaluation cost?</summary>
          <p>We confirm the current rate when we schedule your lesson. Call or email us if you would like it before you send a request.</p>
        </details>
        <details>
          <summary>What happens after the evaluation?</summary>
          <p>We recommend a pathway, a schedule and first goals, and you decide whether to go ahead. Lessons and training begin once the farm’s agreements and release forms are signed.</p>
        </details>
        <details>
          <summary>Do you offer trail rides or one-time rides?</summary>
          <p>No. Our program is built for riders and horses who train consistently.</p>
        </details>
      </div>
    </div>
    <aside class="ev-visit" aria-labelledby="visit-title">
      <h3 id="visit-title">Visit the farm</h3>
      <p>We are on Atoka Road in Marshall, in Fauquier County hunt country.</p>
      <dl>
        <div><dt>Address</dt><dd>2497 Atoka Road<br>Marshall, VA 20115</dd></div>
        <div><dt>Phone</dt><dd><a href="tel:+15402741541">(540) 274-1541</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:info@forecastfarms.com">info@forecastfarms.com</a></dd></div>
        <div><dt>Facilities</dt><dd>Indoor arena with rubberized footing and an outdoor all-weather ring</dd></div>
      </dl>
      <a class="link-arrow" href="{MAP}" target="_blank" rel="noopener">Get directions</a>
    </aside>
  </div>
</section>
</main>'''

page=f'''{head_e}
<div class="ff">
<a class="skip" href="#main">Skip to content</a>

{header}

{body}

{footer}
</div>

{script}
{page_js}
{track}
'''
open('forecast-farms-evaluation-ghl.html','w',encoding='utf-8').write(page)
print('built')
