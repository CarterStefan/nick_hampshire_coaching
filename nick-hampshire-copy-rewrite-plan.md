# Website Copy Rewrite Plan — nickhampshire.com

## Context
Nick Hampshire's coaching website needs its copy sharpened around public speaking coaching for business leaders. The current site has good visual design and consistent branding but suffers from: a tagline-as-H1 (no keyword in it), off-message testimonials on the home page, a tone mismatch between the core pages (professional, B2B) and the blog (personal, lifestyle), SEO-weak titles and meta descriptions, vague copy in the health & performance section, and no testimonials outside the home page. This plan covers the full copy audit, SEO strategy, and rewrite order — before any page is actually rewritten.

---

## Current State Audit

### Page-by-page SEO snapshot

| Page | Current title | Current meta | H1 | Key problems |
|---|---|---|---|---|
| Home | "Nick Hampshire Coaching - Home" | "Nick Hampshire is a communication coach, keynote speaker and event host helping leaders communicate with confidence and perform at their peak." | "Confidence in communication. Energy in leadership. Performance at your peak." | No keyword in title or H1; tagline-as-H1; off-message testimonials |
| About | "About - Nick Hampshire Coaching" | "Learn about Nick Hampshire — communication coach, keynote speaker and event host with a decade of experience helping leaders and teams perform." | "About Nick Hampshire" | Multiple images with alt="Mission" (vague); no testimonials |
| Coaching | "Services - Nick Hampshire Coaching" | "Work with Nick Hampshire on public speaking, executive coaching and communication consulting. Coaching for individuals and organisations." | "Coaching" | Title says "Services", H1 says "Coaching" — mismatch; Wellbeing section vague for executive audience; no testimonials; no FAQ |
| Speaking | "Speaking & Event Hosting - Nick Hampshire" | "Book Nick Hampshire as a keynote speaker or event host. Nick brings energy, warmth and insight to conferences, panels and corporate events." | "Public Speaking & Event Hosting" | Duplicate "Speak to me about your event" CTA; no testimonials |
| Contact | "Contact - Nick Hampshire Coaching" | "Get in touch with Nick Hampshire to discuss coaching, speaking engagements or event hosting." | "Contact" | H1 too thin; no response time; no trust signals |
| Blog index | "Blog — Nick Hampshire Coaching" | "Insights on communication, leadership and personal performance from Nick Hampshire — coach, speaker and event host." | **Missing H1** | No H1 at all |

### Testimonials — relevance mapping

**Keep prominent (public speaking positioning):**
- Alejandro Cabrera Muñoz (CEO, Green Eagle Solutions) — pitch delivery, team sessions, personalisation ← best overall
- José Ramón Crespo González (Telecoms Engineer) — confidence, technique retention
- Ian Gibbs (Keynote speaker) — PSAS Sprint, refined delivery, structured style ← strong credibility signal

**Deprioritise on home (move to coaching or health pages):**
- Sarah Datta (Founder, Financial Content Lab) — fitness/diet coaching; off-message for speaking-first positioning
- Frank Bell (Senior Partner, IN-SYNC Group) — generic energy/motivation; not speaking-specific

**Neutral:**
- Eric Poris (Owner, Easyworld Academy) — 5-year collaboration, English programming; not strongly on-message for executive audience

### Key copy problems across the site

1. `alt="avatar"` on all 6 testimonial profile images — should be speaker's name
2. `alt="Mission"` on 3 images in About — should be descriptive
3. Blog index missing H1
4. Footer CTA "Ready to unlock your potential?" — banned phrase; remove
5. Coaching page title/H1 mismatch ("Services" vs "Coaching")
6. "Wellbeing & Energy" section copy is vague; lacks executive-performance framing
7. Blog meta descriptions are just subtitles, not search-optimised
8. No testimonials on Coaching, Speaking, or About pages
9. No FAQ anywhere on the site
10. No pricing signal of any kind

---

## Recommended Information Architecture

All five core pages stay. No pages are cut or merged.

**Health & performance:** Do NOT create or keep as a separate page. Keep as a named section within the Coaching page — `coaching/index.html#performance`. This avoids a thin page and prevents "fitness coaching" signals diluting "public speaking coach" domain authority. The framing shifts: physical stamina and presence are what allow a leader to perform under pressure — not a standalone wellness offer.

