# UX Principles Reference: Norman, Nielsen, Spool

Distilled from primary sources (read 2026-11-04 via Firecrawl) into checkable rules for
building content and organization websites (parish, nonprofit, school, civic). Every concept
carries the URL it was read from. Quotes are short and attributed; everything else is
paraphrase or our own translation into web rules. Short on time: read Section 4 first.

---

## 0. The three thinkers in one paragraph each

- **Don Norman** (cognitive scientist, *The Design of Everyday Things*, *Emotional Design*,
  co-founder NN/g). His question is: can a person look at a thing and know what it does,
  how to work it, and whether it worked? His vocabulary (affordance, signifier, mapping,
  feedback, conceptual model, constraints, discoverability, gulfs of execution and
  evaluation) is the grammar every other UX idea is written in. His moral stance: when
  people fail, blame the design, not the person.
- **Jakob Nielsen** (usability engineer, co-founder NN/g, "discount usability"). His
  question is: measured against real users doing real tasks, does this interface work?
  He supplies the empirical rules of the web: people scan, not read; hidden navigation
  halves discoverability; 0.1 / 1 / 10 second limits; five users find most problems;
  users expect your site to behave like every other site.
- **Jared Spool** (UIE, Center Centre). His question is: did the user get to the content
  they came for, and did the organization intend the experience it delivered? He supplies
  the link-and-content layer (scent, trigger words, "move forward until found"), the
  economic argument ($300M button), and the strategy layer (design is the rendering of
  intent; experience vision; Kano; design maturity).

Where they overlap, the overlap is the rule: **make the next step visible, labeled in the
user's words, consistent with what the web has taught them, and confirmed with feedback.**
---

## 1. Don Norman

### 1a. Core concepts (with sources)

**Affordance vs. perceived affordance vs. signifier**
Source: https://jnd.org/affordances-and-design/ and https://jnd.org/signifiers-not-affordances/

- An *affordance* (Gibson's term) is a relationship between an object and an actor: what
  actions are possible. Affordances exist whether or not anyone perceives them. On a
  screen, everything "affords clicking," so the affordance itself tells a designer nothing.
- Norman says he should have said *perceived affordance*: "in design, we care much more
  about what the user perceives than what is actually true." (Norman, jnd.org)
- A *signifier* is any perceivable cue (deliberate or accidental) that tells a person what
  is possible, what is happening, or where they are. Underlines, button shading, cursor
  changes, scrollbars, breadcrumbs and "You are here" markers are signifiers. Norman's
  closing line: "Designers of the world: Forget affordances provide signifiers." (Norman,
  *Interactions*, 2008, reposted on jnd.org)
- Four ways a new user learns what a screen can do (jnd.org/affordances-and-design/):
  1. follow convention in both imagery and interaction;
  2. use words to describe the action (labels beat icons; words plus icons beat both);
  3. metaphor (which Norman distrusts);
  4. a coherent conceptual model so that learning one part teaches the rest.
  His warning: "unless we follow the major conventions, we are doomed to fail." (Norman)

**Mapping, feedback, conceptual model, system image**
Source: DOET revised edition, chapter 1 table of contents at
https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/ ;
NN/g restatement at https://www.nngroup.com/articles/ten-usability-heuristics/ (heuristic 2,
"natural mapping")

- *Mapping*: the relationship between controls and their effects. Natural mapping uses
  spatial or cultural correspondence (stove knobs laid out like burners) so no label is
  needed.
- *Feedback*: immediate, informative confirmation that an action was received and what it
  did. Too little leaves people guessing; too much becomes noise.
- *Conceptual model*: the explanation, usually simplified, a person holds of how the thing
  works. The designer's model reaches the user only through the *system image* (the
  product plus its labels, docs and behavior). If the system image is incoherent, the user
  builds the wrong model.

**Constraints and discoverability**
Source: DOET chapter 4, "Knowing What to Do: Constraints, Discoverability, and Feedback"
(TOC at jnd.org link above); physical/logical/cultural constraints explained at
https://jnd.org/affordances-and-design/

- Four constraint types: physical (cannot drag the cursor off-screen), cultural (learned
  conventions such as scrollbar direction), semantic (meaning rules out options), logical
  (if five targets are required and four are visible, one remains).
- *Forcing functions* (interlocks, lock-ins, lock-outs) make the wrong action impossible
  rather than merely discouraged.
- *Discoverability*: can a person figure out what actions are possible and how to perform
  them? Norman lists it with understanding as the two most important characteristics of
  good design.

