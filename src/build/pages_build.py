import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from ffchrome import chrome,assemble,write,LIB_CSS,band,pgrid,quote_tbd
os.chdir(os.environ['FF_OUT'])
PHONE_A='<a class="btn btn-ghost" href="tel:+15402741541">Call (540) 274-1541</a>'
JEV='/contact-us?interest=junior-riding-club'

FOCUS={'horse-training.jpg':'45% 50%','horse-rider.jpg':'58% 50%','about-farm.jpg':'60% 50%','junior-riding-club.jpg':'55% 50%'}

def hero(eyebrow,h1,text,cta,ghost,facts,img,alt,note):
    pos=f' style="object-position:{FOCUS[img]}"' if img in FOCUS else ''
    f='\n'.join(f'      <li><strong>{a}</strong> {b}</li>' for a,b in facts)
    return f'''<section class="hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <p class="eyebrow">{eyebrow}</p>
    <h1 id="hero-title">{h1}</h1>
    <p class="hero-text">{text}</p>
    <div class="hero-ctas">
      {cta}
      {ghost}
    </div>
    <ul class="hero-facts">
{f}
    </ul>
  </div>
  <figure class="ph ph--hero hero-media">
    <img src="images/{img}"{pos} alt="{alt}" fetchpriority="high" onerror="this.remove()">
    <div class="ph-note" aria-hidden="true"><span>Hero photograph</span>{note}</div>
  </figure>
</section>'''

def head(sid,cls,eyebrow,h2,lede,inner):
    return f'''<section id="{sid}" class="section {cls}" aria-labelledby="{sid}-title">
  <div class="wrap">
    <header class="sec-head">
      <div>
        <p class="eyebrow">{eyebrow}</p>
        <h2 id="{sid}-title">{h2}</h2>
      </div>
      <p class="lede">{lede}</p>
    </header>
{inner}
  </div>
</section>'''

def tri(items,two=False):
    cls='tri tri--2' if two else 'tri'
    return f'    <div class="{cls}">\n'+'\n'.join(f'      <div>\n        <h3>{h}</h3>\n        <p>{p}</p>\n      </div>' for h,p in items)+'\n    </div>'

def steps(items):
    n=len(items)
    return f'    <ol class="steps steps--{n}">\n'+'\n'.join(f'      <li class="step">\n        <span class="n" aria-hidden="true">{i}</span>\n        <h3>{h}</h3>\n        <p>{p}</p>\n      </li>' for i,(h,p) in enumerate(items,1))+'\n    </ol>'

def ticks(items):
    return '    <ul class="ticks">\n'+'\n'.join(f'      <li>{a}<span>{b}</span></li>' if b else f'      <li>{a}</li>' for a,b in items)+'\n    </ul>'

def split(sid,cls,eyebrow,h2,lede,right,extra=''):
    return f'''<section id="{sid}" class="section {cls}" aria-labelledby="{sid}-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">{eyebrow}</p>
      <h2 id="{sid}-title">{h2}</h2>
      <p class="lede">{lede}</p>{extra}
    </div>
{right}
  </div>
</section>'''

def quote(text,name,place,cls='deep'):
    return f'''<section class="section {cls}" aria-label="From a client">
  <div class="wrap">
    <figure class="quote-solo">
      <blockquote><p>“{text}”</p></blockquote>
      <figcaption><span class="q-name">{name}</span><span class="q-meta">{place}</span></figcaption>
    </figure>
  </div>
</section>'''

def faq(title,items,cls=''):
    d='\n'.join(f'      <details>\n        <summary>{q}</summary>\n        <p>{a}</p>\n      </details>' for q,a in items)
    return f'''<section id="faq" class="section {cls}" aria-labelledby="faq-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Questions</p>
      <h2 id="faq-title">{title}</h2>
      <p class="lede">Anything else, call <a href="tel:+15402741541">(540) 274-1541</a> or email <a href="mailto:info@forecastfarms.com">info@forecastfarms.com</a>.</p>
    </div>
    <div class="faq-list">
{d}
    </div>
  </div>
</section>'''

