#!/usr/bin/env python3
"""Verifica que tots els enllaços locals de la web generada (`web/`) resolen.

S'executa DESPRÉS de `build_web.py`: recorre els .html generats i comprova que
cada `href`/`src` local apunta a un fitxer existent dins de `web/`. Complementa
`verifica_enllacos.py` (que valida les fonts .md): la reescriptura d'enllaços de
la build pot trencar coses que les fonts no tenen (p. ex. majúscules — GitHub
Pages distingeix majúscules i Windows no, per això un 404 pot no veure's en local).

Un enllaç a un directori es dona per bo només si conté `index.html` (com fa
GitHub Pages). Surt amb codi 1 si troba enllaços trencats (pensat per a CI).

Ús:  python build_web.py && python verifica_web.py
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
WEB = ROOT / "web"

if not WEB.is_dir():
    print("[ERROR] No existeix web/: executa primer build_web.py")
    sys.exit(1)

# Conjunt de rutes reals amb les majúscules EXACTES (Windows és case-insensitive
# i Path.exists() hi enganyaria; GitHub Pages no perdona).
reals = {str(p.relative_to(WEB)).replace("\\", "/") for p in WEB.rglob("*") if p.is_file()}

ATTR_RE = re.compile(r'(?:href|src)="([^"]+)"')

html_files = sorted(WEB.rglob("*.html"))
broken = []
for page in html_files:
    page_dir = page.parent.relative_to(WEB)
    text = page.read_text(encoding="utf-8")
    # No mirem dins d'<script>: hi ha plantilles JS (p. ex. cerca.html) amb ${...}
    text = re.sub(r"<script\b.*?</script>", "", text, flags=re.S)
    for m in ATTR_RE.finditer(text):
        url = html.unescape(m.group(1))
        if url.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        url = url.split("#")[0].split("?")[0]
        if not url:
            continue
        # Resol la ruta relativa a la pàgina, en pur text (sense tocar el disc)
        parts = list(page_dir.parts)
        for seg in url.split("/"):
            if seg in ("", "."):
                continue
            if seg == "..":
                if parts:
                    parts.pop()
            else:
                parts.append(seg)
        target = "/".join(parts)
        if target in reals or f"{target}/index.html" in reals:
            continue
        broken.append((str(page.relative_to(WEB)).replace("\\", "/"), m.group(1)))

if broken:
    print(f"[TRENCAT] {len(broken)} enllacos locals trencats a la web generada:")
    for src, url in broken:
        print(f"   {src}  ->  {url}")
    sys.exit(1)
print(f"[OK] {len(html_files)} pagines .html revisades: tots els enllacos locals resolen.")
