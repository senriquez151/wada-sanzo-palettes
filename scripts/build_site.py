"""Rebuild site/index.html from site/template.html and data/*.json.

Usage: python3 scripts/build_site.py
"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
colors = json.loads((root / "data/colors.json").read_text())
combos = json.loads((root / "data/combinations.json").read_text())

C = [[c["name"], c["hex"], c["rgb"], c["lab"], c["cmyk"], c["lrv"], c["family"], c["gamut_delta_e"]] for c in colors]
K = [[k["colors"], k["best_text_pair"], k["best_contrast"], k["value"], k["chroma"], k["temp"], k["fits"]] for k in combos]
data = ("const COLORS=" + json.dumps(C, separators=(",", ":"), ensure_ascii=False) + ";\n"
        "const COMBOS=" + json.dumps(K, separators=(",", ":")) + ";\n")

body = (root / "site/template.html").read_text().replace("/*DATA*/", data)
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>html{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>'
        '</head><body>')
(root / "site/index.html").write_text(head + body + "</body></html>\n")
print(f"Built site/index.html with {len(colors)} colors and {len(combos)} combinations")
