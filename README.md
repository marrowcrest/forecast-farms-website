# Forecast Farms Website

Demo and source for the new Forecast Farms website: Hunter, Jumper and Equitation training in Marshall, Virginia.

- **`docs/`** is the demo website, served by GitHub Pages. It is kept out of search engines (`noindex`) and the forms show a "preview site" message instead of sending.
- **`ghl/`** holds the same ten pages as paste-ready files for GoHighLevel, for when the site goes live.

Both are generated. **Edit `src/` or `images/`, never `docs/` or `ghl/` directly**: changes there are overwritten on the next build.

## Structure

| Path | What it is |
|---|---|
| `src/home.html` | The homepage, plus the shared styles, menu, footer and scripts every page uses |
| `src/build/` | Content and build code for the other nine pages |
| `src/build/legal_copy.py` | Privacy Policy and Terms text |
| `images/` | Photos for the demo, named after their slots (see below) |
| `build.py` | Builds `ghl/` and `docs/` from `src/` |
| `docs/` | Generated demo website (GitHub Pages) |
| `ghl/` | Generated GoHighLevel files |

## Making changes

| Change | Where |
|---|---|
| Menu, footer, colors, fonts, shared styles | `src/home.html` |
| Homepage text | `src/home.html` |
| Rider Training | `src/build/rider_build.py` |
| Schedule an Evaluation | `src/build/eval_build.py` |
| Horse Training, Horse + Rider Development, Sales, About, Junior Riding Club | `src/build/pages_build.py` |
| Privacy Policy, Terms | `src/build/legal_copy.py` |
| Page titles and descriptions | `PAGES` in `build.py` |

Then rebuild:

```
python build.py
```

On GitHub, pushing changes to `src/`, `images/` or `build.py` rebuilds `docs/` and `ghl/` automatically (see `.github/workflows/build.yml`). The demo updates a minute or two later.

## Pages

| Page | Path | Demo file | GHL file |
|---|---|---|---|
| Home | home page | `docs/index.html` | `ghl/home.html` |
| Schedule an Evaluation | `contact-us` | `docs/contact-us.html` | `ghl/contact-us.html` |
| Rider Training | `rider-training` | `docs/rider-training.html` | `ghl/rider-training.html` |
| Horse Training | `training` | `docs/training.html` | `ghl/training.html` |
| Horse + Rider Development | `horse-rider-development` | `docs/horse-rider-development.html` | `ghl/horse-rider-development.html` |
| Junior Riding Club | `lessons` | `docs/lessons.html` | `ghl/lessons.html` |
| Horse Search & Sales | `sales` | `docs/sales.html` | `ghl/sales.html` |
| About | `about-us` | `docs/about-us.html` | `ghl/about-us.html` |
| Privacy Policy | `privacy-policy` | `docs/privacy-policy.html` | `ghl/privacy-policy.html` |
| Terms & Conditions | `terms-and-conditions` | `docs/terms-and-conditions.html` | `ghl/terms-and-conditions.html` |

## Photos

The homepage's six photos are hosted in GHL Media Storage and linked from `src/home.html`. For every other slot, add the photo to `images/` with the exact file name below and it appears on the next build. Until then, a labeled placeholder shows.

| File | Page | Shot |
|---|---|---|
| `evaluation-lesson.jpg` | Schedule an Evaluation | Denise at the rail watching a rider (landscape) |
| `rider-training.jpg` | Rider Training | A rider schooling over a fence (landscape) |
| `schoolmaster-chief.jpg` | Rider Training, Junior Riding Club | Chief (portrait 4:5) |
| `schoolmaster-audrey.jpg` | Rider Training, Junior Riding Club | Princess Audrey (portrait 4:5) |
| `horse-training.jpg` | Horse Training | Schooling a young horse on the flat (landscape) |
| `horse-rider.jpg` | Horse + Rider Development | Horse and rider in the show ring (landscape) |
| `horse-sales.jpg` | Horse Search & Sales | A rider trying a sales horse (landscape) |
| `about-farm.jpg` | About | Barn, rings and countryside (landscape) |
| `denise-finch.jpg` | About | Denise, mounted or at the barn (portrait 4:5) |
| `junior-riding-club.jpg` | Junior Riding Club | A young rider on a lesson pony (landscape) |

Landscape photos: at least 2000px wide. Portraits: at least 1200 × 1500px. Keep files under about 500 KB each so pages load quickly.

## Going live on GoHighLevel

1. Build in a new GHL website, not the live forecastfarms.com site (it already uses several of these paths).
2. On each page: one full-width section with 0 padding, one Custom Code element, paste the whole file from `ghl/`.
3. Photos in `images/` must be uploaded to GHL Media Storage and their links swapped into the source first, since GHL pages cannot read this repo.
4. Website settings, body (footer) tracking code: the GHL External Tracking script, once, site-wide.
5. Custom fields: Rider Type, Horse Status, Jumping Level, Training Interest, Goals, SMS Consent.
6. Test the forms on Home and Schedule an Evaluation; check Sites > Forms > Submissions > External Forms.
7. Before launch: attorney review of the Privacy Policy and Terms.

## Open items

Placeholders waiting on answers from Denise: pricing and the evaluation lesson price, how horse training is set up, Junior Riding Club plans and levels, the schoolmaster list, recent show results, horses for sale, and the What to bring list.
