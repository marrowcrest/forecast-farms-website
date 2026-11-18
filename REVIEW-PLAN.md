# Forecast Farms website review: plan

## Context
You asked for a review of what to improve on the Forecast Farms site, including a visual UI/UX audit and some light effects on the static pages where they help. The repo `marrowcrest/forecast-farms-website` is connected and cloned (branch `ccr-54305f17-zk27mh`). It's a static site: `src/` + `build.py` generate `docs/` (GitHub Pages demo) and `ghl/` (GoHighLevel paste files). The rules are in `COPY-BRIEF.md`.

### What the first read-only scan found
| Area | Finding |
|---|---|
| Banned words (brief) | Still on built pages: sales (honestly ×2, suitable ×2, "the right home"), lessons (structured ×3, experienced), training (experienced ×3), contact-us (pathway ×2, experienced), about (Suitable), home (experienced). Some are in meta descriptions in `build.py` `PAGES` |
| Heading rule (`<em>` on 2 headings max) | Over the limit: about-us 6, lessons 6, sales 5, contact-us 3 |
| CTA wording | 25 buttons say "Schedule an Evaluation". The brief requires "Schedule an Evaluation Lesson" (22 buttons use it) |
| Photos | `schoolmaster-audrey.jpg` and `horse-sales.jpg` are missing, so placeholders show |
| Motion already in place (`src/home.html`) | Hero text rise and photo settle on load, hover color changes, header blur, nav dropdown fade, phone action bar slide-in, `prefers-reduced-motion` respected. **No scroll-reveal, no image hover, no card lift**, so the page below the hero is fully static |

## Step 1: Visual UI/UX audit (read-only)
Serve `docs/` locally. Use Playwright to take full-page screenshots of all 8 main pages at 1440px and 390px. Save them to the scratchpad.
Review each page for:
- **Visual hierarchy:** heading scale, spacing rhythm, dense or empty sections, whether sections look too alike, CTA visibility
- **Layout:** alignment, image crops, card heights, placeholder blocks, footer
- **Mobile:** tap targets ≥44px, horizontal scroll, sticky Book·Call·Text bar overlapping content, menu
- **Accessibility:** axe scan, color contrast (purple `#7E2B80` on `#EEEDEC`, band text), alt text, focus states, heading order
- **Interaction:** forms (errors, success, the preview-site message), the slider and dialogs, broken links, console errors
- **Performance:** image weight (largest is 430 KB) and srcset use

## Step 2: Copy, SEO and launch audit
- Brief compliance per page: the items above, plus two-beat headings, duplicate testimonials and unconfirmed claims
- SEO: titles and meta descriptions, LocalBusiness structured data, Open Graph tags, canonical URLs
- GHL readiness: `ghl/` files are self-contained; gaps in the go-live checklist

## Step 3: Report
A private artifact page containing:
- Annotated screenshots
- A prioritized table: `Page | Issue | Severity | Fix | Who decides` (you, Denise, or code only)
- A short summary in chat

## Step 4: Proposed effects (subtle, to match the calm, upscale equestrian brand)
All in shared CSS/JS in `src/home.html`. Vanilla code with no libraries, so it pastes cleanly into GHL. All effects turn off under `prefers-reduced-motion`.
| Effect | Where |
|---|---|
| Scroll-reveal: a fade-and-rise as sections enter, staggered for cards (IntersectionObserver plus a `.reveal` class, reusing the existing `ff-rise` easing) | Section headings, cards, photos |
| Slow image zoom on hover (scale 1.03 inside an overflow-hidden frame) | Program and schoolmaster cards |
| Card lift (small translateY and a soft shadow) on hover/focus | Linked cards |
| Animated underline on text links and the arrow nudging on `.link-arrow` | Site-wide |
| Header shrinks and shows its border after scrolling | Header |
| Optional: count-up on "35+ years" | Home and About |
I'll show you a before/after recording before applying any of these widely.

## Step 5: Fixes (only after you approve)
- Code-only fixes (accessibility, links, performance, meta, effects) go in `src/` and `build.py`.
- Copy changes follow the brief: one section per message, a `Part | Now | Proposed` table, and your approval before any edit.
- `src/home.html` is "don't touch" in the brief. The effects and shared fixes need your explicit OK; I'm asking for it here.
- I'll run `python3 build.py` to check the build, leave `docs/` and `ghl/` out of commits, and commit and push to `ccr-54305f17-zk27mh`. No PR unless you ask.

## Verification
- `python3 build.py` builds cleanly.
- Re-run the scans and the axe/Playwright checks; fixed items should drop to zero.
- Retake screenshots and compare before and after.
- Check reduced-motion mode and the 390px layout.
