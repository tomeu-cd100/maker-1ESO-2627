#!/usr/bin/env python3
"""
Generador de rajoles hexagonals amb connector «corbatí» per a talladora làser — Aula Maker (SA3).

Cada rajola és un hexàgon amb una osca en forma de cua d'oronella al mig de cada costat.
Una peça petita en forma de corbatí (dues cues d'oronella unides) uneix dues rajoles veïnes.
Els 6 costats són iguals: les rajoles encaixen en qualsevol orientació.

Crea quatre tipus de fitxer:
    rajola      plantilla d'una rajola (TALL vermell + GRAVAT negre + capa GUIA blava)
    connectors  full de connectors amb el kerf compensat
    mostra      mostra de connectors: 2 cupons amb osca + 4 connectors (kerf 0,0-0,3 mm)
    rusc        esquema del rusc de la classe (només per mirar, no per tallar)

Convenció de capes: TALL = traç vermell (#FF0000), 0.1 mm · GRAVAT = negre (#000000).

ÚS:
    python generador_rajola_hexagonal.py --tipus rajola --salida rajola_hexagonal_SA3.svg
    python generador_rajola_hexagonal.py --tipus connectors --kerf 0.15 --n 24
    python generador_rajola_hexagonal.py --tipus mostra --salida mostra_connectors_SA3.svg
    python generador_rajola_hexagonal.py --tipus rusc --n 24 --salida rusc_esquema_SA3.svg
    python generador_rajola_hexagonal.py --tipus rajola --format dxf --salida rajola_hexagonal_SA3.dxf

xTool Studio: importa el DXF (surt a mida real). No copiïs i enganxis des d'Inkscape: canvia l'escala.

Nota: pensat amb finalitat educativa; talla sempre la mostra de connectors abans del full sencer.
"""
import argparse
import math

# Mides de l'osca (mm). La cua d'oronella s'eixampla cap endins: per això no es desmunta.
AMPLE_VORA = 10.0     # amplada de l'osca a la vora de la rajola (la «cintura» del corbatí)
AMPLE_FONS = 15.0     # amplada de l'osca al fons
FONDARIA = 8.0        # fondària de l'osca
JOC_PUNTA = 0.5       # el connector és 0,5 mm més curt que l'osca: no toca el fons

TALL = 'fill="none" stroke="#FF0000" stroke-width="0.1"'
GUIA = 'fill="none" stroke="#3366FF" stroke-width="0.3" stroke-dasharray="2,1.5"'


def punts_a_cami(pts):
    return "M " + " L ".join(f"{x:.3f},{y:.3f}" for x, y in pts) + " Z"


def rajola(entre_costats):
    """Contorn de la rajola (hexàgon de costat pla a dalt) amb una osca a cada costat."""
    r = entre_costats / math.sqrt(3)  # radi = costat de l'hexàgon
    vertexs = [(r * math.cos(math.radians(60 * k)), r * math.sin(math.radians(60 * k)))
               for k in range(6)]
    pts = []
    for k in range(6):
        (x0, y0), (x1, y1) = vertexs[k], vertexs[(k + 1) % 6]
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        ux, uy = (x1 - x0) / r, (y1 - y0) / r          # direcció del costat
        nx, ny = -mx / math.hypot(mx, my), -my / math.hypot(mx, my)  # cap al centre
        pts.append((x0, y0))
        pts.append((mx - ux * AMPLE_VORA / 2, my - uy * AMPLE_VORA / 2))
        pts.append((mx - ux * AMPLE_FONS / 2 + nx * FONDARIA, my - uy * AMPLE_FONS / 2 + ny * FONDARIA))
        pts.append((mx + ux * AMPLE_FONS / 2 + nx * FONDARIA, my + uy * AMPLE_FONS / 2 + ny * FONDARIA))
        pts.append((mx + ux * AMPLE_VORA / 2, my + uy * AMPLE_VORA / 2))
    return pts


def corbati():
    """Connector centrat a l'origen; la línia d'unió de les dues rajoles és x = 0."""
    llarg = FONDARIA - JOC_PUNTA
    ample_punta = AMPLE_VORA + (AMPLE_FONS - AMPLE_VORA) * llarg / FONDARIA
    return [(-llarg, -ample_punta / 2), (0, -AMPLE_VORA / 2), (llarg, -ample_punta / 2),
            (llarg, ample_punta / 2), (0, AMPLE_VORA / 2), (-llarg, ample_punta / 2)]


