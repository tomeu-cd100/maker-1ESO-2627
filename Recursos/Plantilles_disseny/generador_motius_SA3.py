#!/usr/bin/env python3
"""
Generador del banc de motius per a la rajola del rusc — Aula Maker (SA3).

Cada motiu és una silueta negra (GRAVAT) de 56 mm de diàmetre, la mida del cercle guia de
rajola_hexagonal_SA3.svg: s'importa a Inkscape i ja hi cap sense escalar.

Tot són polígons plens. Els forats (ulls, finestres…) són polígons amb el gir contrari i la
regla de farciment «nonzero»: així el fitxer és un sol camí net, sense formes blanques a sobre
(la làser grava el que és negre, i una forma blanca a sobre no esborra res).

ÚS:
    python generador_motius_SA3.py              # crea motius_SA3/*.svg + motius_SA3_galeria.svg

Nota: pensat amb finalitat educativa; els motius es publiquen amb la llicència del curs (CC BY-SA 4.0).
"""
import math
import os

MIDA_MM = 56.0        # diàmetre del cercle guia de la rajola
RADI_MAX = 48.0       # tot el motiu ha de cabre dins d'aquest radi (espai de dibuix 0-100)


# ---------- Primitives: cada una retorna un polígon (llista de punts) ----------

def orienta(pts, forat=False):
    """Gir positiu per a les formes plenes i negatiu per als forats."""
    area = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
               for i in range(len(pts)))
    if (area > 0) == forat:
        pts = pts[::-1]
    return pts


def poly(pts, forat=False):
    return orienta(list(pts), forat)


def el_lipse(cx, cy, rx, ry, rot=0, forat=False, n=64):
    a = math.radians(rot)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x, y = rx * math.cos(t), ry * math.sin(t)
        pts.append((cx + x * math.cos(a) - y * math.sin(a), cy + x * math.sin(a) + y * math.cos(a)))
    return orienta(pts, forat)


def cercle(cx, cy, r, forat=False):
    return el_lipse(cx, cy, r, r, forat=forat)


def rect(x, y, w, h, forat=False):
    return poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], forat)


def rect_arrodonit(x, y, w, h, r, forat=False):
    pts = []
    for cx, cy, a0 in ((x + w - r, y + r, -90), (x + w - r, y + h - r, 0),
                       (x + r, y + h - r, 90), (x + r, y + r, 180)):
        for i in range(9):
            a = math.radians(a0 + 90 * i / 8)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return orienta(pts, forat)


def barra(x1, y1, x2, y2, w, forat=False):
    """Rectangle de gruix w entre dos punts (una «línia» gruixuda)."""
    l = math.hypot(x2 - x1, y2 - y1)
    nx, ny = -(y2 - y1) / l * w / 2, (x2 - x1) / l * w / 2
    return poly([(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)], forat)


