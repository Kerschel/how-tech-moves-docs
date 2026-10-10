# -*- coding: utf-8 -*-
"""
Shared content model for:
  How-Tech-Moves-10-Video-Concepts.docx
  How-Tech-Moves-10-Video-Concepts.pdf

FINAL, APPROVED COPY. Reproduced character-for-character. Nothing here is
paraphrased, shortened, reordered or editorialised.

Block kinds
-----------
("h1", text)                 document title
("subtitle", text)           standfirst under the title
("rule", "")                 hairline rule closing the title block
("h2", text)                 section heading
("h3", text)                 sub-part label (The reveal / Why it lands / ...)
("body", text)               body paragraph
("lead", text)               bold run-in label on its own line
("olist", [[lead, text]])    numbered list, bold lead label per item
("bullets", [[lead, text]])  bullet list, bold (or empty) lead label
("code", text)               mono "Labels:" block
("pagebreak", "")            hard page break

Lead label "" means the item has no bold label.
"""

BLOCKS = []

# ---------------------------------------------------------------- title block
BLOCKS += [
    ("h1", "How Tech Moves — 10 Cinematic Video Concepts"),
    ("subtitle",
     "Ten explainer ideas in the same mould as the AirTag video: one "
     "counterintuitive truth per video, rebuilt shot-by-shot with clean 3D "
     "product renders and big on-screen labels. Each one is written so you can "
     "hand it to a shooter or an animator and get a finished reel."),
    ("rule", ""),
]

# ------------------------------------------------------- the formula section
BLOCKS += [
    ("h2", "FIRST: THE FORMULA (WHY THE AIRTAG VIDEO WORKS)"),
    ("body",
     "The AirTag video isn’t really about AirTags. Its job is to break one "
     "assumption, then visually rebuild the truth. That’s the whole engine, and "
     "every idea below runs on it."),
    ("lead", "The 5-beat skeleton:"),
    ("olist", [
        ["Cold open (0–1.5s)",
         "— state the impossible thing as a fact. “AirTags don’t use GPS.”"],
        ["Hero shot",
         "— the object isolated in black, lit, 3D-rendered, dead centre. Clean "
         "and clinical, not dramatic."],
        ["Knock down the obvious answer",
         "— show why the thing you assumed can’t possibly work. Big label on "
         "screen: OFFLINE."],
        ["Rebuild the truth",
         "— 3–5 fast visual beats showing the hidden mechanism. One idea per beat."],
        ["Payoff line + loop",
         "— one sentence that reframes everything, then cut back to the opening "
         "image so the reel loops seamlessly."],
    ]),
    ("lead", "Production rules that make it feel expensive:"),
    ("bullets", [
        ["", "Hook lands before the first second is over. No intro, no “hey guys”."],
        ["", "One video = one idea. If you have a second idea, it’s a second video."],
        ["", "Dark background, one lit object. Contrast is what reads as “premium”."],
        ["", "On-screen text = short labels, not sentences. Lower-third, rounded "
             "black box."],
        ["", "Sound design over music — whooshes, clicks, a low hum. Silence is a tool."],
        ["", "30–45 seconds. The deep ones can stretch to 60."],
    ]),
]

# the 10 concepts
BLOCKS += [
    ("pagebreak", ""),
    ("h2", "THE 10 CONCEPTS"),
]

BLOCKS += [
    ("h2", "1. FACE ID — “30,000 INVISIBLE DOTS”"),
    ("h3", "The reveal"),
    ("body",
     "Face ID doesn’t “scan” your face like a camera. It fires 30,000 infrared "
     "dots at it and reads how the pattern warps — building a depth map, not a "
     "picture."),
    ("h3", "Why it lands"),
    ("body",
     "People unlock their phone a hundred times a day and have zero idea how. "
     "Massive share-and-save potential."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:02 — Total blackness. Phone floats in centre. On-screen: "
             "“Your face is being mapped 30,000 times.”"],
        ["", "0:02–0:06 — Push in slowly; the sensor face glows a hidden red in "
             "the dark."],
        ["", "0:06–0:14 — Exploded 3D view of the dot projector. Thousands of "
             "tiny dots fan out in a breath-like cone."],
        ["", "0:14–0:22 — Dots strike a 3D face model, scatter, then resolve into "
             "a glowing wireframe topography map."],
        ["", "0:22–0:30 — Split screen: that depth map vs a flat photo of a face. "
             "A photo fails. A photo always fails."],
        ["Payoff:", "“It’s not looking at your face. It’s measuring it.”"],
    ]),
    ("code", "Labels: 30,000 dots · infrared · depth map · a photo won’t work · Length: 35s"),
]