def eixampla(pts, d):
    """Desplaça cada costat del polígon d mm cap enfora (compensació de kerf)."""
    if d == 0:
        return pts
    n = len(pts)
    area = sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))
    signe = 1 if area > 0 else -1
    linies = []
    for i in range(n):
        (x0, y0), (x1, y1) = pts[i], pts[(i + 1) % n]
        lx, ly = x1 - x0, y1 - y0
        long_ = math.hypot(lx, ly)
        nx, ny = signe * ly / long_, -signe * lx / long_  # normal cap enfora
        linies.append(((x0 + nx * d, y0 + ny * d), (lx, ly)))
    nous = []
    for i in range(n):
        (px, py), (ax, ay) = linies[i - 1]
        (qx, qy), (bx, by) = linies[i]
        det = ax * by - ay * bx
        t = ((qx - px) * by - (qy - py) * bx) / det
        nous.append((px + ax * t, py + ay * t))
    return nous


def svg(ample, alt, cos, comentari):
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<!-- {comentari}\n'
            f'     TALL = vermell 0.1 mm · GRAVAT = negre. Generat per generador_rajola_hexagonal.py (Aula Maker). -->\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" '
            f'width="{ample:.1f}mm" height="{alt:.1f}mm" viewBox="0 0 {ample:.1f} {alt:.1f}">\n'
            + cos + "</svg>\n")


def fitxer_rajola(f):
    r = f / math.sqrt(3)
    ample, alt = 2 * r + 4, f + 4
    cx, cy = ample / 2, alt / 2
    cos = (f'  <g id="TALL" inkscape:groupmode="layer" inkscape:label="TALL" transform="translate({cx:.3f},{cy:.3f})" {TALL}>\n'
           f'    <path d="{punts_a_cami(rajola(f))}"/>\n  </g>\n'
           f'  <g id="GRAVAT" inkscape:groupmode="layer" inkscape:label="GRAVAT" fill="#000000" font-family="sans-serif" text-anchor="middle">\n'
           f'    <!-- Substitueix aquest text pel teu nom (màx. 10 lletres) -->\n'
           f'    <text x="{cx:.2f}" y="{cy + f * 0.36:.2f}" font-size="7" font-weight="bold">NOM</text>\n  </g>\n'
           f'  <!-- GUIA: el teu símbol ha de cabre dins del cercle. AMAGA aquesta capa abans d\'enviar-la a tallar. -->\n'
           f'  <g id="GUIA" inkscape:groupmode="layer" inkscape:label="GUIA (amaga-la abans de tallar)" sodipodi:insensitive="true" '
           f'{GUIA}>\n'
           f'    <circle cx="{cx:.2f}" cy="{cy - f * 0.04:.2f}" r="{f * 0.28:.2f}"/>\n  </g>\n')
    return svg(ample, alt, cos, f"Rajola hexagonal SA3: {f:g} mm entre costats, 6 osques de cua d'oronella.")


