import re,os
os.chdir(os.environ['FF_OUT'])
from ffchrome import chrome
EVAL='/contact-us?interest=rider-training'
head,header,footer,script,track=chrome(current='rider-training',cta_href=EVAL)

css='''
.ff .tri{display:grid;gap:2.5rem 3rem}
.ff .tri>*{min-width:0;padding-top:1.5rem;border-top:1px solid var(--line-strong)}
.ff .tri h3{margin-bottom:.75rem;font-size:clamp(1.5rem,1.3rem + .6vw,1.85rem)}
.ff .tri p{color:var(--fg-soft)}
@media (min-width:900px){.ff .tri{grid-template-columns:repeat(3,minmax(0,1fr))}.ff .tri--2{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ff .fmt{border-bottom:1px solid var(--line)}
.ff .fmt-row{display:grid;gap:.5rem 3rem;padding-block:1.5rem;border-top:1px solid var(--line)}
.ff .fmt-row>*{min-width:0}
.ff .fmt-row h3{font-size:clamp(1.5rem,1.3rem + .6vw,1.85rem)}
.ff .fmt-row p{color:var(--fg-soft)}
.ff .fmt-best{font-size:.95rem;color:var(--fg)}
.ff .fmt-best span{display:block;margin-bottom:.3rem;font:600 .7rem/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--saddle)}
@media (min-width:900px){.ff .fmt-row{grid-template-columns:minmax(0,3fr) minmax(0,5fr) minmax(0,4fr);align-items:baseline}}
.ff .fmt-note{margin-top:1.5rem;font-size:.925rem;color:var(--fg-soft)}
.ff .split{display:grid;gap:2.5rem 5rem;align-items:start}
.ff .split>*{min-width:0}
.ff .split h2{margin-bottom:1.25rem}
@media (min-width:960px){.ff .split{grid-template-columns:minmax(0,5fr) minmax(0,6fr)}}
.ff .ticks li{position:relative;padding:.9rem 0 .9rem 2rem;border-top:1px solid var(--line);color:var(--fg)}
.ff .ticks li:last-child{border-bottom:1px solid var(--line)}
.ff .ticks li::before{content:"";position:absolute;left:.1rem;top:1.25rem;width:.75rem;height:.4rem;border-left:2px solid var(--accent);border-bottom:2px solid var(--accent);transform:rotate(-45deg)}
.ff .ticks li span{display:block;font-size:.925rem;color:var(--fg-soft);margin-top:.15rem}
.ff .sm{min-width:0;display:flex;flex-direction:column;gap:.6rem}
.ff .sm-feature{display:grid;gap:2.5rem 2rem}
.ff .sm-feature>*{min-width:0}
@media (min-width:640px){.ff .sm-feature{grid-template-columns:repeat(2,minmax(0,1fr))}.ff .sm-roster{grid-column:1/-1}}
@media (min-width:1100px){.ff .sm-feature{grid-template-columns:minmax(0,1fr) minmax(0,1fr) minmax(0,1.1fr);gap:2.5rem}.ff .sm-roster{grid-column:auto}}
.ff .sm-roster h3{padding-bottom:.9rem;border-bottom:1px solid var(--line-strong);font:600 .7rem/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--saddle)}
.ff .sm-roster li{padding-block:1.1rem;border-bottom:1px solid var(--line)}
.ff .sm-roster h4{margin:.35rem 0;font:400 1.45rem/1.15 var(--serif);color:var(--fg)}
.ff .sm-roster li p:last-child{font-size:.925rem;color:var(--fg-soft)}
.ff .sm .ph{aspect-ratio:4/5;margin-bottom:.5rem}
.ff .sm-type,.ff .sm .sm-type{font:600 .7rem/1.35 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--saddle)}
.ff .sm h3{font-size:1.6rem}
.ff .sm p{font-size:.925rem;color:var(--fg-soft)}
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
.ff .faq-list details a{color:var(--accent);text-underline-offset:3px}
.ff .cta-band .wrap{display:grid;gap:1.75rem 4rem;align-items:end}
.ff .cta-band h2{max-width:16ch}
.ff .cta-band p{color:var(--band-soft);max-width:32em;margin-top:1rem}
.ff .cta-actions{display:flex;flex-wrap:wrap;gap:.75rem}
.ff .cta-band .btn{background:var(--band-fg);border-color:var(--band-fg);color:var(--band)}
.ff .cta-band .btn:hover{background:transparent;color:var(--band-fg)}
.ff .cta-band .btn-ghost{background:transparent;color:var(--band-fg);border-color:var(--band-line)}
.ff .cta-band .btn-ghost:hover{border-color:var(--band-fg)}
@media (min-width:900px){.ff .cta-band .wrap{grid-template-columns:minmax(0,1fr) auto}}
'''
head_r=head.replace('</style>',css+'</style>')

page_js='''<script>
(()=>{
const HOME='/';
if(HOME!=='/'){document.querySelectorAll('.ff a[href^="/#"]').forEach(a=>a.setAttribute('href',HOME+a.getAttribute('href').slice(1)));document.querySelectorAll('.ff a[href="/"]').forEach(a=>a.setAttribute('href',HOME));}
})();
</script>'''

