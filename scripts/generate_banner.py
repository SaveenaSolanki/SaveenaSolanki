#!/usr/bin/env python3
"""Generate the profile banner (banner.svg) in the cream/bronze scientific system.

Left:    molecular structure + protein ribbon motif
Centre:  identity (name, role, tagline)
Right:   molecule -> interacting proteins -> network transition
Footer:  research keywords

Palette (academic cream/bronze):
  main bg #FFFDF9 · secondary #F8F3EB · panel #F2E8DA
  text #29231E · secondary text #70665B · bronze #A98552 · light gold #CDB585
  border #E5D8C4
"""
import os, math

OUT = os.path.join(os.path.dirname(__file__), "..", "banner.svg")

BG = "#FFFDF9"
PANEL = "#F8F3EB"
TEXT = "#29231E"
STEXT = "#70665B"
BRONZE = "#A98552"
GOLD = "#CDB585"
BORDER = "#E5D8C4"

W, H = 1400, 360


def hexagon(cx, cy, r, stroke, fill="none", sw=2.0, opacity=1.0):
    pts = []
    for k in range(6):
        a = math.pi / 3 * k - math.pi / 6
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}" opacity="{opacity}" stroke-linejoin="round"/>')


def molecule(cx, cy, r=26, color=BRONZE):
    """Small molecular ring with bonds and atom dots."""
    parts = [hexagon(cx, cy, r, color, sw=2.2)]
    for dx, dy in [(2.0, -0.2), (-1.2, 0.9), (-0.6, -0.9), (0.9, 1.0)]:
        parts.append(f'<circle cx="{cx + r * dx:.1f}" cy="{cy + r * dy:.1f}" r="3.4" fill="{color}"/>')
    parts.append(f'<line x1="{cx + r * 1.9:.1f}" y1="{cy - r * 0.55:.1f}" x2="{cx + r * 3.1:.1f}" y2="{cy - r * 0.55:.1f}" stroke="{color}" stroke-width="2.2"/>')
    parts.append(f'<circle cx="{cx + r * 3.1:.1f}" cy="{cy - r * 0.55:.1f}" r="3.2" fill="{color}"/>')
    return "".join(parts)


def ribbon(x0, x1, y, amp=26, color=BRONZE):
    """Protein-ribbon band: two parallel sine paths forming a filled ribbon."""
    n = 48
    top, bot = [], []
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        yt = y + amp * math.sin(2 * math.pi * t * 1.6)
        top.append(f"{x:.1f},{yt - 7:.1f}")
        bot.insert(0, f"{x:.1f},{yt + 7:.1f}")
    pts = " ".join(top + bot)
    return (f'<polygon points="{pts}" fill="{color}" opacity="0.28"/>'
            f'<path d="M " + " L ".join(top)' if False else
            f'<path d="M {" L ".join(top)}" fill="none" stroke="{color}" stroke-width="1.6" opacity="0.75"/>')


def network(cx, cy, color=BRONZE):
    """Small network motif: nodes + edges."""
    nodes = [(cx - 60, cy - 18), (cx - 30, cy + 14), (cx, cy - 22), (cx + 28, cy + 6),
             (cx + 58, cy - 16), (cx + 34, cy + 24), (cx - 8, cy + 30)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 5), (3, 6), (1, 6), (4, 5)]
    parts = []
    for a, b in edges:
        x1, y1 = nodes[a]; x2, y2 = nodes[b]
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="1.4" opacity="0.55"/>')
    for x, y in nodes:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{color}" opacity="0.9"/>')
    return "".join(parts)


def blobs(cx, cy, color=BRONZE):
    """Two interacting protein blobs (rounded organic shapes)."""
    return (
        f'<ellipse cx="{cx - 26}" cy="{cy}" rx="24" ry="30" fill="none" stroke="{color}" stroke-width="2.2" opacity="0.8"/>'
        f'<ellipse cx="{cx + 26}" cy="{cy + 6}" rx="20" ry="26" fill="none" stroke="{color}" stroke-width="2.2" opacity="0.8"/>'
        f'<circle cx="{cx - 14}" cy="{cy - 4}" r="3" fill="{color}"/>'
        f'<circle cx="{cx + 12}" cy="{cy + 10}" r="3" fill="{color}"/>'
    )


def arrow(x1, y, x2, color=BRONZE):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" stroke="{color}" stroke-width="1.8"/>'
            f'<path d="M {x2 - 8} {y - 4} L {x2} {y} L {x2 - 8} {y + 4} Z" fill="{color}"/>')


def render():
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="Saveena Solanki — Computational Biology and Molecular AI">')
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<rect x="18" y="18" width="{W - 36}" height="{H - 36}" rx="18" fill="none" stroke="{BORDER}" stroke-width="1.2"/>')

    # ---- left: molecular structure + protein ribbon ----
    p.append(molecule(120, 120, 26))
    p.append(molecule(230, 210, 20, GOLD))
    p.append(ribbon(60, 320, 260, 24, BRONZE))

    # ---- centre: identity ----
    p.append(f'<text x="640" y="132" text-anchor="middle" font-family="Georgia, Times New Roman, serif" font-size="54" font-weight="700" fill="{TEXT}" letter-spacing="2">SAVEENA SOLANKI</text>')
    p.append(f'<text x="640" y="176" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="22" font-weight="600" fill="{BRONZE}" letter-spacing="6">COMPUTATIONAL BIOLOGIST</text>')
    p.append(f'<text x="640" y="214" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="16.5" fill="{STEXT}">Molecular AI across scales</text>')
    p.append(f'<text x="640" y="250" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14.5" font-weight="600" fill="{TEXT}">Molecules  →  Protein Interactions  →  Biological Systems</text>')
    # thin bronze rule under identity
    p.append(f'<line x1="480" y1="272" x2="800" y2="272" stroke="{GOLD}" stroke-width="1.4"/>')

    # ---- right: molecule -> interaction -> network ----
    p.append(molecule(1080, 150, 22, TEXT))
    p.append(arrow(1116, 150, 1160, BRONZE))
    p.append(blobs(1192, 150, TEXT))
    p.append(arrow(1234, 156, 1278, BRONZE))
    p.append(network(1312, 150, TEXT))

    # ---- footer keywords ----
    p.append(f'<line x1="60" y1="316" x2="{W - 60}" y2="316" stroke="{BORDER}" stroke-width="1"/>')
    p.append(f'<text x="640" y="340" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12.5" letter-spacing="3" fill="{STEXT}">REPRESENTATION LEARNING · TARGETED DEGRADATION · MOLECULAR GLUES · KNOWLEDGE GRAPHS</text>')
    p.append('</svg>')
    return "\n".join(p)


def main():
    out = os.path.abspath(OUT)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(render())
    print("wrote", out)


if __name__ == "__main__":
    main()
