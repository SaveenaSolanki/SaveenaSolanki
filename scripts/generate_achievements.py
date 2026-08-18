#!/usr/bin/env python3
"""Self-hosted GitHub achievements card generator.

Fetches public GitHub profile data and renders a themed "achievement wall"
SVG (analytics/achievements.svg). Designed to run locally or in GitHub
Actions (uses GITHUB_TOKEN when present, else unauthenticated).

Dependencies: none (stdlib only). Python >= 3.9.
"""
import json
import os
import sys
import urllib.request

USER = "SaveenaSolanki"
OUT = os.path.join(os.path.dirname(__file__), "..", "analytics", "achievements.svg")

# ---- palette (matches profile banner) ----
BG = "#0d1117"
CARD = "#161b27"
BORDER = "#212a3b"
TEAL = "#5eead4"
CYAN = "#22d3ee"
VIOLET = "#a78bfa"
SKY = "#38bdf8"
TEXT = "#c9d1d9"
DIM = "#8b949e"


def api(path):
    url = f"https://api.github.com{path}"
    req = urllib.request.Request(url, headers={"User-Agent": "achievements-builder", "Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch():
    user = api(f"/users/{USER}")
    repos = api(f"/users/{USER}/repos?per_page=100&sort=updated")
    total_stars = sum(r["stargazers_count"] for r in repos)
    total_forks = sum(r["forks_count"] for r in repos)
    lang_bytes = {}
    for r in repos:
        try:
            langs = api(f"/repos/{USER}/{r['name']}/languages")
        except Exception:
            continue
        for lang, n in langs.items():
            lang_bytes[lang] = lang_bytes.get(lang, 0) + n
    top_lang = max(lang_bytes, key=lang_bytes.get) if lang_bytes else "—"
    return {
        "repos": user["public_repos"],
        "stars": total_stars,
        "forks": total_forks,
        "followers": user["followers"],
        "following": user["following"],
        "top_lang": top_lang,
    }


def fmt(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


# ---- minimal geometric icons ----
def icon_repo(x, y, c):
    return (
        f'<polygon points="{x},{y} {x+26},{y-13} {x+52},{y} {x+52},{y+26} {x+26},{y+39} {x},{y+26}" '
        f'fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round"/>'
        f'<circle cx="{x+26}" cy="{y+13}" r="4" fill="{c}"/>'
    )


def icon_star(x, y, c):
    pts = []
    for k in range(10):
        r = 26 if k % 2 == 0 else 11
        a = -3.14159 / 2 + k * 3.14159 / 5
        pts.append(f"{x + 26 + r * __import__('math').cos(a):.1f},{y + 26 + r * __import__('math').sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{c}"/>'


def icon_fork(x, y, c):
    return (
        f'<path d="M {x+26} {y+6} v 12 M {x+26} {y+18} c 0 8 -14 6 -14 -4 M {x+26} {y+18} c 0 8 14 6 14 -4" '
        f'fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="round"/>'
        f'<circle cx="{x+26}" cy="{y+5}" r="3" fill="{c}"/>'
        f'<circle cx="{x+12}" cy="{y+28}" r="3" fill="{c}"/>'
        f'<circle cx="{x+40}" cy="{y+28}" r="3" fill="{c}"/>'
    )


def icon_person(x, y, c, second=False):
    dx = 14 if second else 0
    return (
        f'<circle cx="{x+22+dx}" cy="{y+12}" r="7" fill="{c}"/>'
        f'<path d="M {x+8+dx} {y+40} c 0 -9 8.5 -14 14 -14 s 14 5 14 14" fill="{c}"/>'
    )


def icon_lang(x, y, c):
    return (
        f'<path d="M {x+10} {y+8} l -8 18 8 18 M {x+42} {y+8} l 8 18 -8 18 M {x+28} {y+4} l -6 36" '
        f'fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def render(data):
    W, H = 1000, 330
    cards = [
        ("Repositories", fmt(data["repos"]), "public repos", icon_repo, TEAL),
        ("Total Stars", fmt(data["stars"]), "across all repos", icon_star, CYAN),
        ("Total Forks", fmt(data["forks"]), "across all repos", icon_fork, SKY),
        ("Followers", fmt(data["followers"]), "on GitHub", icon_person, VIOLET),
        ("Following", fmt(data["following"]), "on GitHub", lambda x, y, c: icon_person(x, y, c, True), VIOLET),
        ("Top Language", data["top_lang"], "by bytes", icon_lang, TEAL),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub achievements for {USER}">',
        f'<rect width="{W}" height="{H}" fill="{BG}" rx="14"/>',
        '<defs>',
        '<linearGradient id="hd" x1="0" y1="0" x2="1" y2="0">',
        f'<stop offset="0%" stop-color="{TEAL}"/><stop offset="100%" stop-color="{VIOLET}"/>',
        '</linearGradient>',
        '</defs>',
        f'<text x="32" y="46" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="22" font-weight="700" fill="url(#hd)">🏆 Achievement Wall</text>',
        f'<text x="32" y="70" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="12.5" fill="{DIM}">Live GitHub analytics · auto-refreshed by GitHub Actions · {USER}</text>',
    ]
    cw, ch, gap = 300, 104, 20
    x0, y0 = 32, 92
    for i, (label, value, sub, icon, color) in enumerate(cards):
        cx = x0 + (i % 3) * (cw + gap)
        cy = y0 + (i // 3) * (ch + gap)
        parts.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="12" fill="{CARD}" stroke="{BORDER}" stroke-width="1"/>')
        parts.append(icon(cx + 16, cy + 16, color))
        parts.append(f'<text x="{cx+92}" y="{cy+44}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="30" font-weight="700" fill="{TEXT}">{value}</text>')
        parts.append(f'<text x="{cx+92}" y="{cy+68}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="13.5" font-weight="600" fill="{color}">{label}</text>')
        parts.append(f'<text x="{cx+92}" y="{cy+86}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="11.5" fill="{DIM}">{sub}</text>')
    parts.append(
        f'<text x="32" y="{H-14}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="11" fill="{DIM}">'
        "Self-hosted analytics — no third-party badge services. Generated from the GitHub API.</text>"
    )
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    out = os.path.abspath(OUT)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    data = fetch()
    svg = render(data)
    with open(out, "w") as f:
        f.write(svg)
    print(f"wrote {out}")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    sys.exit(main())
