#!/usr/bin/env python3
"""Generate project banners for flagship research repositories.

One visual family — cream/bronze system, molecule motif left,
identity centre, network motif right, family tagline footer.

Usage: python3 generate_project_banner.py <name> <role> <claim> <tagline> <out.svg>
"""
import os, sys, math

BG = "#FFFDF9"
TEXT = "#29231E"
STEXT = "#70665B"
BRONZE = "#A98552"
GOLD = "#CDB585"
BORDER = "#E5D8C4"

W, H = 1400, 300


def hexagon(cx, cy, r, color, sw=2.0):
    pts = []
    for k in range(6):
        a = math.pi / 3 * k - math.pi / 6
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"/>')


def molecule(cx, cy, r=24, color=BRONZE):
    parts = [hexagon(cx, cy, r, color)]
    for dx, dy in [(1.8, -0.2), (-1.1, 0.9), (-0.6, -0.9)]:
        parts.append(f'<circle cx="{cx + r * dx:.1f}" cy="{cy + r * dy:.1f}" r="3.2" fill="{color}"/>')
    return "".join(parts)


def network(cx, cy, color=TEXT):
    nodes = [(cx - 52, cy - 16), (cx - 26, cy + 12), (cx, cy - 20), (cx + 24, cy + 6), (cx + 50, cy - 14)]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
    parts = []
    for a, b in edges:
        x1, y1 = nodes[a]; x2, y2 = nodes[b]
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="1.4" opacity="0.55"/>')
    for x, y in nodes:
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{color}"/>')
    return "".join(parts)


def render(name, role, claim, tagline):
    p = []
    p.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{name} — {claim}">')
    p.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
    p.append(f'<rect x="18" y="18" width="{W - 36}" height="{H - 36}" rx="16" fill="none" stroke="{BORDER}" stroke-width="1.2"/>')
    # left: molecule motif
    p.append(molecule(120, 110, 24))
    p.append(molecule(215, 195, 17, GOLD))
    # centre: identity
    p.append(f'<text x="640" y="118" text-anchor="middle" font-family="Georgia, Times New Roman, serif" font-size="46" font-weight="700" fill="{TEXT}" letter-spacing="2">{name}</text>')
    p.append(f'<text x="640" y="158" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="19" font-weight="600" fill="{BRONZE}" letter-spacing="4">{role}</text>')
    p.append(f'<text x="640" y="196" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="15.5" fill="{STEXT}">{claim}</text>')
    p.append(f'<line x1="470" y1="216" x2="810" y2="216" stroke="{GOLD}" stroke-width="1.4"/>')
    # right: network motif
    p.append(network(1280, 150, TEXT))
    # footer: family tagline
    p.append(f'<line x1="60" y1="258" x2="{W - 60}" y2="258" stroke="{BORDER}" stroke-width="1"/>')
    p.append(f'<text x="640" y="280" text-anchor="middle" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12" letter-spacing="3" fill="{STEXT}">{tagline}</text>')
    p.append('</svg>')
    return "\n".join(p)


if __name__ == "__main__":
    name, role, claim, tagline, out = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w") as f:
        f.write(render(name, role, claim, tagline))
    print("wrote", out)