def cta(h2,p,btn):
    return f'''<section class="section band cta-band" aria-labelledby="cta-title">
  <div class="wrap">
    <div>
      <h2 id="cta-title">{h2}</h2>
      <p>{p}</p>
    </div>
    <div class="cta-actions">
      {btn}
      {PHONE_A}
    </div>
  </div>
</section>'''

def build(slug,fname,preview,title,body,css='',**ck):
    h,hd,ft,sc,tr=chrome(current=slug,**ck)
    page=assemble(h,LIB_CSS+css,hd,'<main id="main">\n'+body+'\n</main>',ft,sc,tr)
    write(fname,preview,title,page,'t_'+slug+'.html')
    return page

# ---------- Horse Training ----------
EV='/contact-us?interest=horse-training'
body='\n\n'.join([
hero('Horse Training','Horse and pony training in <em>Marshall, Virginia.</em>',
 'Denise rides your horse herself, on the flat and over fences, and keeps you posted. She gets the basics right at home first. Shows come when your horse is ready for them.',
 f'<a class="btn" href="{EV}">Schedule an Evaluation Lesson</a>','<a class="btn btn-ghost" href="#how">How It Works</a>',
 [('35+ years','training riders and horses in Marshall'),('Horses and ponies','young, green, off-track and made'),('Indoor arena','plus an outdoor all-weather ring')],
 'horse-training.jpg','A rider schooling a black horse at the canter on the flat','Trainer schooling a young horse'),
head('horses','paper','Horses we train','Horses and ponies we train','Denise starts with what your horse knows now and builds from there, whatever its age or experience.',
 tri([('Young and green horses','Rhythm, straightness and steering first, then a calm introduction to fences and new places.'),
      ('Off-track Thoroughbreds','Restarted at their own pace, with a second career in the hunter ring as the goal.'),
      ('Horses that need a tune-up','Tune-ups for horses that have lost rhythm or confidence, or that need sharpening before the season.'),
      ('Show prospects and ponies','Schooling for the hunter, jumper and equitation rings, including ponies being prepared for junior riders.')],two=True)),
band('images/horse-training-band.jpg','Denise schooling a horse in the outdoor ring','Schooling in the outdoor ring, wide'),
split('approach','','Our approach','How Denise trains a horse','Denise doesn’t rush a horse. The goal is a confident horse that understands its job and does it willingly.',
 ticks([('Schooling at home before shows','A new skill has to work in our ring before it’s tested at a show'),
        ('Flatwork underneath everything','Rhythm, straightness and adjustability come before height'),
        ('Confidence before pressure','Each new step comes when the horse is ready for it'),
        ('One plan for horse and rider','Denise sets goals that fit both you and your horse')])),
head('how','lilac','How it works','How horse training works','Every horse starts with an evaluation lesson. Training begins once you’ve agreed on a plan.',
 steps([('Evaluate','Denise rides or watches your horse to see its training, fitness and temperament, and hears your goals for it.'),
        ('Plan','You and Denise agree on goals, where your horse will be based and how often it’s ridden. That’s the plan for the season.'),
        ('Train','Denise rides your horse on the flat and over fences, and adds shows once it’s ready for them.'),
        ('Report and ride','Denise keeps you posted on how your horse is doing. Lessons on your horse let you feel the changes yourself.')])),
pgrid('Horse training at Forecast Farms',[
 ('images/horse-training-grid-1.jpg','A young horse on the lunge line','A young horse on the lunge'),
 ('https://assets.cdn.filesafe.space/yFHRGgbUYoTRIY9XZIJQ/media/6adc546bd542268bb4f4f358.jpg','Trainer coaching a rider and horse at the rail','Trainer at the rail'),
 ('images/horse-training-grid-3.jpg','A horse over a small fence','A green horse over a small fence')]),
quote('Wonderful environment and scenery with one of the best trainers I have had the chance to work under','Isabelle G.','Google review'),
faq('About Horse Training',[
 ('Does my horse need to stay at the farm?','It depends on the plan. Tell us where your horse lives when you request an evaluation lesson, and Denise will talk through the options with you.'),
 ('How often will my horse be ridden?','It depends on your horse’s age, fitness and goals. You and Denise set the schedule when you agree on the plan.'),
 ('Will I still ride my horse?','Yes, and we recommend it. Lessons on your horse teach you to ride it the way it’s being trained.'),
 ('Do you train ponies?','Yes. Denise trains horses and ponies, including ponies being prepared for junior riders.'),
 ('Can you get my horse ready to sell?','Yes. Through consignment, Denise keeps your horse in work and shows it to buyers it suits, under a written agreement. See <a href="/sales">Horse Search &amp; Sales</a>.'),
 ('What does it cost?','It depends on the training plan. Denise confirms the price after your evaluation lesson.')]),
cta('Start with an <em>evaluation lesson.</em>','Book an evaluation lesson for your horse, and Denise will recommend a training plan for the season.',f'<a class="btn" href="{EV}">Schedule an Evaluation Lesson</a>'),
])
build('training','forecast-farms-horse-training-ghl.html','preview-horse-training.html','Forecast Farms Horse Training',body,cta_href=EV)

