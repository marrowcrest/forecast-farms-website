import os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from ffchrome import chrome,assemble,write,LIB_CSS
os.chdir(os.environ['FF_OUT'])
PHONE_A='<a class="btn btn-ghost" href="tel:+15402741541">Call (540) 274-1541</a>'
JEV='/contact-us?interest=junior-riding-club'

def hero(eyebrow,h1,text,cta,ghost,facts,img,alt,note):
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
    <img src="images/{img}" alt="{alt}" fetchpriority="high" onerror="this.remove()">
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

def quote(text,name,place,cls='paper'):
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
hero('Horse Training','Your horse’s education, <em>moved forward.</em>',
 'Correct, consistent schooling for young, green and experienced horses and ponies, from the trainer who also coaches you. Skills are built at home, and shows give your horse the experience to match.',
 f'<a class="btn" href="{EV}">Schedule a Horse Evaluation</a>','<a class="btn btn-ghost" href="#how">How It Works</a>',
 [('Young and green','horses started correctly'),('Tune-ups','for experienced horses'),('Show mileage','when the horse is ready')],
 'horse-training.jpg','Trainer schooling a young horse on the flat','Trainer schooling a young horse'),
head('horses','paper','Horses we train','Every horse starts <em>where it is.</em>','We train horses and ponies at every stage, with the same priorities: correct basics, confidence, and a horse that is willing to do its job.',
 tri([('Young and green horses','Correct basics from the start: rhythm, straightness, steering, and a calm introduction to fences and new places.'),
      ('Off-track Thoroughbreds','Patient restarting for horses coming off the track, building toward a second career in the hunter ring.'),
      ('Experienced horses','Tune-ups for horses that have lost rhythm or confidence, or that need sharpening before the season.'),
      ('Show prospects and ponies','Preparation for the hunter, jumper and equitation rings, with show experience added as the horse is ready.')],two=True)),
split('approach','','Our approach','Honesty and patience, <em>and a horse that wants to work.</em>','Training is built on honesty, integrity and patience. The goal is a confident horse that understands its job and does it willingly.',
 ticks([('Schooling at home before shows','Skills are confirmed in our ring before they are tested away from home'),
        ('Flatwork underneath everything','Rhythm, straightness and adjustability come before height'),
        ('Confidence before pressure','Each new question is introduced when the horse is ready for it'),
        ('One trainer for horse and rider','The person schooling your horse also coaches you')])),
head('how','lilac','How it works','From evaluation <em>to a better ride.</em>','Every horse starts with an evaluation, and every plan is agreed with the owner before training begins.',
 steps([('Evaluate','Denise rides or watches your horse to assess its training and way of going, and hears your goals for the horse.'),
        ('Plan','Together we agree on goals, where the horse will be based, and how often it is ridden, then set a plan for the season.'),
        ('Train','Training rides on the flat and over fences, with show outings added once the horse is ready for them.'),
        ('Report and ride','You hear how the horse is progressing, and lessons on your own horse let you feel the changes for yourself.')])),
quote('As a trainer she has educated many successful riders and horses.','Richard I.','Charlottesville, Virginia'),
faq('About Horse Training',[
 ('Does my horse need to stay at the farm?','Where your horse is based is part of the training plan. Tell us your situation when you request an evaluation, and we will talk through the options.'),
 ('How often will my horse be ridden?','That depends on the horse’s age, fitness and goals. We set the schedule with you when we agree on the plan.'),
 ('Will I still ride my horse?','Yes, and we recommend it. Lessons on your own horse turn the training into a partnership you can ride.'),
 ('Do you train ponies?','Yes. We train horses and ponies, including ponies being prepared for junior riders.'),
 ('Can you get my horse ready to sell?','Yes. Horses in our consignment program are kept in work and presented to suitable buyers. See <a href="/sales">Horse Search &amp; Sales</a>.'),
 ('What does it cost?','Pricing depends on the training plan. We confirm it after your horse’s evaluation.')]),