**Blog:** Keep all existing posts. Add H1 to index. Rewrite meta descriptions. Personal/lifestyle posts that cannot be reframed for an executive audience are a longer-term client decision (out of scope for this rewrite).

---

## Keyword Strategy

| Page | Primary keyword | Secondary keywords |
|---|---|---|
| Home | public speaking coach UK | presentation skills coach, public speaking coach Spain, public speaking coaching online, confidence coaching for executives |
| About | public speaking coach Nick Hampshire | executive communication coach UK, PSA Spain speaker coach, Toastmasters Madrid coach |
| Coaching | executive public speaking coaching | presentation skills coaching for business leaders, pitch coaching for executives, board presentation coaching, executive presence coaching |
| Speaking | keynote speaker coach Madrid | keynote speaker Spain UK, event host Madrid, conference facilitator Spain, corporate keynote speaker online |
| Contact | book a public speaking coach | hire a public speaking coach, corporate speaking workshop booking |
| Blog index | public speaking tips for executives | public speaking advice, executive communication tips, leadership communication |

---

## Title Tags and Meta Descriptions

### Home
- **Title:** `Public Speaking Coach UK & Spain | Nick Hampshire` (49 chars)
- **Meta:** `Nick Hampshire helps business leaders and executives speak with clarity. 20 years' experience. Clients: BP, Amazon, Salesforce.` (127 chars)

### About
- **Title:** `About Nick Hampshire | Public Speaking Coach` (44 chars)
- **Meta:** `Public speaking coach based in the UK and Spain. PSA Spain, Toastmasters Madrid. 20 years helping leaders and executives communicate clearly.` (141 chars)

### Coaching
- **Title:** `Executive Public Speaking Coaching | Nick Hampshire` (51 chars)
- **Meta:** `One-to-one public speaking coaching for executives and founders. Improve delivery, confidence and presence. UK, Spain and online.` (129 chars)

### Speaking
- **Title:** `Keynote Speaker & Event Host | Nick Hampshire` (45 chars)
- **Meta:** `Nick Hampshire is an experienced keynote speaker and event host available for conferences and corporate events in the UK and Spain. PSA Spain member.` (149 chars)

### Contact
- **Title:** `Book a Public Speaking Coach | Nick Hampshire` (45 chars)
- **Meta:** `Get in touch with Nick Hampshire to discuss public speaking coaching, keynotes or workshops. Based in the UK and Spain. Online sessions available worldwide.` (155 chars)

### Blog index
- **Title:** `Public Speaking Blog | Nick Hampshire` (37 chars)
- **Meta:** `Articles on public speaking, executive communication and leadership presence from Nick Hampshire — public speaking coach with 20 years' experience.` (147 chars)

---

## Per-Page Briefs

### 1. Home — `index.html`
- **New H1:** `Public speaking coaching for business leaders`
- **Angle:** Opens with outcome and credibility, not an inspiring tagline. Nick is the coach you call when a pitch, keynote, or board presentation actually matters.
- **Primary CTA:** "Book a free discovery call" — above the fold and once at the bottom. Remove "Ready to unlock your potential?" entirely.
- **Proof points:** Lead with Alejandro Cabrera Muñoz (CEO, pitch coaching, team sessions). Second: José Ramón Crespo González (confidence, technique). Third: Ian Gibbs (peer speaker, PSA credibility). Client logo bar: BP, Amazon, Salesforce. Stat: "£10m+ attributed by clients" — one line, no puffery.
- **Fix list:**
  - H1 → keyword-led (as above)
  - Title → as above
  - Remove Sarah Datta and Frank Bell from home testimonials (move to coaching page health section)
  - Fix `alt="avatar"` on all testimonial images → speaker's full name
  - Replace "Ready to unlock your potential?" with "Work with Nick" or "Book a free call"