# ---------- Horse + Rider Development ----------
EV='/contact-us?interest=horse-rider-development'
body='\n\n'.join([
hero('Horse + Rider Development','One plan <em>for both of you.</em>',
 'Denise sets goals for you and your horse together, then plans your lessons and her training rides around them for the season.',
 f'<a class="btn" href="{EV}">Schedule an Evaluation Lesson</a>','<a class="btn btn-ghost" href="#included">What’s Included</a>',
 [('Training rides','by Denise herself'),('Lessons','on your own horse'),('Show plans','target shows and divisions chosen with you')],
 'horse-rider.jpg','A rider in show attire jumping a grey horse over a white fence','Horse and rider in the show ring'),
head('who','paper','Who it’s for','For owners who train with their own horse','It’s for owners who want their horse and their own riding to move forward together.',
 tri([('New partnerships','You’ve just bought or leased a horse and want help getting used to each other.'),
      ('Moving up','You want to move up a height or division, and you want your horse ready for it too.'),
      ('Competing pairs','You show, and you want a season plan with goals for both of you, reviewed as you go.')])),
band('images/horse-rider-band.jpg','Horse and rider warming up at a show','Warming up at a show, wide'),
split('included','','What’s included','Lessons and training rides in one program','Rider Training and Horse Training run as one program. What Denise teaches your horse in a training ride is what you practice in your next lesson.',
 ticks([('Rider lessons on your horse','Private or semi-private, built around the training plan'),
        ('Training rides for your horse','Denise schools your horse on what you’re working on in your lessons'),
        ('A season plan','Goals, target shows and divisions, set with you at the start of the season'),
        ('Progress reviews','You and Denise check horse and rider against the plan at each stage'),
        ('Show preparation as a pair','Course walks, warm-ups and a plan for each class')])),
head('season','lilac','The season','Plan, train, compete and review','Each season follows the same cycle, so you always know what you are working on and why.',
 steps([('Set the plan','The season starts with an evaluation lesson for horse and rider. You and Denise agree on goals and choose target shows and divisions.'),
        ('Train and review','Your lessons and Denise’s training rides work toward the plan. Denise adjusts the plan when something isn’t working.'),
        ('Compete and reflect','After each show, you and Denise go over what went well and what needs work, and update the plan.')])),
pgrid('Horse and rider at Forecast Farms',[
 ('images/horse-rider-grid-1.jpg','Denise riding a client’s horse','A training ride by Denise'),
 ('images/horse-rider-grid-2.jpg','The owner riding the same horse in a lesson','The owner in a lesson on that horse'),
 ('images/horse-rider-grid-3.jpg','Walking a course at a show','Walking the course together')],cls='paper'),
quote('I especially appreciate how much they emphasize the safety of both horse and rider in every lesson.','Julia T.','Google review'),
faq('About Horse + Rider Development',[
 ('How is this different from Rider Training and Horse Training?','It combines them under one plan. Your lessons and Denise’s training rides on your horse are scheduled together and work toward the same goals.'),
 ('Do I have to show?','No. Most pairs in this program want to show, but the same plan works for a new pair building confidence first.'),
 ('Which shows do you go to?','That depends on your level and goals. You and Denise choose the shows and set the calendar at the start of the season.'),
 ('What does it cost?','It depends on the plan for horse and rider. Denise confirms the price after your evaluation lesson.')],cls='paper'),
cta('Start with an <em>evaluation lesson.</em>','In one lesson, Denise watches you and your horse together, then recommends a plan for the season.',f'<a class="btn" href="{EV}">Schedule an Evaluation Lesson</a>'),
])
build('horse-rider-development','forecast-farms-horse-rider-ghl.html','preview-horse-rider-development.html','Forecast Farms Horse + Rider',body,cta_href=EV)