def arc_gruixut(cx, cy, r_ext, r_int, a0, a1, forat=False, n=32):
    """Tros d'anell entre els angles a0 i a1 (graus; y cap avall, 90° = a baix)."""
    ext = [(cx + r_ext * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
            cy + r_ext * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
    int_ = [(cx + r_int * math.cos(math.radians(a1 - (a1 - a0) * i / n)),
             cy + r_int * math.sin(math.radians(a1 - (a1 - a0) * i / n))) for i in range(n + 1)]
    return orienta(ext + int_, forat)


def estrella_pts(cx, cy, r_ext, r_int, puntes=5, gir=-90):
    return [(cx + (r_ext if i % 2 == 0 else r_int) * math.cos(math.radians(gir + 180 * i / puntes)),
             cy + (r_ext if i % 2 == 0 else r_int) * math.sin(math.radians(gir + 180 * i / puntes)))
            for i in range(2 * puntes)]


def creu(cx, cy, braç, mig, forat=False):
    """Creu (signe +): braç = llargada des del centre, mig = mig gruix."""
    return poly([(cx - mig, cy - braç), (cx + mig, cy - braç), (cx + mig, cy - mig), (cx + braç, cy - mig),
                 (cx + braç, cy + mig), (cx + mig, cy + mig), (cx + mig, cy + braç), (cx - mig, cy + braç),
                 (cx - mig, cy + mig), (cx - braç, cy + mig), (cx - braç, cy - mig), (cx - mig, cy - mig)], forat)


# ---------- Els motius (espai de dibuix 0-100, centre 50,50) ----------

def futbol():
    pent = estrella_pts(50, 50, 14, 14 * math.cos(math.radians(36)), 5)[::2]
    s = [cercle(50, 50, 44), cercle(50, 50, 39, forat=True), poly(pent)]
    for x, y in pent:
        a = math.degrees(math.atan2(y - 50, x - 50))
        # pentàgon petit a la vora, enganxat a l'anella, i la costura que el lliga al central
        px, py = 50 + 34 * math.cos(math.radians(a)), 50 + 34 * math.sin(math.radians(a))
        s.append(poly(estrella_pts(px, py, 8, 8 * math.cos(math.radians(36)), 5, gir=a)[::2]))
        s.append(barra(x, y, 50 + 27 * math.cos(math.radians(a)), 50 + 27 * math.sin(math.radians(a)), 3.5))
        # costura fins al pentàgon de la vora següent (tanca els hexàgons blancs)
        qx, qy = 50 + 34 * math.cos(math.radians(a + 72)), 50 + 34 * math.sin(math.radians(a + 72))
        s.append(barra(px, py, qx, qy, 3.5))
    return s


def bicicleta():
    s = [cercle(25, 62, 17), cercle(25, 62, 12, forat=True), cercle(75, 62, 17), cercle(75, 62, 12, forat=True)]
    for a, b in (((25, 62), (48, 62)), ((48, 62), (40, 34)), ((40, 34), (25, 62)), ((48, 62), (68, 38)),
                 ((40, 38), (68, 38)), ((68, 38), (75, 62)), ((66, 38), (64, 28))):
        s.append(barra(*a, *b, 4.5))
    s += [barra(33, 32, 47, 32, 5), barra(60, 28, 72, 28, 5)]
    return s


def nota_musical():
    return [el_lipse(30, 74, 11, 8, -20), el_lipse(66, 66, 11, 8, -20),
            barra(39.5, 72, 39.5, 26, 5), barra(75.5, 64, 75.5, 18, 5),
            poly([(37, 24), (78, 15), (78, 25), (37, 34)])]


def comandament():
    s = [rect_arrodonit(10, 30, 80, 42, 20), creu(30, 51, 10, 3.5, forat=True)]
    s += [cercle(x, y, 4.5, forat=True) for x, y in ((70, 42), (79, 51), (70, 60), (61, 51))]
    return s


def llibre():
    s = [poly([(12, 30), (47, 36), (47, 78), (12, 72)]), poly([(53, 36), (88, 30), (88, 72), (53, 78)])]
    for k in range(3):
        s.append(barra(19, 42 + 10 * k, 41, 46 + 10 * k, 3, forat=True))
        s.append(barra(59, 46 + 10 * k, 81, 42 + 10 * k, 3, forat=True))
    return s


def paleta():
    s = [el_lipse(50, 52, 42, 34), cercle(66, 70, 7, forat=True)]
    s += [cercle(x, y, 6, forat=True) for x, y in ((28, 44), (44, 30), (63, 32), (30, 64))]
    return s


def camera():
    return [rect_arrodonit(14, 34, 72, 42, 8), rect(32, 26, 22, 10),
            cercle(50, 55, 16, forat=True), cercle(50, 55, 11), cercle(50, 55, 5, forat=True),
            rect(70, 39, 10, 6, forat=True)]


def gat():
    return [cercle(50, 58, 30), poly([(24, 44), (28, 12), (46, 30)]), poly([(76, 44), (72, 12), (54, 30)]),
            el_lipse(39, 54, 4.5, 6.5, forat=True), el_lipse(61, 54, 4.5, 6.5, forat=True),
            poly([(45, 65), (55, 65), (50, 71)], forat=True)]


def pota():
    return [el_lipse(50, 66, 21, 17), el_lipse(25, 42, 8, 11, -20), el_lipse(42, 27, 8, 11),
            el_lipse(58, 27, 8, 11), el_lipse(75, 42, 8, 11, 20)]


def peix():
    return [el_lipse(44, 50, 30, 19), poly([(66, 50), (90, 30), (90, 70)]),
            cercle(28, 46, 4, forat=True), barra(42, 38, 42, 62, 3, forat=True)]


def cor():
    pts = []
    for i in range(120):
        t = 2 * math.pi * i / 120
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((50 + 2.6 * x, 48 - 2.6 * y))
    return [poly(pts)]


def estrella():
    return [poly(estrella_pts(50, 53, 44, 18))]


def llamp():
    return [poly([(58, 6), (24, 54), (46, 54), (36, 94), (76, 40), (54, 40), (66, 6)])]


def somriure():
    return [cercle(50, 50, 42), el_lipse(36, 38, 5, 8, forat=True), el_lipse(64, 38, 5, 8, forat=True),
            arc_gruixut(50, 50, 28, 20, 20, 160, forat=True)]


def sol():
    s = [cercle(50, 50, 22)]
    for k in range(8):
        a = 45 * k
        s.append(poly([(50 + 28 * math.cos(math.radians(a - 11)), 50 + 28 * math.sin(math.radians(a - 11))),
                       (50 + 46 * math.cos(math.radians(a)), 50 + 46 * math.sin(math.radians(a))),
                       (50 + 28 * math.cos(math.radians(a + 11)), 50 + 28 * math.sin(math.radians(a + 11)))]))
    return s


def lluna():
    """Lluna creixent: cercle gran menys un cercle desplaçat (calculat com un sol polígon)."""
    R, (cx, cy), r = 40, (64, 40), 34
    d = math.hypot(cx - 50, cy - 50)
    dir_ = math.degrees(math.atan2(cy - 50, cx - 50))
    th = math.degrees(math.acos((R * R + d * d - r * r) / (2 * R * d)))
    ph = math.degrees(math.acos((r * r + d * d - R * R) / (2 * r * d)))
    ext = [(50 + R * math.cos(math.radians(a)), 50 + R * math.sin(math.radians(a)))
           for a in [dir_ + th + (360 - 2 * th) * i / 60 for i in range(61)]]
    int_ = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
            for a in [dir_ + 180 + ph - 2 * ph * i / 60 for i in range(61)]]
    if math.dist(ext[-1], int_[0]) > math.dist(ext[-1], int_[-1]):
        int_ = int_[::-1]
    return [poly(ext + int_)]


def muntanya():
    return [poly([(12, 76), (42, 18), (74, 76)]), poly([(50, 76), (68, 44), (88, 76)]),
            poly([(36, 35), (40, 40), (44, 35), (49, 40), (49, 43.5), (44, 38.5), (40, 43.5), (36, 38.5)], forat=True)]


def pi_():
    return [poly([(50, 8), (28, 38), (72, 38)]), poly([(50, 22), (22, 58), (78, 58)]),
            poly([(50, 40), (16, 80), (84, 80)]), rect(43, 78, 14, 14)]


def flor():
    s = [cercle(50 + 28 * math.cos(math.radians(60 * k)), 50 + 28 * math.sin(math.radians(60 * k)), 15)
         for k in range(6)]
    return s + [cercle(50, 50, 11), cercle(50, 50, 5, forat=True)]


def onades():
    s = []
    for y0 in (38, 62):
        dalt = [(x, y0 + 8 * math.sin(2 * math.pi * (x - 10) / 40)) for x in range(10, 91, 2)]
        baix = [(x, y + 9) for x, y in dalt[::-1]]
        s.append(poly(dalt + baix))
    return s


def coet():
    return [poly([(50, 8), (58, 16), (63, 28), (64, 66), (36, 66), (37, 28), (42, 16)]),
            cercle(50, 38, 7, forat=True),
            poly([(37, 46), (22, 72), (37, 66)]), poly([(63, 46), (78, 72), (63, 66)]),
            poly([(42, 70), (58, 70), (50, 90)])]


def xef():
    return [cercle(32, 38, 15), cercle(50, 30, 17), cercle(68, 38, 15), rect(32, 38, 36, 28),
            rect(30, 70, 40, 12)]


def metge():
    return [cercle(50, 50, 42), creu(50, 50, 28, 9, forat=True)]


def engranatge():
    pts, dents = [], 10
    for k in range(dents):
        a = 360 / dents * k
        for da, r in ((-13, 34), (-8, 43), (8, 43), (13, 34)):
            pts.append((50 + r * math.cos(math.radians(a + da)), 50 + r * math.sin(math.radians(a + da))))
    return [poly(pts), cercle(50, 50, 13, forat=True)]


def matras():
    return [poly([(42, 12), (58, 12), (58, 36), (80, 82), (20, 82), (42, 36)]), rect(37, 8, 26, 6),
            poly([(34, 56), (66, 56), (68, 60), (32, 60)], forat=True),
            cercle(44, 70, 3.5, forat=True), cercle(57, 67, 2.5, forat=True)]


def codi():
    return [barra(34, 28, 14, 50, 7), barra(14, 50, 34, 72, 7), barra(66, 28, 86, 50, 7),
            barra(86, 50, 66, 72, 7), barra(58, 22, 42, 78, 7)]


# (fitxer, nom visible, categoria, funció)
MOTIUS = [
    ("futbol", "Pilota", "Esport i joc", futbol),
    ("bicicleta", "Bicicleta", "Esport i joc", bicicleta),
    ("comandament", "Videojocs", "Esport i joc", comandament),
    ("nota_musical", "Música", "Art i cultura", nota_musical),
    ("paleta", "Pintura", "Art i cultura", paleta),
    ("camera", "Fotografia", "Art i cultura", camera),
    ("llibre", "Llibres", "Art i cultura", llibre),
    ("gat", "Gat", "Animals", gat),
    ("pota", "Gossos i mascotes", "Animals", pota),
    ("peix", "Peix / mar", "Animals", peix),
    ("sol", "Sol", "Natura", sol),
    ("lluna", "Lluna", "Natura", lluna),
    ("muntanya", "Muntanya", "Natura", muntanya),
    ("pi", "Bosc", "Natura", pi_),
    ("flor", "Flor", "Natura", flor),
    ("onades", "Mar / platja", "Natura", onades),
    ("cor", "Cor", "Com sóc", cor),
    ("estrella", "Estrella", "Com sóc", estrella),
    ("llamp", "Llamp / energia", "Com sóc", llamp),
    ("somriure", "Somriure", "Com sóc", somriure),
    ("coet", "Espai", "Què vull ser", coet),
    ("xef", "Cuina", "Què vull ser", xef),
    ("metge", "Salut", "Què vull ser", metge),
    ("engranatge", "Enginyeria", "Què vull ser", engranatge),
    ("matras", "Ciència", "Què vull ser", matras),
    ("codi", "Programació", "Què vull ser", codi),
]


def cami(poligons, escala=1.0, dx=0.0, dy=0.0):
    return " ".join("M " + " L ".join(f"{dx + x * escala:.2f},{dy + y * escala:.2f}" for x, y in p) + " Z"
                    for p in poligons)


def comprova(nom, poligons):
    r = max(math.dist((x, y), (50, 50)) for p in poligons for x, y in p)
    if r > RADI_MAX:
        print(f"  ⚠️  {nom}: arriba a radi {r:.1f} (> {RADI_MAX}): no cap al cercle")


def main():
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "motius_SA3")
    os.makedirs(carpeta, exist_ok=True)
    e = MIDA_MM / 100
    for fitxer, nom, categoria, f in MOTIUS:
        p = f()
        comprova(fitxer, p)
        with open(os.path.join(carpeta, f"{fitxer}.svg"), "w", encoding="utf-8") as fh:
            fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n'
                     f'<!-- Motiu «{nom}» ({categoria}) per a la rajola del rusc SA3. GRAVAT = negre. '
                     f'Diàmetre {MIDA_MM:g} mm: cap al cercle guia sense escalar. Aula Maker, CC BY-SA 4.0. -->\n'
                     f'<svg xmlns="http://www.w3.org/2000/svg" width="{MIDA_MM:g}mm" height="{MIDA_MM:g}mm" '
                     f'viewBox="0 0 {MIDA_MM:g} {MIDA_MM:g}">\n'
                     f'  <path id="{fitxer}" fill="#000000" fill-rule="nonzero" d="{cami(p, e)}"/>\n</svg>\n')

    # Galeria: 6 columnes, cada motiu dins del seu cercle guia, amb el nom a sota.
    col, cel_w, cel_h = 6, 70, 84
    files = math.ceil(len(MOTIUS) / col)
    cos = ""
    for i, (fitxer, nom, _, f) in enumerate(MOTIUS):
        x0, y0 = (i % col) * cel_w + 7, (i // col) * cel_h + 6
        cos += (f'  <circle cx="{x0 + 28}" cy="{y0 + 28}" r="28" fill="none" stroke="#3366FF" '
                f'stroke-width="0.4" stroke-dasharray="2,1.5"/>\n'
                f'  <path fill="#000000" d="{cami(f(), e, x0, y0)}"/>\n'
                f'  <text x="{x0 + 28}" y="{y0 + 67}" font-family="sans-serif" font-size="5.5" '
                f'text-anchor="middle" fill="#222222">{nom}</text>\n'
                f'  <text x="{x0 + 28}" y="{y0 + 74}" font-family="monospace" font-size="3.6" '
                f'text-anchor="middle" fill="#666666">{fitxer}.svg</text>\n')
    with open(os.path.join(os.path.dirname(carpeta), "motius_SA3_galeria.svg"), "w", encoding="utf-8") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?>\n'
                 f'<!-- Galeria del banc de motius SA3 (només per mirar). Generat per generador_motius_SA3.py. -->\n'
                 f'<svg xmlns="http://www.w3.org/2000/svg" width="{col * cel_w}mm" height="{files * cel_h}mm" '
                 f'viewBox="0 0 {col * cel_w} {files * cel_h}">\n'
                 f'  <rect width="100%" height="100%" fill="#ffffff"/>\n{cos}</svg>\n')
    print(f"Creats: {len(MOTIUS)} motius a {carpeta} + motius_SA3_galeria.svg")


if __name__ == "__main__":
    main()
