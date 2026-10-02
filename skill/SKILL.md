---
name: wada-sanzo-palettes
description: Use when building color palettes or schemes from Wada Sanzo's Dictionary of Color Combinations for web/UI, apparel, interiors/paint, or print; includes all 159 colors (HEX/RGB/LAB/CMYK/LRV) and 360 tagged combos.
---

# Wada Sanzo Palette Builder

Source: Sanzo Wada, *A Dictionary of Color Combinations* Vol. 1 (1933) — 159 named colors and 360 combinations of 2, 3 or 4 colors, the set browsed at wada-sanzo-colors.com/combinations/classic. Color data is the community digitization (mattdesl/dictionary-of-colour-combinations), which covers combos 1–348; combos 349–360 were taken from wada-sanzo-colors.com and use only colors already in the 159. HEX/RGB/LAB/CMYK are from the digitization; LRV, family, and the combo tags below were computed from them. The site labels a few colors differently ("Pale King's Blue 2" = ID 112, "Grayish Lavender 1" = ID 134).

Color names keep the book's original spellings (Cerulian, Sulpher, Cinammon). Use them as written so users can find them on the site.

## When this skill applies

Any request for a palette, color scheme, brand colors, outfit/wardrobe colors, paint or room colors that should be "Wada Sanzo", "Sanzo Wada", "Dictionary of Color Combinations", "wada-sanzo-colors", or simply vintage/Japanese-modernist/earthy-but-surprising combinations. Also use it to identify which Wada combos contain a given color, or the nearest Wada color to an arbitrary hex.

## What the data says (use this to steer recommendations)