# ---------- Horse Search & Sales ----------
EV='/contact-us?interest=horse-search'
body='\n\n'.join([
hero('Horse Search &amp; Sales','Horses and ponies for sale and lease in <em>Marshall, Virginia.</em>',
 'Whether you are buying, leasing or selling, we bring the same judgment we train with: matching the horse to the rider and the rider’s goals.',
 f'<a class="btn" href="{EV}">Start a Horse Search</a>','<a class="btn btn-ghost" href="#search">How a Search Works</a>',
 [('Buy','with full-service search'),('Lease','horses and ponies'),('Sell','through consignment')],
 'horse-sales.jpg','A rider trying a sales horse in the ring','A rider trying a sales horse'),
head('search','paper','Horse search','How a horse search works','We help from the first conversation, through the vet check, to bringing your new horse home.',
 steps([('Assess','We start with the rider: level, goals, budget, and the kind of horse that will help them progress.'),
        ('Search','We look for horses and ponies that fit, and arrange for you to see and try them.'),
        ('Vet','We guide you through a pre-purchase examination by a veterinarian of your choice.'),
        ('Bring home','We help arrange delivery, so your new horse arrives home ready to start work.')])),
band('images/sales-band.jpg','A sales horse being shown in the ring','A sales horse in the ring, wide'),
split('available','','Sales and leasing','Horses and ponies for sale or lease','We offer a selection of green and made horses and ponies for sale or lease. Our list changes often, so tell us what you are looking for and we will share the horses that fit.',
 ticks([('Professionally trained and handled',''),
        ('Trailer, clip, cross-tie and stand quietly','Good manners on the ground as well as under saddle'),
        ('Strengths and needs described','What each horse has done, and what it still needs'),
        ('References available','From riders who have bought or leased from us')]),
 extra=f'\n      <a class="link-arrow" href="{EV}">Ask about current horses</a>'),
split('consign','lilac','Consignment','Selling a horse through consignment','We accept horses for consignment, keep them in consistent work, and show them to buyers they suit.',
 ticks([('Kept in work','Training rides that keep the horse sharp and show it at its best'),
        ('The whole picture for buyers','Buyers hear what the horse is and what it needs'),
        ('Matched to buyers it suits','We look for a home where the horse will succeed'),
        ('Terms in writing','Every consignment has a written agreement')])),
pgrid('Sales horses at Forecast Farms',[
 ('images/sales-grid-1.jpg','A rider trying a horse','A rider trying a horse'),
 ('images/sales-grid-2.jpg','A pony standing quietly in the cross-ties','Quiet in the cross-ties'),
 ('images/sales-grid-3.jpg','A horse loading onto a trailer','Loading on the trailer')]),
quote_tbd(),
faq('About buying, leasing and selling',[
 ('Can I see the horses you have for sale?','Yes. Our list changes often, so contact us with what you are looking for and we will share the horses currently available.'),
 ('Should I get a pre-purchase exam?','Yes. We strongly recommend a pre-purchase examination by a veterinarian of your choice for every purchase or lease.'),
 ('Do you lease ponies?','Yes. We lease horses and ponies, which is a practical step for riders who are not ready to buy.'),
 ('How does consignment work?','Your horse stays in work while we show it to buyers it suits. Terms are set out in a written agreement before the horse arrives.')],cls='paper'),
cta('Tell us what you’re <em>looking for.</em>','Share the rider’s level, goals and budget, and we will start the search.',f'<a class="btn" href="{EV}">Start a Horse Search</a>'),
])
build('sales','forecast-farms-sales-ghl.html','preview-sales.html','Forecast Farms Horse Sales',body,cta_href=EV)

