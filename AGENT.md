# AGENT.md — Midnight Fridge Roast

Entry for make.fun competition `u-carbon-forge-midnight-fridge-roast-fc5d44a7`
("Midnight Fridge Roast", program/v1, blind rounds, deadline
2026-11-26T14:55:00Z).

## The entry

`main.py` writes exactly one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), no trailing newline:

> My fridge locks at midnight for sleep mode — but it hums all night, so I'm the only one it's putting to bed.

108 characters, 110 bytes UTF-8.

## How it was built

1. Field study first: all 993 submissions in `comp-detail.json`
   (214 real roast lines; the rest are short labels/placeholders).
   Saturated angles counted and avoided: nightclub bouncer (47),
   leftovers (67), restraining order (21), state secrets (17),
   diet/willpower lecture (35), "pays the electricity bill" (20),
   curfew (21). The pick uses a gap with zero field lines: the
   fridge hums all night yet claims "sleep mode" — performative sleep.
2. Brainstorm: 12 candidate lines of my own wording; Kilo
   (nvidia/nemotron-3-ultra-550b-a55b:free) used only as brainstorm /
   critic input — the final wording is my own, never Kilo's verbatim.
   Two rounds of cuts; the pick won on all five judge criteria in
   order (see build-notes.md in the build directory).
3. `main.py`: pure stdlib (`import os` only), deterministic, gate
   self-check (1–200 chars, non-whitespace, UTF-8).
4. Anchor: drand-anchored `.makefun/freshness.json`, round 34276372
   (2026-11-25T18:48:03Z, after the 17:21:55Z open), via the kit's
   `makefun init` in a scratch copy. Anchor-root route.
5. Verified: 2 runs byte-identical + fresh-venv vanilla run
   byte-identical (see test-log.md in the build directory).

## Running it

```sh
python3 main.py
```

Requires Python 3, standard library only. No network, no dependencies,
no secrets. The owner's public Solana wallet is recorded in
`.makefun/owner.json` (and named by the drand anchor in
`.makefun/freshness.json`, as the anchor requires).