BLOCKS += [
    ("h2", "2. HOW YOUR PHONE KNOWS WHERE YOU ARE WITHOUT GPS"),
    ("h3", "The reveal"),
    ("body",
     "GPS needs open sky and about 30 seconds. But your phone often knows "
     "instantly — because it’s matching the Wi-Fi networks and cell towers "
     "around you against a giant map of where those signals live."),
    ("h3", "Why it lands"),
    ("body",
     "Direct continuation of the AirTag idea. Strong trivia value, easy to demo "
     "on screen."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:03 — Inside a shopping mall, the location dot appears "
             "perfectly. Label: No GPS signal."],
        ["", "0:03–0:08 — Cut to a satellite in orbit. “GPS needs four "
             "satellites.” Cut to the mall roof, blocking every one of them."],
        ["", "0:08–0:18 — 3D render of nearby Wi-Fi routers lighting up like "
             "beacons, each with a signal ring pulsing outward."],
        ["", "0:18–0:26 — The phone “fingerprints” the list of networks it can "
             "hear and matches it to a database of where those networks are."],
        ["", "0:26–0:34 — Overlay: cell towers triangulating as a backup when no "
             "Wi-Fi is around."],
        ["Payoff:", "“It’s not asking the sky. It’s asking the crowd around it.”"],
    ]),
    ("code", "Labels: no GPS · 4 satellites · Wi-Fi fingerprint · cell triangulation · Length: 40s"),
]

BLOCKS += [
    ("h2", "3. TAP-TO-PAY — “YOUR CARD NUMBER NEVER LEAVES YOUR PHONE”"),
    ("h3", "The reveal"),
    ("body",
     "When you tap your phone, your real card number is never transmitted. A "
     "single-use token stands in for it — even Apple and Google never hand your "
     "digits to the terminal."),
    ("h3", "Why it lands"),
    ("body",
     "Money + security + something people do daily without understanding it."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:03 — Slow-motion tap on a payment terminal; a shockwave ring "
             "blooms from the point of contact."],
        ["", "0:03–0:09 — X-ray cutaway of phone and terminal, 3D, suspended. A "
             "beam travels the 3-centimetre gap."],
        ["", "0:09–0:18 — Where you’d expect 4111 1111…, a random token number "
             "appears instead — then dissolves after a single use."],
        ["", "0:18–0:27 — Rapid montage of hundreds of tokens being issued for one "
             "card, each one locked to a single device."],
        ["", "0:27–0:33 — Cut to the terminal: it never saw the real number. "
             "It can’t."],
        ["Payoff:", "“Your card number never crossed the gap. A body double did.”"],
    ]),
    ("code", "Labels: 3 cm · token, not your number · one tap = one token · Length: 35s"),
]

BLOCKS += [
    ("h2", "4. THE PADLOCK — WHY WHATSAPP CAN’T READ YOUR MESSAGES"),
    ("h3", "The reveal"),
    ("body",
     "That green padlock means the message is scrambled before it ever leaves "
     "your phone. The key exists only on the two devices — the company itself "
     "never holds a copy."),
    ("h3", "Why it lands"),
    ("body",
     "Privacy is evergreen, and it flirts with the “wait, really?” "
     "conspiracy-adjacent curiosity that drives comments."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:04 — A message travels as a glowing envelope across a dark "
             "globe. It reaches a server and instantly scrambles into static."],
        ["", "0:04–0:11 — Padlock close-up. Two keys light up — one on sender’s "
             "phone, one on the receiver’s, nowhere else."],
        ["", "0:11–0:19 — The “man in the middle”: a hand reaches for the envelope "
             "mid-flight and closes on nothing but noise."],
        ["", "0:19–0:27 — The honest wrinkle: turn on cloud backups and you can "
             "punch a hole straight through this."],
        ["Payoff:", "“The message isn’t hidden from the server. The server never "
                    "had the key.”"],
    ]),
    ("code", "Labels: end-to-end · 2 keys, 0 copies · backups can break this · Length: 40s"),
]

BLOCKS += [
    ("h2", "5. CALLING FOR HELP FROM THE MIDDLE OF NOWHERE — SATELLITE SOS"),
    ("h3", "The reveal"),
    ("body",
     "No signal, no towers, no Wi-Fi — you point your phone at a satellite and "
     "send an emergency text in about fifteen seconds, over a link the phone was "
     "never designed to use."),
    ("h3", "Why it lands"),
    ("body",
     "Life-saving, high-emotion, and genuinely cinematic. Very shareable."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:04 — Remote terrain, storm or mountains. Phone displays No "
             "Service."],
        ["", "0:04–0:10 — UI shifts: “Point your phone at the sky.” An on-screen "
             "reticle hunts for the satellite."],
        ["", "0:10–0:18 — 3D render of a low-orbit satellite streaking overhead; "
             "a thin beam snaps into place and locks."],
        ["", "0:18–0:27 — Bandwidth is tiny, so only a compressed text survives — "
             "show the size difference against a normal message and the slow "
             "“sending…” bar."],
        ["Payoff:", "“It’s not a phone call. It’s a whisper aimed at orbit.”"],
    ]),
    ("code", "Labels: no towers · lock and hold · 15 seconds · Length: 40s"),
]