# ---------- About ----------
EV='/contact-us'
ABOUT_CSS='''
.ff .bio{display:grid;gap:3rem 5rem;align-items:start}
.ff .bio>*{min-width:0}
.ff .bio .ph{aspect-ratio:4/5}
.ff .bio h2{margin-bottom:1.5rem}
.ff .bio-copy>p{color:var(--fg-soft);max-width:34em}
.ff .bio-copy>p+p{margin-top:1rem}
.ff .bio-copy .d-note{margin-top:2.25rem}
.ff .record{display:grid;gap:2rem 3rem;margin-top:2.5rem}
.ff .record h3{margin-bottom:.75rem;font:600 .7rem/1.2 var(--sans);letter-spacing:.16em;text-transform:uppercase;color:var(--saddle)}
.ff .record li{padding:.7rem 0;border-top:1px solid var(--line);font-size:.95rem;line-height:1.5}
.ff .record li:last-child{border-bottom:1px solid var(--line)}
.ff .record li span{display:block;font-size:.875rem;color:var(--fg-soft)}
@media (min-width:640px){.ff .record{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1000px){.ff .bio{grid-template-columns:minmax(0,4fr) minmax(0,7fr)}.ff .bio .ph{position:sticky;top:calc(72px + 2rem)}}
'''
bio='''<section id="denise" class="section paper" aria-labelledby="denise-title">
  <div class="wrap bio">
    <figure class="ph">
      <img src="images/denise-finch.jpg" alt="Denise Finch, head trainer at Forecast Farms" loading="lazy" onerror="this.remove()">
      <div class="ph-note" aria-hidden="true"><span>Photograph</span>Denise Finch</div>
    </figure>
    <div class="bio-copy">
      <p class="eyebrow">Head trainer</p>
      <h2 id="denise-title">Denise Finch</h2>
      <p>Denise has ridden since childhood. She trained at the J.E.S. School in Vienna, Virginia, and built a competition record across ponies, equitation, hunters and jumpers.</p>
      <p>As a trainer, she has educated many successful riders and horses, and clients value her eye for future show ring prospects. Her lessons are known for clear, uncomplicated instruction that covers the fundamentals riders need to move up, with close attention to both horse and rider.</p>
      <figure class="d-note">
        <p class="draft-tag">Draft: waiting for Denise’s approval</p>
        <blockquote><p>“Safety comes first here, for the horse and for the rider. After that, I want horse and rider to improve together, because neither gets far without the other. The best way to see how we work is an evaluation lesson.”</p></blockquote>
        <figcaption><span class="q-name">Denise Finch</span><span class="q-meta">Head trainer, Forecast Farms</span></figcaption>
      </figure>
      <div class="record">
        <div>
          <h3>In the saddle</h3>
          <ul>
            <li>Upperville Horse Show<span>Champion, Local Pony Hunter</span></li>
            <li>Washington International Horse Show<span>Local Day finalist</span></li>
            <li>Pony Finals<span>Champion</span></li>
            <li>Dominion Saddlery<span>High Point Champion Jumper, two years running</span></li>
            <li>Equitation 15–17<span>Champion over fences and under saddle</span></li>
          </ul>
        </div>
        <div>
          <h3>As a trainer</h3>
          <ul>
            <li>Regional year-end championships<span>Riders and horses in pony hunter, special junior/amateur and adult divisions</span></li>
            <li>High-point trainer recognition<span>Regional year-end standings</span></li>
            <li>Professional Rider award</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>'''
