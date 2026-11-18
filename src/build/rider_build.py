import re,os
os.chdir(os.environ['FF_OUT'])
from ffchrome import chrome,band,pgrid
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
horses='    <div class="sm-grid">\n'+''.join([
horse('chief','Chief','Pony of the Americas · 13.0 hands','The farm’s most popular lesson pony, and a steady partner for junior riders.'),
horse('audrey','Princess Audrey','Welsh pony cross mare · 12.2 hands','With Denise since she was two, and shown at local and recognized shows.'),
horse('herman','Herman','Thoroughbred · <span class="tbd">height to confirm</span>','Local show and foxhunting experience. Quiet enough for riders building confidence.'),
horse('remi','Remi','Thoroughbred × Percheron · <span class="tbd">height to confirm</span>','Big, quiet and steady. Gives advanced riders a horse to refine their flatwork on.'),
horse('freddy','Freddy','Welsh × Quarter Horse · Large pony · <span class="tbd">height to confirm</span>','Local show and Pony Club experience. A favorite with junior and adult riders alike.'),
])+'    </div>\n'

BAND=band('images/rider-training-band.jpg','A lesson in the indoor arena at Forecast Farms','A lesson in the indoor arena, wide')
GRID=pgrid('Lessons at Forecast Farms',[
('images/rider-training-grid-1.jpg','A rider working on the flat','Flatwork: rhythm and straightness'),
('images/rider-training-grid-2.jpg','A rider in a gymnastic grid','A gymnastic grid'),
('images/rider-training-grid-3.jpg','A rider walking a course','Walking a course before a round')])