BLOCKS += [
    ("h2", "6. HOW HEADPHONES CREATE SILENCE — NOISE CANCELLING"),
    ("h3", "The reveal"),
    ("body",
     "Your headphones don’t block noise. They listen to it, then play the exact "
     "opposite sound wave so the two cancel each other into nothing."),
    ("h3", "Why it lands"),
    ("body",
     "Everyone owns a pair. The physics is satisfying to watch and easy to "
     "render beautifully."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:03 — Macro shot of an ear; exterior noise visualised as a "
             "glowing wave."],
        ["", "0:03–0:09 — A microphone samples the wave; an exact copy is made in "
             "a fraction of a second."],
        ["", "0:09–0:17 — The copy flips upside-down — an inverted wave in 3D, "
             "crest matching trough."],
        ["", "0:17–0:25 — The two waves meet head-on and flatten into a dead "
             "straight line. Silence, rendered."],
        ["", "0:25–0:32 — The honest caveat: brilliant on steady hums, weak on a "
             "sudden voice or a baby crying."],
        ["Payoff:", "“Silence isn’t the absence of sound. It’s sound fighting "
                    "itself.”"],
    ]),
    ("code", "Labels: sample · invert · cancel · steady noise only · Length: 35s"),
]

BLOCKS += [
    ("h2", "7. HOW AI PAINTS A PICTURE FROM PURE STATIC — DIFFUSION"),
    ("h3", "The reveal"),
    ("body",
     "An AI image doesn’t start blank. It starts as random TV static and "
     "de-noises it, step by step, until only your prompt remains."),
    ("h3", "Why it lands"),
    ("body",
     "AI curiosity is the top-performing tech category right now, and the "
     "static-to-photo transformation is a spectacular visual payoff."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:03 — Full-screen white noise, aggressive and loud. Hold it "
             "just long enough to be uncomfortable."],
        ["", "0:03–0:08 — A prompt types on screen: “a leopard in the rain.” The "
             "static begins to clump."],
        ["", "0:08–0:20 — Time-lapse in 3D: static → blobs → shapes → a sharp "
             "photograph. The money shot."],
        ["", "0:20–0:28 — Show it being guided — a scatter of images from its "
             "training nudging each step toward the answer."],
        ["Payoff:", "“It never drew the leopard. It erased the noise until only "
                    "the leopard was left.”"],
    ]),
    ("code", "Labels: pure noise · prompt · de-noise × 50 · Length: 40s"),
]

BLOCKS += [
    ("h2", "8. WHY YOUR NIGHT PHOTOS LOOK IMPOSSIBLE — COMPUTATIONAL PHOTOGRAPHY"),
    ("h3", "The reveal"),
    ("body",
     "Your camera doesn’t take one photo at night. It takes 10 to 30 in a "
     "fraction of a second, then stacks them — filling in light no single shot "
     "ever saw."),
    ("h3", "Why it lands"),
    ("body",
     "Everyone has fought a dark photo. Instantly relatable, and the “stack” "
     "visual is gorgeous."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:03 — Night street, phone raised. The preview on screen is "
             "grainy and dark."],
        ["", "0:03–0:09 — A “shutter” sound; a stack of twenty faint images flies "
             "together into a single pile."],
        ["", "0:09–0:18 — 3D stacking in motion: each blurry frame aligns, noise "
             "cancels out, brightness multiplies."],
        ["", "0:18–0:26 — Reveal: one crisp, bright, impossible-looking photo."],
        ["", "0:26–0:34 — The honest catch: any movement smears, because this is a "
             "stack, not a single frozen instant."],
        ["Payoff:", "“You didn’t capture the dark. You averaged it away.”"],
    ]),
    ("code", "Labels: 20 frames · align · stack · noise cancels · Length: 40s"),
]

