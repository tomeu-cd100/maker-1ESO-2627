#!/usr/bin/env python3
"""Verifica la coherència competencial entre la matriu de traçabilitat i les SA.

Comprova tres invariants (pensat per a CI, com `verifica_enllacos.py`):

  1. **§2 de cada SA ↔ matriu §4.** Els criteris (CA) de la secció «## 2» de cada
     `SAx.md` han de coincidir *exactament* amb la fila de la SA a la matriu de
     `Avaluació/Criteris_i_qualificacio.md` §4 (focals + constants = fila de la matriu).
  2. **Constants ben declarats.** Els CA marcats a *totes* les SA de la matriu (les
     constants) s'han de derivar de la matriu i aparèixer a la línia «Constants
     (totes les SA)» de cada SA.
  3. **§8 ⊆ §2.** Cap criteri qualificat a la taula d'avaluació (§8) d'una SA pot
     quedar fora de la seva §2.

La **SA9** és integradora i té la §2 en prosa («integra totes les competències»): se'n
verifica només que ho digui explícitament (queda exempta de la comparació cel·la a cel·la).

Ús:  python verifica_competencies.py     (surt amb codi 1 si troba incoherències)
"""

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).parent
MATRIU = ROOT / "Avaluació" / "Criteris_i_qualificacio.md"
CA_RE = re.compile(r"CA\d\.\d")

# --- 1. Llegeix la matriu de traçabilitat (§4) -----------------------------------
matrix = {}  # CA -> set de núm. de SA (1..9) marcats amb ●
for line in MATRIU.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\|\s*(CA\d\.\d)\b", line)
    if not m:
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    # cells[0] = etiqueta del criteri; cells[1:10] = SA1..SA9
    sa_cells = cells[1:10]
    matrix[m.group(1)] = {i + 1 for i, c in enumerate(sa_cells) if "●" in c}

if len(matrix) != 19:
    print(f"[AVÍS] esperava 19 criteris CA a la matriu, n'he trobat {len(matrix)}.")

# Constants = CA presents a TOTES les 9 SA de la matriu (derivats, no fixats a mà)
CONSTANTS = {ca for ca, sas in matrix.items() if sas >= set(range(1, 10))}

# fila de la matriu per SA: {n: set(CA)}
matrix_by_sa = {n: {ca for ca, sas in matrix.items() if n in sas} for n in range(1, 10)}


def section(text, num):
    """Retorna el text de la secció «## {num}.» fins a la següent «## »."""
    m = re.search(rf"^## {num}\.[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


problems = []
for n in range(1, 10):
    hits = list(ROOT.glob(f"Classes/SA{n}_*/SA{n}.md"))
    if not hits:
        problems.append(f"SA{n}: no trobo el fitxer SA{n}.md")
        continue
    text = hits[0].read_text(encoding="utf-8")
    sec2 = section(text, 2)

    if n == 9:
        # SA integradora: §2 en prosa, exempta de la comparació exacta
        if "totes les competències" not in sec2.lower().replace("competencies", "competències"):
            problems.append("SA9: la §2 hauria de dir explícitament que integra «totes les competències»")
        continue

    ca2 = set(CA_RE.findall(sec2))
    expected = matrix_by_sa[n]

    manquen = expected - ca2
    sobren = ca2 - expected
    if manquen:
        problems.append(f"SA{n} §2: falten (la matriu els marca): {', '.join(sorted(manquen))}")
    if sobren:
        problems.append(f"SA{n} §2: sobren (la matriu NO els marca): {', '.join(sorted(sobren))}")

    # Les constants han d'aparèixer a la §2 (via la línia «Constants»)
    if not CONSTANTS <= ca2:
        problems.append(f"SA{n} §2: no hi consten tots els constants {sorted(CONSTANTS)}")

    # §8 ⊆ §2
    ca8 = set(CA_RE.findall(section(text, 8)))
    fora = ca8 - ca2
    if fora:
        problems.append(f"SA{n} §8: qualifica criteris que no són a la §2: {', '.join(sorted(fora))}")

if problems:
    print(f"[INCOHERENT] {len(problems)} problema(es) de coherència competencial:")
    for p in problems:
        print(f"   - {p}")
    sys.exit(1)

print(
    f"[OK] Matriu ↔ §2 ↔ §8 coherents a les 9 SA. "
    f"Constants (a totes les SA): {' · '.join(sorted(CONSTANTS))}."
)
