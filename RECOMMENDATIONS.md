# Forecast Farms website: recommendations and approvals

Status record for the November 2026 review. Approved by Mich on 18 Nov 2026 ("yes in all"). This supersedes the conflicting parts of `COPY-BRIEF.md` where noted under "Rule changes".

- Audit report (private page, share from its menu): https://claude.ai/artifact/JjiNqktcH6HMsj8GcFLrvc
- Plan: `REVIEW-PLAN.md`
- Work branch: `ccr-54305f17-zk27mh`. It reaches the demo after a pull request is merged into `main`.

## Approval notes from Mich

- **#1 Prices:** use a placeholder until Denise answers.
- **#3 Google rating:** show it only if the rating is above 4.7.
- **#11 Specifics:** yes.
- Everything else: approved as recommended.

## A. Getting more people to book

| # | Idea | Status |
|---|---|---|
| 1 | Show prices: the evaluation lesson and lesson rates ("from $X"). A placeholder for now | Placeholders on Home (program cards, evaluation lesson); waiting on Denise |
| 2 | Cut the form from 9 fields to 4: name, phone or email, who it's for (rider / horse / both), message | **Done** on the branch (Home and Schedule an Evaluation) |
| 3 | Google rating near the top of the homepage, linked to the reviews. Shown only if it's above 4.7 | **Done**: shows 5.0 from 10 reviews (testimonial bank, 6 Nov 2026). Needs the exact Google reviews link |
| 4 | One matched testimonial on every inner page (word for word, from the testimonial bank) | Approved |

## B. Structure

| # | Idea | Status |
|---|---|---|
| 5 | Homepage from 11 sections to 7: top banner and facts strip, then programs, how the evaluation works, Denise, testimonials, who it's for, and the form. "Hunter, jumper or equitation" moves to Rider Training. The Sales section becomes a link | **Done** on the branch |
| 6 | Inner pages: one full-width photo band, one large quote and one photo grid each, to break the repeated layout | Approved |
| 7 | A "Meet the schoolmasters" gallery: photo, breed, size and one line for each of the five | Approved; photos in the Photos list below |
| 8 | A "New riders: start here" FAQ page: prices, lesson length, what to bring, schedule, cancellations | Approved, waiting on Denise |
| 9 | A short note from Denise in her own voice, signed, on Home and About | Draft on Home, marked as a draft; About next. Denise approves the text |

## C. Copy

| # | Idea | Status |
|---|---|---|
| 10 | Headings say what and where, e.g. "Hunter, jumper and equitation lessons in Marshall, Virginia" | Home and Rider Training's new section done; other inner pages next |
| 11 | Specifics instead of general claims: years, named shows, named horses, the facilities | Approved; new facts confirmed by Denise first |
| 12 | Finish the cleanup: banned words, italic headings (2 per page), two-beat headings | Approved |
| 13 | Shorter body text: one or two sentences per section intro | Approved |

## D. Visual

| # | Idea | Status |
|---|---|---|
| 14 | A half-day professional photo shoot: lessons, jumping, the barn, the schoolmasters, Denise teaching | Approved; Mich handles the photo upgrade, last (Photos list below) |
| 15 | Scroll-in fade, photo zoom on hover, card lift, arrow nudge, header shrink | **Done** on the branch (commit a2195f2) |
| 16 | A 6–8 second silent video loop at the top of the homepage | Approved for later, after the shoot |
| 17 | Visit section with a photo of the farm entrance and a "Get directions" button | **Done** on Home, with the barn photo until an entrance photo is shot |

## E. Google and tracking

| # | Idea | Status |
|---|---|---|
| 18 | Business details for Google (structured data) and page titles of 60 characters or fewer | Approved |
| 19 | Track form sends and taps on Call and Text in GoHighLevel | Approved |
| 20 | One footer line naming nearby towns: Middleburg, The Plains, Warrenton, Upperville | Approved |
| 21 | "Notes from the ring" page built from the Monday tip posts | Approved for later |

## Testimonial bank decisions (Mich, 18 Nov 2026)

| Topic | Decision | Owner |
|---|---|---|
| Testimonials on the site | Use only quotes that are in the testimonial bank, word for word. Credit stays "First name + initial, Google review" | Claude |
| Quotes already on the site (4 on Home, 4 on inner pages) | Check each against the bank; any quote not in it comes off | Claude, once the bank's quote list is pasted in |
| "Jane Smith, Middleburg, VA" placeholder on intro.forecastfarms.com | Take the page down. If it has to stay, remove the quote today. It is not in this repo | Mich / Denise (GHL) |
| Facebook Page reviews | Turn on after launch | Denise |
| LinkedIn recommendations (Joan Russo, Jay Tobias, 2011) | Ask each person before reusing; use Google reviews first | Mich / Denise |
| 2★ Yelp review ("a place for beginners") | No website change; Denise may reply publicly. Year not in the pasted bank | Denise |