cta('Start with a <em>horse evaluation.</em>','Bring your horse for an evaluation, and we will recommend a training plan for the season.',f'<a class="btn" href="{EV}">Schedule a Horse Evaluation</a>'),
])
build('training','forecast-farms-horse-training-ghl.html','preview-horse-training.html','Forecast Farms Horse Training',body,cta_href=EV)

# ---------- Horse + Rider Development ----------
EV='/contact-us?interest=horse-rider-development'
body='\n\n'.join([
hero('Horse + Rider Development','One plan <em>for both of you.</em>',
 'For pairs that need to progress together: the horse’s way of going and the rider’s effectiveness trained as one partnership, toward the same goals for the season.',
 f'<a class="btn" href="{EV}">Schedule an Evaluation</a>','<a class="btn btn-ghost" href="#included">What’s Included</a>',
 [('One plan','for horse and rider'),('Season goals','set and reviewed'),('Show-ready','as a pair')],
 'horse-rider.jpg','A horse and rider competing in the hunter ring','Horse and rider in the show ring'),
head('who','paper','Who it’s for','For partnerships <em>with somewhere to go.</em>','Horse + Rider Development suits owners who want their horse and their own riding to move forward on the same timeline.',
 tri([('New partnerships','You have just bought or leased a horse and want the two of you on the same page quickly.'),
      ('Moving up','You are ready for a new height or division and want horse and rider prepared for it together.'),
      ('Competing pairs','You show, and you want a season plan with goals for both of you, reviewed as you go.')])),
split('included','','What’s included','Lessons and training rides, <em>planned together.</em>','Rider Training and Horse Training run as one program, so what the horse learns in a training ride is what the rider practices in the next lesson.',
 ticks([('Rider lessons on your horse','Private or semi-private, built around the training plan'),
        ('Training rides for your horse','Schooling that prepares the horse for what you are working on'),
        ('A season plan','Goals, target shows and divisions, set at the start of the season'),
        ('Progress reviews','Regular check-ins on horse and rider against the plan'),
        ('Show preparation as a pair','Course walks, warm-ups and a plan for each class')])),
head('season','lilac','The season','A plan you can see, <em>and adjust.</em>','Each season follows the same cycle, so you always know what you are working on and why.',
 steps([('Set the plan','At the start of the season we evaluate horse and rider, agree on goals, and choose target shows and divisions.'),
        ('Train and review','Lessons and training rides work toward the plan. We review progress at each stage and adjust when needed.'),
        ('Compete and reflect','After each show we look at what went well and what needs work, and fold it back into the plan.')])),
faq('About Horse + Rider Development',[
 ('How is this different from Rider Training and Horse Training?','It combines them under one plan. The horse’s training and the rider’s lessons are scheduled together and measured against the same goals.'),
 ('Do I have to show?','Most pairs in this program have competition goals, but the same plan works for a new partnership that wants to build confidence first.'),
 ('Which shows do you go to?','We choose shows that fit each pair’s level and goals, and set the calendar with you at the start of the season.'),
 ('What does it cost?','Pricing depends on the plan for horse and rider. We confirm it after your evaluation.')],cls='paper'),
cta('Start with an <em>evaluation.</em>','We evaluate horse and rider together, then recommend a plan for the season.',f'<a class="btn" href="{EV}">Schedule an Evaluation</a>'),
])
build('horse-rider-development','forecast-farms-horse-rider-ghl.html','preview-horse-rider-development.html','Forecast Farms Horse + Rider',body,cta_href=EV)

