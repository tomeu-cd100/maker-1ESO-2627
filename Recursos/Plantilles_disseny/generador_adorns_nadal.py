#!/usr/bin/env python3
"""
Generador de plantilles d'adorns de Nadal per a talladora làser — Aula Maker (mini-repte SA3b).

Crea dos fitxers:
    plantilla   3 adorns pla (bola, estrella i avet) amb forat per al cordill, capa GUIA
                (zona del símbol) i text NOM per gravar.
    encaix      ⭐ avet 3D: dues peces iguals que s'encaixen en creu (ranura = gruix - kerf),
                el mateix principi que el connector del rusc (SA3).

Convenció de capes: TALL = traç vermell (#FF0000) 0.1 mm · GRAVAT = negre · GUIA = blau discontinu.

ÚS:
    python generador_adorns_nadal.py --tipus plantilla --salida adorns_nadal_SA3b.svg
    python generador_adorns_nadal.py --tipus encaix --gruix 3 --kerf 0.15 --salida avet_3d_SA3b.svg
"""
import argparse
import math

TALL = 'fill="none" stroke="#FF0000" stroke-width="0.1"'
GUIA = 'fill="none" stroke="#3366FF" stroke-width="0.3" stroke-dasharray="2,1.5"'
R_PESTANYA = 6.0   # pestanya rodona on va el forat del cordill
R_FORAT = 2.0      # forat de Ø4 mm (hi passa un cordill o una cinta fina)


def f(x):
    return f"{x:.3f}"


def cami_amb_pestanya(pts):
    """Polígon tancat on el primer punt és el vèrtex de dalt: el substitueix per una pestanya
    rodona (arc de radi R_PESTANYA centrat al vèrtex) perquè el forat tingui fusta al voltant."""
    top = pts[0]
    prev, nxt = pts[-1], pts[1]

    def entrada(p):
        dx, dy = p[0] - top[0], p[1] - top[1]
        d = math.hypot(dx, dy)
        return (top[0] + dx / d * R_PESTANYA, top[1] + dy / d * R_PESTANYA)

    a, b = entrada(prev), entrada(nxt)
    d = f"M {f(b[0])},{f(b[1])} "
    d += " ".join(f"L {f(x)},{f(y)}" for x, y in pts[1:]) + " "
    d += f"L {f(a[0])},{f(a[1])} A {R_PESTANYA},{R_PESTANYA} 0 1 1 {f(b[0])},{f(b[1])} Z"
    return d


def forat(cx, cy):
    return f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{R_FORAT}"/>'


def bola(cx, cy):
    """Bola de Ø70 mm amb el capçal (on va el forat)."""
    r = 35.0
    cap_w, cap_h = 14.0, 10.0
    # punts on el capçal talla el cercle
    ang = math.asin((cap_w / 2) / r)
    xl, yl = cx - cap_w / 2, cy - r * math.cos(ang)
    xr = cx + cap_w / 2
    top = cy - r - cap_h + 2
    d = (f"M {f(xr)},{f(yl)} A {r},{r} 0 1 1 {f(xl)},{f(yl)} "
         f"L {f(xl)},{f(top + 3)} Q {f(xl)},{f(top)} {f(xl + 3)},{f(top)} "
         f"L {f(xr - 3)},{f(top)} Q {f(xr)},{f(top)} {f(xr)},{f(top + 3)} Z")
    return d, (cx, top + 4.5), (cx, cy - 3, 21.0), (cx, cy + 25)


def estrella(cx, cy):
    """Estrella de 5 puntes (Ø80 mm) amb pestanya a la punta de dalt."""
    R, r = 40.0, 19.0
    pts = []
    for k in range(10):
        rad = R if k % 2 == 0 else r
        a = math.radians(-90 + 36 * k)
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return cami_amb_pestanya(pts), (cx, cy - R), (cx, cy - 5, 12.0), (cx, cy + 13)


def avet(cx, cy, alt=80.0, ample=64.0):
    """Avet de 3 pisos + tronc, amb pestanya a la punta."""
    top = cy - alt / 2
    pis = [(0.38, 0.45), (0.68, 0.72), (0.88, 1.0)]  # (alçada relativa del pis, ample relatiu)
    dreta, esq = [], []
    for k, (h, w) in enumerate(pis):
        y = top + h * alt
        if k > 0:  # entrant del pis anterior
            yi = top + pis[k - 1][0] * alt  # esglaó horitzontal cap endins
            wi = pis[k - 1][1] * 0.62
            dreta.append((cx + wi * ample / 2, yi))
            esq.append((cx - wi * ample / 2, yi))
        dreta.append((cx + w * ample / 2, y))
        esq.append((cx - w * ample / 2, y))
    tronc_w, tronc_h = 12.0, alt * 0.12
    ybase = top + 0.88 * alt
    pts = [(cx, top)] + dreta + [(cx + tronc_w / 2, ybase), (cx + tronc_w / 2, ybase + tronc_h),
                                 (cx - tronc_w / 2, ybase + tronc_h), (cx - tronc_w / 2, ybase)]
    pts += list(reversed(esq))
    return cami_amb_pestanya(pts), (cx, top), (cx, top + 0.55 * alt, 13.0), (cx, ybase + tronc_h / 2 + 1.6)