BLOCKS += [
    ("h2", "9. WHY STREAMING NEVER BUFFERS — THE INTERNET LIVES NEXT DOOR"),
    ("h3", "The reveal"),
    ("body",
     "Netflix isn’t streaming from a data centre across an ocean. Copies of the "
     "show are cached inside your local internet provider, minutes away — "
     "sometimes a few kilometres from your house."),
    ("h3", "Why it lands"),
    ("body",
     "Universal, frictionless, and it reframes something everyone uses without a "
     "thought."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:03 — You press play. A globe spins and a line races in from "
             "the US… then the whole shot rewinds."],
        ["", "0:03–0:10 — The truth: an unmarked, windowless building near your "
             "town, tagged simply cache."],
        ["", "0:10–0:20 — 3D map: your house, your road, the cache. The file "
             "travels 5 km, not 8,000."],
        ["", "0:20–0:30 — Pull back: millions of these caches form a hidden mesh "
             "that pre-loads what you’re about to watch."],
        ["Payoff:", "“The internet isn’t far away. The internet moved in down the "
                    "street.”"],
    ]),
    ("code", "Labels: not the US · 5 km away · pre-loaded · Length: 40s"),
]

BLOCKS += [
    ("h2", "10. WHY YOUR PHONE CHARGES FAST, THEN SLOW — THE 80% RULE"),
    ("h3", "The reveal"),
    ("body",
     "The last 20% isn’t slow by accident. Fast-charging a nearly-full battery "
     "physically damages it, so the phone deliberately stages the final stretch."),
    ("h3", "Why it lands"),
    ("body",
     "Everyone has watched this happen; almost nobody knows the reason. "
     "Practical and satisfying."),
    ("h3", "Cinematic scene"),
    ("bullets", [
        ["", "0:00–0:04 — Timer on screen: 0→50% in twenty minutes. Then "
             "80→100% takes longer than the entire first half."],
        ["", "0:04–0:11 — Zoom into the battery; ions flow fast and freely at low "
             "charge."],
        ["", "0:11–0:19 — As it fills, the ions crowd together and heat climbs — "
             "show the heat as a red bloom."],
        ["", "0:19–0:27 — 3D comparison: charging under pressure vs the gentle "
             "trickle at the top end."],
        ["", "0:27–0:33 — The real killer is heat, not the current — so the phone "
             "throttles itself on purpose."],
        ["Payoff:", "“It’s not tired. It’s protecting itself from the last 20%.”"],
    ]),
    ("code", "Labels: 0→50% fast · ions crowd · heat · deliberate · Length: 35s"),
]

# ----------------------------------------------------------------- bonus
BLOCKS += [
    ("pagebreak", ""),
    ("h2", "BONUS — THE DIRECT SEQUEL TO YOUR AIRTAG VIDEO"),
    ("h3", "Ultra-Wideband: how your phone points to the exact centimetre."),
    ("body",
     "AirTags don’t just show you a blob on a map — a newer phone will literally "
     "point an arrow at the tag to the centimetre. That’s a second, different "
     "technology inside the same product: Ultra-Wideband, which measures the "
     "time a radio pulse takes to bounce, not signal strength. It’s the natural "
     "“part 2” — same hero object, new hidden mechanism, and it re-hooks "
     "everyone who watched the first one."),
]

# ------------------------------------------------------- running as a series
BLOCKS += [
    ("pagebreak", ""),
    ("h2", "HOW TO RUN THIS AS A SERIES"),
    ("bullets", [
        ["Batch it.",
         "These ten share one visual language, so shoot the renders and record "
         "voiceover in one or two sessions."],
        ["Make the formula the brand.",
         "Same skeleton, same fonts, same label style, same payoff-line cadence. "
         "Viewers should recognise a How Tech Moves video in the first second, "
         "before they read the handle."],
        ["One CTA, repeated.",
         "End every reel with the same line inviting a follow or a save — "
         "consistency compounds."],
        ["Publish order:",
         "lead with #1 Face ID and #7 Diffusion (broadest curiosity), then "
         "alternate a hardware one with a hidden-software one so the feed never "
         "feels repetitive."],
        ["Reuse the objects.",
         "Phone, earbuds, payment terminal, battery — a small prop list covers "
         "all ten, and the 3D assets pay for themselves across the series."],
    ]),
]

# ----------------------------------------------------- self-check on import
def concepts():
    return [b[1] for b in BLOCKS if b[0] == "h2" and b[1][0].isdigit()]


def labels_lines():
    return [b[1] for b in BLOCKS if b[0] == "code"]


def audit():
    """Structural sanity checks on the shared model."""
    h1 = [b for b in BLOCKS if b[0] == "h1"]
    h2 = [b for b in BLOCKS if b[0] == "h2"]
    h3 = [b for b in BLOCKS if b[0] == "h3"]
    code = [b for b in BLOCKS if b[0] == "code"]
    breaks = [b for b in BLOCKS if b[0] == "pagebreak"]
    return {
        "h1": len(h1), "h2": len(h2), "h3": len(h3),
        "code": len(code), "pagebreaks": len(breaks),
        "concepts": len(concepts()),
        "blocks": len(BLOCKS),
    }
