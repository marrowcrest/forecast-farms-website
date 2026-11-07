# Forecast Farms copy rewrite brief

The rules for every Claude session rewriting copy on this site. Several sessions run at once, one per page group. If anything here conflicts with what Mich says in chat, Mich wins.

- Demo site: https://marrowcrest.github.io/forecast-farms-website/
- Original site (backup): https://marrowcrest.github.io/forecast-farms-website/v1/
- Testimonial bank (read with docs tools, never edit): https://claude.ai/artifact/4Pa241fsbtwFFsJMb5JmfW

## The job

Copy only. Layout, components, classes, photos, small labels (eyebrows) and the italic tails on headings (`<em>`) stay as they are. Don't add or remove sections, cards or fields unless Mich approves it.

## One section per message

1. Read your page's block in its builder file and the approved homepage in `src/home.html`. Don't send Mich a page map or several sections.
2. Send ONE section:
   - a table `Part | Now | Proposed`, with unchanged rows marked *(keep)*
   - 2 to 4 short "why" bullets
   - decisions, if any, as a table of options with your recommendation first
   - end with: "Approve, or tell me what to change."
3. Wait for her approval. Apply exactly what she approved, deploy, then send the link to that section and the next section's proposal in the same message.
4. Put links and tables in your final message. Text written between tool calls is not shown to her.

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

Word for word, whole sentences only. No "…" excerpts, no fixed punctuation or typos, no edits of any kind. Don't use the same quote on two pages. Pick from the testimonial bank.

## Confirmed facts

- Family-owned, run by head trainer Denise Finch. 2497 Atoka Road, Marshall, VA 20115. (540) 274-1541, info@forecastfarms.com.
- Hunter, jumper and equitation for junior and adult riders, on their own horse, a ship-in, or a farm schoolmaster.
- Indoor arena and an outdoor all-weather ring, so lessons run all year.
- 35+ years training riders and horses in Marshall. Denise won Local Pony Hunter at Upperville.
- Denise teaches some lessons. Trusted, qualified assistant instructors teach others. Denise does the training herself: training rides on horses, and riders training for shows.
- The Junior Riding Club (ages 4 to 7) is still offered.
- Sales: green and made horses and ponies for sale or lease, consignment under a written agreement, and a pre-purchase exam recommended.
- Denise answers form requests herself in the GHL app.

## Not confirmed (never state as fact)

- Group lessons. Don't mention them.
- Prices, lesson length, weekly schedule, the year the farm started, show results, the current horse list, Junior Riding Club details, what to bring, policies.
- Mich chose to keep the homepage saying riders work with Denise. On inner pages, don't add new claims that Denise teaches every lesson.

## Who works on what

| Session | Pages, in order | Builder block |
|---|---|---|
| Main | Rider Training | `src/build/rider_build.py` |
| A | Horse Training, then Horse + Rider Development | `pages_build.py`: Horse Training, Horse + Rider Development |
| B | Junior Riding Club, then Horse Search & Sales | `pages_build.py`: Junior Riding Club, Horse Search & Sales |
| C | About, then Contact (evaluation request page) | `pages_build.py`: About; `src/build/eval_build.py` |

Page links: `training.html`, `horse-rider-development.html`, `lessons.html`, `sales.html`, `about-us.html`, `contact-us.html` on the demo site.

## How Mich likes it

Bottom line first, tables, a recommendation on every decision, options rather than open questions, and push back when something is off.