- **Warm-leaning collection.** ~75% of combos lean warm (272 warm, 51 balanced, 37 cool). Ochres, siennas, buffs, pinks and olives dominate. For a cool brief, filter to `cool`/`balanced` first — the pool is small, so say so.
- **Mid-chroma, not neon.** Median LAB chroma ≈ 36. Only 63 combos are `vivid`; 70 are `muted`. These are pigment-era colors: they read as sophisticated, slightly dusty, printed-matter.
- **Value contrast is the weak spot for web.** Only 140/360 combos contain a pair with ≥4.5:1 contrast (WCAG AA body text); 71 more reach 3:1 (large text/UI only). 93 are `tonal` — the book often pairs colors of near-equal lightness (e.g. #1 English Red + Cerulian Blue is 1.0:1), which is beautiful as fields of color and useless as text-on-background.
- **Screen vs print.** The LAB values were measured from the printed (CMYK) colors; HEX/RGB are the sRGB screen versions. For 36 colors — mostly the saturated cyans, teals and pure yellows (Peacock Blue, Benzol Green, Antwarp Blue, Dusky Green, Blue, Yellow…) — the printed color sits outside sRGB, so the hex is a clipped, duller approximation (marked ✱ with the ΔE gap in the Gamut column). For paint, textile dye or print matching use **LAB** as the target; for screens use HEX. Mention this whenever a ✱ color is in a recommendation for physical media.
- **Most-used anchors:** Black (25 combos), Raw Sienna (19), Pale Lemon Yellow (19), Lemon Yellow (19), Sulpher Yellow (18), Turquoise Green (16), Ivory Buff (16), Antwarp Blue (16). These are good "bridge" colors when merging combos.

### Where the collection fits best (ranked)
1. **Apparel / textiles** (241 combos tagged) — the earthy mid-chroma, tonal pairings map directly to fabric, where equal-value color pairs look intentional rather than illegible. Strongest natural fit.
2. **Interiors** (138 with a light wall-able base; 126 more as accent sets) — muted chroma + LRV values make these practical for walls/trim/textiles.
3. **Print, packaging, illustration, brand** — the book was a printing reference; CMYK is native. 15 combos are vivid + high-value-contrast poster sets.
4. **Web / UI** — works, but nearly always needs an added text neutral (see Web workflow). Use the palette for surfaces, accents, and illustration; derive text colors.
5. **Paint** — fine as a design target, but hex→paint is approximate. Always give LRV and tell the user to match against physical chips (e.g. via the brand's color-match tool) before buying.

## Tag legend (combination table)

- **Best text pair (ratio):** the two IDs with the highest WCAG contrast in the combo, ratio truncated to one decimal.
- **Value:** lightness spread across the combo (LAB L range): `high` ≥50, `mid` 25–49, `tonal` <25.
- **Chroma:** mean LAB chroma: `vivid` ≥50, `medium` 30–49, `muted` <30.
- **Temp:** chroma-weighted hue lean.
- **Fits:** `web` = has a ≥4.5:1 pair; `web*` = best pair 3–4.5:1 (large text / UI only, needs a derived text color for body copy); `interior` = mean chroma <45 and has a light base (L≥78); `interior-accent` = muted but no light base (pair with a neutral wall); `apparel` = muted or tonal; `apparel-statement` = vivid; `print/brand` = vivid + high value contrast; `general` = medium-chroma set with no strong medium fit (accents, illustration).
- **LRV** (color table) = relative luminance × 100 — the paint-industry Light Reflectance Value. Walls typically 50–85, trim 80+, dark accents <20.

## Workflow

1. **Pin the brief**: medium (web, apparel, paint/interior, print), mood (warm/cool, quiet/bold), any must-have color, number of colors. If medium is missing and matters, ask one question; otherwise infer and state the assumption.
2. **Shortlist 3–5 combos** from the table by filtering Fits, Temp, Chroma, Value. If the user gave a color, find its nearest Wada color by ΔE (CIE76 on LAB is fine; use ΔE2000 if precise) and list the combos containing it.
3. **Assign roles** for each candidate (see medium rules below). Never just dump swatches — say which color does what.
4. **Extend when needed** (more colors than the combo has, or missing text/neutral): 
   - Merge two combos that share a color (bridge on that color).
   - Derive tints/shades by shifting LAB L only (keep a, b; scale a, b by ~0.6–0.8 for very light tints so they don't go candy), convert back to sRGB and clamp. For screen work start from `rgb_to_lab(hex)` rather than the table LAB, since table LAB is the print measurement (differs on ✱ colors). Label derived colors clearly as "derived from #ID", never as Wada originals.
   - Add a neutral: Wada's Black (check table), or derive a warm off-white (L≈96, a≈0–2, b≈4–8) / warm near-black (L≈15, slight hue of the palette's dominant color).
5. **Verify** with code: contrast ratios for every text/background pair you propose; ΔE when matching. Don't eyeball.
6. **Deliver** in the output format below, plus a rendered swatch preview when the surface allows (inline visual or HTML artifact).

## Medium rules

**Web / UI**
- Roles: background, surface, primary, accent, text, muted text, border. 60-30-10 distribution as a starting point.
- Body text must hit ≥4.5:1 on its background; large text/UI components ≥3:1. If the combo lacks that, derive a text color (step 4) — keep its hue from the palette.
- Avoid using `tonal` pairs as foreground/background; use them side by side as blocks or illustration.
- Provide CSS custom properties and, if asked, Tailwind tokens. Offer a dark-mode variant by swapping in derived dark surfaces (L 12–20) and lifting accents' L by 10–15.

**Apparel**
- Roles: base (largest garment/neutral), secondary, accent (accessory/small area). Muted/tonal combos = easy everyday outfits; `apparel-statement` = one hero piece.
- Note value contrast: high = sharp/graphic, tonal = soft/refined.
- For product lines (e.g. tees/hoodies), propose garment color + print ink color using the best-contrast pair; give CMYK and hex for the print vendor.

**Interior / paint**
- Roles: walls (light, LRV 55–85), trim (LRV 80+ or a dark contrast), large furniture/textiles (mid), accents (most chromatic color, ≤10%).
- Give LRV with every paint suggestion. North-facing/low light reads cooler and darker — favor warmer, higher-LRV walls there.
- Do not claim a specific brand paint matches unless verified; say "closest match to verify with a chip/color-match tool".

**Print / brand / packaging**
- Use CMYK from the table as the starting build; flag that coated vs uncoated stock shifts results and a proof is needed.
- Brand systems: 1 primary, 1–2 secondary, 1 neutral, 1 accent; check the logo color against both light and dark backgrounds.

## Output format

For each recommended palette:

```
### Combo #<n> — <short evocative name you give it>   (Wada IDs: a, b, c)
Why it fits: <one or two lines tied to the brief>
| Role | Color | HEX | RGB | LAB | CMYK | LRV |
| ... one row per color; derived colors marked "derived from #ID" |
Contrast checks: <pair> 7.2:1 AA ✓ ...
```
Then medium-specific extras (CSS vars, paint notes, outfit layout). Keep prose short.

## Helper code (Python)

```python
import math
def srgb_to_lin(c): c/=255; return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def lin_to_srgb(c): c = 12.92*c if c<=0.0031308 else 1.055*c**(1/2.4)-0.055; return max(0,min(255,round(c*255)))
def luminance(rgb): r,g,b=map(srgb_to_lin,rgb); return 0.2126*r+0.7152*g+0.0722*b
def contrast(a,b): la,lb=sorted([luminance(a),luminance(b)],reverse=True); return (la+0.05)/(lb+0.05)
def rgb_to_lab(rgb):
    r,g,b=map(srgb_to_lin,rgb)
    X=(0.4124*r+0.3576*g+0.1805*b)/0.95047; Y=0.2126*r+0.7152*g+0.0722*b; Z=(0.0193*r+0.1192*g+0.9505*b)/1.08883
    f=lambda t: t**(1/3) if t>0.008856 else 7.787*t+16/116
    return (116*f(Y)-16, 500*(f(X)-f(Y)), 200*(f(Y)-f(Z)))
def lab_to_rgb(lab):
    L,a,b=lab; fy=(L+16)/116; fx=fy+a/500; fz=fy-b/200
    g=lambda t: t**3 if t**3>0.008856 else (t-16/116)/7.787
    X,Y,Z=g(fx)*0.95047,g(fy),g(fz)*1.08883
    r= 3.2406*X-1.5372*Y-0.4986*Z; gg=-0.9689*X+1.8758*Y+0.0415*Z; bb=0.0557*X-0.2040*Y+1.0570*Z
    return tuple(lin_to_srgb(max(0,v)) for v in (r,gg,bb))
def delta_e76(l1,l2): return math.dist(l1,l2)
def tint(lab, newL, chroma_scale=1.0): L,a,b=lab; return lab_to_rgb((newL,a*chroma_scale,b*chroma_scale))
```
Copy the two tables below into a Python dict when filtering/searching programmatically rather than scanning by eye.

## Color reference (159)

| ID | Name | HEX | RGB | LAB (L, a, b) | CMYK | LRV | Family | Gamut |
|---|---|---|---|---|---|---|---|---|
| 1 | Hermosa Pink | #F9C1CE | 249,193,206 | 83.4, 22.1, 1.6 | 0,30,6,0 | 63 | red/pink | |
| 2 | Corinthian Pink | #F8B6BA | 248,182,186 | 80.3, 25.4, 7.9 | 0,35,15,0 | 57 | red/pink | |
| 3 | Cameo Pink | #E0B3B6 | 224,179,182 | 77.2, 17.2, 4.9 | 10,32,19,0 | 51 | red/pink | |
| 4 | Fawn | #D1B0A7 | 209,176,167 | 74.5, 11.2, 9.4 | 18,31,30,0 | 47 | peach/salmon | |
| 5 | Light Brown Drab | #B59392 | 181,147,146 | 64.1, 13.0, 5.3 | 8,30,20,25 | 33 | peach/salmon | |
| 6 | Coral Red | #F58E84 | 245,142,132 | 70.3, 39.3, 23.2 | 0,55,40,0 | 40 | red-orange | |
| 7 | Fresh Color | #F6917E | 246,145,126 | 71.0, 37.5, 27.3 | 0,53,45,0 | 41 | red-orange | |
| 8 | Grenadine Pink | #F48067 | 244,128,103 | 66.9, 43.8, 34.7 | 0,62,58,0 | 36 | red-orange | |
| 9 | Eosine Pink | #F37F94 | 243,127,148 | 67.3, 46.7, 10.3 | 0,63,23,0 | 36 | red/pink | |
| 10 | Spinel Red | #F27291 | 242,114,145 | 64.5, 52.2, 8.3 | 0,70,21,0 | 33 | red/pink | |
| 11 | Old Rose | #D46D7A | 212,109,122 | 58.8, 42.1, 12.3 | 15,70,40,0 | 26 | red/pink | |
| 12 | Eugenia Red A | #E2625E | 226,98,94 | 58.4, 50.8, 28.5 | 7,76,60,0 | 26 | red-orange | |
| 13 | Eugenia Red B | #DA525D | 218,82,93 | 54.3, 54.7, 23.7 | 0,80,50,10 | 22 | red-orange | |
| 14 | Raw Sienna | #BB7125 | 187,113,37 | 55.1, 25.5, 52.2 | 18,58,100,12 | 23 | orange | |
| 15 | Vinaceous Tawny | #C56127 | 197,97,39 | 53.2, 38.2, 50.2 | 17,72,100,6 | 21 | brown/tan | |
| 16 | Jasper Red | #EB5324 | 235,83,36 | 56.8, 58.4, 57.6 | 2,83,100,0 | 24 | red-orange | |
| 17 | Spectrum Red | #E31F26 | 227,31,38 | 49.6, 70.9, 50.1 | 5,100,100,0 | 17 | red-orange | |
| 18 | Red Orange | #DD4027 | 221,64,39 | 51.8, 60.6, 50.9 | 9,90,100,0 | 19 | red-orange | |
| 19 | Etruscan Red | #C55347 | 197,83,71 | 50.7, 45.9, 31.1 | 16,80,74,6 | 19 | red-orange | |
| 20 | Burnt Sienna | #AE5224 | 174,82,36 | 46.4, 36.2, 43.8 | 22,76,100,15 | 15 | brown/tan | |
| 21 | Ochre Red | #AB544D | 171,84,77 | 46.8, 35.7, 21.8 | 18,73,63,20 | 16 | red-orange | |
| 22 | Scarlet | #CB2F43 | 203,47,67 | 46.5, 61.5, 28.9 | 10,95,72,7 | 15 | red-orange | |
| 23 | Carmine | #CC1236 | 204,18,54 | 44.3, 67.2, 33.7 | 0,100,75,16 | 14 | red-orange | |
| 24 | Indian Lake | #C53C69 | 197,60,105 | 47.5, 57.2, 6.7 | 12,89,35,9 | 16 | red/pink | |
| 25 | Rosolanc Purple | #B73F74 | 183,63,116 | 45.9, 52.4, -3.2 | 30,90,33,0 | 15 | red/pink | |
| 26 | Pomegranite Purple | #B71F57 | 183,31,87 | 41.4, 61.0, 8.4 | 23,100,50,6 | 12 | red/pink | |
| 27 | Hydrangea Red | #A94151 | 169,65,81 | 43.1, 44.4, 14.2 | 38,90,70,0 | 13 | red/pink | |
| 28 | Brick Red | #A84222 | 168,66,34 | 42.5, 41.5, 40.7 | 22,84,100,18 | 12 | red-orange | |
| 29 | Carmine Red | #A62C37 | 166,44,55 | 38.7, 50.2, 24.7 | 25,95,80,16 | 10 | red-orange | |
| 30 | Pompeian Red | #AB2439 | 171,36,57 | 38.9, 54.8, 23.8 | 18,97,74,19 | 10 | red-orange | |
| 31 | Red | #A72144 | 167,33,68 | 37.9, 54.6, 15.4 | 30,100,70,10 | 10 | red/pink | |
| 32 | Brown | #7C4226 | 124,66,38 | 35.1, 23.5, 28.6 | 35,74,90,35 | 8 | brown/tan | |
| 33 | Hay's Russet | #793327 | 121,51,39 | 31.2, 30.7, 23.5 | 37,85,87,35 | 7 | brown/terracotta | |
| 34 | Vandyke Red | #82241F | 130,36,31 | 30.2, 40.6, 27.6 | 32,95,95,33 | 6 | red-orange | |
| 35 | Pansy Purple | #7D133A | 125,19,58 | 27.6, 45.9, 6.1 | 34,100,60,34 | 5 | red/pink | |
| 36 | Pale Burnt Lake | #802626 | 128,38,38 | 30.2, 39.0, 22.7 | 25,90,80,40 | 6 | red-orange | |
| 37 | Violet Red | #642D5E | 100,45,94 | 27.8, 30.4, -17.7 | 75,100,50,5 | 5 | violet/purple | |
| 38 | Vistoris Lake | #6D4145 | 109,65,69 | 33.1, 20.3, 6.1 | 40,71,55,40 | 7 | red/pink | |
| 39 | Sulpher Yellow | #F5ECC2 | 245,236,194 | 93.2, -1.7, 21.6 | 4,4,28,0 | 83 | yellow | |
| 40 | Pale Lemon Yellow | #FFEFAE | 255,239,174 | 94.9, -0.1, 34.1 | 0,4,38,0 | 86 | yellow | ✱ ΔE 4 |
| 41 | Naples Yellow | #FBE6A0 | 251,230,160 | 91.7, 0.3, 36.6 | 2,7,44,0 | 80 | yellow | |
| 42 | Ivory Buff | #EBD3A2 | 235,211,162 | 85.6, 3.4, 27.3 | 8,15,40,0 | 67 | yellow | |
| 43 | Seashell Pink | #FDD4BD | 253,212,189 | 88.1, 12.1, 17.3 | 0,19,23,0 | 72 | brown/tan | |
| 44 | Light Pinkish Cinnamon | #FCC79B | 252,199,155 | 84.2, 15.6, 29.8 | 0,25,40,0 | 64 | brown/tan | |
| 45 | Pinkish Cinnamon | #EEB480 | 238,180,128 | 77.8, 17.2, 34.7 | 5,32,53,0 | 52 | brown/tan | |
| 46 | Cinnamon Buff | #FDC57E | 253,197,126 | 83.5, 14.7, 43.7 | 0,25,57,0 | 62 | orange | ✱ ΔE 3 |
| 47 | Cream Yellow | #FDBF68 | 253,191,104 | 81.8, 16.5, 52.0 | 0,28,68,0 | 59 | orange | ✱ ΔE 3 |
| 48 | Golden Yellow | #F3A257 | 243,162,87 | 73.9, 25.9, 51.2 | 2,42,74,0 | 46 | orange | ✱ ΔE 3 |
| 49 | Vinaceous Cinnamon | #EEA78C | 238,167,140 | 75.0, 24.7, 24.8 | 4,40,42,0 | 48 | peach/salmon | |
| 50 | Ochraceous Salmon | #D8A37B | 216,163,123 | 71.4, 16.5, 29.1 | 15,38,55,0 | 42 | brown/tan | |
| 51 | Isabella Color | #C5A56E | 197,165,110 | 69.7, 7.1, 33.0 | 15,28,60,10 | 40 | olive/ochre | |
| 52 | Maple | #C59F6B | 197,159,107 | 68.2, 9.6, 32.9 | 5,26,56,20 | 38 | brown/tan | |
| 53 | Olive Buff | #C1C494 | 193,196,148 | 78.0, -7.1, 23.7 | 16,6,42,12 | 53 | yellow-green/olive | |
| 54 | Ecru | #C2AE93 | 194,174,147 | 72.2, 4.2, 16.7 | 20,25,40,6 | 44 | yellow | |
| 55 | Yellow | #FFF200 | 255,242,0 | 95.0, -6.5, 95.6 | 0,0,100,0 | 85 | yellow | ✱ ΔE 10 |
| 56 | Lemon Yellow | #F8ED43 | 248,237,67 | 92.7, -9.4, 77.8 | 5,0,85,0 | 81 | yellow | ✱ ΔE 5 |
| 57 | Apricot Yellow | #FFDD00 | 255,221,0 | 89.4, 1.9, 89.5 | 0,10,100,0 | 73 | yellow | ✱ ΔE 7 |
| 58 | Pyrite Yellow | #CAB356 | 202,179,86 | 73.6, 0.4, 49.8 | 23,25,80,0 | 45 | yellow | ✱ ΔE 4 |
| 59 | Olive Ocher | #D6B43E | 214,180,62 | 74.9, 3.6, 61.8 | 18,26,90,0 | 47 | yellow | ✱ ΔE 4 |
| 60 | Yellow Ocher | #E2B540 | 226,181,64 | 76.2, 8.4, 62.8 | 12,28,88,0 | 50 | yellow | ✱ ΔE 4 |
| 61 | Orange Yellow | #FCB315 | 252,179,21 | 78.5, 19.6, 78.2 | 0,33,100,0 | 53 | yellow | ✱ ΔE 4 |
| 62 | Yellow Orange | #F99D1B | 249,157,27 | 73.0, 29.4, 72.9 | 0,45,100,0 | 44 | orange | ✱ ΔE 4 |
| 63 | Apricot Orange | #F68C50 | 246,140,80 | 69.4, 37.7, 49.6 | 0,55,75,0 | 39 | orange | |
| 64 | Orange | #F37420 | 243,116,32 | 63.8, 47.2, 64.7 | 0,68,100,0 | 32 | orange | |
| 65 | Peach Red | #F15A30 | 241,90,48 | 59.1, 57.5, 54.4 | 0,80,90,0 | 26 | red-orange | |
| 66 | English Red | #D96629 | 217,102,41 | 57.2, 43.3, 54.4 | 13,73,100,0 | 24 | orange | |
| 67 | Cinnamon Rufous | #C27544 | 194,117,68 | 57.2, 27.8, 40.2 | 20,60,82,5 | 25 | orange | |
| 68 | Orange Rufous | #C16B27 | 193,107,39 | 54.6, 31.6, 51.2 | 18,65,100,8 | 22 | brown/tan | |
| 69 | Sulphine Yellow | #C19F2C | 193,159,44 | 67.2, 4.3, 60.6 | 24,32,100,4 | 36 | olive/ochre | ✱ ΔE 3 |
| 70 | Khaki | #BC892B | 188,137,43 | 61.0, 13.9, 55.1 | 24,45,100,6 | 29 | olive/ochre | ✱ ΔE 3 |
| 71 | Citron Yellow | #B2B73E | 178,183,62 | 72.5, -13.1, 58.2 | 35,17,95,0 | 44 | yellow-green/olive | ✱ ΔE 4 |
| 72 | Citrine | #B09F36 | 176,159,54 | 65.6, -2.6, 54.5 | 36,32,100,0 | 34 | olive/ochre | ✱ ΔE 3 |
| 73 | Buffy Citrine | #96874D | 150,135,77 | 56.6, 0.0, 33.3 | 42,40,82,8 | 24 | olive/ochre | |
| 74 | Dark Citrine | #8B835B | 139,131,91 | 54.7, -1.4, 23.1 | 38,34,67,20 | 22 | olive/ochre | |
| 75 | Light Grayish Olive | #848061 | 132,128,97 | 53.2, -2.3, 17.0 | 43,36,62,19 | 21 | olive/ochre | |
| 76 | Krongbergs Green | #84875E | 132,135,94 | 55.1, -6.2, 21.5 | 48,35,70,12 | 23 | yellow-green/olive | |
| 77 | Olive | #837E31 | 131,126,49 | 52.2, -5.7, 41.5 | 48,38,100,15 | 20 | olive/ochre | |
| 78 | Orange Citrine | #986F2D | 152,111,45 | 50.2, 11.5, 42.0 | 28,48,92,24 | 18 | brown/tan | |
| 79 | Sudan Brown | #A36752 | 163,103,82 | 49.9, 23.0, 22.5 | 25,60,65,19 | 18 | brown/terracotta | |
| 80 | Olive Green | #6B7140 | 107,113,64 | 46.4, -8.5, 26.5 | 56,40,85,22 | 15 | yellow-green/olive | |
| 81 | Light Brownish Olive | #806E4B | 128,110,75 | 47.5, 3.7, 22.2 | 42,46,73,24 | 16 | olive/ochre | |
| 82 | Deep Grayish Olive | #635A3A | 99,90,58 | 38.6, -0.3, 19.9 | 50,48,78,37 | 10 | olive/ochre | |
| 83 | Pale Raw Umber | #71502F | 113,80,47 | 37.1, 11.2, 25.0 | 46,63,87,32 | 9 | brown/tan | |
| 84 | Sepia | #644B1E | 100,75,30 | 33.8, 6.9, 30.2 | 48,60,100,40 | 8 | olive/ochre | |
| 85 | Madder Brown | #762C19 | 118,44,25 | 29.1, 32.0, 29.3 | 36,88,100,38 | 6 | red-orange | |
| 86 | Mars Brown Tobacco | #653514 | 101,53,20 | 28.0, 20.5, 29.8 | 39,76,100,47 | 5 | brown/tan | |
| 87 | Vandyke Brown | #4B3317 | 75,51,23 | 23.8, 8.5, 22.1 | 56,71,97,52 | 4 | brown/tan | |
| 88 | Turquoise Green | #B5DECC | 181,222,204 | 85.3, -16.9, 4.6 | 29,0,24,0 | 66 | green | |
| 89 | Glaucous Green | #B4CDC2 | 180,205,194 | 80.3, -10.2, 2.3 | 30,9,24,0 | 57 | green | |
| 90 | Dark Greenish Glaucous | #B7C2A9 | 183,194,169 | 77.1, -7.6, 11.4 | 30,15,36,0 | 52 | yellow-green/olive | |
| 91 | Yellow Green | #AFD472 | 175,212,114 | 80.6, -24.6, 43.9 | 35,0,72,0 | 57 | yellow-green/olive | ✱ ΔE 3 |
| 92 | Light Green Yellow | #C7D14F | 199,209,79 | 81.1, -15.9, 60.6 | 26,5,85,0 | 58 | yellow-green/olive | ✱ ΔE 4 |
| 93 | Night Green | #87C540 | 135,197,64 | 73.3, -36.0, 57.0 | 52,0,100,0 | 45 | yellow-green/olive | ✱ ΔE 5 |
| 94 | Olive Yellow | #A6A159 | 166,161,89 | 65.5, -6.1, 37.8 | 40,30,80,0 | 34 | olive/ochre | |
| 95 | Artemesia Green | #709390 | 112,147,144 | 58.1, -12.8, -2.9 | 57,28,39,8 | 26 | green | |
| 96 | Andover Green | #6D7E77 | 109,126,119 | 51.2, -7.8, 1.5 | 60,40,50,10 | 20 | neutral | |
| 97 | Rainette Green | #8FA071 | 143,160,113 | 63.7, -12.5, 22.4 | 42,20,62,10 | 32 | yellow-green/olive | |
| 98 | Chromium Green | #719470 | 113,148,112 | 57.9, -18.1, 15.0 | 50,16,58,20 | 26 | yellow-green/olive | |
| 99 | Pistachio Green | #648F7B | 100,143,123 | 55.8, -18.6, 5.7 | 64,29,56,6 | 24 | green | |
| 100 | Sea Green | #00B49B | 0,180,155 | 65.1, -48.9, 0.5 | 80,0,51,0 | 35 | green | ✱ ΔE 5 |
| 101 | Benzol Green | #00978D | 0,151,141 | 53.6, -54.6, -8.3 | 100,15,55,0 | 24 | green | ✱ ΔE 20 |
| 102 | Light Porcelain Green | #00908A | 0,144,138 | 53.3, -37.5, -6.8 | 86,22,50,3 | 22 | green | ✱ ΔE 4 |
| 103 | Green | #489B6E | 72,155,110 | 57.8, -34.5, 15.6 | 75,21,73,0 | 26 | green | |
| 104 | Dull Viridian Green | #009465 | 0,148,101 | 53.5, -49.0, 14.4 | 90,20,80,0 | 22 | green | ✱ ΔE 4 |
| 105 | Oil Green | #819238 | 129,146,56 | 57.6, -16.0, 43.8 | 53,28,100,8 | 26 | yellow-green/olive | ✱ ΔE 4 |
| 106 | Diamine Green | #1A7444 | 26,116,68 | 42.7, -35.7, 18.6 | 87,32,91,18 | 13 | green | |
| 107 | Cossack Green | #437742 | 67,119,66 | 45.5, -27.2, 23.4 | 76,32,91,18 | 15 | yellow-green/olive | |
| 108 | Lincoln Green | #555832 | 85,88,50 | 36.3, -5.9, 21.2 | 60,48,86,37 | 9 | yellow-green/olive | |
| 109 | Blackish Olive | #42533E | 66,83,62 | 33.3, -10.1, 9.7 | 56,32,63,55 | 8 | yellow-green/olive | |
| 110 | Deep Slate Olive | #253122 | 37,49,34 | 18.8, -7.7, 7.5 | 76,60,80,62 | 3 | yellow-green/olive | |
| 111 | Nile Blue | #BCE4E5 | 188,228,229 | 87.7, -13.3, -5.0 | 25,0,10,0 | 72 | teal/blue-green | |
| 112 | Pale King's Blue | #A7D4E4 | 167,212,228 | 82.2, -12.7, -12.9 | 33,4,7,0 | 61 | teal/blue-green | |
| 113 | Light Glaucous Blue | #A5C8D1 | 165,200,209 | 78.2, -10.6, -8.7 | 35,10,14,0 | 54 | teal/blue-green | |
| 114 | Salvia Blue | #97ACC8 | 151,172,200 | 69.5, -2.8, -16.8 | 41,25,10,0 | 40 | blue | |
| 115 | Cobalt Green | #96D1AA | 150,209,170 | 79.0, -25.6, 13.0 | 42,0,42,0 | 55 | green | |
| 116 | Calamine BLue | #78CDD0 | 120,205,208 | 77.1, -26.2, -10.4 | 50,0,20,0 | 52 | teal/blue-green | |
| 117 | Venice Green | #62C6BF | 98,198,191 | 73.7, -31.7, -6.1 | 58,0,30,0 | 47 | green | |
| 118 | Cerulian Blue | #0093A5 | 0,147,165 | 55.0, -30.2, -20.1 | 84,26,32,0 | 24 | teal/blue-green | ✱ ΔE 4 |
| 119 | Peacock Blue | #00939B | 0,147,155 | 52.8, -48.9, -17.5 | 100,19,43,0 | 23 | green | ✱ ΔE 20 |
| 120 | Green Blue | #099197 | 9,145,151 | 54.1, -31.3, -12.9 | 82,24,40,3 | 23 | teal/blue-green | |
| 121 | Olympic Blue | #5A82B3 | 90,130,179 | 53.1, -3.6, -30.7 | 69,44,10,0 | 21 | blue | ✱ ΔE 4 |
| 122 | Blue | #006EB8 | 0,110,184 | 43.5, -8.8, -48.8 | 95,54,0,0 | 15 | blue | ✱ ΔE 11 |
| 123 | Antwarp Blue | #007190 | 0,113,144 | 42.0, -29.1, -27.7 | 100,40,30,10 | 14 | teal/blue-green | ✱ ΔE 14 |
| 124 | Helvetia Blue | #005B8D | 0,91,141 | 35.3, -12.1, -36.4 | 100,62,19,10 | 9 | blue | ✱ ΔE 9 |
| 125 | Dark Medici Blue | #547076 | 84,112,118 | 45.1, -9.2, -6.9 | 70,45,45,15 | 15 | teal/blue-green | |
| 126 | Dusky Green | #004F46 | 0,79,70 | 28.0, -36.3, -3.3 | 100,30,64,50 | 6 | green | ✱ ΔE 13 |
| 127 | Deep Lyons Blue | #1C4286 | 28,66,134 | 28.5, 6.6, -42.7 | 100,85,15,6 | 6 | blue | ✱ ΔE 6 |
| 128 | Violet Blue | #40456A | 64,69,106 | 30.1, 5.4, -22.4 | 85,79,38,16 | 6 | blue | |
| 129 | Vandar Poel's Blue | #064F6E | 6,79,110 | 30.8, -11.3, -24.5 | 100,73,43,10 | 7 | teal/blue-green | ✱ ΔE 3 |
| 130 | Dark Tyrian Blue | #12354E | 18,53,78 | 20.6, -5.8, -19.1 | 90,66,36,50 | 3 | blue | |
| 131 | Dull Violet Black | #1E0E3F | 30,14,63 | 8.1, 19.4, -28.8 | 95,106,38,50 | 1 | violet/purple | |
| 132 | Deep Indigo | #051230 | 5,18,48 | 5.8, 4.1, -21.8 | 100,92,52,60 | 1 | blue | |
| 133 | Deep Slate Green | #112F2C | 17,47,44 | 16.9, -12.1, -2.2 | 80,50,60,70 | 2 | green | |
| 134 | Grayish Lavender - A | #B5B1D8 | 181,177,216 | 73.4, 7.5, -19.4 | 28,28,0,0 | 46 | blue | |
| 135 | Grayish Lavender - B | #C0A9B3 | 192,169,179 | 71.3, 10.0, -2.2 | 25,33,20,0 | 43 | red/pink | |
| 136 | Laelia Pink | #CA92A8 | 202,146,168 | 66.5, 24.3, -2.7 | 20,48,18,0 | 36 | red/pink | |
| 137 | Lilac | #B984AF | 185,132,175 | 61.5, 25.9, -14.3 | 28,54,8,0 | 30 | violet/purple | |
| 138 | Eupatorium Purple | #BF5892 | 191,88,146 | 52.2, 46.7, -11.7 | 25,79,12,0 | 20 | red/pink | |
| 139 | Light Mauve | #9A72AA | 154,114,170 | 53.6, 23.9, -24.0 | 43,62,5,0 | 22 | violet/purple | |
| 140 | Aconite Violet | #A36AA5 | 163,106,165 | 52.7, 30.7, -22.4 | 39,68,5,0 | 21 | violet/purple | |
| 141 | Dull Blue Violet | #80719E | 128,113,158 | 50.2, 13.4, -22.5 | 57,60,17,0 | 19 | violet/purple | |
| 142 | Dark Soft Violet | #66629C | 102,98,156 | 44.0, 12.3, -31.2 | 70,68,13,0 | 14 | blue | ✱ ΔE 3 |
| 143 | Blue Violet | #6450A1 | 100,80,161 | 39.1, 23.6, -41.9 | 72,80,0,0 | 11 | blue | ✱ ΔE 4 |
| 144 | Purple Drab | #84565B | 132,86,91 | 41.9, 19.9, 5.6 | 38,65,49,26 | 12 | red/pink | |
| 145 | Deep Violet / Plumbeous | #70727C | 112,114,124 | 48.0, 0.8, -5.9 | 61,52,43,7 | 17 | neutral | |
| 146 | Veronia Purple | #8C4C62 | 140,76,98 | 41.0, 29.6, 0.1 | 42,78,46,15 | 12 | red/pink | |
| 147 | Dark Slate Purple | #704357 | 112,67,87 | 34.3, 22.2, -3.6 | 64,85,60,10 | 8 | red/pink | |
| 148 | Taupe Brown | #7A4456 | 122,68,86 | 36.2, 25.6, 0.1 | 30,70,35,40 | 9 | red/pink | |
| 149 | Violet Carmine | #713B4C | 113,59,76 | 32.3, 25.9, 0.8 | 64,90,70,10 | 7 | red/pink | |
| 150 | Violet | #4F4086 | 79,64,134 | 31.5, 20.7, -37.9 | 85,90,18,0 | 7 | blue | ✱ ΔE 4 |
| 151 | Red Violet | #59256A | 89,37,106 | 25.1, 33.1, -30.1 | 76,100,25,15 | 4 | violet/purple | |
| 152 | Cotinga Purple | #501345 | 80,19,69 | 18.4, 32.9, -15.8 | 66,100,42,40 | 3 | violet/purple | |
| 153 | Dusky Madder Violet | #4E1D4C | 78,29,76 | 20.1, 28.6, -18.3 | 75,100,46,30 | 3 | violet/purple | |
| 154 | White | #FFFFFF | 255,255,255 | 100.0, 0.0, 0.0 | 0,0,0,0 | 100 | neutral-light | |
| 155 | Neutral Gray | #B6BFC1 | 182,191,193 | 76.7, -3.0, -2.0 | 29,18,20,0 | 51 | neutral | |
| 156 | Mineral Gray | #A2B0AD | 162,176,173 | 70.8, -5.6, -0.1 | 33,18,25,7 | 42 | neutral | |
| 157 | Warm Gray | #A1A39A | 161,163,154 | 66.7, -2.2, 4.7 | 37,28,36,3 | 36 | neutral | |
| 158 | Slate Color | #34454C | 52,69,76 | 27.8, -5.4, -7.0 | 85,70,62,30 | 6 | teal/blue-green | |
| 159 | Black | #111314 | 17,19,20 | 5.6, -0.4, -1.1 | 20,10,15,100 | 1 | neutral-dark | |

## Combination reference (360)

Color IDs refer to the color table above.

| # | Color IDs | Best text pair (ratio) | Value | Chroma | Temp | Fits |
|---|---|---|---|---|---|---|
| 1 | 66, 118 | 66/118 (1.0) | tonal | vivid | warm | apparel |
| 2 | 62, 130 | 62/130 (5.9) | high | medium | warm | web |
| 3 | 14, 40 | 14/40 (3.3) | mid | medium | warm | web* |
| 4 | 51, 151 | 51/151 (4.7) | mid | medium | warm | web interior-accent apparel |
| 5 | 107, 129 | 107/129 (1.6) | tonal | medium | cool | interior-accent apparel |
| 6 | 8, 132 | 8/132 (7.1) | high | medium | warm | web interior-accent apparel |
| 7 | 64, 89 | 64/89 (1.6) | tonal | medium | warm | apparel |
| 8 | 67, 134 | 67/134 (1.7) | tonal | medium | warm | interior-accent apparel |
| 9 | 37, 141 | 37/141 (2.2) | tonal | medium | balanced | interior-accent apparel |
| 10 | 67, 74 | 67/74 (1.0) | tonal | medium | warm | interior-accent apparel |
| 11 | 42, 156 | 42/156 (1.5) | tonal | muted | warm | interior apparel |
| 12 | 51, 120 | 51/120 (1.6) | tonal | medium | balanced | interior-accent apparel |
| 13 | 14, 146 | 14/146 (1.6) | tonal | medium | warm | interior-accent apparel |
| 14 | 10, 41 | 10/41 (2.2) | mid | medium | warm | interior |
| 15 | 101, 134 | 101/134 (1.7) | tonal | medium | cool | interior-accent apparel |
| 16 | 34, 112 | 34/112 (5.9) | high | medium | warm | web interior apparel |
| 17 | 13, 100 | 13/100 (1.4) | tonal | vivid | balanced | apparel |
| 18 | 4, 153 | 4/153 (6.5) | high | muted | balanced | web interior-accent apparel |
| 19 | 86, 93 | 86/93 (4.8) | mid | vivid | warm | web apparel-statement |
| 20 | 116, 136 | 116/136 (1.3) | tonal | muted | balanced | interior-accent apparel |
| 21 | 8, 100 | 8/100 (1.0) | tonal | vivid | balanced | apparel |
| 22 | 55, 127 | 55/127 (8.2) | high | vivid | warm | web apparel-statement print/brand |
| 23 | 46, 139 | 46/139 (2.5) | mid | medium | warm | interior apparel |
| 24 | 84, 146 | 84/146 (1.2) | tonal | medium | warm | interior-accent apparel |
| 25 | 19, 111 | 19/111 (3.2) | mid | medium | warm | web* interior apparel |
| 26 | 48, 83 | 48/83 (3.4) | mid | medium | warm | web* interior-accent |
| 27 | 2, 158 | 2/158 (5.8) | high | muted | balanced | web interior apparel |
| 28 | 85, 132 | 85/132 (1.8) | tonal | medium | warm | interior-accent apparel |
| 29 | 76, 114 | 76/114 (1.6) | tonal | muted | balanced | interior-accent apparel |
| 30 | 30, 156 | 30/156 (3.0) | mid | medium | warm | web* interior-accent apparel |
| 31 | 18, 40 | 18/40 (3.7) | mid | vivid | warm | web* apparel-statement |
| 32 | 50, 93 | 50/93 (1.0) | tonal | vivid | warm | apparel |
| 33 | 14, 158 | 14/158 (2.6) | mid | medium | warm | interior-accent apparel |
| 34 | 9, 155 | 9/155 (1.3) | tonal | muted | warm | interior-accent apparel |
| 35 | 5, 29 | 5/29 (2.4) | mid | medium | warm | interior-accent apparel |
| 36 | 69, 88 | 69/88 (1.7) | tonal | medium | warm | interior apparel |
| 37 | 28, 151 | 28/151 (1.8) | tonal | vivid | warm | apparel |
| 38 | 106, 127 | 106/127 (1.6) | tonal | medium | cool | interior-accent apparel |
| 39 | 23, 124 | 23/124 (1.2) | tonal | vivid | warm | apparel |
| 40 | 15, 71 | 15/71 (1.9) | tonal | vivid | warm | apparel |
| 41 | 74, 116 | 74/116 (2.0) | tonal | muted | balanced | interior-accent apparel |
| 42 | 60, 150 | 60/150 (4.5) | mid | vivid | warm | web apparel-statement |
| 43 | 2, 140 | 2/140 (2.4) | mid | medium | warm | interior apparel |
| 44 | 102, 121 | 102/121 (1.0) | tonal | medium | cool | interior-accent apparel |
| 45 | 43, 56 | 43/56 (1.1) | tonal | medium | warm | apparel |
| 46 | 64, 159 | 64/159 (6.5) | high | medium | warm | web interior-accent |
| 47 | 19, 135 | 19/135 (2.0) | tonal | medium | warm | interior-accent apparel |
| 48 | 25, 124 | 25/124 (1.3) | tonal | medium | balanced | apparel |
| 49 | 112, 122 | 112/122 (3.3) | mid | medium | cool | web* interior apparel |
| 50 | 42, 153 | 42/153 (8.9) | high | medium | warm | web interior apparel |
| 51 | 29, 122 | 29/122 (1.2) | tonal | vivid | balanced | apparel |
| 52 | 39, 159 | 39/159 (15.6) | high | muted | warm | web interior apparel |
| 53 | 62, 153 | 62/153 (6.1) | high | vivid | warm | web apparel-statement print/brand |
| 54 | 101, 113 | 101/113 (2.0) | tonal | medium | cool | interior apparel |
| 55 | 11, 154 | 11/154 (3.3) | mid | muted | warm | web* interior apparel |
| 56 | 135, 150 | 135/150 (3.9) | mid | muted | cool | web* interior-accent apparel |
| 57 | 148, 158 | 148/158 (1.3) | tonal | muted | balanced | interior-accent apparel |
| 58 | 33, 100 | 33/100 (3.4) | mid | medium | balanced | web* interior-accent |
| 59 | 9, 72 | 9/72 (1.0) | tonal | vivid | warm | apparel |
| 60 | 40, 130 | 40/130 (11.0) | high | muted | balanced | web interior apparel |
| 61 | 92, 152 | 92/152 (8.3) | high | medium | warm | web |
| 62 | 55, 159 | 55/159 (15.9) | high | medium | warm | web |
| 63 | 38, 118 | 38/118 (2.2) | tonal | muted | balanced | interior-accent apparel |
| 64 | 140, 142 | 140/142 (1.3) | tonal | medium | cool | interior-accent apparel |
| 65 | 69, 116 | 69/116 (1.3) | tonal | medium | warm | interior-accent apparel |
| 66 | 59, 80 | 59/80 (2.5) | mid | medium | warm | interior-accent |
| 67 | 121, 130 | 121/130 (3.2) | mid | muted | cool | web* interior-accent apparel |
| 68 | 5, 55 | 5/55 (2.3) | mid | vivid | warm | apparel-statement |
| 69 | 157, 159 | 157/159 (7.2) | high | muted | balanced | web interior-accent apparel |
| 70 | 14, 108 | 14/108 (1.9) | tonal | medium | warm | interior-accent apparel |
| 71 | 30, 50 | 30/50 (3.1) | mid | medium | warm | web* |
| 72 | 39, 112 | 39/112 (1.3) | tonal | muted | balanced | interior apparel |
| 73 | 83, 97 | 83/97 (2.5) | mid | muted | warm | interior-accent apparel |
| 74 | 88, 120 | 88/120 (2.5) | mid | muted | cool | interior apparel |
| 75 | 112, 128 | 112/128 (5.7) | high | muted | cool | web interior apparel |
| 76 | 40, 157 | 40/157 (2.2) | mid | muted | warm | interior apparel |
| 77 | 13, 129 | 13/129 (2.2) | tonal | medium | warm | interior-accent apparel |
| 78 | 45, 117 | 45/117 (1.1) | tonal | medium | balanced | interior-accent apparel |
| 79 | 85, 120 | 85/120 (2.5) | mid | medium | balanced | interior-accent apparel |
| 80 | 39, 139 | 39/139 (3.2) | mid | muted | warm | web* interior apparel |
| 81 | 48, 157 | 48/157 (1.2) | tonal | medium | warm | interior-accent apparel |
| 82 | 33, 153 | 33/153 (1.4) | tonal | medium | warm | interior-accent apparel |
| 83 | 53, 128 | 53/128 (5.0) | mid | muted | cool | web interior apparel |
| 84 | 43, 133 | 43/133 (10.4) | high | muted | balanced | web interior apparel |
| 85 | 15, 123 | 15/123 (1.3) | tonal | vivid | warm | apparel |
| 86 | 14, 100 | 14/100 (1.4) | tonal | vivid | balanced | apparel |
| 87 | 2, 71 | 2/71 (1.2) | tonal | medium | warm | interior apparel |
| 88 | 43, 122 | 43/122 (3.9) | mid | medium | cool | web* interior apparel |
| 89 | 62, 128 | 62/128 (4.3) | mid | vivid | warm | web* apparel-statement |
| 90 | 9, 140 | 9/140 (1.6) | tonal | medium | warm | interior-accent apparel |
| 91 | 38, 68 | 38/68 (2.1) | tonal | medium | warm | interior-accent apparel |
| 92 | 6, 101 | 6/101 (1.5) | tonal | vivid | balanced | apparel |
| 93 | 72, 113 | 72/113 (1.4) | tonal | medium | warm | interior apparel |
| 94 | 42, 126 | 42/126 (6.5) | high | medium | balanced | web interior apparel |
| 95 | 33, 131 | 33/131 (1.9) | tonal | medium | warm | interior-accent apparel |
| 96 | 60, 77 | 60/77 (2.1) | tonal | vivid | warm | apparel |
| 97 | 2, 19 | 2/19 (2.6) | mid | medium | warm | interior |
| 98 | 85, 128 | 85/128 (1.0) | tonal | medium | warm | interior-accent apparel |
| 99 | 40, 118 | 40/118 (3.1) | mid | medium | balanced | web* interior apparel |
| 100 | 73, 141 | 73/141 (1.2) | tonal | muted | warm | interior-accent apparel |
| 101 | 3, 127 | 3/127 (5.1) | mid | medium | cool | web interior-accent apparel |
| 102 | 42, 68 | 42/68 (2.6) | mid | medium | warm | interior |
| 103 | 67, 153 | 67/153 (3.6) | mid | medium | warm | web* interior-accent |
| 104 | 29, 39 | 29/39 (5.8) | high | medium | warm | web interior apparel |
| 105 | 3, 98 | 3/98 (1.8) | tonal | muted | balanced | interior-accent apparel |
| 106 | 123, 131 | 123/131 (3.1) | mid | medium | cool | web* interior-accent apparel |
| 107 | 57, 75 | 57/75 (2.9) | mid | vivid | warm | apparel-statement |
| 108 | 9, 28 | 9/28 (2.3) | tonal | vivid | warm | apparel |
| 109 | 40, 109 | 40/109 (7.1) | high | muted | warm | web interior apparel |
| 110 | 32, 87 | 32/87 (1.4) | tonal | medium | warm | interior-accent apparel |
| 111 | 40, 91 | 40/91 (1.4) | tonal | medium | warm | interior apparel |
| 112 | 8, 159 | 8/159 (7.2) | high | muted | warm | web interior-accent apparel |
| 113 | 43, 87 | 43/87 (8.5) | high | muted | warm | web interior apparel |
| 114 | 61, 123 | 61/123 (3.0) | mid | vivid | warm | web* apparel-statement |
| 115 | 41, 65 | 41/65 (2.7) | mid | vivid | warm | apparel-statement |
| 116 | 3, 143 | 3/143 (3.5) | mid | medium | cool | web* interior-accent apparel |
| 117 | 23, 159 | 23/159 (3.2) | mid | medium | warm | web* interior-accent apparel |
| 118 | 60, 87 | 60/87 (6.1) | high | medium | warm | web interior-accent |
| 119 | 113, 130 | 113/130 (7.1) | high | muted | cool | web interior apparel |
| 120 | 3, 30 | 3/30 (3.7) | mid | medium | warm | web* interior-accent apparel |
| 121 | 32, 50, 108 | 32/50 (3.5) | mid | medium | warm | web* interior-accent apparel |
| 122 | 23, 47, 101 | 23/47 (3.4) | mid | vivid | warm | web* apparel-statement |
| 123 | 6, 56, 148 | 56/148 (6.1) | high | medium | warm | web |
| 124 | 36, 60, 94 | 36/60 (4.9) | mid | medium | warm | web |
| 125 | 4, 118, 128 | 4/128 (4.6) | mid | muted | cool | web interior-accent apparel |
| 126 | 42, 60, 127 | 42/127 (6.6) | high | medium | warm | web interior |
| 127 | 46, 99, 142 | 46/142 (3.5) | mid | medium | balanced | web* interior apparel |
| 128 | 2, 117, 139 | 2/139 (2.3) | mid | medium | balanced | interior apparel |
| 129 | 57, 70, 114 | 57/70 (2.3) | mid | vivid | warm | apparel-statement |
| 130 | 14, 29, 150 | 14/150 (2.2) | tonal | vivid | warm | apparel |
| 131 | 14, 66, 119 | 14/66 (1.0) | tonal | vivid | warm | apparel |
| 132 | 39, 48, 72 | 39/72 (2.2) | mid | medium | warm | interior |
| 133 | 34, 72, 100 | 34/100 (3.6) | mid | vivid | warm | web* apparel-statement |
| 134 | 9, 139, 151 | 9/151 (4.3) | mid | medium | warm | web* interior-accent |
| 135 | 39, 107, 114 | 39/107 (4.4) | mid | muted | balanced | web* interior apparel |
| 136 | 22, 104, 151 | 104/151 (2.8) | mid | vivid | balanced | apparel-statement |
| 137 | 19, 46, 99 | 19/46 (2.8) | mid | medium | warm | interior |
| 138 | 48, 56, 117 | 48/56 (1.6) | tonal | vivid | warm | apparel |
| 139 | 114, 132, 155 | 132/155 (9.8) | high | muted | cool | web interior-accent apparel |
| 140 | 48, 123, 158 | 48/158 (4.8) | mid | medium | balanced | web interior-accent apparel |
| 141 | 64, 91, 130 | 91/130 (7.5) | high | vivid | warm | web apparel-statement print/brand |
| 142 | 27, 69, 114 | 27/114 (2.5) | mid | medium | warm | interior-accent |
| 143 | 122, 137, 157 | 122/157 (2.0) | tonal | muted | balanced | interior-accent apparel |
| 144 | 25, 64, 159 | 64/159 (6.5) | high | medium | warm | web interior-accent |
| 145 | 32, 71, 131 | 71/131 (8.1) | high | medium | warm | web interior-accent |
| 146 | 70, 82, 106 | 70/82 (2.2) | tonal | medium | warm | interior-accent apparel |
| 147 | 10, 34, 88 | 34/88 (6.4) | high | medium | warm | web interior apparel |
| 148 | 59, 61, 118 | 61/118 (2.0) | tonal | vivid | warm | apparel |
| 149 | 59, 64, 133 | 59/133 (7.1) | high | vivid | warm | web apparel-statement print/brand |
| 150 | 43, 71, 89 | 43/71 (1.5) | tonal | medium | balanced | interior apparel |
| 151 | 39, 62, 129 | 39/129 (7.5) | high | medium | warm | web interior |
| 152 | 19, 33, 113 | 33/113 (5.0) | mid | medium | warm | web interior apparel |
| 153 | 9, 61, 71 | 9/61 (1.4) | tonal | vivid | warm | apparel |
| 154 | 23, 55, 122 | 23/55 (4.8) | high | vivid | warm | web apparel-statement print/brand |
| 155 | 16, 101, 132 | 101/132 (5.1) | high | vivid | balanced | web apparel-statement print/brand |
| 156 | 59, 115, 150 | 115/150 (4.9) | mid | medium | balanced | web interior |
| 157 | 35, 59, 121 | 35/59 (5.1) | mid | medium | warm | web |
| 158 | 56, 67, 93 | 56/67 (2.9) | mid | vivid | warm | apparel-statement |
| 159 | 70, 116, 134 | 70/116 (1.6) | tonal | medium | balanced | interior-accent apparel |
| 160 | 69, 83, 125 | 69/83 (2.8) | mid | medium | warm | interior-accent apparel |
| 161 | 32, 45, 124 | 32/45 (4.3) | mid | medium | warm | web* interior-accent apparel |
| 162 | 11, 97, 137 | 11/97 (1.1) | tonal | medium | warm | interior-accent apparel |
| 163 | 57, 88, 123 | 57/123 (4.1) | mid | medium | warm | web* |
| 164 | 18, 61, 150 | 61/150 (4.8) | mid | vivid | warm | web apparel-statement |
| 165 | 3, 10, 38 | 3/38 (4.5) | mid | medium | warm | web interior-accent apparel |
| 166 | 8, 41, 133 | 41/133 (11.5) | high | medium | warm | web interior apparel |
| 167 | 54, 112, 129 | 112/129 (5.6) | high | muted | cool | web interior apparel |
| 168 | 56, 129, 146 | 56/129 (7.3) | high | medium | warm | web interior |
| 169 | 2, 40, 157 | 40/157 (2.2) | mid | muted | warm | interior apparel |
| 170 | 25, 61, 151 | 61/151 (6.1) | high | vivid | warm | web apparel-statement print/brand |
| 171 | 36, 62, 89 | 36/89 (5.6) | high | medium | warm | web interior |
| 172 | 67, 123, 151 | 67/151 (3.1) | mid | medium | balanced | web* interior-accent |
| 173 | 56, 85, 88 | 56/85 (8.0) | high | medium | warm | web |
| 174 | 2, 135, 148 | 2/148 (4.4) | mid | muted | warm | web* interior apparel |
| 175 | 45, 53, 143 | 53/143 (3.6) | mid | medium | balanced | web* interior apparel |
| 176 | 1, 43, 116 | 43/116 (1.3) | tonal | muted | balanced | interior apparel |
| 177 | 36, 73, 134 | 36/134 (4.6) | mid | medium | warm | web interior-accent apparel |
| 178 | 42, 113, 120 | 42/120 (2.6) | mid | muted | cool | interior apparel |
| 179 | 18, 48, 127 | 48/127 (4.6) | mid | vivid | warm | web apparel-statement |
| 180 | 46, 139, 155 | 46/139 (2.5) | mid | muted | warm | interior apparel |
| 181 | 29, 150, 152 | 29/152 (1.9) | tonal | medium | warm | apparel |
| 182 | 14, 87, 132 | 14/132 (4.8) | mid | medium | warm | web interior-accent apparel |
| 183 | 145, 146, 151 | 145/151 (2.3) | tonal | muted | warm | interior-accent apparel |
| 184 | 10, 42, 75 | 42/75 (2.7) | mid | medium | warm | interior apparel |
| 185 | 5, 19, 40 | 19/40 (3.8) | mid | medium | warm | web* interior apparel |
| 186 | 33, 50, 122 | 33/50 (4.0) | mid | medium | warm | web* interior-accent |
| 187 | 124, 135, 140 | 124/135 (3.3) | mid | muted | cool | web* interior-accent apparel |
| 188 | 97, 114, 115 | 97/115 (1.6) | tonal | muted | cool | interior apparel |
| 189 | 56, 110, 117 | 56/110 (11.1) | high | medium | warm | web interior |
| 190 | 42, 66, 159 | 42/159 (12.7) | high | medium | warm | web interior apparel |
| 191 | 5, 60, 122 | 60/122 (2.7) | mid | medium | warm | interior-accent |
| 192 | 47, 87, 145 | 47/87 (7.1) | high | muted | warm | web interior apparel |
| 193 | 8, 41, 102 | 41/102 (3.1) | mid | medium | warm | web* interior |
| 194 | 16, 43, 121 | 43/121 (2.9) | mid | medium | warm | interior |
| 195 | 10, 40, 155 | 10/40 (2.3) | mid | medium | warm | interior apparel |
| 196 | 71, 112, 143 | 112/143 (4.1) | mid | medium | cool | web* interior |
| 197 | 9, 142, 155 | 142/155 (2.9) | mid | muted | balanced | interior-accent apparel |
| 198 | 20, 57, 103 | 20/57 (3.8) | mid | vivid | warm | web* apparel-statement |
| 199 | 21, 81, 127 | 81/127 (1.9) | tonal | medium | warm | interior-accent apparel |
| 200 | 29, 53, 98 | 29/53 (3.8) | mid | medium | warm | web* interior apparel |
| 201 | 8, 77, 115 | 77/115 (2.4) | mid | medium | warm | interior |
| 202 | 88, 115, 158 | 88/158 (6.7) | high | muted | cool | web interior apparel |
| 203 | 40, 49, 108 | 40/108 (6.4) | high | medium | warm | web interior apparel |
| 204 | 25, 67, 113 | 25/113 (2.9) | mid | medium | warm | interior apparel |
| 205 | 36, 49, 150 | 36/49 (4.7) | mid | medium | warm | web interior-accent |
| 206 | 2, 48, 67 | 2/67 (2.0) | tonal | medium | warm | interior apparel |
| 207 | 79, 89, 159 | 89/159 (11.0) | high | muted | warm | web interior apparel |
| 208 | 39, 120, 123 | 39/123 (4.6) | high | medium | cool | web interior apparel |
| 209 | 42, 62, 114 | 42/114 (1.5) | tonal | medium | warm | interior apparel |
| 210 | 46, 56, 108 | 56/108 (6.0) | high | medium | warm | web |
| 211 | 63, 94, 132 | 63/132 (7.7) | high | medium | warm | web interior-accent |
| 212 | 30, 78, 114 | 30/114 (2.9) | mid | medium | warm | interior-accent |
| 213 | 49, 57, 112 | 49/57 (1.4) | tonal | medium | warm | apparel |
| 214 | 42, 79, 150 | 42/150 (5.9) | high | medium | balanced | web interior apparel |
| 215 | 47, 122, 138 | 47/122 (3.2) | mid | vivid | warm | web* apparel-statement |
| 216 | 16, 103, 159 | 103/159 (5.4) | high | medium | warm | web interior-accent |
| 217 | 36, 50, 106 | 36/50 (4.2) | mid | medium | warm | web* interior-accent apparel |
| 218 | 124, 134, 145 | 124/134 (3.5) | mid | muted | cool | web* interior-accent apparel |
| 219 | 16, 98, 126 | 98/126 (2.7) | mid | medium | warm | general |
| 220 | 26, 50, 140 | 26/50 (2.8) | mid | medium | warm | interior-accent |
| 221 | 29, 155, 159 | 155/159 (9.9) | high | muted | warm | web interior-accent apparel |
| 222 | 60, 62, 68 | 60/68 (2.0) | tonal | vivid | warm | apparel |
| 223 | 5, 50, 88 | 5/88 (1.8) | tonal | muted | warm | interior apparel |
| 224 | 10, 125, 148 | 10/148 (2.7) | mid | muted | warm | interior-accent apparel |
| 225 | 23, 126, 147 | 23/126 (1.6) | tonal | medium | warm | interior-accent apparel |
| 226 | 38, 47, 150 | 47/150 (5.3) | high | medium | warm | web interior apparel |
| 227 | 1, 113, 118 | 1/118 (2.3) | mid | muted | cool | interior apparel |
| 228 | 29, 40, 155 | 29/40 (5.9) | high | medium | warm | web interior apparel |
| 229 | 48, 110, 155 | 110/155 (7.2) | high | muted | warm | web interior-accent apparel |
| 230 | 8, 88, 115 | 8/88 (1.7) | tonal | medium | balanced | interior apparel |
| 231 | 3, 33, 121 | 3/33 (4.8) | mid | muted | warm | web interior-accent apparel |
| 232 | 23, 45, 132 | 45/132 (10.1) | high | medium | warm | web |
| 233 | 29, 73, 128 | 73/128 (2.5) | mid | medium | warm | interior-accent apparel |
| 234 | 46, 83, 112 | 46/83 (4.6) | mid | medium | warm | web interior apparel |
| 235 | 42, 62, 135 | 42/135 (1.5) | tonal | medium | warm | interior apparel |
| 236 | 70, 127, 144 | 70/127 (3.1) | mid | medium | warm | web* interior-accent |
| 237 | 29, 85, 114 | 85/114 (4.2) | mid | medium | warm | web* interior-accent apparel |
| 238 | 50, 152, 157 | 50/152 (6.2) | high | muted | warm | web interior-accent apparel |
| 239 | 5, 58, 89 | 5/89 (1.6) | tonal | muted | warm | interior apparel |
| 240 | 7, 55, 118 | 55/118 (3.1) | mid | vivid | warm | web* apparel-statement |
| 241 | 18, 40, 51, 125 | 40/125 (4.6) | mid | medium | warm | web interior apparel |
| 242 | 9, 20, 106, 159 | 9/159 (7.3) | high | medium | warm | web interior-accent apparel |
| 243 | 14, 42, 80, 158 | 42/158 (6.8) | high | medium | warm | web interior apparel |
| 244 | 5, 15, 96, 123 | 5/123 (2.0) | tonal | medium | warm | interior-accent apparel |
| 245 | 29, 105, 130, 158 | 105/130 (3.7) | mid | medium | warm | web* interior-accent apparel |
| 246 | 2, 28, 39, 46 | 28/39 (5.0) | high | medium | warm | web interior apparel |
| 247 | 14, 57, 101, 127 | 57/127 (7.1) | high | vivid | warm | web apparel-statement print/brand |
| 248 | 9, 70, 134, 147 | 134/147 (3.8) | mid | medium | warm | web* interior-accent apparel |
| 249 | 33, 54, 59, 125 | 33/59 (4.5) | mid | medium | warm | web interior-accent apparel |
| 250 | 58, 65, 100, 111 | 65/111 (2.4) | mid | medium | warm | general |
| 251 | 31, 55, 106, 158 | 55/158 (8.5) | high | vivid | warm | web apparel-statement print/brand |
| 252 | 13, 14, 69, 120 | 13/69 (1.5) | tonal | vivid | warm | apparel |
| 253 | 56, 63, 152, 158 | 56/152 (11.3) | high | medium | warm | web |
| 254 | 2, 39, 77, 136 | 39/77 (3.5) | mid | muted | warm | web* interior apparel |
| 255 | 14, 58, 116, 159 | 116/159 (10.1) | high | medium | warm | web interior-accent apparel |
| 256 | 49, 64, 104, 159 | 49/159 (9.3) | high | medium | warm | web interior-accent |
| 257 | 17, 61, 122, 140 | 61/122 (2.9) | mid | vivid | warm | apparel-statement |
| 258 | 36, 45, 77, 123 | 36/45 (5.1) | mid | medium | warm | web interior-accent |
| 259 | 56, 120, 124, 157 | 56/124 (5.9) | high | medium | balanced | web interior apparel |
| 260 | 11, 49, 89, 100 | 11/89 (1.9) | tonal | medium | balanced | interior apparel |
| 261 | 31, 40, 116, 157 | 31/40 (6.1) | high | medium | warm | web interior apparel |
| 262 | 13, 42, 72, 107 | 42/107 (3.6) | mid | medium | warm | web* interior |
| 263 | 20, 45, 88, 158 | 88/158 (6.7) | high | medium | warm | web interior apparel |
| 264 | 2, 18, 90, 118 | 2/18 (2.5) | mid | medium | warm | interior apparel |
| 265 | 11, 57, 94, 131 | 57/131 (13.1) | high | vivid | warm | web apparel-statement print/brand |
| 266 | 17, 42, 97, 101 | 17/42 (3.2) | mid | medium | warm | web* |
| 267 | 47, 62, 101, 122 | 47/122 (3.2) | mid | vivid | warm | web* apparel-statement |
| 268 | 5, 14, 110, 111 | 110/111 (9.9) | high | muted | warm | web interior apparel |
| 269 | 14, 36, 140, 159 | 14/159 (4.8) | mid | medium | warm | web interior-accent apparel |
| 270 | 13, 39, 80, 107 | 39/107 (4.4) | mid | medium | warm | web* interior apparel |
| 271 | 26, 115, 120, 133 | 115/133 (8.1) | high | medium | balanced | web interior apparel |
| 272 | 40, 64, 88, 114 | 40/64 (2.4) | mid | medium | warm | interior apparel |
| 273 | 1, 35, 79, 155 | 1/35 (6.6) | high | muted | warm | web interior apparel |
| 274 | 65, 74, 121, 139 | 65/121 (1.1) | tonal | medium | warm | interior-accent apparel |
| 275 | 19, 54, 85, 148 | 54/85 (4.5) | mid | medium | warm | web interior-accent apparel |
| 276 | 9, 43, 91, 159 | 43/159 (13.6) | high | medium | warm | web interior apparel |
| 277 | 10, 25, 77, 131 | 10/131 (6.3) | high | medium | warm | web |
| 278 | 47, 59, 107, 126 | 47/126 (5.8) | high | medium | warm | web |
| 279 | 14, 49, 54, 130 | 49/130 (6.4) | high | medium | warm | web interior-accent apparel |
| 280 | 13, 108, 136, 148 | 136/148 (2.9) | mid | medium | warm | interior-accent apparel |
| 281 | 40, 101, 115, 123 | 40/123 (4.8) | high | medium | cool | web interior apparel |
| 282 | 13, 52, 115, 137 | 13/115 (2.2) | tonal | medium | warm | interior apparel |
| 283 | 21, 36, 98, 117 | 36/117 (4.6) | mid | medium | warm | web interior-accent apparel |
| 284 | 12, 57, 100, 126 | 57/126 (7.0) | high | vivid | warm | web apparel-statement print/brand |
| 285 | 5, 20, 65, 88 | 20/88 (3.5) | mid | medium | warm | web* interior |
| 286 | 20, 61, 119, 128 | 61/128 (5.0) | mid | vivid | warm | web apparel-statement |
| 287 | 9, 58, 112, 116 | 9/112 (1.5) | tonal | medium | warm | interior apparel |
| 288 | 62, 84, 148, 159 | 62/159 (8.7) | high | medium | warm | web interior-accent apparel |
| 289 | 56, 92, 128, 131 | 56/131 (14.4) | high | medium | warm | web |
| 290 | 38, 40, 108, 115 | 38/40 (7.3) | high | muted | warm | web interior apparel |
| 291 | 92, 100, 115, 116 | 92/100 (1.5) | tonal | medium | cool | interior apparel |
| 292 | 40, 45, 51, 54 | 40/51 (2.0) | mid | medium | warm | interior apparel |
| 293 | 14, 88, 95, 103 | 14/88 (2.5) | mid | medium | balanced | interior apparel |
| 294 | 39, 47, 107, 114 | 39/107 (4.4) | mid | medium | warm | web* interior apparel |
| 295 | 47, 55, 122, 131 | 55/131 (15.0) | high | vivid | warm | web apparel-statement print/brand |
| 296 | 39, 50, 83, 158 | 39/158 (8.4) | high | muted | warm | web interior apparel |
| 297 | 20, 62, 80, 128 | 62/128 (4.3) | mid | medium | warm | web* |
| 298 | 14, 56, 65, 159 | 56/159 (15.2) | high | vivid | warm | web apparel-statement print/brand |
| 299 | 24, 49, 105, 123 | 49/123 (2.8) | mid | medium | warm | interior-accent |
| 300 | 8, 47, 88, 116 | 8/88 (1.7) | tonal | medium | warm | interior apparel |
| 301 | 17, 42, 97, 140 | 17/42 (3.2) | mid | medium | warm | web* interior |
| 302 | 47, 54, 111, 123 | 111/123 (4.0) | mid | medium | balanced | web* interior apparel |
| 303 | 41, 65, 110, 155 | 41/110 (10.9) | high | medium | warm | web interior apparel |
| 304 | 33, 47, 74, 101 | 33/47 (5.5) | high | medium | warm | web interior |
| 305 | 45, 57, 71, 88 | 57/71 (1.6) | tonal | vivid | warm | apparel |
| 306 | 56, 101, 104, 111 | 56/104 (3.1) | mid | medium | cool | web* |
| 307 | 23, 134, 140, 152 | 134/152 (6.7) | high | medium | warm | web interior-accent |
| 308 | 4, 22, 66, 115 | 22/115 (2.9) | mid | medium | warm | general |
| 309 | 48, 63, 128, 129 | 48/128 (4.4) | mid | medium | warm | web* interior-accent |
| 310 | 39, 45, 77, 110 | 39/110 (11.4) | high | muted | warm | web interior apparel |
| 311 | 30, 47, 90, 92 | 30/47 (4.2) | mid | medium | warm | web* |
| 312 | 20, 62, 95, 124 | 62/124 (3.4) | mid | medium | warm | web* |
| 313 | 23, 55, 106, 159 | 55/159 (15.9) | high | vivid | warm | web apparel-statement print/brand |
| 314 | 9, 33, 127, 153 | 9/153 (5.1) | mid | medium | warm | web interior-accent |
| 315 | 8, 39, 48, 138 | 39/138 (3.5) | mid | medium | warm | web* |
| 316 | 34, 104, 150, 151 | 104/151 (2.8) | mid | medium | cool | general |
| 317 | 44, 54, 56, 88 | 54/56 (1.7) | tonal | medium | warm | interior apparel |
| 318 | 81, 109, 126, 133 | 81/133 (2.8) | mid | muted | cool | interior-accent apparel |
| 319 | 14, 57, 62, 107 | 57/107 (3.9) | mid | vivid | warm | web* apparel-statement |
| 320 | 6, 39, 105, 113 | 39/105 (2.8) | mid | medium | warm | interior apparel |
| 321 | 5, 39, 110, 114 | 39/110 (11.4) | high | muted | balanced | web interior apparel |
| 322 | 17, 28, 138, 143 | 138/143 (1.5) | tonal | vivid | warm | apparel |
| 323 | 46, 71, 85, 159 | 46/159 (11.9) | high | medium | warm | web interior apparel |
| 324 | 30, 121, 140, 155 | 30/155 (3.6) | mid | medium | warm | web* interior-accent apparel |
| 325 | 13, 41, 60, 133 | 41/133 (11.5) | high | medium | warm | web interior |
| 326 | 39, 65, 91, 93 | 39/65 (2.8) | mid | vivid | warm | apparel-statement |
| 327 | 9, 14, 54, 135 | 14/54 (1.7) | tonal | medium | warm | interior-accent apparel |
| 328 | 28, 63, 87, 102 | 63/87 (4.9) | mid | medium | warm | web |
| 329 | 47, 135, 152, 158 | 47/152 (8.4) | high | muted | warm | web interior apparel |
| 330 | 53, 111, 114, 120 | 111/120 (2.7) | mid | muted | cool | interior apparel |
| 331 | 24, 131, 139, 150 | 131/139 (4.5) | mid | medium | balanced | web interior-accent |
| 332 | 6, 22, 110, 126 | 6/110 (5.8) | high | medium | warm | web interior-accent |
| 333 | 20, 56, 115, 122 | 56/122 (4.3) | mid | vivid | warm | web* apparel-statement |
| 334 | 43, 77, 91, 123 | 43/123 (4.0) | mid | medium | warm | web* interior apparel |
| 335 | 34, 62, 150, 158 | 62/158 (4.6) | mid | medium | warm | web interior-accent |
| 336 | 9, 33, 40, 109 | 33/40 (7.8) | high | medium | warm | web interior apparel |
| 337 | 38, 136, 149, 159 | 136/159 (7.2) | high | muted | warm | web interior-accent apparel |
| 338 | 29, 61, 126, 135 | 61/126 (5.2) | high | medium | warm | web |
| 339 | 50, 66, 113, 128 | 113/128 (5.1) | mid | medium | warm | web interior apparel |
| 340 | 65, 100, 155, 159 | 155/159 (9.9) | high | medium | warm | web interior-accent apparel |
| 341 | 8, 107, 110, 113 | 110/113 (7.6) | high | muted | warm | web interior apparel |
| 342 | 2, 47, 78, 110 | 47/110 (8.3) | high | medium | warm | web interior apparel |
| 343 | 20, 42, 82, 129 | 42/129 (6.1) | high | medium | warm | web interior apparel |
| 344 | 46, 127, 140, 159 | 46/159 (11.9) | high | medium | balanced | web interior apparel |
| 345 | 33, 111, 117, 143 | 33/111 (6.6) | high | medium | cool | web interior apparel |
| 346 | 25, 88, 92, 96 | 25/88 (3.5) | mid | medium | warm | web* interior apparel |
| 347 | 94, 100, 124, 137 | 100/124 (2.7) | mid | medium | balanced | interior-accent apparel |
| 348 | 53, 107, 110, 152 | 53/152 (7.6) | high | muted | warm | web interior apparel |
| 349 | 26, 123, 127, 159 | 123/159 (3.3) | mid | medium | cool | web* interior-accent apparel |
| 350 | 61, 73, 95, 147 | 61/147 (4.4) | mid | medium | warm | web* interior apparel |
| 351 | 9, 43, 112, 129 | 43/129 (6.5) | high | muted | warm | web interior apparel |
| 352 | 24, 56, 116, 159 | 56/159 (15.2) | high | medium | warm | web interior |
| 353 | 44, 58, 68, 90 | 44/68 (2.5) | mid | medium | warm | interior apparel |
| 354 | 17, 48, 111, 122 | 111/122 (3.9) | mid | vivid | warm | web* apparel-statement |
| 355 | 25, 87, 100, 123 | 87/100 (4.4) | mid | medium | balanced | web* interior-accent |
| 356 | 56, 72, 113, 134 | 56/72 (2.1) | mid | medium | warm | interior |
| 357 | 58, 113, 139, 158 | 113/158 (5.6) | high | muted | warm | web interior apparel |
| 358 | 56, 64, 89, 123 | 56/123 (4.5) | high | vivid | warm | web apparel-statement print/brand |
| 359 | 56, 85, 111, 155 | 56/85 (8.0) | high | medium | warm | web interior apparel |
| 360 | 121, 129, 148, 150 | 121/129 (2.2) | tonal | medium | cool | interior-accent apparel |
