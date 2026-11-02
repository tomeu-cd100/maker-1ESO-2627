"""Genera els PDF per a l'alumnat a partir dels imprimibles de la web (web/impressos/*.html).

Ús (amb el Python 3.11 real, després de `build_web.py`):
    py -3.11 genera_pdf_impressos.py SA3

Fa servir Chrome/Edge sense interfície (A4, mida real, sense capçaleres) i desa els PDF a
`PDF_alumnat/<SA>/` (gitignored: són artefactes, la font és l'HTML de `web_assets/impressos/`).
Per afegir una SA, amplia el diccionari PDFS.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web" / "impressos"
OUT = ROOT / "PDF_alumnat"

# SA -> [(imprimible.html, nom del PDF)]
PDFS = {
    "SA3": [
        ("rajola_paper_SA3.html", "SA3_1_Quadern_rajola_rusc.pdf"),
        ("banc_motius_paper_SA3.html", "SA3_2_Banc_de_motius.pdf"),
        ("targetes_rusc_SA3.html", "SA3_3_Targetes_Fira.pdf"),
        ("adorns_nadal_paper_SA3b.html", "SA3b_Adorn_de_Nadal.pdf"),
    ],
}

NAVEGADORS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]


def navegador() -> str:
    for n in NAVEGADORS:
        if os.path.exists(n):
            return n
    sys.exit("No trobo Chrome ni Edge.")


def main():
    sas = sys.argv[1:] or list(PDFS)
    if not WEB.is_dir():
        sys.exit("Primer genera la web: py -3.11 build_web.py")
    nav = navegador()
    perfil = tempfile.mkdtemp(prefix="pdf_impressos_")
    for sa in sas:
        dest = OUT / sa
        dest.mkdir(parents=True, exist_ok=True)
        for html, pdf in PDFS[sa]:
            src = (WEB / html).as_uri()
            out = dest / pdf
            subprocess.run([nav, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                            f"--user-data-dir={perfil}", f"--print-to-pdf={out}", src],
                           check=True, capture_output=True, timeout=120)
            print(f"OK {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
