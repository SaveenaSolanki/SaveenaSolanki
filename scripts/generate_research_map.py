#!/usr/bin/env python3
"""Generate the research-program flow diagram (research-map.svg).

Visualizes the one research arc: represent molecules -> model interactions
-> predict biological consequence. Palette matches the profile banner
(espresso / parchment / gold). Stdlib only; runnable in CI if needed.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "research-map.svg")

BG = "#17110d"
CARD = "#241a14"
BORDER = "#3a2c1e"
GOLD = "#d4b87a"
TAN = "#ac946f"
CREAM = "#f5e3ca"
DIM = "#a08a6c"

W = 900

# node: (title, caption, cx, cy, width, emphasis)
NODES = [
    ("MOLECULES", "chemical space · SMILES · graphs · quantum · bioactivity", 450, 116, 400, False),
    ("ChemicalDice · CDI", "multimodal molecular representation learning", 450, 246, 400, True),
    ("PROTEIN\u2013LIGAND INTERACTIONS", "what molecules do to proteins", 450, 376, 400, False),
    ("SynGlue", "generative AI for PROTACs · targeted degradation", 285, 536, 330, True),
    ("MetaboGlue", "molecular glues · metabolite-mediated PPIs", 615, 536, 330, True),
    ("PROTEIN INTERACTION MODULATION", "degradation · stabilization · rewiring", 450, 696, 400, False),
    ("KNOWLEDGE GRAPHS · PATHWAYS", "how interventions propagate through biology", 450, 826, 400, False),
    ("BIOLOGICAL STATE", "disease biology · state-space reasoning", 450, 956, 400, False),
    ("MOLECULAR INTERVENTION", "design targets learned from data", 450, 1086, 400, True),
]

NODE_H = 64
ARROW = "M0 0 L7 3.5 L0 7 Z"  # triangle pointing down (translated/rotated per use)


def box(cx, cy, w, title, caption, emphasis):
    x0, y0 = cx - w / 2, cy - NODE_H / 2
    stroke = GOLD if emphasis else TAN
    title_fill = CREAM if emphasis else CREAM
    cap_fill = GOLD if emphasis else DIM
    parts = [
        f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{w:.0f}" height="{NODE_H}" rx="10" fill="{CARD}" stroke="{stroke}" stroke-width="{1.6 if emphasis else 1.1}"/>',
        f'<text x="{cx:.0f}" y="{y0 + 26:.0f}" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="{18 if emphasis else 17}" font-weight="700" fill="{title_fill}" letter-spacing="{1.5 if emphasis else 0.5}">{title}</text>',
        f'<text x="{cx:.0f}" y="{y0 + 46:.0f}" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="11.5" fill="{cap_fill}">{caption}</text>',
    ]
    return "".join(parts)


def v_arrow(x, y1, y2):
    """Vertical arrow from y1 (tip below box) to y2 (tip above next box)."""
    return (
        f'<line x1="{x:.0f}" y1="{y1:.0f}" x2="{x:.0f}" y2="{y2 - 7:.0f}" stroke="{TAN}" stroke-width="2"/>'
        f'<path d="{ARROW}" transform="translate({x - 3.5:.0f},{y2 - 7:.0f})" fill="{GOLD}"/>'
    )


def path_arrow(segments, tip_x, tip_y):
    """Polyline ending in a downward arrowhead whose tip lands at (tip_x, tip_y)."""
    pts = " ".join(f"{x:.0f},{y:.0f}" for x, y in segments)
    return (
        f'<polyline points="{pts}" fill="none" stroke="{TAN}" stroke-width="2" stroke-linejoin="round"/>'
        f'<path d="{ARROW}" transform="translate({tip_x - 3.5:.0f},{tip_y - 7:.0f})" fill="{GOLD}"/>'
    )


def render():
    parts = []
    H = 1184
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="My research program — from molecules to biological systems">')
    parts.append(f'<rect width="{W}" height="{H}" fill="{BG}" rx="14"/>')
    parts.append('<defs>')
    parts.append('<linearGradient id="hd2" x1="0" y1="0" x2="1" y2="0">')
    parts.append(f'<stop offset="0%" stop-color="{GOLD}"/><stop offset="100%" stop-color="{CREAM}"/>')
    parts.append('</linearGradient>')
    parts.append('</defs>')

    # header
    parts.append(f'<text x="450" y="46" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="24" font-weight="700" fill="url(#hd2)" letter-spacing="5">MY RESEARCH PROGRAM</text>')
    parts.append(f'<text x="450" y="72" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12.5" fill="{DIM}" letter-spacing="1">REPRESENT MOLECULES → MODEL INTERACTIONS → PREDICT BIOLOGICAL CONSEQUENCE</text>')

    # ---- connectors (node bottoms / tops from NODES) ----
    # MOLECULES(bottom 148) -> CDI(top 214)
    parts.append(v_arrow(450, 148, 214))
    # CDI(278) -> PLI(344)
    parts.append(v_arrow(450, 278, 344))
    # PLI(408) -> split branch (462) -> SynGlue(top 504) / MetaboGlue(top 504)
    parts.append(path_arrow([(450, 408), (450, 462), (285, 462)], 285, 504))
    parts.append(path_arrow([(450, 408), (450, 462), (615, 462)], 615, 504))
    # SynGlue(568) & MetaboGlue(568) -> merge (614) -> modulation(top 664)
    parts.append(path_arrow([(285, 568), (285, 614), (450, 614), (450, 657)], 450, 664))
    parts.append(path_arrow([(615, 568), (615, 614), (450, 614), (450, 657)], 450, 664))
    # modulation(728) -> KG(794) ; KG(858) -> state(924) ; state(988) -> intervention(1054)
    parts.append(v_arrow(450, 728, 794))
    parts.append(v_arrow(450, 858, 924))
    parts.append(v_arrow(450, 988, 1054))

    for title, caption, cx, cy, w, emph in NODES:
        parts.append(box(cx, cy, w, title, caption, emph))

    parts.append('</svg>')
    return "\n".join(parts)


def main():
    out = os.path.abspath(OUT)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(render())
    print("wrote", out)


if __name__ == "__main__":
    main()