def fitxer_connectors(n, kerf):
    pts = punts_a_cami(eixampla(corbati(), kerf))
    pas_x, pas_y, columnes = 2 * FONDARIA + 3, AMPLE_FONS + 3, 6
    files = math.ceil(n / columnes)
    cos = f'  <g id="TALL" {TALL}>\n'
    for i in range(n):
        x = 2 + FONDARIA + (i % columnes) * pas_x
        y = 2 + AMPLE_FONS / 2 + (i // columnes) * pas_y
        cos += f'    <path transform="translate({x:.2f},{y:.2f})" d="{pts}"/>\n'
    cos += "  </g>\n"
    return svg(columnes * pas_x + 1, files * pas_y + 1, cos,
               f"{n} connectors corbatí per a la rajola hexagonal SA3, kerf compensat {kerf:g} mm.")


def fitxer_mostra():
    # Cupó: rectangle 30x22 amb una osca centrada a la vora superior.
    ample_c, alt_c = 30.0, 22.0
    def cupo(x0, y0):
        m = x0 + ample_c / 2
        return punts_a_cami([(x0, y0), (m - AMPLE_VORA / 2, y0), (m - AMPLE_FONS / 2, y0 + FONDARIA),
                             (m + AMPLE_FONS / 2, y0 + FONDARIA), (m + AMPLE_VORA / 2, y0),
                             (x0 + ample_c, y0), (x0 + ample_c, y0 + alt_c), (x0, y0 + alt_c)])
    cos = f'  <g id="TALL" {TALL}>\n'
    cos += f'    <path d="{cupo(3, 3)}"/>\n    <path d="{cupo(37, 3)}"/>\n'
    for i, k in enumerate((0.0, 0.1, 0.2, 0.3)):
        cos += (f'    <path transform="translate({11 + i * 16:.2f},38)" '
                f'd="{punts_a_cami(eixampla(corbati(), k))}"/>\n')
    cos += '  </g>\n  <g id="GRAVAT" fill="#000000" font-family="sans-serif" text-anchor="middle">\n'
    for i, k in enumerate(("0,0", "0,1", "0,2", "0,3")):
        cos += f'    <text x="{11 + i * 16:.2f}" y="52" font-size="3.2">{k}</text>\n'
    cos += ('    <text x="35" y="58" font-size="3" font-weight="bold">MOSTRA DE CONNECTORS</text>\n'
            '    <text x="35" y="62" font-size="2.6">Entra amb el polze i no cau si sacseges?</text>\n'
            '    <text x="35" y="65.5" font-size="2.6">Aquest número és el vostre kerf.</text>\n  </g>\n')
    return svg(70, 68, cos, "Mostra de connectors SA3: 2 cupons amb osca + 4 connectors (kerf 0,0 / 0,1 / 0,2 / 0,3 mm).")


def fitxer_rusc(n, f):
    """Esquema del mural: rajoles en files decalades (costat pla a dalt) i connectors on es toquen."""
    r = f / math.sqrt(3)
    columnes = max(3, round(math.sqrt(n * 1.6)))
    centres = []
    for i in range(n):
        c, fila = i % columnes, i // columnes
        centres.append((r + 4 + c * 1.5 * r, f / 2 + 4 + fila * f + (f / 2 if c % 2 else 0)))
    ample = max(x for x, _ in centres) + r + 4
    alt = max(y for _, y in centres) + f / 2 + 4
    contorn = punts_a_cami(rajola(f))
    cos = f'  <g {TALL.replace("#FF0000", "#999999").replace("0.1", "0.6")}>\n'
    cos += "".join(f'    <path transform="translate({x:.2f},{y:.2f})" d="{contorn}"/>\n' for x, y in centres)
    cos += '  </g>\n  <g fill="#E8A317" stroke="#7A5200" stroke-width="0.4">\n'
    corb = corbati()
    for i, (x0, y0) in enumerate(centres):
        for x1, y1 in centres[i + 1:]:
            if abs(math.hypot(x1 - x0, y1 - y0) - f) < 0.5:   # veïnes: centres a f mm
                ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
                cos += (f'    <path transform="translate({(x0 + x1) / 2:.2f},{(y0 + y1) / 2:.2f}) '
                        f'rotate({ang:.1f})" d="{punts_a_cami(corb)}"/>\n')
    cos += '  </g>\n  <g fill="#555555" font-family="sans-serif" text-anchor="middle" font-size="9">\n'
    cos += "".join(f'    <text x="{x:.2f}" y="{y + 3:.2f}">{i + 1}</text>\n' for i, (x, y) in enumerate(centres))
    cos += "  </g>\n"
    return svg(ample, alt, cos, f"Esquema del rusc SA3: {n} rajoles i els connectors (taronja). No és per tallar.")


# ---------------------------------------------------------------- DXF
# xTool Studio no importa bé l'SVG d'Inkscape i, si el copies i l'enganxes, el canvia d'escala
# (l'hexàgon passa de 115,5 × 100 a uns 200 × 171 mm) i les osques deixen d'encaixar.
# El DXF va en mil·límetres reals ($INSUNITS = 4): s'importa directament i a mida.

def dxf(polilinies, textos=()):
    """polilinies: llista de (capa, punts) en mm, eix y cap amunt.
    textos: llista de (x, y, alçada, text) a la capa GRAVAT."""
    # Tot dins del quadrant positiu, amb 2 mm de marge: algunes aplicacions situen
    # malament el que queda a coordenades negatives.
    tots = [p for _, pts in polilinies for p in pts]
    dx = 2 - min(x for x, _ in tots)
    dy = 2 - min(y for _, y in tots)
    polilinies = [(c, [(x + dx, y + dy) for x, y in pts]) for c, pts in polilinies]
    textos = [(x + dx, y + dy, h, t) for x, y, h, t in textos]
    l = ["0", "SECTION", "2", "HEADER", "9", "$ACADVER", "1", "AC1009",
         "9", "$INSUNITS", "70", "4", "9", "$MEASUREMENT", "70", "1", "0", "ENDSEC",
         "0", "SECTION", "2", "TABLES", "0", "TABLE", "2", "LAYER", "70", "2",
         "0", "LAYER", "2", "TALL", "70", "0", "62", "1", "6", "CONTINUOUS",
         "0", "LAYER", "2", "GRAVAT", "70", "0", "62", "7", "6", "CONTINUOUS",
         "0", "ENDTAB", "0", "ENDSEC", "0", "SECTION", "2", "ENTITIES"]
    for capa, pts in polilinies:
        l += ["0", "POLYLINE", "8", capa, "66", "1", "70", "1", "10", "0", "20", "0", "30", "0"]
        for x, y in pts:
            l += ["0", "VERTEX", "8", capa, "10", f"{x:.4f}", "20", f"{y:.4f}", "30", "0"]
        l += ["0", "SEQEND", "8", capa]
    for x, y, h, t in textos:
        l += ["0", "TEXT", "8", "GRAVAT", "10", f"{x:.3f}", "20", f"{y:.3f}", "30", "0",
              "40", f"{h:g}", "1", t, "72", "1", "11", f"{x:.3f}", "21", f"{y:.3f}", "31", "0"]
    l += ["0", "ENDSEC", "0", "EOF"]
    return "\n".join(l) + "\n"


def mou(pts, dx, dy):
    """Trasllada i inverteix l'eix y (SVG va cap avall, DXF cap amunt)."""
    return [(x + dx, -(y + dy)) for x, y in pts]


def dxf_rajola(f):
    # Només el contorn de tall: el nom i el símbol s'afegeixen a xTool.
    return dxf([("TALL", mou(rajola(f), 0, 0))])


def dxf_connectors(n, kerf):
    pas_x, pas_y, columnes = 2 * FONDARIA + 3, AMPLE_FONS + 3, 6
    pts = eixampla(corbati(), kerf)
    return dxf([("TALL", mou(pts, 2 + FONDARIA + (i % columnes) * pas_x,
                             2 + AMPLE_FONS / 2 + (i // columnes) * pas_y)) for i in range(n)])


def dxf_mostra():
    ample_c, alt_c = 30.0, 22.0
    def cupo(x0, y0):
        m = x0 + ample_c / 2
        return [(x0, y0), (m - AMPLE_VORA / 2, y0), (m - AMPLE_FONS / 2, y0 + FONDARIA),
                (m + AMPLE_FONS / 2, y0 + FONDARIA), (m + AMPLE_VORA / 2, y0),
                (x0 + ample_c, y0), (x0 + ample_c, y0 + alt_c), (x0, y0 + alt_c)]
    pol = [("TALL", mou(cupo(3, 3), 0, 0)), ("TALL", mou(cupo(37, 3), 0, 0))]
    # 18 mm entre connectors (fan uns 15 mm): amb 16 mm, els talls quedaven a 0,4 mm i cremaven.
    pol += [("TALL", mou(eixampla(corbati(), k), 10 + i * 18, 38)) for i, k in enumerate((0.0, 0.1, 0.2, 0.3))]
    txt = [(10 + i * 18, -52, 3.2, k) for i, k in enumerate(("0,0", "0,1", "0,2", "0,3"))]
    txt.append((37, -58, 3, "MOSTRA DE CONNECTORS"))
    return dxf(pol, txt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tipus", choices=["rajola", "connectors", "mostra", "rusc"], default="rajola")
    ap.add_argument("--format", choices=["svg", "dxf"], default="svg",
                    help="dxf per importar directament a xTool Studio a mida real")
    ap.add_argument("--mida", type=float, default=100, help="mida de la rajola entre costats (mm)")
    ap.add_argument("--kerf", type=float, default=0.15, help="kerf a compensar als connectors (mm)")
    ap.add_argument("--n", type=int, default=24, help="nombre de connectors o de rajoles del rusc")
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()

    if a.format == "dxf":
        if a.tipus == "rusc":
            ap.error("el rusc és un esquema per mirar: només en SVG")
        contingut = {"rajola": lambda: dxf_rajola(a.mida),
                     "connectors": lambda: dxf_connectors(a.n, a.kerf),
                     "mostra": dxf_mostra}[a.tipus]()
        sortida = a.salida or f"{a.tipus}.dxf"
        with open(sortida, "w", encoding="ascii") as fh:
            fh.write(contingut)
        print(f"Creat: {sortida}  (tipus {a.tipus}, DXF en mm)")
        return
    if a.tipus == "rajola":
        contingut, nom = fitxer_rajola(a.mida), "rajola_hexagonal.svg"
    elif a.tipus == "connectors":
        contingut, nom = fitxer_connectors(a.n, a.kerf), "connectors.svg"
    elif a.tipus == "mostra":
        contingut, nom = fitxer_mostra(), "mostra_connectors.svg"
    else:
        contingut, nom = fitxer_rusc(a.n, a.mida), "rusc_esquema.svg"
    sortida = a.salida or nom
    with open(sortida, "w", encoding="utf-8") as fh:
        fh.write(contingut)
    print(f"Creat: {sortida}  (tipus {a.tipus})")


if __name__ == "__main__":
    main()