def plantilla():
    W, H = 260.0, 100.0
    peces = [("Bola", bola(45, 55)), ("Estrella", estrella(130, 52)), ("Avet", avet(215, 52))]
    tall, guia, gravat = [], [], []
    for nom, (d, (hx, hy), (gx, gy, gr), (tx, ty)) in peces:
        tall.append(f'    <path d="{d}"/>')
        tall.append("    " + forat(hx, hy))
        guia.append(f'    <circle cx="{f(gx)}" cy="{f(gy)}" r="{gr}"/>')
        gravat.append(f'    <text x="{f(tx)}" y="{f(ty)}" font-size="6" font-weight="bold" text-anchor="middle">NOM</text>')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Adorns de Nadal (mini-repte SA3b): bola, estrella i avet amb forat per al cordill.
     TALL = vermell 0.1 mm · GRAVAT = negre. Esborra els 2 adorns que no facis servir.
     Generat per generador_adorns_nadal.py (Aula Maker, CC BY-SA 4.0). -->
<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">
  <g id="TALL" inkscape:groupmode="layer" inkscape:label="TALL" {TALL}>
{chr(10).join(tall)}
  </g>
  <g id="GRAVAT" inkscape:groupmode="layer" inkscape:label="GRAVAT" fill="#000000" font-family="sans-serif" text-anchor="middle">
    <!-- Substitueix NOM pel teu nom o la teva inicial i converteix-lo a camí -->
{chr(10).join(gravat)}
  </g>
  <!-- GUIA: el símbol ha de cabre dins del cercle. AMAGA aquesta capa abans de tallar. -->
  <g id="GUIA" inkscape:groupmode="layer" inkscape:label="GUIA (amaga-la abans de tallar)" sodipodi:insensitive="true" {GUIA}>
{chr(10).join(guia)}
  </g>
</svg>
'''


def avet_encaix(gruix, kerf):
    """Dues peces d'avet (90 mm): A amb ranura de baix a mig, B de dalt a mig. S'encaixen en creu."""
    alt, ample = 90.0, 70.0
    ranura = gruix - kerf  # el làser es menja el kerf: la ranura dibuixada és més estreta
    W, H = 170.0, 105.0

    def peca(cx, cy, des_de_dalt):
        top, yb, bot = cy - alt / 2, cy - alt / 2 + alt * 0.9, cy + alt / 2
        mig, s = cy, ranura / 2
        dreta = [(cx + ample / 2, yb), (cx + 6, yb), (cx + 6, bot)]
        esq = [(cx - 6, bot), (cx - 6, yb), (cx - ample / 2, yb)]
        if des_de_dalt:
            # peça B: la ranura baixa des de la punta fins a la meitat (sense pestanya)
            ye = top + s * (yb - top) / (ample / 2)
            pts = [(cx + s, ye)] + dreta + esq + [(cx - s, ye), (cx - s, mig), (cx + s, mig)]
            return "M " + " L ".join(f"{f(x)},{f(y)}" for x, y in pts) + " Z", None
        # peça A: la ranura puja des de la base (pel tronc) fins a la meitat; pestanya a dalt
        pts = [(cx, top)] + dreta + [(cx + s, bot), (cx + s, mig), (cx - s, mig), (cx - s, bot)] + esq
        return cami_amb_pestanya(pts), (cx, top)

    da, (hx, hy) = peca(45, 52, False)
    db, _ = peca(125, 52, True)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- ⭐ Avet 3D encaixat (mini-repte SA3b): 2 peces, ranura = gruix {gruix} - kerf {kerf} = {ranura:.2f} mm.
     Peça A (forat per penjar-lo) + peça B. S'encaixen en creu. TALL = vermell 0.1 mm.
     Generat per generador_adorns_nadal.py (Aula Maker, CC BY-SA 4.0). -->
<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">
  <g id="TALL" inkscape:groupmode="layer" inkscape:label="TALL" {TALL}>
    <path d="{da}"/>
    {forat(hx, hy)}
    <path d="{db}"/>
  </g>
  <g id="GRAVAT" inkscape:groupmode="layer" inkscape:label="GRAVAT" fill="#000000" font-family="sans-serif" text-anchor="middle" font-size="5" font-weight="bold">
    <text x="45" y="{52 + 90 * 0.4 - 38:.1f}">A</text>
    <text x="125" y="{52 + 90 * 0.4:.1f}">B</text>
  </g>
</svg>
'''


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tipus", choices=["plantilla", "encaix"], default="plantilla")
    ap.add_argument("--gruix", type=float, default=3.0, help="gruix de la fusta (mm)")
    ap.add_argument("--kerf", type=float, default=0.15, help="kerf de l'equip (mm), el de la mostra de la SA3")
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    if a.tipus == "plantilla":
        svg, nom = plantilla(), a.salida or "adorns_nadal_SA3b.svg"
    else:
        svg, nom = avet_encaix(a.gruix, a.kerf), a.salida or "avet_3d_SA3b.svg"
    with open(nom, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"OK {nom}")


if __name__ == "__main__":
    main()