def horse(slug,name,typ,text):
    return f'''      <article class="sm">
        <figure class="ph"><img src="images/schoolmaster-{slug}.jpg" alt="{name}, a Forecast Farms schoolmaster" loading="lazy" onerror="this.remove()"><div class="ph-note" aria-hidden="true"><span>Photograph</span>{name}</div></figure>
        <p class="sm-type">{typ}</p>
        <h3>{name}</h3>
        <p>{text}</p>
      </article>
'''
def roster(name,typ,text):
    return f'''          <li>
            <p class="sm-type">{typ}</p>
            <h4>{name}</h4>
            <p>{text}</p>
          </li>
'''
horses=''.join([
horse('chief','Chief','Pony of the Americas · 13.0 hands','The farm’s most popular lesson pony, and a steady partner for junior riders.'),
horse('audrey','Princess Audrey','Welsh pony cross mare · 12.2 hands','With Denise since she was two, and shown at local and recognized shows. A small pony for junior riders ready to compete.'),
])+'''      <aside class="sm-roster" aria-labelledby="roster-title">
        <h3 id="roster-title">Also in the program</h3>
        <ul>
'''+''.join([
roster('Herman','Thoroughbred','Local show and foxhunting experience. Quiet enough for riders building confidence, with plenty to teach advanced riders.'),
roster('Remi','Thoroughbred × Percheron','Big, quiet and steady. Looks after riders building their foundation and gives advanced riders a horse to refine their flatwork on.'),
roster('Freddy','Welsh × Quarter Horse · Large pony','Local show and Pony Club experience. A favorite with junior and adult riders alike.'),
])+'''        </ul>
      </aside>
'''