visit='''    <section class="visit" aria-labelledby="visit-title">
      <h3 id="visit-title">Visit the farm</h3>
      <p>Come for an evaluation lesson to see the farm and ride with Denise.</p>
      <dl>
        <div><dt>Address</dt><dd>2497 Atoka Road<br>Marshall, VA 20115</dd></div>
        <div><dt>Phone</dt><dd><a href="tel:+15402741541">(540) 274-1541</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:info@forecastfarms.com">info@forecastfarms.com</a></dd></div>
      </dl>
      <a class="link-arrow" href="https://www.google.com/maps/dir/?api=1&amp;destination=2497+Atoka+Rd+Marshall+VA+20115" target="_blank" rel="noopener">Get directions</a>
    </section>'''
body='\n\n'.join([
hero('About Forecast Farms','A family farm in <em>Virginia hunt country.</em>',
 'A family-owned hunter, jumper and equitation program on Atoka Road in Marshall, led by trainer Denise Finch. For more than 35 years: safety first, then horse and rider improving together.',
 f'<a class="btn" href="{EV}">Schedule an Evaluation Lesson</a>','<a class="btn btn-ghost" href="#denise">Meet Denise</a>',
 [('35+ years','training riders and horses'),('Family-owned','in Marshall, Virginia'),('Year-round','indoor and outdoor rings')],
 'about-farm.jpg','A rider on a grey horse in front of the barn at Forecast Farms','The barn and rings on Atoka Road'),
bio,
band('images/about-band.jpg','The rings and countryside around Forecast Farms','The rings and hunt country, wide'),
head('farm','','The farm','Indoor arena, all-weather ring and barn','Facilities that keep training going in every season, in Fauquier County hunt country.',
 tri([('Indoor arena','Rubberized footing for year-round riding, whatever the weather.'),
      ('Outdoor all-weather ring','Room to school courses and ride in the open through the season.'),
      ('The barn','A 14-stall barn where horses in the program are cared for every day.')])),
head('values','lilac','How we work','How we work with horses and riders','Programs and horses change over the years. These priorities have stayed the same.',
 tri([('Safety first','Horses matched to each rider, sound fundamentals and close supervision come before everything else.'),
      ('Horse and rider together','We develop the horse and the rider at the same time, because neither progresses far without the other.'),
      ('Plain feedback','You always know what you are working on, what is improving and what still needs work.')])),
pgrid('Life at Forecast Farms',[
 ('images/about-grid-1.jpg','The farm entrance on Atoka Road','The farm entrance'),
 ('images/about-grid-2.jpg','Horses turned out in the paddock','Horses in the paddock'),
 ('images/about-grid-3.jpg','Inside the 14-stall barn','Inside the barn')],cls='paper'),
quote('Her professionalism and experience are second to none - she is a superb trainer who teaches at an individual level, with a care and investment in her students that comes directly from the heart.','Jenn W.','Google review'),
f'''<section id="visit" class="section" aria-labelledby="visit-sec-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Find us</p>
      <h2 id="visit-sec-title">Find the farm on Atoka Road in Marshall</h2>
      <p class="lede">We are in Fauquier County, Virginia. The best first step is an evaluation lesson, where you can see the farm and ride with Denise.</p>
    </div>
{visit}
  </div>
</section>''',
cta('Start with an <em>evaluation lesson.</em>','One lesson to see where you are, agree on goals and recommend the right training.',f'<a class="btn" href="{EV}">Schedule an Evaluation Lesson</a>'),
])
build('about-us','forecast-farms-about-ghl.html','preview-about.html','Forecast Farms About',body,css=ABOUT_CSS,cta_href=EV)