**The seven stages of action and the two gulfs**
Source: DOET chapter 2 (text excerpt via
https://dl.icdst.org/pdfs/files4/4bb8d08a9b309df7d86e62ec4056ceef.pdf ; TOC at jnd.org);
NN/g explainer https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/

- Stages of execution: goal, plan, specify, perform. Stages of evaluation: perceive,
  interpret, compare. The seven user questions, in Norman's words:
  1. What do I want to accomplish?
  2. What are the alternative action sequences?
  3. What action can I do now?
  4. How do I do it?
  5. What happened?
  6. What does it mean?
  7. Is this okay? Have I accomplished my goal?
  "Anyone using a product should always be able to determine the answers to all seven
  questions." (Norman, DOET)
- Information that answers 1-4 is *feedforward* (signifiers, constraints, mappings,
  conceptual model). Information that answers 5-7 is *feedback*.
- The *gulf of execution* is the gap between intention and the available controls; the
  *gulf of evaluation* is the gap between the system's state and the user's understanding
  of it. NN/g's Whitenton notes that evaluation has two sub-tasks, perceiving and
  interpreting; execution has planning and manipulating. A visible status can still be
  misread (her Bluetooth "Off" toggle example).
- Root-cause analysis: keep asking why. Norman extends Levitt's drill: nobody wants the
  quarter-inch hole either; they want the shelf on the wall.

**Human error vs. design error; slips vs. mistakes**
Source: https://jnd.org/human-error-no-bad-design/ ; DOET chapter 5 TOC; NN/g heuristic 5

- "Over 90% of industrial accidents are blamed on human error." (Norman) His reply: at
  that rate the cause is the design, not the person. Mode errors (the ferry case) happen
  when the system signals its state too subtly.
- *Slips* are unconscious errors of execution (right goal, wrong action; often from
  inattention or similar-looking controls). *Mistakes* are errors of intention from a wrong
  conceptual model. Slips are reduced by constraints and good defaults; mistakes by better
  models, visible state, and undo.
- "It is time to stop blaming people and instead to design for people." (Norman)
- Related essay, title as rule: "Error Messages Are Evil" (https://jnd.org/error-messages-are-evil/).

**Emotional Design: visceral, behavioral, reflective**
Source: https://jnd.org/emotional-design-people-and-things/ ; NN/g summary
https://www.nngroup.com/videos/3-levels-emotional-processing/

- Visceral: "that initial impact, to its appearance." Behavioral: "look and feel — the total
  experience of using a product." Reflective: "ones thoughts afterwards, how it makes one
  feel, the image it portrays." (Norman)
- The Jacob Jensen alarm clock study: beautiful (visceral), prestigious (reflective),
  unusable (behavioral). A tester near tears still wanted to buy it. Different people and
  different products weight the three levels differently; a functional tool must pass the
  behavioral test first.
- "The crime is not lack of knowledge, it is lack of application, and in many cases, lack
  of concern." (Norman, on unusable products and manuals)
- DOET chapter 2 adds: design must take place at all three levels.

**Complexity vs. confusion** (DOET ch. 6 heading: "Complexity Is Good; It Is Confusion
That Is Bad"). A rich organization is legitimately complex; the failure is confusion:
complexity without structure, signifiers, or a model.

### 1b. Memorable quotes (Norman)

- "Designers of the world: Forget affordances provide signifiers." (jnd.org, 2008)
- "unless we follow the major conventions, we are doomed to fail." (jnd.org)
- "It is time to stop blaming people and instead to design for people." (jnd.org, 2014)
- "Complexity Is Good; It Is Confusion That Is Bad." (DOET, ch. 6 heading)
- "The crime is not lack of knowledge, it is lack of application." (jnd.org)
### 1c. What this means for a website (checkable rules)

Signifiers and perceived affordance
- Every clickable thing must look clickable *before* hover: links in body copy are
  underlined or clearly colored, buttons have a filled or outlined shape, cards that are
  whole-card links show a visible arrow or link text. Test: screenshot the page, hand it
  to someone, ask them to circle everything they could click. Misses and false positives
  are both defects.
- Nothing that is not clickable may look clickable (no underlined non-links, no
  button-shaped headings).
- Icons never appear without a text label except for universally conventional ones
  (search magnifier, close X), and even those get `aria-label`.
- Scrollable or expandable regions signal it: a partially visible next item, a chevron,
  "Show all 12 events." Test: can a user tell there is more without trying?

Mapping
- Navigation order matches the mental hierarchy (Visit, Worship, Grow, Serve, Give), and
  the footer repeats the same order. Related controls sit next to what they control (a
  "Download" button sits on the document it downloads, not in a sidebar).
- Form labels sit immediately above or beside their fields; error messages sit next to
  the field they describe.

Feedback and system status
- Every action produces a visible response within 0.1 s (button press state, link
  focus/hover), and any action that takes longer than 1 s shows a progress state.
- After a form submits, the page says what happened, what will happen next, and when
  ("Thanks, Maria. We'll email you within two business days."). Never return a blank page
  or a silent reload.
- Current location is always shown: highlighted nav item, page title that matches the link
  that led there, breadcrumbs on deep pages.

Conceptual model and system image
- The site has one coherent model the user can state in a sentence ("Pages are grouped by
  what I'm trying to do"). Section names, URLs, headings and nav labels all use the same
  words for the same things. Test: list every distinct label used for the same destination;
  there should be one.
- The same component behaves the same way everywhere (an accordion never navigates away on
  one page and expands in place on another).

Constraints and error design
- Prefer constraints to warnings: date pickers over free-text dates, selects for fixed
  lists, `type="email"` and `inputmode` so the right keyboard appears.
- Design for slips: destructive or costly actions (unsubscribe, delete registration) are
  spaced from common actions, named precisely, and reversible or confirmed.
- Design for mistakes: state is visible (which tab, which filter, which step of 3), and
  there is always an obvious way back.
- Rewrite every error message to say what is wrong and how to fix it in plain words. If
  an error can be prevented by a better default or a constraint, do that instead.

Seven stages as a page audit
- For the page's top task, walk the seven questions in order. Where does the page fail to
  answer one? That is the defect to fix. Typical failures: Q3 "What can I do now?" (no
  visible call to action above the fold); Q5 "What happened?" (no confirmation); Q7 "Is
  this okay?" (no way to verify a registration went through).

Emotional design
- Visceral: first paint must be composed, legible, on-brand, with real photography, not
  stock. This buys forgiveness for later friction, but only if behavioral quality follows.
- Behavioral: the top three tasks (service times, directions, contact; or events,
  registration, giving) complete without surprise on a phone.
- Reflective: the site should leave people feeling the organization is competent and
  cares; that comes from accurate, current, specific content more than from decoration.
  Stale dates and broken links are reflective-level damage.

---

## 2. Jakob Nielsen

### 2a. Core concepts (with sources)

**The 10 usability heuristics (1994, reviewed Jan 30 2024)**
Source: https://www.nngroup.com/articles/ten-usability-heuristics/
The current article's definitions, quoted exactly (each is Nielsen's bolded statement):

1. **Visibility of System Status.** "The design should always keep users informed about
   what is going on, through appropriate feedback within a reasonable amount of time."
2. **Match Between the System and the Real World.** "The design should speak the users'
   language. Use words, phrases, and concepts familiar to the user, rather than internal
   jargon. Follow real-world conventions, making information appear in a natural and
   logical order."
3. **User Control and Freedom.** "Users often perform actions by mistake. They need a
   clearly marked 'emergency exit' to leave the unwanted action without having to go
   through an extended process."
4. **Consistency and Standards.** "Users should not have to wonder whether different
   words, situations, or actions mean the same thing. Follow platform and industry
   conventions."
5. **Error Prevention.** "Good error messages are important, but the best designs
   carefully prevent problems from occurring in the first place. Either eliminate
   error-prone conditions, or check for them and present users with a confirmation
   option before they commit to the action."
6. **Recognition Rather than Recall.** "Minimize the user's memory load by making
   elements, actions, and options visible. The user should not have to remember
   information from one part of the interface to another. Information required to use
   the design (e.g. field labels or menu items) should be visible or easily retrievable
   when needed."
7. **Flexibility and Efficiency of Use.** "Shortcuts — hidden from novice users — may
   speed up the interaction for the expert user so that the design can cater to both
   inexperienced and experienced users. Allow users to tailor frequent actions."
8. **Aesthetic and Minimalist Design.** "Interfaces should not contain information that
   is irrelevant or rarely needed. Every extra unit of information in an interface
   competes with the relevant units of information and diminishes their relative
   visibility."
9. **Help Users Recognize, Diagnose, and Recover from Errors.** "Error messages should be
   expressed in plain language (no error codes), precisely indicate the problem, and
   constructively suggest a solution."
10. **Help and Documentation.** "It's best if the system doesn't need any additional
    explanation. However, it may be necessary to provide documentation to help users
    understand how to complete their tasks."

Nielsen's note on the page: the ten "have remained relevant and unchanged since 1994."
Heuristic 5 distinguishes slips (inattention) from mistakes (wrong mental model), which is
Norman's taxonomy. Heuristic 8 explicitly "doesn't mean you have to use a flat design."

**How users read on the web (1997) and the F-pattern (2006, reviewed Aug 2026)**
Sources: https://www.nngroup.com/articles/how-users-read-on-the-web/ ;
https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/

- "79 percent of our test users always scanned any new page they came across; only 16
  percent read word-by-word." (Nielsen, 1997)
- Prescription: highlighted keywords, meaningful (not clever) subheadings, bulleted
  lists, one idea per paragraph, inverted pyramid, "half the word count (or less)."
- Measured effect: concise text +58% usability, scannable layout +47%, objective language
  +27%, all three combined +124%. "promotional language imposes a cognitive burden"
  because readers stop to disbelieve it. Users "detested 'marketese'."
- Credibility rises with good writing, quality graphics and outbound links.
- F-pattern (Pernice): people read the first lines across, then a shorter second line,
  then down the left edge. It happens when text is unformatted, the user wants to be
  efficient, and is not committed enough to read everything. "The F-pattern is the
  default pattern when there are no strong cues to attract the eyes towards meaningful
  information." It is bad for users and businesses because content on the right and lower
  down goes unseen. Other patterns: layer-cake (headings only), spotted, marking,
  bypassing, commitment.
- Antidotes: most important points in the first two paragraphs; headings and subheadings
  that look more important than body text; front-load the first two words of headings and
  links; visually group related small chunks; bold key phrases; links with
  information-bearing words (never "click here", "more"); bullets and numbers; cut.

**Response-time limits (1993, updated 2014)**
Source: https://www.nngroup.com/articles/response-times-3-important-limits/

- **0.1 second**: feels instantaneous; "no special feedback is necessary except to display
  the result." The limit for feeling you are directly manipulating the UI.
- **1.0 second**: "the limit for the user's flow of thought to stay uninterrupted"; the
  user notices the delay but keeps going. Beyond 1 s, show the system is working.
- **10 seconds**: "the limit for keeping the user's attention focused on the dialogue."
  Beyond it, give a percent-done indicator and a way to cancel; expect the user to need
  to reorient on return.
- Percent-done indicators for anything over ~10 s; for 2-10 s a lighter busy cue. These
  limits are perceptual and have been the same for decades regardless of technology.

**Test with 5 users (2000)**
Source: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/

- Problems found = N(1 - (1-L)^n), with L about 31% per user, so 5 users find roughly 85%.
  "zero users give zero insights." Better to run "3 studies with 5 users each" than one
  with 15, because the point is to fix and retest, not to document. If there are highly
  distinct user groups, test 3-4 from each.

**Jakob's Law**
Source: https://www.nngroup.com/videos/jakobs-law-internet-ux/ (and heuristic 4)

- "Users spend most of their time on other sites. This means that users prefer your site
  to work the same way as all the other sites they already know." Their expectations are
  set elsewhere; deviation costs learning.

**Information scent and navigation**
Sources: https://www.nngroup.com/articles/information-scent/ (Budiu) ;
https://www.nngroup.com/articles/hamburger-menus/ (Pernice and Budiu)

- Information scent is the user's estimate, from a link's representation, of how likely
  the destination is to answer their question and how long it will take. It comes from
  the link label (most important), accompanying text and image, surrounding context, and
  the user's prior knowledge and trust. "Learn more" has low scent for everyone.
- Images beside links must be representative of the category (Rosch's robin, not chicken).
  Do not rely on page context for meaning; on mobile the context scrolls away.
- Landing pages that are one big image with little text fail to confirm the user is in
  the right place; people leave rather than scroll.
- Clickbait spends trust; brand is experience.
- Hidden navigation (179 participants, 6 sites): "Discoverability is cut almost in half by
  hiding a website's main navigation." Desktop hidden menus used in 27% of cases vs. 48-50%
  visible/combo; desktop tasks 39% slower; mobile 15% slower; task-difficulty ratings 21%
  higher. Causes: low salience, low scent, extra work, no standard, low familiarity.
- Recommendations: on desktop, never hide top-level navigation. On phones, show up to 4
  top-level links visibly; if more, hide some but add in-page links to important content.
  "mobile-first is not the same as mobile-only."

**Carousels and auto-forwarding**
Sources: https://www.nngroup.com/articles/auto-forwarding/ (Nielsen) ;
https://www.nngroup.com/articles/designing-effective-carousels/ (Pernice, reviewed Aug 2026)

- Nielsen's Siemens case: a £100 offer in 98-point type was missed because the panel
  auto-rotated every 5 s. "Accordions and carousels should show a new panel only when
  users ask for it." Auto-forwarding harms accessibility, slow readers, non-native readers,
  single-item visibility, user control, and makes the block look like an ad.
- "people only click links that (a) make sense and (b) describe something they want."
- Pernice: people "often immediately scroll past these large images." A single strong
  static hero is usually better than a carousel. If you must: 5 or fewer frames; crisp
  text and images; show how many frames and which is current; controls inside the
  carousel; recognizably distinct frame buttons; large targets; never auto-forward on
  mobile; time by 3 words per second; put the important content elsewhere on the site too.

**Animation**
Source: https://www.nngroup.com/articles/animation-purpose-ux/ (Laubheimer)

- "Animation in UX must be unobtrusive, brief, and subtle. Use it for feedback,
  state-change and navigation metaphors, and to enhance signifiers." Motion captures
  peripheral vision, so gratuitous motion is distracting by biology. Good uses: confirming
  an action, showing a mode or state change, showing where an overlay or accordion came
  from, previewing a drag result. Bad uses: decoration, "surface-level delight (that
  quickly sours)", attention hijacking (flashing countdowns are a dark pattern). Related
  NN/g finding: scroll-triggered text animations delay users.

**Mobile**
Source: https://www.nngroup.com/articles/mobile-ux/ (Budiu)

- Constraints: small screen (a 30-inch screenful is 5 phone screens; "mobile content is
  twice as difficult"), portable therefore interruptible (average mobile session 72 s vs.
  150 s desktop), single window, touch (bigger targets, typing is hard), variable
  connectivity. Strengths: GPS, camera, tel: links, notifications.
- Rules: high content-to-chrome ratio; prioritize ruthlessly; design for interruption
  (save state, gist before detail); be self-sufficient (no task should require leaving);
  undo matters more; minimize page loads; use device features instead of typing.

**Accessibility**
Source: https://www.nngroup.com/articles/accessibility-is-not-enough/ (Nielsen, 2005) ;
https://www.nngroup.com/articles/accessibility-inclusivity-study-guide/

- "Accessibility is a necessary, but not nearly sufficient, objective." Passing a
  checklist does not mean a screen-reader user can complete a task. Disability is a
  continuum; most people over 45 need resizable text. Test with four or five people who
  use assistive technology, on realistic tasks, with their own tools. Write alt text that
  helps complete the task, not just that exists.

### 2b. Memorable quotes (Nielsen and NN/g)

- "They don't. People rarely read Web pages word by word." (Nielsen, 1997)
- "zero users give zero insights." (Nielsen, 2000)
- "Spend this budget on 3 studies with 5 users each!" (Nielsen, 2000)
- "Users spend most of their time on other sites." (Nielsen, Jakob's Law)
- "Accordions and carousels should show a new panel only when users ask for it." (Nielsen)
- "Accessibility is a necessary, but not nearly sufficient, objective." (Nielsen)
- "mobile-first is not the same as mobile-only." (Pernice and Budiu)
### 2c. What this means for a website (checkable rules)

Writing and scanning
- Each page states its most important fact in the first two paragraphs, ideally the first
  sentence. Test: read only the first paragraph; can you answer the page's main question?
- Headings are informative, front-loaded, and visually heavier than body text. Test: read
  only the headings (the layer-cake test); the page's story should still make sense.
- Body copy is cut to about half of the first draft. Paragraphs carry one idea. Lists are
  bulleted. Numbers appear as numerals.
- No marketese. Delete "world-class", "vibrant", "hottest", and any superlative you cannot
  prove. Replace adjectives with facts (times, counts, names, places).
- Key phrases are bolded sparingly so that bold still means something.

Links and information scent
- Every link label predicts its destination on its own. Test: cover the page, read only
  the links; each must tell you where it goes. "Learn more", "Click here", "Read more"
  fail unless the destination noun is inside the link text.
- The first two words of a link or heading carry the meaning.
- Thumbnails and icons beside links depict the destination's actual category, not mood.
- Link text and the destination page's H1 match closely enough that arrival is confirmed.

Navigation
- Desktop: top-level navigation is always visible; no hamburger. Mobile: four or fewer
  top-level links shown; anything hidden is backed by in-page links to the key pages.
- Consistent placement: logo top-left linking home, search visible if the site has more
  than a few dozen pages, footer with the full map.
- The current section is marked in the navigation on every page.
- Avoid centered logos and novel nav placements; follow Jakob's Law.

Feedback and response time
- Interactive feedback (hover, focus, pressed) within 100 ms; page-to-page navigation
  under 1 s on a typical phone connection, or show a progress cue; anything over 10 s has
  a progress indicator and cancel.
- Progress for multi-step forms: "Step 2 of 3", with the step names.

Carousels, heroes, motion
- Default to a single static hero with one message and one call to action. If a carousel
  survives, apply the eight carousel guidelines above and never auto-rotate on mobile.
- Any animation must do one of: confirm an action, show a state change, explain where
  something came from, strengthen a signifier. Decorative motion is removed. Honor
  `prefers-reduced-motion`. No scroll-triggered text reveals that delay reading.

Mobile
- Content-to-chrome ratio is high; the first screen of every page is content, not a
  header plus hero plus nav.
- Phone numbers are `tel:` links, addresses open maps, dates can be added to calendars,
  forms use correct input types, touch targets are at least about 44 px.
- A task interrupted and resumed does not lose the user's input.

Testing
- Before any redesign ships, five people (or three from each of two distinct groups, for
  example newcomers and members) attempt the top tasks while thinking aloud. Fix, then
  test again. Include at least one assistive-technology user on realistic tasks.

Accessibility (beyond the checklist)
- Alt text answers "what would a sighted user get from this?"; decorative images get
  empty alt. Headings form a real outline. Keyboard reaches everything in order with a
  visible focus ring. Text resizes to 200% without loss. Contrast meets WCAG AA. Nothing
  moves on its own.

---

## 3. Jared Spool

### 3a. Core concepts (with sources)

**Scent of information, trigger words, Move-Forward-Until-Found**
Source: https://articles.centercentre.com/trigger_words/ (2004)

- A page can do only one of two things: "either it contains the content the user wants
  or it contains the links to get them to the content they want." If it does neither, the
  user stops. Spool calls this the Move-Forward-Until-Found rule.
- *Trigger words* are the words that make a user click because they match the words in
  the user's head. In UIE's study, when users succeeded, their own pre-stated description
  words appeared on the home page 72% of the time; when they failed, 6%.
- Failed on-site searches are a log of your users' trigger words. When users searched,
  they typed their description words.
- Links labeled 1-8 or "View 01" (the landscaper example) have no scent. Analog Devices
  improved by putting far more specific component names on the home page.
- Finding trigger words: field visits, personas that list the words each persona would
  use, and usability tests. "The purpose of every link is to move users forward."
- NN/g's information-scent article (section 2) is the same theory from the Xerox PARC
  information-foraging work; Spool's contribution is the trigger-word practice.

**The $300 Million Button**
Source: https://articles.centercentre.com/three_hund_million_button/ (2009)

- A login/register form placed between cart and checkout. New shoppers resented
  registering ("I'm not here to enter into a relationship. I just want to buy something."
  - test participant, quoted by Spool). Repeat shoppers could not remember credentials;
  45% had multiple registrations; 160,000 password requests a day, 75% of whom never
  completed the purchase.
- Fix: replace *Register* with *Continue* and the sentence "You do not need to create an
  account to make purchases on our site." Purchases rose 45%; +$15M the first month, +$300M
  the first year. "All we did was change a button." (Spool)
- Lesson: a form the team saw as helping users was a barrier; the only way to know was to
  watch real people attempt the real task.

**Design is the rendering of intent**
Source: https://articles.centercentre.com/design_rendering_intent/ (2013)

- "The designer imagines an outcome and puts forth activities to make that outcome real."
  Two government sites (Global Entry signup vs. We The People) differed not in resources
  but in intention: one intended to "get the service up and running", the other intended
  to show government could ship clean, easy design.
- Quoting Robert Fabricant: "Behavior is the medium of design." If users behave in ways
  you did not intend (abandon, misread, err), change the design until they do.
- Everyone whose intention shapes the outcome (business, legal, engineering) is designing;
  the experienced designer's job becomes aligning the team on one intention and then
  rendering it faithfully. Research exists to produce a shared intention.

**The Magic Escalator of Acquired Knowledge**
Source: https://articles.centercentre.com/magic_escalator/ (2011)

- *Current knowledge*: what the user knows before they arrive. *Target knowledge*: what
  they need to know to finish the task. The gap is the design problem.
- Two ways to close it: *training* (move current knowledge up: help text, tours) or
  *simplifying* (move target knowledge down: fewer concepts, familiar words, steps that
  match what users already know). "do you train your user or do you reduce the need to
  learn something?" (Spool) Simplifying is usually the better answer.
- Personas are useful precisely when they capture each persona's current knowledge.

**Five design-decision styles (the "tiers")**
Source: https://articles.centercentre.com/figuring-out-your-design-decision-style/ (2016)

1. *Unintentional design*: the experience emerges from technical and business decisions;
   nobody chose it (the placeholder error "Sex is required."). Cheap, and "Once you remove
   quality as a requirement, building your product gets a whole lot easier and cheaper."
2. *Self design*: designing for yourself; works only when the team uses the product daily
   and thinks alike (first iPhone).
3. *Genius design*: so much accumulated domain knowledge that research is predictable;
   earned only by doing activity-focused design first.
4. *Activity-focused design*: research users and their activities (personas, scenarios,
   journey maps, usability tests, field studies); the standard user-centered approach.
5. *Experience-focused design*: design the whole journey before, between and after the
   interactions (Disney MagicBand); very expensive.
   Teams should choose a style deliberately and stick with it; skipping research silently
   drops a team back to self design.

**Five stages of UX design maturity (organizational)**
Source: https://jmspool.medium.com/driving-product-teams-to-become-more-design-mature-4ebbaf1cf9dd
(2019)

- Dark Ages; Spot UX Design; UX Design as a Service; Embedded UX Design; Infused UX Design
  (non-designers make good design decisions). Each team, not the organization, has a
  stage. Levers: exposure to real users (earliest stage); restating business goals as
  experience goals (second stage).
**Experience vision and UX strategy**
Source: https://articles.centercentre.com/the-experience-vision-a-self-fulfilling-ux-strategy/ (2019)

- An experience vision is a story about the user's experience some years out (Apple's
  1987 Knowledge Navigator, delivered as the 2010 iPad; an insurer's "tree falls on the
  garage" story). It specifies the outcome, not the UI. It is a flag on the horizon that
  lets everyone take baby steps in the same direction and lets each person see their own
  work in it. Build it from immersive research into current frustrations, then ask "What's
  the best experience we could imagine providing?" on a ~5-year horizon.
- "It shifts from 'we need to make great designs' to 'we need to make this be our users'
  experience.'" (Spool)

**Delight, frustration, and the Kano model**
Source: https://articles.centercentre.com/understanding-the-kano-model-a-tool-for-sophisticated-designers/ (2018)

- Three forces: *basic expectations* ("The bad frustrates, yet the good doesn't impress"),
  *performance payoff* (more investment, more satisfaction, linearly), and *excitement
  generators* (unexpected delight: Zappos early delivery, Groupon copy, TripIt parsing).
- Excitement generators migrate to basic expectations as everyone copies them (Flickr's
  personalized home page).
- "excitement generators won't delight users who are frustrated when you don't meet their
  basic expectations." This is the source of Spool's often-repeated line that delight
  starts with removing frustration (the slogan form comes from his talks, which we did
  not read; the Kano article is the written basis).

**The Long Wow**
Source: https://articles.centercentre.com/the_long_wow/ (Brandon Schauer, Adaptive Path,
2008, published by UIE; Spool cites it, he did not write it)

- Loyalty is built by repeated, planned moments of "wow" over time, not by loyalty
  programs. "measuring loyalty doesn't create loyalty." Four steps: know your delivery
  platform (touchpoints), tackle a wide area of unmet needs, build a repeatable
  empathy-and-prototype process, and stage the wow moments in a pipeline. The OXO angled
  measuring cup is the canonical example.

**Content first / "the page is the product"**
Note: we did not locate a primary Spool article using the phrase "the page is the
product." The idea as he writes it is the Move-Forward-Until-Found rule (above) plus the
trigger-word study: a page's value is the content it holds or the links it offers; layout
and chrome exist to get people to content. Treat "content first" as the practical
corollary, not as a Spool quotation.

### 3b. Memorable quotes (Spool and sources he published)

- "All we did was change a button." (Spool, 2009)
- "I'm not here to enter into a relationship. I just want to buy something." (test
  participant, quoted by Spool)
- "Design is the rendering of intent." (Spool, 2013)
- "The purpose of every link is to move users forward." (Spool, 2004)
- "Once you remove quality as a requirement, building your product gets a whole lot easier
  and cheaper." (Spool, 2016)
- "The bad frustrates, yet the good doesn't impress." (Spool on basic expectations, 2018)
- "measuring loyalty doesn't create loyalty." (Schauer, 2008)
### 3c. What this means for a website (checkable rules)

Scent and trigger words
- Before writing navigation, collect the actual words visitors use (emails to the office,
  phone questions, search logs, five short interviews). Those words go in the nav labels,
  headings and link text. Test: take the ten most common visitor questions; do their
  nouns appear on the home page?
- Every page passes Move-Forward-Until-Found: it either answers the question in its title
  or it links, with specific labels, to the page that does. A page that is only a
  paragraph of welcome text and a photo fails.
- Home page: more specific links beat fewer generic ones. "Mass Times", "Baptism",
  "Food Pantry Hours" outperform "Worship", "Sacraments", "Outreach" used alone. Use the
  category word plus the specific word.
- Review on-site search logs and 404s monthly; each repeated failed query is a missing
  trigger word.

Forms and barriers (the $300M lesson)
- No account or login is required to do the thing the person came to do (register for
  an event, sign up for a newsletter, give once, ask a question).
- Every field must justify itself; fields that exist for the database but not for the
  task are removed or made optional.
- Watch five real people attempt the top form. Where they hesitate, the form is wrong,
  not the person.

Intent
- Write the intended experience for each key page in one sentence before designing it
  ("A first-time visitor finds this weekend's service time and the parking entrance in
  under 20 seconds on a phone"). Review the shipped page against that sentence.
- Treat unexpected user behavior (bounces, repeated clicks, abandoned forms) as a
  rendering failure to fix, not a user failure to tolerate.

Magic escalator
- For each task, list what a newcomer already knows and what the page assumes. Remove
  the assumptions (insider terms, acronyms, "the Hall", unexplained ministry names) or
  explain them inline. Prefer simplifying to adding help text.
- Inline glosses, not tooltips, for necessary jargon.

Decision style and maturity
- Decide, and write down, that the site is built by activity-focused design: observe real
  visitors, test with them, iterate. When time pressure tempts self design, name it.
- Give non-designers on the team (office staff, volunteers who post events) the two or
  three rules that matter most (plain headings, descriptive links, real photos) so good
  decisions happen without a designer in the room.

Kano and delight
- List the basic expectations and meet all of them first: correct service times, working
  phone number, current events, fast load, works on a phone, forms that send. Only then
  spend effort on excitement generators (a beautifully written welcome, a "what to expect
  on your first visit" page, a one-tap "add to calendar").
- Recheck basics quarterly; they decay (dates, staff, links).

Experience vision and the long wow
- Write a one-paragraph five-year experience vision for the site's audience and keep it
  at the top of the project doc; use it to resolve disputes about features.
- Plan a pipeline of small improvements rather than one big launch; each release should
  contain one visible "that's thoughtful" moment.

---

## 4. UX review checklist (yes/no per page or template)

Mark each No as a defect with a severity. Sources in brackets.
### Navigation and information scent
1. Is the top-level navigation visible without a click on desktop? [Nielsen hamburger study]
2. On phones, are the four most important destinations visible without opening a menu,
   with in-page links backing anything hidden? [Nielsen hamburger study]
3. Does every nav label use a word a first-time visitor would say, not an internal
   name? [Nielsen heuristic 2; Spool trigger words]
4. Covering the page and reading only the links, can you predict every destination?
   [Nielsen information scent; Spool]
5. Does each link's first two words carry its meaning? [Pernice F-pattern]
6. Does every page either answer its question or link specifically to the page that
   does? [Spool Move-Forward-Until-Found]
7. Is the current section highlighted and does the page title match the link that led
   here? [Nielsen heuristic 1; Norman feedback]
8. Does the logo link home from the top-left, and does the footer repeat the full site
   map? [Jakob's Law]
9. Are there zero "Learn more" / "Click here" / "Read more" links without a destination
   noun inside the link text? [Nielsen information scent]

### Page scanning and content hierarchy
10. Does the first paragraph answer the page's main question? [Nielsen, Pernice]
11. Reading only the headings, does the page still make sense? [layer-cake test]
12. Is body copy roughly half the length of a conventional draft, one idea per
    paragraph, with lists bulleted? [Nielsen 1997]
13. Is the copy free of marketese and unprovable superlatives? [Nielsen 1997]
14. Is the most important content in the top-left reading zone rather than a right
    rail that reads as an ad? [F-pattern; banner blindness]
15. Is there one primary call to action above the fold, visibly a button? [Norman
    signifiers; Nielsen heuristic 8]
16. Could a reader circle every clickable element from a static screenshot with no
    false positives? [Norman signifiers]

### Feedback and system status
17. Does every interactive element show hover, focus and pressed states within
    100 ms? [Nielsen response times; Norman feedback]
18. Do actions over 1 s show the system is working, and over 10 s show progress and a
    cancel? [Nielsen response times]
19. After any submission, does the page say what happened and what happens next?
    [Nielsen heuristic 1; Norman stage 5-7]
20. Is the user's location in any multi-step flow shown ("Step 2 of 3")? [heuristic 1]
21. Is there always an obvious way back or out of any overlay, accordion, or flow?
    [heuristic 3]

### Forms and errors
22. Can the top task be completed with no account or login? [$300M button]
23. Does every field exist for the user's task rather than for the database? [Spool]
24. Are constraints used instead of warnings (input types, pickers, selects, sensible
    defaults)? [Norman constraints; heuristic 5]
25. Is every error message in plain language, next to its field, saying what is wrong
    and how to fix it? [heuristic 9; Norman "Error Messages Are Evil"]
26. Are destructive or costly actions separated, precisely named, and reversible or
    confirmed? [Norman slips; heuristic 3]
27. Have five real people attempted the form while thinking aloud since it last changed?
    [Nielsen 5 users]

### Performance perception
28. Does the page become usable in under 1 s on a mid-range phone over 4G, or show a
    meaningful first paint plus progress? [Nielsen limits]
29. Are images sized and compressed so the hero does not block text? [Budiu mobile]
30. Does the design avoid layout shifts that move a target after the user starts to
    tap? [Norman slips; Nielsen too-fast/too-slow]

### Mobile
31. Is the first phone screen mostly content rather than header, hero and chrome?
    [Budiu content-to-chrome]
32. Are touch targets large and spaced, with phone numbers, addresses and dates as
    live tel:, map and calendar links? [Budiu]
33. Does an interrupted task keep its state when the user returns? [Budiu]
34. Does nothing auto-rotate or auto-play on mobile? [Pernice carousels; Nielsen]
35. Is the content identical in substance to desktop, with mobile-first not meaning
    mobile-only? [Pernice and Budiu]

### Accessibility
36. Is every image's alt text written to convey what a sighted user gets, with
    decorative images given empty alt? [Nielsen "Accessibility Is Not Enough"]
37. Do headings form a true outline (one H1, no skipped levels)? [NN/g accessibility]
38. Can every control be reached and operated by keyboard in a sensible order with a
    visible focus ring? [NN/g keyboard accessibility]
39. Does text contrast meet WCAG AA and does the page survive 200% zoom? [Nielsen
    resizable fonts]
40. Does the site respect prefers-reduced-motion and contain no self-moving content?
    [Nielsen auto-forwarding; Laubheimer]
41. Has at least one assistive-technology user tried the top tasks with their own
    tools? [Nielsen]

### Emotional and reflective design
42. Does the first paint look composed, legible and on-brand with real photography?
    [Norman visceral]
43. Do the three most common tasks complete without surprise? [Norman behavioral]
44. Are all dates, names, times and links current, so the organization reads as
    competent and caring? [Norman reflective; Kano basics]
45. Is every animation justified as feedback, state change, spatial orientation, or
    signifier, and nothing else? [Laubheimer]
46. Is the hero a single static message rather than a carousel? [Pernice; Nielsen]
47. Can the team state the intended experience of the page in one sentence, and does
    the page deliver it? [Spool intent]
48. Are all Kano basics met before any delight features were added? [Spool Kano]
49. Does the page assume only knowledge a newcomer has, with insider terms explained or
    removed? [Spool magic escalator]
50. Would a visitor leave with one small "that was thoughtful" moment? [Long Wow]

---

## 5. Source list (all read in full unless noted)

Don Norman
- https://jnd.org/signifiers-not-affordances/
- https://jnd.org/affordances-and-design/
- https://jnd.org/emotional-design-people-and-things/
- https://jnd.org/human-error-no-bad-design/
- https://jnd.org/books/the-design-of-everyday-things-revised-and-expanded-edition/ (full TOC)
- https://jnd.org/error-messages-are-evil/ (excerpt via search)
- DOET ch. 2 excerpt: https://dl.icdst.org/pdfs/files4/4bb8d08a9b309df7d86e62ec4056ceef.pdf (excerpt via search)
- https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/ (Whitenton on Norman)

Jakob Nielsen / NN/g
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.nngroup.com/articles/how-users-read-on-the-web/
- https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/
- https://www.nngroup.com/articles/response-times-3-important-limits/
- https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- https://www.nngroup.com/videos/jakobs-law-internet-ux/
- https://www.nngroup.com/articles/information-scent/
- https://www.nngroup.com/articles/hamburger-menus/
- https://www.nngroup.com/articles/auto-forwarding/
- https://www.nngroup.com/articles/designing-effective-carousels/
- https://www.nngroup.com/articles/animation-purpose-ux/
- https://www.nngroup.com/articles/mobile-ux/
- https://www.nngroup.com/articles/accessibility-is-not-enough/
- https://www.nngroup.com/articles/accessibility-inclusivity-study-guide/ (excerpt via search)

Jared Spool / UIE / Center Centre
- https://articles.centercentre.com/three_hund_million_button/
- https://articles.centercentre.com/design_rendering_intent/
- https://articles.centercentre.com/magic_escalator/
- https://articles.centercentre.com/trigger_words/
- https://articles.centercentre.com/figuring-out-your-design-decision-style/
- https://articles.centercentre.com/the-experience-vision-a-self-fulfilling-ux-strategy/
- https://articles.centercentre.com/understanding-the-kano-model-a-tool-for-sophisticated-designers/
- https://articles.centercentre.com/the_long_wow/ (Brandon Schauer, published by UIE)
- https://jmspool.medium.com/driving-product-teams-to-become-more-design-mature-4ebbaf1cf9dd

Not located as primary text: a Spool article containing the exact phrase "the page is the
product"; the slogan "delight comes from eliminating frustration" exists in talk form, with
the Kano article as its written basis.