# ---------- Horse Search & Sales ----------
EV='/contact-us?interest=horse-search'
body='\n\n'.join([
hero('Horse Search &amp; Sales','The right horse, <em>matched with care.</em>',
 'Whether you are buying, leasing or selling, we bring the same judgment we train with: matching the horse to the rider and the rider’s goals.',
 f'<a class="btn" href="{EV}">Start a Horse Search</a>','<a class="btn btn-ghost" href="#search">How a Search Works</a>',
 [('Buy','with full-service search'),('Lease','horses and ponies'),('Sell','through consignment')],
 'horse-sales.jpg','A rider trying a sales horse in the ring','A rider trying a sales horse'),
head('search','paper','Horse search','From first conversation <em>to bringing your horse home.</em>','We help from the first assessment of what you need, through the vetting process, to delivering your new horse home.',
 steps([('Assess','We start with the rider: level, goals, budget, and the kind of horse that will help them progress.'),
        ('Search','We look for horses and ponies that fit, and arrange for you to see and try them.'),
        ('Vet','We guide you through a pre-purchase examination by a veterinarian of your choice.'),
        ('Bring home','We help arrange delivery, so your new horse arrives home ready to start work.')])),
split('available','','Sales and leasing','Horses ready <em>for their next rider.</em>','We offer a selection of green and made horses and ponies for sale or lease. Our list changes often, so tell us what you are looking for and we will share the horses that fit.',
 ticks([('Professionally trained and handled',''),
        ('Trailer, clip, cross-tie and stand quietly','Good manners on the ground as well as under saddle'),
        ('Described honestly','Strengths, needs and experience, as we know them'),
        ('References available','From riders who have bought or leased from us')]),
 extra=f'\n      <a class="link-arrow" href="{EV}">Ask about current horses</a>'),
split('consign','lilac','Consignment','Selling a horse? <em>Consign it with us.</em>','We accept horses for consignment, keep them in consistent work, and present them to buyers who suit them, so your horse sells to the right home.',
 ticks([('Kept in work','Training rides that keep the horse sharp and show it at its best'),
        ('Presented honestly','Buyers hear what the horse is and what it needs'),
        ('Matched to suitable buyers','We look for a home where the horse will succeed'),
        ('Terms in writing','Every consignment has a written agreement')])),
faq('About buying, leasing and selling',[
 ('Can I see the horses you have for sale?','Yes. Our list changes often, so contact us with what you are looking for and we will share the horses currently available.'),
 ('Should I get a pre-purchase exam?','Yes. We strongly recommend a pre-purchase examination by a veterinarian of your choice for every purchase or lease.'),
 ('Do you lease ponies?','Yes. We lease horses and ponies, which is a practical step for riders who are not ready to buy.'),
 ('How does consignment work?','Your horse stays in work while we present it to suitable buyers. Terms are set out in a written agreement before the horse arrives.')],cls='paper'),
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
      <h2 id="denise-title">Denise <em>Finch</em></h2>
      <p>Denise has ridden since childhood. She trained at the J.E.S. School in Vienna, Virginia, and built a competition record across ponies, equitation, hunters and jumpers.</p>
      <p>As a trainer, she has educated many successful riders and horses, and clients value her eye for future show ring prospects. Her lessons are known for clear, uncomplicated instruction that covers the fundamentals riders need to move up, with close attention to both horse and rider.</p>
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
visit='''    <aside class="visit" aria-labelledby="visit-title">
      <h3 id="visit-title">Visit the farm</h3>
      <p>Come for an evaluation lesson to see the farm and ride with Denise.</p>
      <dl>
        <div><dt>Address</dt><dd>2497 Atoka Road<br>Marshall, VA 20115</dd></div>
        <div><dt>Phone</dt><dd><a href="tel:+15402741541">(540) 274-1541</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:info@forecastfarms.com">info@forecastfarms.com</a></dd></div>
      </dl>
      <a class="link-arrow" href="https://www.google.com/maps/search/?api=1&amp;query=2497+Atoka+Rd+Marshall+VA+20115" target="_blank" rel="noopener">Get directions</a>
    </aside>'''
body='\n\n'.join([
hero('About Forecast Farms','A family farm in <em>Virginia hunt country.</em>',
 'Forecast Farms is a family-owned Hunter, Jumper and Equitation program on Atoka Road in Marshall, led by trainer Denise Finch. For more than 35 years, the farm has trained riders and horses with the same priorities: safety first, then the development of horse and rider together.',
 f'<a class="btn" href="{EV}">Schedule an Evaluation</a>','<a class="btn btn-ghost" href="#denise">Meet Denise</a>',
 [('35+ years','training riders and horses'),('Family-owned','in Marshall, Virginia'),('Year-round','indoor and outdoor rings')],
 'about-farm.jpg','The barn and riding rings at Forecast Farms in Marshall, Virginia','The barn and rings on Atoka Road'),
bio,
head('farm','','The farm','Built for <em>year-round training.</em>','The farm sits in Fauquier County hunt country, with facilities that keep training consistent through every season.',
 tri([('Indoor arena','Rubberized footing for year-round riding, whatever the weather.'),
      ('Outdoor all-weather ring','Room to school courses and ride in the open through the season.'),
      ('The barn','A 14-stall barn where horses in the program are cared for every day.')])),
head('values','lilac','How we work','Three things <em>that do not change.</em>','Programs and horses change over the years. These priorities have stayed the same.',
 tri([('Safety first','Suitable horses, sound fundamentals and close supervision come before everything else.'),
      ('Horse and rider together','We develop the horse and the rider at the same time, because neither progresses far without the other.'),
      ('Plain feedback','You always know what you are working on, what is improving and what still needs work.')])),
quote('At Forecast Farms Denise makes you feel like family every time.','Beth P.','The Plains, Virginia'),
f'''<section id="visit" class="section" aria-labelledby="visit-sec-title">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Find us</p>
      <h2 id="visit-sec-title">On Atoka Road, <em>in Marshall.</em></h2>
      <p class="lede">We are in Fauquier County, Virginia. The best first step is an evaluation lesson, where you can see the farm and ride with Denise.</p>
    </div>
{visit}
  </div>
</section>''',
cta('Start with an <em>evaluation lesson.</em>','One lesson to see where you are, agree on goals and recommend the right training.',f'<a class="btn" href="{EV}">Schedule an Evaluation</a>'),
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
hero('Junior Riding Club · Ages 4 to 7','Where young riders <em>start right.</em>',
 'Safe, structured, confidence-building lessons for riders ages 4 to 7. Young riders learn to ride and to care for horses through a level-by-level curriculum, on ponies chosen for the job.',
 BOOK_BTN,'<a class="btn btn-ghost" href="#plans">See Plans</a>',
 [('Ages 4–7','safe, structured lessons'),('Level by level','progress you can see'),('Ponies','chosen for young riders')],
 'junior-riding-club.jpg','A young rider on a lesson pony with an instructor','Young rider on a lesson pony'),
head('learn','paper','What riders learn','Skills in the saddle, <em>and around the barn.</em>','Every rider follows the same curriculum, one level at a time, so parents always know what their rider is working on.',
 tri([('Riding basics','Balance, steering and a secure position at the walk and trot, then the canter as each rider is ready.'),
      ('Horse care','Grooming, tacking up and safe handling, taught in unmounted lessons as well as in the saddle.'),
      ('Safety habits','How to move around horses, lead them, and behave in the barn and the ring.'),
      ('Confidence','Small, clear goals at each level, so every rider knows what they have achieved.')],two=True)),
head('plans','','Plans','Choose how often <em>your rider rides.</em>','Every plan includes the full curriculum and progress sheets. More lessons mean faster progress through the levels.',plans),
head('ponies','lilac','The ponies','Ponies chosen <em>for young riders.</em>','Young riders learn on experienced ponies that are patient, steady and suited to their size.',ponies),
split('next','paper','Moving up','When they are ready, <em>the next step is clear.</em>','The Junior Riding Club is the first stage of the Forecast Farms progression. Riders who outgrow it move into Rider Training with the same trainer and a clear path toward the hunter, jumper and equitation rings.',
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
