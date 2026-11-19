# Aperture

Aperture is the custom display typeface made for Shade. Heavy is the primary
face; Thin is preserved as a separate related face. This is a working study, not an
artist-accepted or production-ready font release.

The game and the public font study are versioned separately; this repository
contains the public construction study and is not a download for the exact
font build currently in the game.

## Files
- `fonts/ShadeHeavyStudy.ttf` and `.woff`: Heavy study 0.006, 142 encoded characters.
- `fonts/ShadeThinDraft.ttf`: separate Thin uppercase/numeral study.
- `sources/`: editable paths and construction scripts.

DIN remains Shade's body typeface. No DIN binaries or extracted DIN outlines,
game artwork, screenshots, or game source are included here.

## Build
Install Python 3 and `pip install -r requirements.txt`. Run
`python sources/extend-heavy.py` or `python sources/thin-build.py`.
Build outputs appear beside source; committed distribution fonts are in `fonts/`.
Proof generation currently requires DejaVu Sans at the Linux path in the scripts.
Portable builds and reproducible distribution packaging remain release work.

## Review status
Heavy includes genuine lowercase, accents and selected extended Latin forms.
Remaining work includes optical spacing/kerning, broader name coverage,
combining-mark behavior, portable tooling, and actual-menu review with icons in
both themes at multiple screen sizes. Passing font structure checks does not
constitute visual acceptance. Do not silently replace Thin with Heavy.

## Provenance
Original DEMO lettering was constructed and refined with an AI assistant under
Steven's art direction, including tapered and widened revisions approved on
October 30, 2026. These forms are retained in the source paths; subsequent
letters are explicit editable constructions. Thin descends from the separate
EARLY ACCESS / COMING SOON monoline lettering. DIN is a visual influence, not a
bundled or extracted source. This project versions the typeface independently
of the game.

## Licenses
Fonts and glyph/path source data are licensed under SIL Open Font License 1.1
(`OFL.txt`), with no Reserved Font Names. Python build scripts and documentation
are licensed under MIT (`LICENSE-MIT`). This grant covers this repository's
custom typeface material, not Shade's unrelated artwork or third-party fonts.