body=f'''<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <p class="eyebrow">Rider Training</p>
    <h1 id="hero-title">A seat and a system <em>that work on any horse.</em></h1>
    <p class="hero-text">Structured Hunter, Jumper and Equitation instruction for junior and adult riders, on your own horse, a ship-in, or one of our experienced schoolmasters. Each lesson builds on the last, toward goals we set together.</p>
    <div class="hero-ctas">
      <a class="btn" href="{EVAL}">Schedule an Evaluation</a>
      <a class="btn btn-ghost" href="#schoolmasters">Meet the Schoolmasters</a>
    </div>
    <ul class="hero-facts">
      <li><strong>Private</strong> and semi-private lessons</li>
      <li><strong>Year-round</strong> indoor arena and all-weather ring</li>
      <li><strong>Ship-ins</strong> welcome</li>
    </ul>
  </div>
  <figure class="ph ph--hero hero-media">
    <img src="images/rider-training.jpg" alt="A rider schooling over a fence during a lesson at Forecast Farms" fetchpriority="high" onerror="this.remove()">
    <div class="ph-note" aria-hidden="true"><span>Hero photograph</span>Rider schooling over a fence</div>
  </figure>
</section>

<section id="who" class="section paper" aria-labelledby="who-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Who it’s for</p>
        <h2 id="who-title">For riders who want their riding <em>to change.</em></h2>
      </div>
      <p class="lede">Rider Training is for riders who ride consistently and want measurable progress, whatever horse they ride.</p>
    </header>
    <div class="tri">
      <div>
        <h3>Junior riders</h3>
        <p>Riders under 18 building a correct foundation for the hunter, jumper and equitation rings. Parents hear what we are working on and why.</p>
      </div>
      <div>
        <h3>Adult riders</h3>
        <p>Adults returning to riding, moving up a level, or preparing to show, who want clear instruction and an honest read on their progress.</p>
      </div>
      <div>
        <h3>Owners and ship-ins</h3>
        <p>Riders with their own horse, based here or trailered in, who want lessons that account for that horse’s training as well as their own.</p>
      </div>
    </div>
  </div>
</section>

<section id="formats" class="section" aria-labelledby="fmt-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Lesson formats</p>
        <h2 id="fmt-title">Choose the format <em>that fits the goal.</em></h2>
      </div>
      <p class="lede">Lessons run year-round in our indoor arena with rubberized footing and our outdoor all-weather ring.</p>
    </header>
    <div class="fmt">
      <div class="fmt-row">
        <h3>Private</h3>
        <p>One rider and the trainer’s full attention for the whole lesson.</p>
        <p class="fmt-best"><span>Best for</span>Specific goals, a new horse partnership, and show preparation</p>
      </div>
      <div class="fmt-row">
        <h3>Semi-private</h3>
        <p>Two riders at a similar level, working on shared exercises with individual correction.</p>
        <p class="fmt-best"><span>Best for</span>Steady progress with a riding partner at your level</p>
      </div>
      <div class="fmt-row">
        <h3>Small group</h3>
        <p>A few riders at a similar level, riding exercises together in the ring.</p>
        <p class="fmt-best"><span>Best for</span>Extra saddle time and learning to ride with others in the ring</p>
      </div>
    </div>
    <p class="fmt-note">We recommend a format and schedule after your evaluation.</p>
  </div>
</section>

<section id="work" class="section lilac" aria-labelledby="work-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">What we work on</p>
        <h2 id="work-title">Fundamentals first, <em>then height.</em></h2>
      </div>
      <p class="lede">Every lesson works on the same four areas. The balance between them shifts as the rider progresses.</p>
    </header>
    <div class="tri tri--2">
      <div>
        <h3>Position and seat</h3>
        <p>An independent seat, a following hand and a secure leg, so the aids come from position rather than strength.</p>
      </div>
      <div>
        <h3>Flatwork</h3>
        <p>Rhythm, straightness, transitions and adjustability. The flat is where most jumping problems are solved.</p>
      </div>
      <div>
        <h3>Gymnastics and lines</h3>
        <p>Poles, gymnastic grids and related distances that train the eye, the count and the feel for the canter.</p>
      </div>
      <div>
        <h3>Courses and equitation</h3>
        <p>Riding a planned track, bending lines and turns, and the equitation tests that sharpen accuracy in every ring.</p>
      </div>
    </div>
  </div>
</section>

<section id="showing" class="section paper" aria-labelledby="show-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Preparing to show</p>
      <h2 id="show-title">Show when you are ready, <em>and ready when you show.</em></h2>
      <p class="lede">Showing is optional. When a rider and horse are ready to compete, preparation becomes part of the lesson plan.</p>
    </div>
    <ul class="ticks">
      <li>Choosing the right divisions<span>Based on the rider’s skills and the horse’s experience</span></li>
      <li>Walking and planning courses<span>Counting lines, choosing turns and setting a pace</span></li>
      <li>Building a warm-up<span>A routine that settles horse and rider before the round</span></li>
      <li>Rounds that reflect the work at home<span>Results that track with preparation, show after show</span></li>
    </ul>
  </div>
</section>

<section id="schoolmasters" class="section" aria-labelledby="sm-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Our schoolmasters</p>
        <h2 id="sm-title">No horse yet? <em>Ride one of ours.</em></h2>
      </div>
      <p class="lede">Our experienced horses and ponies teach riders at every stage of the program. We match each rider with the right one after the evaluation.</p>
    </header>
    <div class="sm-feature">
{horses}    </div>
  </div>
</section>

<section id="voice" class="section paper" aria-label="From a rider">
  <div class="wrap">
    <figure class="quote-solo">
      <blockquote><p>“She pays close attention not only to the horse’s way of going but also the rider so the two are on the same page.”</p></blockquote>
      <figcaption><span class="q-name">Jana</span><span class="q-meta">Fairfax, Virginia</span></figcaption>
    </figure>
  </div>
</section>

<section id="faq" class="section" aria-labelledby="faq-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Questions</p>
      <h2 id="faq-title">About Rider Training</h2>
      <p class="lede">Anything else, call <a href="tel:+15402741541">(540) 274-1541</a> or email <a href="mailto:info@forecastfarms.com">info@forecastfarms.com</a>.</p>
    </div>
    <div class="faq-list">
      <details>
        <summary>I don’t have a horse. Can I still train?</summary>
        <p>Yes. Many riders start on one of our schoolmasters. We match horse and rider after your evaluation, and leasing is an option when you are ready for more time in the saddle.</p>
      </details>
      <details>
        <summary>Can I bring my own horse?</summary>
        <p>Yes. Horses based at the farm and ship-ins are both welcome. For a ship-in, bring a current negative Coggins and vaccination records.</p>
      </details>
      <details>
        <summary>How often should I ride?</summary>
        <p>Consistency matters more than intensity. We recommend a lesson schedule after your evaluation, based on your goals and your horse.</p>
      </details>
      <details>
        <summary>Do you take beginners?</summary>
        <p>Riders ages 4 to 7 start in our <a href="/lessons">Junior Riding Club</a>. Older beginners start with an evaluation, and we will tell you honestly whether our program is the right fit.</p>
      </details>
      <details>
        <summary>Do I have to show?</summary>
        <p>No. Many riders train for the skills alone. When you want to compete and you and your horse are ready, we prepare you for it.</p>
      </details>
      <details>
        <summary>What does it cost?</summary>
        <p>Pricing depends on the lesson format and how often you ride. We confirm it at your evaluation.</p>
      </details>
    </div>
  </div>
</section>

<section class="section band cta-band" aria-labelledby="cta-title">
  <div class="wrap">
    <div>
      <h2 id="cta-title">Start with an <em>evaluation lesson.</em></h2>
      <p>One lesson to see where you are, agree on goals, and recommend the right format and schedule.</p>
    </div>
    <div class="cta-actions">
      <a class="btn" href="{EVAL}">Schedule an Evaluation</a>
      <a class="btn btn-ghost" href="tel:+15402741541">Call (540) 274-1541</a>
    </div>
  </div>
</section>
</main>'''

page=f'''{head_r}
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
open('forecast-farms-rider-training-ghl.html','w',encoding='utf-8').write(page)
print('built')
