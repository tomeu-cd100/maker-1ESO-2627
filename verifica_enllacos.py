#!/usr/bin/env python3
"""Verifica que totes les referències internes dels .md apunten a fitxers existents.

Comprova dos estils de referència:
  1. Enllaços markdown:  [text](Carpeta/Fitxer.md)
  2. Referències en codi: `Carpeta/Fitxer.md` (l'estil dominant del material)

Els noms sols (`Fitxa_alumnat.md`) es resolen primer a la carpeta del document.
Surt amb codi 1 si troba referències trencades (pensat per a CI).

Ús:  python verifica_enllacos.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SKIP_DIRS = {"web", ".git", ".github", ".claude", "web_assets"}

md_files = [p for p in ROOT.rglob("*.md")
            if not any(part in SKIP_DIRS for part in p.parts)]
all_rel = {str(p.relative_to(ROOT)).replace("\\", "/") for p in md_files}
by_name = {}
for rel in all_rel:
    by_name.setdefault(rel.rsplit("/", 1)[-1], []).append(rel)

LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)\)")
CODE_RE = re.compile(r"`([^`\n]+?\.md)`")

broken = []
for p in md_files:
    rel = str(p.relative_to(ROOT)).replace("\\", "/")
    cur_dir = rel.rsplit("/", 1)[0] if "/" in rel else ""
    text = p.read_text(encoding="utf-8")
    refs = set(LINK_RE.findall(text)) | set(CODE_RE.findall(text))
    for ref in refs:
        clean = ref.replace("%20", " ").lstrip("./").strip()
        # referències genèriques intencionades: «SAx.md», «Rubrica_SAx.md»,
        # «Classes/SAx_…/Fitxa_alumnat.md» — parlen de "el de cada SA"
        if "sax" in clean.lower() or "…" in clean:
            continue
        if clean in all_rel:
            continue
        if cur_dir and f"{cur_dir}/{clean}" in all_rel:
            continue
        # el nom sol existeix en alguna carpeta (p. ex. Exemple_resolt.md,
        # que hi és a les 9 SA): referència genèrica vàlida
        if by_name.get(clean.rsplit("/", 1)[-1]):
            continue
        broken.append((rel, ref))

if broken:
    print(f"[TRENCAT] {len(broken)} referencies trencades:")
    for src, ref in broken:
        print(f"   {src}  ->  {ref}")
    sys.exit(1)
print(f"[OK] {len(md_files)} fitxers .md revisats: cap referencia trencada.")