# ---------- Junior Riding Club ----------
JRC_CSS='''
.ff .plans{display:grid;gap:1.25rem}
.ff .plan{display:flex;flex-direction:column;min-width:0;padding:clamp(1.5rem,2.5vw,2rem);background:var(--surface);border-top:2px solid var(--line-strong);border-radius:2px}
.ff .plan--mid{border-top-color:var(--accent)}
.ff .plan h3{font-size:1.75rem}
.ff .plan .price{margin-top:.6rem;font:400 2.4rem/1 var(--serif);color:var(--fg);font-variant-numeric:tabular-nums}
.ff .plan .price span{font:400 .9rem/1 var(--sans);color:var(--fg-soft)}
.ff .plan .plan-sub{margin-top:.5rem;font-size:.9rem;color:var(--fg-soft)}
.ff .plan ul{margin-top:1.25rem}
.ff .plan li{position:relative;padding:.6rem 0 .6rem 1.4rem;border-top:1px solid var(--line);font-size:.925rem;line-height:1.5}
.ff .plan li::before{content:"";position:absolute;left:.15rem;top:1.05rem;width:.4rem;height:.4rem;border-radius:50%;background:var(--accent)}
.ff .plans-note{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:1rem 2rem;margin-top:1.5rem;padding:1.25rem 1.5rem;background:var(--surface);border-radius:2px}
.ff .plans-note p{color:var(--fg)}
.ff .plans-note strong{font:400 1.35rem/1 var(--serif)}
@media (min-width:900px){.ff .plans{grid-template-columns:repeat(3,minmax(0,1fr))}}
.ff .sm-pair{display:grid;gap:2rem}
@media (min-width:600px){.ff .sm-pair{grid-template-columns:repeat(2,minmax(0,1fr))}}
'''
BOOK_BTN=f'<a class="btn" href="{JEV}">Schedule an Evaluation Lesson</a>'
def plan(name,price,sub,items,mid=False):
    li='\n'.join(f'          <li>{x}</li>' for x in items)
    return f'''      <div class="plan{' plan--mid' if mid else ''}">
        <h3>{name}</h3>
        <p class="price">${price}<span> / month</span></p>
        <p class="plan-sub">{sub}</p>
        <ul>
{li}
        </ul>
      </div>'''
plans=f'''    <div class="plans">
{plan('Bronze',375,'Four lessons a month',['4 riding lessons per month','1 unmounted lesson per month','Custom progress sheets','Private online community','Horsesense learning levels curriculum'])}
{plan('Silver',700,'Eight lessons a month',['Everything in Bronze','8 riding lessons per month','1 practice ride per month for riders at Blue level and above'],mid=True)}
{plan('Gold',900,'Twelve lessons a month',['Everything in Silver','12 riding lessons per month','2 practice rides per month for riders at Orange level and above'])}
    </div>
    <div class="plans-note">
      <p>New to the club? Every rider starts with an evaluation lesson to find the right level and plan.</p>
      {BOOK_BTN}
    </div>'''
def pony(slug,name,typ,text):
    return f'''      <article class="sm">
        <figure class="ph"><img src="images/schoolmaster-{slug}.jpg" alt="{name}, a lesson pony at Forecast Farms" loading="lazy" onerror="this.remove()"><div class="ph-note" aria-hidden="true"><span>Photograph</span>{name}</div></figure>
        <p class="sm-type">{typ}</p>
        <h3>{name}</h3>
        <p>{text}</p>
      </article>'''