## Rule changes (replace the matching lines in COPY-BRIEF.md)

| Rule before | Rule now |
|---|---|
| Prices are never stated | Show prices once Denise confirms them; placeholders until then |
| No new sections without approval | Sections #4–7 are approved as a package |
| Headings plain and descriptive | Still plain, and they may include place names |
| `src/home.html` and `build.py` are don't-touch | One session owns the shared files, so sessions don't collide |
| Main button says "Schedule an Evaluation Lesson" everywhere | Same, except the header button stays "Schedule an Evaluation" to fit |

**Unchanged:** no invented facts, testimonials word for word, legal text untouched.

## Done so far

- Audit: visual review on desktop and phone, accessibility scan, link check, copy and SEO review
- #15 effects, a full-screen phone menu, and the footer heading and landmark accessibility fixes (commit a2195f2)
- Homepage rebuild: #5 (7 sections; disciplines moved to Rider Training; Sales is a link), #2, #17, and the Home parts of #1, #3, #9 and #10

## Questions for Denise

1. **Prices:** the evaluation lesson, private and semi-private lessons, horse training, and Horse + Rider Development
2. **Junior Riding Club:** are $375 / $700 / $900 a month still right? Are the level names (Blue, Orange), the private online community and the Horsesense curriculum current?
3. **Lessons:** lesson length, weekly schedule, cancellation policy
4. **What to bring:** confirm the list on the evaluation page (helmet standard, boots, gloves, Coggins and vaccinations for ship-ins, tack)
5. **Photos:** moved to the Photos list below (Mich resolves last)
6. **Google:** the exact reviews link from the Google Business Profile (rating 5.0 from 10 reviews is in the testimonial bank, 6 Nov 2026)
7. **Testimonials:** Jana's last initial, and OK to credit quotes as "First name + initial, Google review"
8. **Her note (#9):** a few sentences in her own words, or approve a draft
9. **Specifics (#11):** any facts to add, such as the indoor arena size, show results, how long each schoolmaster has been at the farm
10. **Horses for sale:** the current list, or "ask us" for now
11. **Homepage quotes:** are Jessica M., Jana, Richard I. and Beth P. Google reviews? They are credited by town today; the rule is "First name + initial, Google review"
12. **Photos:** moved to the Photos list below (Mich resolves last)

## Photos: Mich resolves last

Mich is upgrading the photos and will resolve this list after the rest of the work. Until then, pages use the current photos or labeled placeholders, and any new photo comment is added here instead of blocking the work. Spec (README): landscape at least 2000px wide, portrait at least 1200 × 1500px, under about 500 KB.

| # | Slot | Comment | Suggestion |
|---|---|---|---|
| P1 | Home hero (GHL media `…0f59`, hunter on a grey) | 1448 × 1086, under the 2000px spec; 3.1 MB file | Replace with a 2000px+ version under 500 KB |
| P2 | Rider Training disciplines: Hunter, Jumper, Equitation (GHL media `…fa346`, `…0f50`, `…f806`; moved from Home) | 1122 × 1402, under the 1200 × 1500 spec; 2.5–3.2 MB each | Replace with larger, lighter versions |
| P3 | Rider Training, Jumper photo (`…0f50`) | Same shot as the Rider Training hero (`rider-training.jpg`) | A different jumper photo |
| P4 | Home Visit block (#17) | Uses the barn and ring photo (`…4e14`, 6000 × 4000, 2.5 MB) instead of the farm entrance | Add a farm entrance photo; also export the barn photo smaller |
| P5 | Trainer at the rail (GHL media `…f358`, 1200 × 1500) | No longer used: it was in the "How Denise teaches" section removed from Home | Reuse it on About or in an inner-page photo grid (#6) |
| P6 | `denise-finch.jpg` (About) | 1080 × 1350, under the 1200 × 1500 spec | Replace with a 1200 × 1500+ portrait |
| P7 | `schoolmaster-audrey.jpg` (Rider Training, Junior Riding Club) | Missing, so a placeholder shows | Add the photo |
| P8 | Herman, Remi, Freddy (#7 schoolmaster gallery) | No photos yet | Add one 4:5 portrait each |
| P9 | `horse-sales.jpg` (Horse Search & Sales) | Missing, so a placeholder shows | Add the photo |
| P10 | Inner-page photo bands and grids (#6) | Each page needs one wide band and 3–4 grid photos | Built with current photos or placeholders; swap them in your upgrade |
| P11 | Homepage video loop (#16) | Waits on new footage | After the photo upgrade |
