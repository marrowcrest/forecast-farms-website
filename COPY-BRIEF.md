# Forecast Farms copy rewrite brief

The rules for every Claude session rewriting copy on this site. Several sessions run at once, one per page group. If anything here conflicts with what Mich says in chat, Mich wins.

- Demo site: https://marrowcrest.github.io/forecast-farms-website/
- Original site (backup): https://marrowcrest.github.io/forecast-farms-website/v1/
- Testimonial bank (read with docs tools, never edit): https://claude.ai/artifact/4Pa241fsbtwFFsJMb5JmfW

## The job

Copy only. Layout, components, classes, photos and small labels (eyebrows) stay as they are. Don't add or remove sections, cards or fields unless Mich approves it. Headings follow the rule below.

## Headings (new rule, Mich, 13 Nov 2026)

This replaces the old rule that the italic tails on headings (`<em>`) were locked.

- Heading wording can be rewritten, including the part that used to be the italic tail. It needs Mich's approval like any other copy.
- Italics (`<em>`) appear on two headings per page only: the hero heading and the bottom banner. Every other heading is plain, with no `<em>`.
- Section headings are plain and descriptive. They say what the section holds, in the reader's words. Example: "Private or semi-private lessons", not "Choose the format *that fits the goal.*"
- Avoid the two-beat rhythm ("X, and Y.") and wordplay. Don't repeat the eyebrow.
- Why: 44 of the site's 55 headings used the same plain-half-plus-italic-tail shape, and Mich judged that it read as templated. Readers of sectioned pages look mainly at the headings (Nielsen Norman Group, layer-cake scanning pattern), and look-alike headings make people re-read (usability.gov Research-Based Guidelines, chapter 9).
- Rollout: Session A applies it to Rider Training first, then sends Mich one heading table per finished page (Horse Training, Horse + Rider Development, then the homepage, which still needs her approval before any edit). Other sessions apply it on their own pages.

## One section per message

1. Read your page's block in its builder file and the approved homepage in `src/home.html`. Don't send Mich a page map or several sections.
2. Send ONE section:
   - a table `Part | Now | Proposed`, with unchanged rows marked *(keep)*
   - 2 to 4 short "why" bullets
   - decisions, if any, as a table of options with your recommendation first
   - end with: "Approve, or tell me what to change."
3. Wait for her approval. Apply exactly what she approved, deploy, then send the link to that section and the next section's proposal in the same message.
4. Put links and tables in your final message. Text written between tool calls is not shown to her.

Exception: a heading-only pass on a finished page goes to Mich as one table for the whole page.

## Applying an approved section

```
git pull --rebase
# edit only your page's block, with exact-match replacements (assert each old string occurs once)
python3 build.py                 # check it builds
git restore docs ghl images      # don't commit generated files; the GitHub Action rebuilds them
git add src && git commit        # end the message with your session's attribution lines
git pull --rebase && git push    # if the push is rejected, pull --rebase and push again
gh run list -L 3                 # wait until "Build site" and "pages build and deployment" succeed
```

## Don't touch

- `src/home.html`, `src/build/ffchrome.py`, `build.py`, `.github/`, `archive/`: shared by every page. If a change seems needed there, propose it to Mich and stop.
- Other pages' blocks. `src/build/pages_build.py` holds five pages: edit only yours.
- Legal and compliance text: the SMS consent line, the Terms and Privacy lines, and the legal pages.
- The evaluation form. The Contact page copies it from `src/home.html`, and its wording is handled in the main session (homepage Section 11). Session C rewrites the rest of the Contact page.

## Voice

- Plain, specific words, short sentences. Say what happens and who does it.
- Cut filler: "structured", "experienced", "suitable", "measurable progress", "honest/honestly", "the right home", "pathway", "journey", "tailored", "holistic", "elevate", and wordplay headings.
- Use the site's words: evaluation lesson, program (not pathway), schoolmaster, training rides.
- The main button says "Schedule an Evaluation Lesson" on every page.
- No new claims. A fact must come from the current site copy, the facts below, or Mich. If one is missing, keep the line and add the question to your decisions table.
- When you propose something beyond wording (a new element, a different offer), back it with a cited source.

## Testimonials

Word for word, whole sentences only. No "…" excerpts, no fixed punctuation or typos, no edits of any kind. Don't use the same quote on two pages. Pick from the testimonial bank. Credit Google reviewers by first name and last initial, with "Google review" (Mich, 13 Nov 2026): Virginia Code § 8.01-40 requires written consent to use a person's name in advertising.

## Confirmed facts

- Family-owned, run by head trainer Denise Finch. 2497 Atoka Road, Marshall, VA 20115. (540) 274-1541, info@forecastfarms.com.
- Hunter, jumper and equitation for junior and adult riders, on their own horse, a ship-in, or a farm schoolmaster.
- Indoor arena and an outdoor all-weather ring, so lessons run all year.
- 35+ years training riders and horses in Marshall. Denise won Local Pony Hunter at Upperville.
- Denise teaches some lessons. Trusted, qualified assistant instructors teach others. Denise does the training herself: training rides on horses, and riders training for shows.
- The Junior Riding Club (ages 4 to 7) is still offered.
- The five schoolmasters named on Rider Training (Chief, Princess Audrey, Herman, Remi, Freddy) are all still at the farm (Mich, 14 Nov 2026).
- Sales: green and made horses and ponies for sale or lease, consignment under a written agreement, and a pre-purchase exam recommended.
- Denise answers form requests herself in the GHL app.

## Not confirmed (never state as fact)

- Group lessons. Don't mention them. (The "Small group" card was removed from Rider Training on 13 Nov 2026.)
- Prices, lesson length, weekly schedule, the year the farm started, show results, the current horse list, Junior Riding Club details, what to bring, policies.
- Mich chose to keep the homepage saying riders work with Denise. On inner pages, don't add new claims that Denise teaches every lesson.
- The open questions for Denise are in `claude/denise-questions.md` in the project.

## Who works on what

| Session | Pages, in order | Builder block |
|---|---|---|
| A | Horse Training and Horse + Rider Development (done), then Rider Training (taken over from the main session on 13 Nov 2026, at Mich's request) | `pages_build.py`: Horse Training, Horse + Rider Development; `src/build/rider_build.py` |
| B | Junior Riding Club, then Horse Search & Sales | `pages_build.py`: Junior Riding Club, Horse Search & Sales |
| C | About, then Contact (evaluation request page) | `pages_build.py`: About; `src/build/eval_build.py` |

Page links: `rider-training.html`, `training.html`, `horse-rider-development.html`, `lessons.html`, `sales.html`, `about-us.html`, `contact-us.html` on the demo site.

## How Mich likes it

Bottom line first, tables, a recommendation on every decision, options rather than open questions, and push back when something is off.