body=f'''<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <p class="eyebrow">Rider Training</p>
    <h1 id="hero-title">Hunter, jumper and equitation lessons in <em>Marshall, Virginia.</em></h1>
    <p class="hero-text">For junior and adult riders, on your own horse, a ship-in, or one of our schoolmasters. Each lesson builds on the last, toward goals we set with you.</p>
    <div class="hero-ctas">
      <a class="btn" href="{EVAL}">Schedule an Evaluation Lesson</a>
      <a class="btn btn-ghost" href="#schoolmasters">Meet the Schoolmasters</a>
    </div>
    <ul class="hero-facts">
      <li><strong>Private</strong> and semi-private lessons</li>
      <li><strong>Year-round</strong> indoor arena and all-weather ring</li>
      <li><strong>35+ years</strong> training riders and horses</li>
    </ul>
  </div>
  <figure class="ph ph--hero hero-media">
    <img src="images/rider-training.jpg" style="object-position:48% 50%" alt="A rider schooling over a fence during a lesson at Forecast Farms" fetchpriority="high" onerror="this.remove()">
    <div class="ph-note" aria-hidden="true"><span>Hero photograph</span>Rider schooling over a fence</div>
  </figure>
</section>

<section id="who" class="section paper" aria-labelledby="who-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Who it’s for</p>
        <h2 id="who-title">For junior riders, adult riders and horse owners</h2>
      </div>
      <p class="lede">Rider Training is for riders who ride consistently and want to keep improving, whatever horse they ride.</p>
    </header>
    <div class="tri">
      <div>
        <h3>Junior riders</h3>
        <p>Riders under 18 building a correct foundation for the hunter, jumper and equitation rings. Parents hear what we are working on and why.</p>
      </div>
      <div>
        <h3>Adult riders</h3>
        <p>Adults returning to riding, moving up a level, or preparing to show. You hear what is improving and what still needs work.</p>
      </div>
      <div>
        <h3>Owners and ship-ins</h3>
        <p>Riders with their own horse, based here or trailered in. Your lessons take your horse’s training into account as well as your own.</p>
      </div>
    </div>
  </div>
</section>

<section id="disciplines" class="section" aria-labelledby="disc-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">The disciplines</p>
        <h2 id="disc-title">What the hunter, jumper and equitation rings judge</h2>
      </div>
      <p class="lede">Each ring scores something different, so we train for the ring you want to ride in.</p>
    </header>
    <div class="disc-grid">
      <article class="disc">
        <figure class="ph">
          <img src="https://assets.cdn.filesafe.space/yFHRGgbUYoTRIY9XZIJQ/media/6adcc77936aa4a07e89fa346.jpg" alt="A hunter cantering to a fence in a smooth, even rhythm" loading="lazy" onerror="this.remove()">
          <div class="ph-note" aria-hidden="true"><span>Photograph</span>Hunter round, even rhythm to a fence</div>
        </figure>
        <h3>Hunter</h3>
        <p>The hunter ring comes from the hunting field. The judge scores the horse, so the goal is a smooth round at an even pace.</p>
        <dl class="disc-meta">
          <div><dt>Judged on</dt><dd>The horse’s way of going, jumping form, manners, and an even pace with accurate distances.</dd></div>
          <div><dt>Suits riders who</dt><dd>Like rhythm and precision.</dd></div>
        </dl>
      </article>
      <article class="disc">
        <figure class="ph">
          <img src="https://assets.cdn.filesafe.space/yFHRGgbUYoTRIY9XZIJQ/media/6adcc7799c1511d5b99c0f50.jpg" alt="A jumper turning tightly toward a colored oxer" loading="lazy" onerror="this.remove()">
          <div class="ph-note" aria-hidden="true"><span>Photograph</span>Jumper turning to a colored oxer</div>
        </figure>
        <h3>Jumper</h3>
        <p>Jumpers are scored on faults and time, not style. The fastest clear round wins, so control and tight turns matter most.</p>
        <dl class="disc-meta">
          <div><dt>Judged on</dt><dd>Faults and time: rails down, refusals and time penalties, often decided in a jump-off.</dd></div>
          <div><dt>Suits riders who</dt><dd>Enjoy technical courses, tight turns and riding against the clock.</dd></div>
        </dl>
      </article>
      <article class="disc">
        <figure class="ph">
          <img src="https://assets.cdn.filesafe.space/yFHRGgbUYoTRIY9XZIJQ/media/6adcc779d542268bb4fef806.jpg" alt="An equitation rider in a correct, quiet position over a fence" loading="lazy" onerror="this.remove()">
          <div class="ph-note" aria-hidden="true"><span>Photograph</span>Equitation rider, correct position</div>
        </figure>
        <h3>Equitation</h3>
        <p>Equitation judges the rider, not the horse. The best riders make a hard course look easy.</p>
        <dl class="disc-meta">
          <div><dt>Judged on</dt><dd>The rider’s position, use of the aids, control and accuracy of the track, with tests in some classes.</dd></div>
          <div><dt>Suits riders who</dt><dd>Want a correct position, which helps in every ring.</dd></div>
        </dl>
      </article>
    </div>
  </div>
</section>

<section id="formats" class="section paper" aria-labelledby="fmt-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Lesson formats</p>
        <h2 id="fmt-title">Private or semi-private lessons</h2>
      </div>
      <p class="lede">Lessons run year-round in our indoor arena with rubberized footing and our outdoor all-weather ring.</p>
    </header>
    <div class="fmt">
      <div class="fmt-row">
        <h3>Private</h3>
        <p>One rider and one instructor for the whole lesson.</p>
        <p class="fmt-best"><span>Best for</span>A specific goal, a new horse, or getting ready for a show</p>
      </div>
      <div class="fmt-row">
        <h3>Semi-private</h3>
        <p>Two riders at a similar level. You ride the same exercises and each get your own corrections.</p>
        <p class="fmt-best"><span>Best for</span>Steady progress with a riding partner at your level</p>
      </div>
    </div>
    <p class="fmt-note">After your evaluation lesson, we recommend a format and a schedule.</p>
  </div>
</section>

{BAND}

<section id="work" class="section lilac" aria-labelledby="work-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">What we work on</p>
        <h2 id="work-title">What every lesson works on</h2>
      </div>
      <p class="lede">Every lesson works on the same four areas. How much time each one gets changes as you improve.</p>
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

{GRID}

<section id="showing" class="section paper" aria-labelledby="show-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Preparing to show</p>
      <h2 id="show-title">Getting ready to show</h2>
      <p class="lede">Showing is optional. When you are both ready, show preparation becomes part of your lessons.</p>
    </div>
    <ul class="ticks">
      <li>Choosing your divisions<span>Based on your skills and your horse’s experience</span></li>
      <li>Walking and planning courses<span>Counting lines, choosing turns and setting a pace</span></li>
      <li>Building a warm-up<span>A routine that settles horse and rider before the round</span></li>
      <li>Rounds that match your work at home<span>You enter a show once your rounds at home are ready for it</span></li>
    </ul>
  </div>
</section>

<section id="schoolmasters" class="section" aria-labelledby="sm-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">Our schoolmasters</p>
        <h2 id="sm-title">Meet the schoolmasters</h2>
      </div>
      <p class="lede">No horse yet? Five schoolmasters teach riders at every stage. We match you with one after your evaluation lesson.</p>
    </header>
{horses}  </div>
</section>

<section id="voice" class="section deep" aria-label="From a rider">
  <div class="wrap">
    <figure class="quote-solo">
      <blockquote><p>“I took a 35 year break from riding and Denise &amp; her team are helping me get back in the saddle again with confidence.”</p></blockquote>
      <figcaption><span class="q-name">Jenn P.</span><span class="q-meta">Google review</span></figcaption>
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
        <p>Yes. Many riders start on one of our schoolmasters. We match you with one after your evaluation lesson, and you can lease a horse when you want more time in the saddle.</p>
      </details>
      <details>
        <summary>Can I bring my own horse?</summary>
        <p>Yes. Horses based at the farm and ship-ins are both welcome. For a ship-in, bring a current negative Coggins and vaccination records.</p>
      </details>
      <details>
        <summary>How often should I ride?</summary>
        <p>Riding regularly matters more than riding a lot at once. After your evaluation lesson, we recommend a schedule based on your goals and your horse.</p>
      </details>
      <details>
        <summary>Do you take beginners?</summary>
        <p>Riders ages 4 to 7 start in our <a href="/lessons">Junior Riding Club</a>. Older beginners start with an evaluation lesson, and we tell you then whether Rider Training fits.</p>
      </details>
      <details>
        <summary>Do I have to show?</summary>
        <p>No. Many riders train for the skills alone. When you want to compete and you and your horse are ready, we prepare you for it.</p>
      </details>
      <details>
        <summary>What does it cost?</summary>
        <p>The price depends on the lesson format and how often you ride. Denise confirms it after your evaluation lesson.</p>
      </details>
    </div>
  </div>
</section>

<section class="section band cta-band" aria-labelledby="cta-title">
  <div class="wrap">
    <div>
      <h2 id="cta-title">Start with an <em>evaluation lesson.</em></h2>
      <p>In one lesson, we see how you ride, agree on your goals, and recommend a lesson format and schedule.</p>
    </div>
    <div class="cta-actions">
      <a class="btn" href="{EVAL}">Schedule an Evaluation Lesson</a>
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