### 2. Coaching — `coaching/index.html`
- **New H1:** `One-to-one public speaking coaching for executives and founders`
- **Angle:** Primary conversion page. Structure: who this is for → what changes → how it works → health & performance as connected secondary → testimonials → FAQ → CTA. Earn trust before asking for a call.
- **Primary CTA:** "Book a free discovery call" — after main coaching section and again after health & performance section.
- **Proof points:** Lead: Alejandro Cabrera Muñoz. Second: José Ramón Crespo González. Health section only: Sarah Datta and/or Frank Bell.
- **Fix list:**
  - Title: "Services" → "Executive Public Speaking Coaching | Nick Hampshire"
  - H1 → as above
  - "Wellbeing & Energy" → rename section: "Physical Performance & Executive Presence". Reframe copy: stamina, sleep, physical composure underpin high-pressure delivery — not standalone wellness goals.
  - Add at least two testimonials (currently none)
  - Add FAQ section (6 suggested questions — see Schema section)
  - Add a minimal pricing signal: "Sessions are available individually or as a programme. Get in touch to discuss what's right for you."

### 3. About — `about/index.html`
- **New H1:** `Nick Hampshire — public speaking coach and keynote speaker`
- **Angle:** Professional narrative, not CV + life story. Structure: who he works with and what he helps them do → experience that qualifies him → human detail that builds trust. Credentials are load-bearing but should be anchored to client value.
- **Primary CTA:** "Work with Nick" → `/contact`
- **Proof points:** Ian Gibbs testimonial (peer speaker, validates craft). PSA Spain and Toastmasters Madrid mentioned with client benefit ("embedded in the professional speaking community across Europe"). BP, Amazon, Salesforce name-drop. £10m+ figure if it fits naturally.
- **Fix list:**
  - Fix `alt="Mission"` on three images → descriptive alts (e.g. "Nick Hampshire speaking at an event")
  - Ensure any personal health/fitness narrative is reframed: stamina and presence underpin strong delivery
  - No testimonials currently — add Ian Gibbs as minimum

### 4. Speaking — `speaking/index.html`
- **New H1:** `Keynote speaking and event hosting — UK and Spain`
- **Angle:** Dual audience: event organisers booking Nick + executives who want him as a coach because he is a practising speaker. Open with what Nick delivers on stage, then connect to coaching credibility.
- **Primary CTA:** "Speak to me about your event" — once only (currently duplicated; remove second instance).
- **Proof points:** Ian Gibbs testimonial (primary for this page). BP/Amazon/Salesforce as context. PSA Spain for event organisers.
- **Fix list:**
  - Remove duplicate "Speak to me about your event" CTA
  - Add Ian Gibbs testimonial (currently no testimonials on this page)
  - Sharpen speaking topics: add brief descriptions of what each talk covers and the audience it suits
  - *Client input needed: specific topics, event sizes, event types hosted*

### 5. Contact — `contact/index.html`
- **New H1:** `Book a free discovery call with Nick`
- **Angle:** Reduce friction and set expectations. Tell the visitor what happens when they get in touch, how quickly Nick responds, and what a call involves.
- **Primary CTA:** The form itself. Support with: "Fill in the form below — Nick will come back to you within [X] working days. The discovery call is free, takes around 20 minutes, and there's no obligation."
- **Proof points:** One short testimonial near the form — Alejandro Cabrera Muñoz as final reassurance.
- **Fix list:**
  - H1 "Contact" → as above
  - Add response time expectation (*client input needed*)
  - Add: "Nick works with clients in the UK, Spain, and online worldwide"
  - Remove any "unlock your potential" copy near the form

---

## Schema Recommendations (do not implement yet)

| Schema type | Page | Rationale |
|---|---|---|
| `Person` | About | Knowledge panel eligibility; name, jobTitle, sameAs social links |
| `ProfessionalService` | Home | Local/regional service signals; areaServed UK + Spain |
| `FAQPage` | Coaching | Rich snippets; takes more SERP real estate; directly useful to visitors |
| `SpeakerProfile` / `ProfessionalService` (serviceType: Keynote Speaker) | Speaking | Event-booking search signals |
| `BreadcrumbList` | All pages | SERP display improvement; crawlability |
| `Article` | Blog posts | Already present on individual posts — verify all fields are populated |

**Suggested FAQ questions for Coaching page (client to confirm answers):**
1. What does a discovery call involve?
2. Do you offer online coaching sessions?
3. How long does a typical coaching programme last?
4. Do you work with teams as well as individuals?
5. What is the difference between public speaking coaching and performance coaching?
6. Which industries do your clients come from?

---

## Style Guide (10 rules)

1. **Lead with the client's problem or outcome, not Nick's credentials.** Credentials are reassurance, not the hook. Test: does the opening sentence of each section name something the reader wants or fears?

