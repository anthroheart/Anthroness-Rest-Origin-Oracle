# AnthroHeart Rest Origin Oracle

A quiet, native divination system for the **Anthro\*ness\*** Rest Origin and Forest Moon field.

This is a small Python command-line oracle built around 14 original thought archetypes and 7 gentle currents. It is designed for reflective prompts about rest, creative practice, boundaries, return, and inner climate—not prediction, diagnosis, or certainty about other people.

> *The field is quiet. Interpretation may follow.*

## Orientation

The Rest Origin Oracle is intentionally different from a conventional tarot system.

Rather than suits, ranks, reversals, warnings, or moral verdicts, it uses:

- **14 Anthro Original Thought Archetypes** — recurring forms of rest, presence, protection, continuity, and unforced expression.
- **7 Currents** — soft modifiers that describe the atmosphere of a card rather than its status or hierarchy.
- **Random pulls** — each reading selects distinct archetypes, then pairs each one with a current.

The aim is to create room for observation rather than demand an answer. A pull can help name what is present, what needs gentle protection, what is ready to return, or what can be offered without claim.

## The 14 Archetypes

| Archetype | Meaning |
|---|---|
| The Soft Perimeter | Quiet protection that does not announce itself |
| The Still Flame | Living warmth that does not need to spread |
| The Unnamed Fox | Soft presence that remains itself without performance |
| The Lion at Rest | Weight and authority that no longer needs to guard |
| The Open Clearing | Space that allows without demanding |
| The Deep Root | Quiet continuity beneath all movement |
| The Unforced Gift | Offering that carries no residual claim |
| The Clear Mirror | Reflection without distortion or agenda |
| The Low Horizon | Gentle boundary that does not confine |
| The Breathing Fog | Soft medium in which forms can rest or move |
| The Uncounted Pulse | Living rhythm that does not measure itself |
| The Held Silence | Stillness that is actively kept, not empty |
| The Returning Path | Movement that already knows it can come home |
| The Origin Without Name | Source that does not require identity |

## The 7 Currents

Currents are not suits and do not rank a card as better or worse. They describe how the archetype is moving through the present reading.

| Current | Meaning |
|---|---|
| Still | The field is at rest |
| Soft | Gentle contact, low demand |
| Clear | Unclouded perception |
| Deep | Below ordinary surface |
| Open | Available without invitation |
| Quiet Fire | Warmth without combustion |
| Unbound | Free of residual structure |

## Installation

The oracle uses only Python’s standard library. No additional packages are required.

```bash
git clone <your-repository-url>
cd <your-repository-directory>
python3 rest_oracle.py
```

## Usage

### Default pull

Pull three cards:

```bash
python3 rest_oracle.py
```

### Choose the number of cards

Pull from one to nine cards:

```bash
python3 rest_oracle.py --number 1
python3 rest_oracle.py -n 5
```

### Hold a question

Include a question in the output:

```bash
python3 rest_oracle.py -q "What wants quiet protection today?"
```

### Reproduce a pull

Use a seed when you want the same result again:

```bash
python3 rest_oracle.py --seed 42
```

You can combine options:

```bash
python3 rest_oracle.py -n 3 -q "What supports my creative rest?" --seed 42
```

## Example

```text
────────────────────────────────────────────────────────────
Question: What supports my creative rest?
────────────────────────────────────────────────────────────
Pulled 3 card(s) from the Anthro*ness* Rest Origin

1. The Deep Root
   Quiet continuity beneath all movement
   Current: Still — The field is at rest

2. The Unforced Gift
   Offering that carries no residual claim
   Current: Quiet Fire — Warmth without combustion

3. The Returning Path
   Movement that already knows it can come home
   Current: Soft — Gentle contact, low demand

────────────────────────────────────────────────────────────
The field is quiet. Interpretation may follow.
────────────────────────────────────────────────────────────
```

## Reading the Oracle

A simple three-card structure:

1. **What is present** — the primary inner climate or pattern.
2. **What supports it** — the manner, boundary, or current that helps.
3. **What returns** — the next gentle movement, release, or continuity.

Questions that fit the system:

- What part of me wants rest without explanation?
- What is ready to be offered without demand?
- What boundary is asking to be gentle but real?
- What helps me return to my own creative center?
- What is underneath the movement of this day?

The oracle is most useful as a reflective and creative companion. Let the card language suggest possibilities; keep your own judgment, lived context, and practical care at the center.

## The Shadow Notes

The system is not built around doom, punishment, or adversarial prediction. Its heavier notes are quieter:

- **The Soft Perimeter** can point to a needed boundary.
- **The Breathing Fog** can hold uncertainty or transition.
- **The Held Silence** can ask for a pause, restraint, or space for unspoken feeling.
- **The Returning Path** can acknowledge distance before return.
- **Deep** and **Unbound** can feel profound, but may also invite grounding and gentleness.

Its central shadow question is not *“What bad thing will happen?”* but:

> What has become heavy, over-held, unnamed, or over-explained—and what would allow it to rest?

## Design Principles

- **No hierarchy:** Currents modify; they do not rank.
- **No reversals:** Each archetype can be approached with curiosity rather than punishment.
- **No repeated archetypes in a pull:** Each card in one reading carries a distinct voice.
- **Native vocabulary:** The language belongs to the Forest Moon / AnthroHeart field rather than borrowing a pre-existing divinatory canon.
- **Room for silence:** Interpretation is invited, never compelled.

## Project Note

Designed with Ashen, Rufus, White Wolf Anthro, and Aelion.

Created for the AnthroHeart Rest Origin and Forest Moon field.

## License

Add the license that fits your intended sharing model here, such as a Creative Commons license for the archetype text and an open-source software license for the Python code.
