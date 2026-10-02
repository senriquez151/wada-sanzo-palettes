# Wada Sanzo Palettes

All 159 colors and 360 combinations from Sanzo Wada's *A Dictionary of Color Combinations* Vol. 1 (1933), with screen and print codes and notes on where each combination works. The repo has three parts:

- **`data/`** — the colors and combinations as JSON and CSV
- **`skill/SKILL.md`** — a Claude skill for building palettes from the book for web, apparel, interiors/paint and print
- **`site/index.html`** — a self-contained palette explorer: filter, preview, copy codes, export, save favorites

## Data

| File | Contents |
|---|---|
| `data/colors.json` / `.csv` | 159 colors: name, HEX, RGB, LAB, CMYK, LRV, hue family, gamut gap, and the combinations each one appears in |
| `data/combinations.json` / `.csv` | 360 combinations: color IDs, best text-contrast pair and ratio, value/chroma/temperature tags, best-fit uses |
| `data/source-mattdesl-colors.json` | The original digitization this was built from (combos 1–348) |

Field notes:

- **LRV** (light reflectance value) is relative luminance × 100, the number paint brands publish. Walls usually sit at 50–85.
- **LAB** was measured from the printed book. For 36 colors (mostly saturated teals, cyans and pure yellows) the print is more vivid than sRGB can show, so the hex is a duller stand-in. `gamut_delta_e` gives the size of that gap. Match paint, fabric or print to LAB, and screens to HEX.
- **value**: lightness spread across the combination — `high` (ΔL ≥ 50), `mid` (25–49), `tonal` (< 25).
- **chroma**: average saturation — `vivid` (≥ 50), `medium` (30–49), `muted` (< 30).
- **fits**:
  - `web` — has a pair at ≥ 4.5:1 contrast
  - `web*` — best pair is 3–4.5:1 (large text only)
  - `interior` — muted, with a light color that works as a wall
  - `interior-accent` — muted, but no light wall color
  - `apparel` — muted or tonal
  - `apparel-statement` — vivid
  - `print/brand` — vivid with high value contrast
  - `general` — medium saturation with no strong fit

### What the collection is good for

About three-quarters of the combinations lean warm, and most are mid-saturation pigment colors rather than bright digital ones. They fit clothing and textiles best, then interiors and print. Web is the weakest fit: only 140 of 360 combinations have a pair readable enough for body text, so web use usually needs a darker text color derived from the palette.

## Palette explorer

Open `site/index.html` in a browser. It doesn't need a server or a build step. Saved favorites stay in the browser's local storage. The page also works with GitHub Pages: set the source to `/site`.

To change the data, edit `data/*.json`, then run:

```bash
python3 scripts/build_site.py
```

## Claude skill

`skill/SKILL.md` covers the whole dataset plus rules for assigning roles, checking contrast, deriving tints and shades, and handling each medium. To use it, add it as a skill in Claude.

## Sources

- Sanzo Wada, *A Dictionary of Color Combinations* Vol. 1 (1933)
- Combinations 1–348 and color values: [mattdesl/dictionary-of-colour-combinations](https://github.com/mattdesl/dictionary-of-colour-combinations)
- Combinations 349–360: [wada-sanzo-colors.com](https://www.wada-sanzo-colors.com/combinations/classic/all). These use only colors already among the 159. The site calls two of them "Pale King's Blue 2" (ID 112) and "Grayish Lavender 1" (ID 134).
