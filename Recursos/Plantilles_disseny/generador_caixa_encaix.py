#!/usr/bin/env python3
"""
Generador de caixes amb encaix (finger joints) per a talladora làser — Aula Maker (SA3).

Crea un SVG amb les 6 cares d'una caixa rectangular amb dits d'encaix, llest per tallar.
Convenció de capes: TALL = traç vermell (#FF0000), gruix de línia 0.1 mm.

ÚS:
    python generador_caixa_encaix.py            # caixa per defecte 80x80x50, fusta 3 mm
    python generador_caixa_encaix.py --ancho 100 --largo 60 --alto 40 --grosor 3 --salida caixa.svg

Després: obre el SVG a Inkscape/xTool Creative Space, comprova mides i assigna el contorn a TALL.
Nota: pensat amb finalitat educativa; comprova sempre amb una mostra d'encaix abans de tallar-ho tot.
"""
import argparse

def fingers(length, t):
    """Nombre de dits senar perquè comenci i acabi amb 'pestanya' (mín. 3)."""
    n = max(3, int(length // (t * 3)))
    if n % 2 == 0:
        n -= 1
    return n

def edge(x, y, length, t, horizontal, out_start):
    """
    Genera els punts d'una vora amb dits d'encaix.
    out_start=True: la vora comença sortint cap enfora (pestanya).
    Retorna llista de punts (x, y) al llarg de la vora.
    """
    n = fingers(length, t)
    seg = length / n
    pts = [(x, y)]
    cx, cy = x, y
    out = out_start
    for i in range(n):
        if horizontal:
            cx += seg
            pts.append((cx, cy))
            if i < n - 1:
                cy += t if out else -t
                pts.append((cx, cy))
        else:
            cy += seg
            pts.append((cx, cy))
            if i < n - 1:
                cx += -t if out else t
                pts.append((cx, cy))
        out = not out
    return pts

def panel_path(w, h, t, top, right, bottom, left):
    """Crea un camí tancat d'un panell w x h. Cada vora: True=dits sortints, None=recta."""
    pts = []
    # Top (esquerra -> dreta)
    if top is None:
        pts += [(0, 0), (w, 0)]
    else:
        pts += edge(0, 0, w, t, True, top)
    # Right (dalt -> baix)
    if right is None:
        pts += [(w, 0), (w, h)]
    else:
        pts += edge(w, 0, h, t, False, right)
    # Bottom (dreta -> esquerra) -> generem d'esquerra a dreta i invertim
    if bottom is None:
        pts += [(w, h), (0, h)]
    else:
        e = edge(0, h, w, t, bottom, True)
        pts += list(reversed(e))
    # Left (baix -> dalt)
    if left is None:
        pts += [(0, h), (0, 0)]
    else:
        e = edge(0, 0, h, t, left, False)
        pts += list(reversed(e))
    d = "M " + " L ".join(f"{px:.2f},{py:.2f}" for px, py in pts) + " Z"
    return d

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ancho", type=float, default=80, help="amplada interior aprox. (mm)")
    ap.add_argument("--largo", type=float, default=80, help="llargada interior aprox. (mm)")
    ap.add_argument("--alto", type=float, default=50, help="alçada (mm)")
    ap.add_argument("--grosor", type=float, default=3.0, help="gruix del material (mm)")
    ap.add_argument("--salida", default="caixa_encaix.svg")
    a = ap.parse_args()

    W, L, H, t = a.ancho, a.largo, a.alto, a.grosor
    gap = 8  # separació entre panells al full

    # Definició de les 6 cares (amb dits a les vores que toquen una altra cara)
    panels = [
        ("Base",     W, L, dict(top=True,  right=True,  bottom=True,  left=True)),
        ("Tapa",     W, L, dict(top=True,  right=True,  bottom=True,  left=True)),
        ("Frontal",  W, H, dict(top=None,  right=True,  bottom=False, left=True)),
        ("Posterior",W, H, dict(top=None,  right=True,  bottom=False, left=True)),
        ("Lateral1", L, H, dict(top=None,  right=False, bottom=False, left=False)),
        ("Lateral2", L, H, dict(top=None,  right=False, bottom=False, left=False)),
    ]

    parts, x_off, y_off, row_h, max_w = [], gap, gap, 0, 0
    for name, w, h, edges in panels:
        if x_off + w + gap > 600:  # nova fila si no hi cap
            x_off = gap
            y_off += row_h + gap
            row_h = 0
        d = panel_path(w, h, t, **edges)
        parts.append(f'<g transform="translate({x_off:.2f},{y_off:.2f})">'
                     f'<path d="{d}" fill="none" stroke="#FF0000" stroke-width="0.1"/>'
                     f'<text x="{w/2:.1f}" y="{h/2:.1f}" font-family="sans-serif" '
                     f'font-size="4" fill="#cccccc" text-anchor="middle">{name}</text></g>')
        x_off += w + gap
        row_h = max(row_h, h)
        max_w = max(max_w, x_off)
    total_h = y_off + row_h + gap

    svg = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
           f'<!-- Caixa amb encaix {W}x{L}x{H} mm, gruix {t} mm. TALL=vermell 0.1mm. '
           f'Generat per generador_caixa_encaix.py (Aula Maker). -->\n'
           f'<svg xmlns="http://www.w3.org/2000/svg" width="{max_w:.1f}mm" '
           f'height="{total_h:.1f}mm" viewBox="0 0 {max_w:.1f} {total_h:.1f}">\n'
           + "\n".join(parts) + "\n</svg>\n")

    with open(a.salida, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Creat: {a.salida}  ({W}x{L}x{H} mm, gruix {t} mm)")

if __name__ == "__main__":
    main()