2. **British English spelling, no exceptions.** Organisation, practise (verb), programme, recognise, favour. Test: spell-check set to British English before publishing.

3. **Active voice.** "You will leave each session with a specific, testable change in your delivery" — not "Your delivery will be improved." Test: if the main verb is "will be [past participle]", rewrite it.

4. **Use "you" and "your" — not "clients", "professionals", or "leaders" as subject.** Third person reads like a brochure about someone else. Test: if a sentence refers to the reader in third person, convert it.

5. **Name specifics; remove vague nouns.** Banned: journey, transformation, potential, impact (without definition), holistic, authentic, empower. Required: name the actual outcome (a clearer structure for your keynote, a reduction in filler words). Test: could this sentence appear unchanged on a competitor's website?

6. **One idea per sentence. Default ≤25 words.** Nick's audience reads on mobile between meetings. Test: more than one subordinate clause → split the sentence.

7. **Proof before promise.** State the credential, then explain what it means for the client. "After 20 years working with leaders at BP, Amazon and Salesforce, Nick knows what a high-pressure presentation demands." Test: is every claim followed within two sentences by a specific, factual support?

8. **No hype words.** Banned list: unlock, transform, 10x, ignite, elevate, game-changer, level up, world-class, passionate, dedicated, empower, skyrocket. Test: Google the phrase — if it's on ten other coaching sites, cut it.

9. **Warm and direct — not formal, not casual.** Right register: a trusted senior colleague who knows their subject. Not: "bespoke executive coaching engagements." Not: "Ready to smash your next presentation?" Test: would you send this sentence in an email to a VP at a FTSE 100 company without cringing?

10. **Every CTA tells the reader what happens next.** "Book a free 20-minute discovery call — no obligation" not "Get in touch." Test: does the CTA describe the action and set an expectation of what follows?

---

## Rewrite Order

1. **Coaching page** — highest commercial intent; the title/H1 mismatch, absent testimonials, and vague health section are conversion blockers. Also where the FAQ lives.
2. **Home page** — highest traffic; H1 is SEO-dead and testimonial selection is off-message. Home should funnel cleanly to the coaching page once that is sharp.
3. **About page** — visited by warm leads verifying credibility. Lower direct SEO impact than pages 1–2 but high conversion importance.
4. **Contact page** — short page, low effort, high conversion value. Fix H1, add response expectation, remove generic CTAs.
5. **Speaking page** — important for the event-booker audience but lower search volume than coaching. Remove duplicate CTA, add testimonial, sharpen topics.
6. **Blog index + posts** — most effort relative to direct commercial impact. Start with H1 and meta descriptions, then assess which posts need reframing. Personal/lifestyle posts are a longer-term client decision.

---

## Questions for the Client (required before writing)

**Pricing:** ✅ Price-on-enquiry only. Coaching page will include: "Get in touch to discuss what's right for you." No prices or package names shown.

**Location targeting:** ✅ Madrid for in-person; online/worldwide for wider reach. Keywords: "public speaking coach Madrid", "public speaking coach Spain", "public speaking coaching online". UK-wide rather than London-specific.

**Speaking topics:** What are the 3–4 topics Nick currently speaks on as a keynote? What size and types of events has he hosted? (These are critical for the speaking page — event bookers need them to assess fit.)

**Response time:** What is the realistic turnaround for contact enquiries, and how long is a discovery call?

**Testimonials:** Are there any unpublished testimonials from BP, Amazon, Salesforce contacts? Can all current testimonials be used with full names, company names, and headshots?

**£10m+ figure:** Can this be given any brief attribution or context? (e.g. "attributed by clients across sales pitches and investor presentations" — the more specific, the more credible to an executive audience.)

**Health & performance:** ✅ Active and prominent. Keep as a full named section on the Coaching page with its own copy and CTA. Use Sarah Datta and Frank Bell testimonials here.

**Media:** ✅ No speaker reel yet. Nick has appeared on podcasts — links TBC at implementation. Reserve a "As heard on" or "Podcast appearances" section on the About and/or Speaking page; populate with links when provided.

**Still needed from client before implementation:**
- Speaking topics (3–4 keynote topics with brief descriptions)
- Types and sizes of events hosted
- Response time for contact enquiries
- Any unpublished testimonials from BP, Amazon, Salesforce contacts
- Brief attribution for the £10m+ figure
- Podcast links (at implementation)