ponies='    <div class="sm-pair">\n'+pony('chief','Chief','Pony of the Americas · 13.0 hands','The farm’s most popular lesson pony, and a steady first partner for young riders.')+'\n'+pony('audrey','Princess Audrey','Welsh pony cross mare · 12.2 hands','With Denise since she was two, shown at local and recognized shows, and a favorite with young riders.')+'\n    </div>'
body='\n\n'.join([
hero('Junior Riding Club · Ages 4 to 7','Riding lessons for ages 4 to 7 in <em>Marshall, Virginia.</em>',
 'Safe, confidence-building lessons with a level-by-level curriculum. Young riders learn to ride and to care for horses, on ponies chosen for the job.',
 BOOK_BTN,'<a class="btn btn-ghost" href="#plans">See Plans</a>',
 [('Ages 4–7','lessons built for young riders'),('Level by level','progress you can see'),('Ponies','chosen for young riders')],
 'junior-riding-club.jpg','A young rider on a lesson pony with an instructor','Young rider on a lesson pony'),
head('learn','paper','What riders learn','Riding, horse care and safety','Every rider follows the same curriculum, one level at a time, so parents always know what their rider is working on.',
 tri([('Riding basics','Balance, steering and a secure position at the walk and trot, then the canter as each rider is ready.'),
      ('Horse care','Grooming, tacking up and safe handling, taught in unmounted lessons as well as in the saddle.'),
      ('Safety habits','How to move around horses, lead them, and behave in the barn and the ring.'),
      ('Confidence','Small, clear goals at each level, so every rider knows what they have achieved.')],two=True)),
band('images/junior-riding-club-band.jpg','Young riders on ponies in the indoor arena','Young riders in the indoor arena, wide'),
head('plans','','Plans','Monthly plans','Every plan includes the full curriculum and progress sheets. More lessons mean faster progress through the levels.',plans),
head('ponies','lilac','The ponies','The lesson ponies','Young riders learn on patient, steady ponies suited to their size.',ponies),
pgrid('The Junior Riding Club',[
 ('images/junior-riding-club-grid-1.jpg','A young rider grooming a pony','Grooming before the lesson'),
 ('images/junior-riding-club-grid-2.jpg','A young rider leading a pony','Leading a pony'),
 ('images/junior-riding-club-grid-3.jpg','A young rider at the trot','First trot')]),
quote_tbd(),
split('next','paper','Moving up','After the Junior Riding Club','Riders who outgrow the club move into Rider Training with the same trainer, toward the hunter, jumper and equitation rings.',
 ticks([('Same trainer, same standards','Riders keep working with the person who knows them'),
        ('Progress that follows the rider','Their levels and progress sheets carry forward'),
        ('A path to the show ring','Showing becomes an option when the rider is ready')]),
 extra='\n      <a class="link-arrow" href="/rider-training">See Rider Training</a>'),
faq('For parents',[
 ('What should my rider wear?','A properly fitted, ASTM/SEI-certified riding helmet, boots with a heel, and long pants or riding tights.'),
 ('How do riders move up a level?','Each level has clear skills to master. When a rider is ready, they move to the next level, and you see it on their progress sheet.'),
 ('What is a practice ride?','Extra time in the saddle to work on skills from lessons. Practice rides are included in the Silver and Gold plans for riders at the levels listed.'),
 ('What happens at the evaluation lesson?','Your rider rides with an instructor so we can see where they are, and we recommend the right starting level and plan. It is also a chance for you to see how the club works.'),
 ('My rider is 8 or older. Where do they start?','Riders 8 and older start with an evaluation lesson for <a href="/rider-training">Rider Training</a>. <a href="/contact-us?interest=rider-training">Request an evaluation</a>.')]),
cta('Start with an <em>evaluation lesson.</em>','One lesson to find your rider’s starting level and the plan that fits.',BOOK_BTN),
])
build('lessons','forecast-farms-junior-riding-club-ghl.html','preview-junior-riding-club.html','Forecast Farms Junior Riding Club',body,css=JRC_CSS,cta_href=JEV)
print('built 5 pages')
