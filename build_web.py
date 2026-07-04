#!/usr/bin/env python3
"""Generador de la web estàtica de l'Aula Maker.

Converteix tots els .md del repositori a HTML dins de `web/`, amb una plantilla
compartida, enllaços interns reescrits (també les referències en `codi`) i
portades per a docents i alumnat.

Ús:  python build_web.py     (regenera web/ sencera)
Requereix: pip install markdown
"""

import html
import re
import shutil
import unicodedata
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
OUT = ROOT / "web"

SECTIONS = [
    "Programació didàctica",
    "Classes",
    "Avaluació",
    "Normativa",
    "Reptes",
    "Simulacions",
    "Memòria de treball",
    "Recursos",
]

SECTION_ICONS = {
    "Programació didàctica": "📚",
    "Classes": "🧩",
    "Avaluació": "📊",
    "Normativa": "🛡️",
    "Reptes": "🏅",
    "Simulacions": "💻",
    "Memòria de treball": "🗂️",
    "Recursos": "🧰",
}

SA_CARDS = [
    ("SA0", "Punt de partida", "setm. 1", "📍 Benvinguda, seguretat i avaluació 0", "SA0_Punt_de_partida"),
    ("SA1", "Benvinguts a l'Aula Maker", "1r trim.", "🔑 Clauer gravat a làser", "SA1_Benvinguts_Aula_Maker"),
    ("SA2", "Dissenyem en 2D", "1r trim.", "📐 Marcapàgines o etiqueta", "SA2_Dissenyem_en_2D"),
    ("SA3", "Projecte làser: la meva identitat", "1r trim. ⭐", "🪵 Objecte d'identitat amb encaixos", "SA3_Projecte_laser_identitat"),
    ("SA4", "Del 2D al 3D", "2n trim.", "🧊 Figura o clauer 3D", "SA4_Del_2D_al_3D"),
    ("SA5", "Modelatge 3D funcional", "2n trim.", "🔧 Peça útil impresa", "SA5_Modelatge_3D_funcional"),
    ("SA6", "Repte de disseny 3D", "2n trim. ⭐", "🤝 Solució per a un usuari real", "SA6_Repte_disseny_3D"),
    ("SA7", "Captura el món en 360", "3r trim.", "🌐 Tour virtual del centre", "SA7_Captura_360"),
    ("SA8", "Explorem la Realitat Virtual", "3r trim.", "🥽 Escena VR interactiva", "SA8_Explorem_la_VR"),
    ("SA9", "Projecte final Aula Maker", "3r trim. ⭐", "🎪 Estand a la Fira Aula Maker", "SA9_Projecte_final"),
]

ALUMNAT_LINKS = [
    ("📖", "Vocabulari bàsic del curs", "Classes/SA0_Punt_de_partida/Vocabulari_basic.md", "Totes les paraules maker, explicades curt i clar"),
    ("📔", "El diari de taller", "Avaluació/Diari_de_taller.md", "La teva llibreta maker: una entrada per sessió"),
    ("🔍", "Com m'avaluaran?", "Avaluació/Avaluacio_explicada_alumnat.md", "Tot el sistema d'avaluació explicat en una pàgina"),
    ("🌱", "Rúbrica amigable", "Avaluació/Rubrica_alumnat_amigable.md", "Els nivells 🌱🙂💪🌟 en primera persona"),
    ("🛠️", "Passaport maker", "Reptes/Passaport_maker.md", "Carnets, insígnies i segells: tot el joc en un paper"),
    ("🏅", "Reptes express", "Reptes/Index_reptes.md", "Reptes curts 2D, 3D i immersius amb insígnies"),
    ("🚀", "El meu objecte del curs", "Reptes/Projecte_personal.md", "El projecte personal que creix tot l'any"),
    ("🛡️", "Normes de seguretat", "Normativa/Normes_seguretat_taller.md", "Lectura obligatòria abans de tocar màquines"),
    ("🥽", "Protocol d'ús de la VR", "Normativa/Protocol_us_VR.md", "Temps, higiene i seguretat amb les ulleres"),
    ("🧭", "Les 5 Grans Idees", "Programació didàctica/Grans_idees_maker.md", "El que quedarà quan oblidis els menús d'Inkscape"),
    ("🏛️", "El Museu dels Errors", "Programació didàctica/Museu_dels_errors.md", "Aquí els errors valen punts si n'aprenem"),
]

DOCENT_DESTACATS = [
    ("🚀", "Guia d'inici docent", "00_Guia_inici_docent.md", "Per on començar: la posada en marxa completa"),
    ("🗺️", "Guió del curs, sessió a sessió", "00_Guio_del_curs_docent.md", "Les 35 setmanes: què preparar, què fer i què registrar"),
    ("📅", "Diari de classe, dia a dia", "00_Diari_de_classe_docent.md", "Cada sessió al detall: minutatge, estacions, checklist i punt crític"),
    ("👥", "Guia del co-docent", "00_Guia_inici_codocent.md", "Una pàgina per al company de desdoblament"),
    ("🤝", "Codocència i desdoblament", "Programació didàctica/Codocencia_desdoblament.md", "Rotació, estacions i repartiment d'avaluació"),
    ("⏱️", "Gestió del temps-màquina", "Programació didàctica/Gestio_temps_maquina_fabricacio.md", "Batch, cua, paral·lel: el coll d'ampolla resolt"),
    ("🗓️", "Temporització anual", "Programació didàctica/Temporitzacio_anual.md", "Setmana a setmana, amb contingències"),
    ("📊", "Criteris i qualificació", "Avaluació/Criteris_i_qualificacio.md", "El mapa operatiu de l'avaluació"),
]

MD = markdown.Markdown(extensions=["tables", "sane_lists", "fenced_code"])


def slugify(name: str) -> str:
    """converteix «Programació didàctica» en «programacio-didactica»"""
    base = unicodedata.normalize("NFKD", name)
    base = "".join(c for c in base if not unicodedata.combining(c))
    base = base.lower().replace(" ", "-")
    base = re.sub(r"[^a-z0-9._/-]", "", base)
    return base


def collect_md_files():
    files = []
    for p in sorted(ROOT.glob("*.md")):
        files.append(p)
    for section in SECTIONS:
        d = ROOT / section
        if d.is_dir():
            files.extend(sorted(d.rglob("*.md")))
    return files


def out_path_for(md_path: Path) -> str:
    rel = md_path.relative_to(ROOT)
    return slugify(str(rel.with_suffix(".html")).replace("\\", "/"))


def page_title(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


# ── mapes globals ──────────────────────────────────────────────────────────
MD_FILES = collect_md_files()
PATH_MAP = {}  # «Avaluació/Diari_de_taller.md» (tal com s'escriu als docs) → html
for p in MD_FILES:
    rel = str(p.relative_to(ROOT)).replace("\\", "/")
    PATH_MAP[rel] = out_path_for(p)
    PATH_MAP[rel.replace(" ", "%20")] = out_path_for(p)
NAME_MAP = {}  # nom sol («Diari_de_taller.md») → llista de rutes
for rel in list(PATH_MAP):
    if "%20" in rel:
        continue
    NAME_MAP.setdefault(rel.rsplit("/", 1)[-1], []).append(rel)

FOLDER_MAP = {f"{s}/": slugify(s) + "/index.html" for s in SECTIONS}
FOLDER_MAP.update({f"{s.replace(' ', '%20')}/": v for s, v in
                   [(s, slugify(s) + "/index.html") for s in SECTIONS]})
FOLDER_MAP["web/"] = "index.html"  # el README enllaça la web des de dins la web


def resolve_ref(ref: str, current_rel_dir: str) -> str | None:
    """Torna la ruta html (des de l'arrel de web/) d'una referència .md, o None."""
    ref = ref.strip().lstrip("./")
    if ref in PATH_MAP:
        return PATH_MAP[ref]
    if current_rel_dir:
        candidate = f"{current_rel_dir}/{ref}"
        if candidate in PATH_MAP:
            return PATH_MAP[candidate]
    name = ref.rsplit("/", 1)[-1]
    hits = NAME_MAP.get(name, [])
    if len(hits) == 1:
        return PATH_MAP[hits[0]]
    # noms repetits (Fitxa_alumnat.md…): prioritza la carpeta actual
    for h in hits:
        if current_rel_dir and h.startswith(current_rel_dir + "/"):
            return PATH_MAP[h]
    return None


def rel_prefix(out_rel: str) -> str:
    depth = out_rel.count("/")
    return "../" * depth


def rewrite_links(html_text: str, out_rel: str, current_rel_dir: str) -> str:
    prefix = rel_prefix(out_rel)

    # 1) enllaços markdown reals cap a .md o carpetes
    def fix_href(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        target = None
        if href.rstrip("/") + "/" in FOLDER_MAP or href in FOLDER_MAP:
            target = FOLDER_MAP.get(href, FOLDER_MAP.get(href.rstrip("/") + "/"))
        elif href.endswith(".md"):
            target = resolve_ref(href.replace("%20", " "), current_rel_dir)
        elif href.endswith((".svg", ".py")):
            asset = href.replace("%20", " ")
            cand = asset if (ROOT / asset).exists() else f"{current_rel_dir}/{asset}"
            if (ROOT / cand).exists():
                target = slugify(cand)
        elif href.endswith(".xlsx"):
            # les plantilles xlsx es copien a web/impressos/ amb el nom original
            target = "impressos/" + href.rsplit("/", 1)[-1]
        if target:
            return f'href="{prefix}{target}"'
        return m.group(0)

    html_text = re.sub(r'href="([^"]+)"', fix_href, html_text)

    # 2) referències dins de <code>…</code> (l'estil dominant del material)
    def fix_code(m):
        inner = m.group(1)
        clean = html.unescape(inner)
        base = re.split(r"\s*§", clean)[0].strip().rstrip("`").strip()
        target = None
        if base.endswith(".md"):
            target = resolve_ref(base, current_rel_dir)
        elif base in FOLDER_MAP:
            target = FOLDER_MAP[base]
        if target:
            return f'<a class="doclink" href="{prefix}{target}"><code>{inner}</code></a>'
        return m.group(0)

    html_text = re.sub(r"<code>([^<]+)</code>", fix_code, html_text)
    return html_text


def checkboxify(html_text: str) -> str:
    html_text = re.sub(r"<li>\[ \]", '<li class="task">☐', html_text)
    html_text = re.sub(r"<li>\[x\]", '<li class="task done">☑', html_text, flags=re.I)
    html_text = re.sub(r"<p>\[ \]", '<p class="task">☐', html_text)
    return html_text


def render_page(title: str, body: str, out_rel: str, crumb: list[tuple[str, str | None]]) -> str:
    prefix = rel_prefix(out_rel)
    crumb_html = " <span class=\"sep\">›</span> ".join(
        f'<a href="{prefix}{href}">{html.escape(text)}</a>' if href else f"<span>{html.escape(text)}</span>"
        for text, href in crumb
    )
    return f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · Aula Maker 1r ESO</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🛠️</text></svg>">
</head>
<body>
<header class="site-header">
  <a class="brand" href="{prefix}index.html">🛠️ <strong>Aula Maker</strong> <span>1r ESO</span></a>
  <nav>
    <a href="{prefix}index.html">Inici</a>
    <a href="{prefix}sa.html">Les 9 SA</a>
    <a href="{prefix}docent.html">Docent</a>
    <a href="{prefix}alumnat.html">Alumnat</a>
    <a href="{prefix}families.html">Famílies</a>
    <a href="{prefix}cerca.html" title="Cerca">🔍</a>
    <button id="theme" title="Canvia el tema" aria-label="Canvia el tema">🌗</button>
  </nav>
</header>
<div class="crumb">{crumb_html}</div>
<main class="content">
{body}
</main>
<footer class="site-footer">
  <p>«Aula Maker» · optativa de 1r d'ESO · curs 2026-2027 · material sota
  <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ca">CC BY-SA 4.0</a></p>
</footer>
<script>
const t=document.getElementById('theme');
const saved=localStorage.getItem('theme');
if(saved)document.documentElement.dataset.theme=saved;
t.onclick=()=>{{const d=document.documentElement.dataset;
d.theme=(d.theme==='dark')?'light':'dark';localStorage.setItem('theme',d.theme);}};
</script>
</body>
</html>
"""


SEARCH_INDEX = []  # {t: títol, u: url, s: secció, x: text pla}


def build_doc_pages():
    pages = {}  # rel md → (title, out_rel)
    for p in MD_FILES:
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        out_rel = PATH_MAP[rel]
        text = p.read_text(encoding="utf-8")
        title = page_title(text, p.stem.replace("_", " "))
        MD.reset()
        body = MD.convert(text)
        current_dir = rel.rsplit("/", 1)[0] if "/" in rel else ""
        body = rewrite_links(body, out_rel, current_dir)
        body = checkboxify(body)
        body = f'<article class="doc">{body}</article>'
        crumb = [("Inici", "index.html")]
        if "/" in rel:
            section = rel.split("/")[0]
            crumb.append((section, slugify(section) + "/index.html"))
            if rel.count("/") > 1:  # subcarpeta (SA de Classes)
                crumb.append((rel.split("/")[1].replace("_", " "), None))
        crumb.append((title if len(title) < 60 else title[:57] + "…", None))
        out = OUT / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(title, body, out_rel, crumb), encoding="utf-8")
        pages[rel] = (title, out_rel)
        plain = re.sub(r"<[^>]+>", " ", body)
        plain = re.sub(r"\s+", " ", html.unescape(plain)).strip()
        SEARCH_INDEX.append({
            "t": title, "u": out_rel,
            "s": rel.split("/")[0] if "/" in rel else "Inici",
            "x": plain[:4000],
        })
    return pages


def card(href: str, icon: str, title: str, desc: str, badge: str = "") -> str:
    b = f'<span class="badge">{badge}</span>' if badge else ""
    return (f'<a class="card" href="{href}"><div class="card-icon">{icon}</div>'
            f'<div><h3>{html.escape(title)} {b}</h3><p>{html.escape(desc)}</p></div></a>')


def build_section_indexes(pages):
    for section in SECTIONS:
        entries = [(rel, t) for rel, (t, _o) in pages.items()
                   if rel.startswith(section + "/")]
        if not entries:
            continue
        out_rel = slugify(section) + "/index.html"
        icon = SECTION_ICONS.get(section, "📄")
        if section == "Classes":
            body = [f"<h1>{icon} El curs, SA a SA (SA0 + les 9 SA)</h1>"]
            for code, name, trim, product, folder in SA_CARDS:
                docs = [(rel, t) for rel, t in entries if f"/{folder}/" in "/" + rel]
                links = []
                for rel, t in docs:
                    label = {"SA": "📖 La SA completa", "Fi": "✏️ Fitxa de l'alumnat",
                             "Ru": "📊 Rúbrica", "Ex": "🌟 Exemple resolt"}.get(
                        rel.rsplit("/", 1)[-1][:2], t)
                    links.append(f'<a href="../{pages[rel][1]}">{label}</a>')
                body.append(
                    f'<section class="sa-block"><h2>{code} — {html.escape(name)} '
                    f'<span class="badge">{trim}</span></h2>'
                    f'<p class="product">{html.escape(product)}</p>'
                    f'<div class="linkrow">{" · ".join(links)}</div></section>')
            body_html = "\n".join(body)
        else:
            items = "\n".join(
                f'<a class="card" href="../{pages[rel][1]}"><div class="card-icon">{icon}</div>'
                f'<div><h3>{html.escape(t)}</h3><p>{html.escape(rel.rsplit("/", 1)[-1])}</p></div></a>'
                for rel, t in entries)
            body_html = f"<h1>{icon} {html.escape(section)}</h1>\n<div class='grid'>{items}</div>"
        (OUT / out_rel).parent.mkdir(parents=True, exist_ok=True)
        (OUT / out_rel).write_text(
            render_page(section, body_html, out_rel,
                        [("Inici", "index.html"), (section, None)]),
            encoding="utf-8")


def build_home(pages):
    sa_grid = "\n".join(
        f'<a class="card sa" href="classes/{slugify(folder)}/{slugify(code)}.html">'
        f'<div class="card-icon">{product.split()[0]}</div>'
        f'<div><h3>{code} · {html.escape(name)} <span class="badge">{trim}</span></h3>'
        f'<p>{html.escape(product.split(" ", 1)[1])}</p></div></a>'
        for code, name, trim, product, folder in SA_CARDS)
    body = f"""
<section class="hero">
  <h1>🛠️ Aula Maker</h1>
  <p class="tagline">Optativa de 1r d'ESO · imaginar, dissenyar i <strong>fabricar de veritat</strong>:
  talladora làser, impressió 3D, càmera 360 i realitat virtual.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="docent.html">👩‍🏫 Soc docent</a>
    <a class="btn" href="alumnat.html">🧑‍🎓 Soc alumne/a</a>
    <a class="btn" href="families.html">👨‍👩‍👧 Soc família</a>
  </div>
</section>
<section>
  <h2>El curs, SA a SA</h2>
  <div class="grid">{sa_grid}</div>
</section>
<section>
  <h2>Les 5 Grans Idees del curs</h2>
  <div class="ideas">
    <span>1️⃣ El material mana</span><span>2️⃣ Petit i acabat guanya gran i a mitges</span>
    <span>3️⃣ Mesura dues vegades, fabrica una</span><span>4️⃣ L'error és informació</span>
    <span>5️⃣ Dissenyem per a algú</span>
  </div>
  <p><a class="doclink" href="programacio-didactica/grans_idees_maker.html">→ Què volen dir i on es veuen</a></p>
</section>
"""
    (OUT / "index.html").write_text(
        render_page("Inici", body, "index.html", [("Inici", None)]), encoding="utf-8")

    # Alumnat
    cards = "\n".join(card(PATH_MAP[rel], icon, t, d) for icon, t, rel, d in ALUMNAT_LINKS)
    fitxes = "\n".join(
        f'<a class="chip" href="classes/{slugify(folder)}/fitxa_alumnat.html">{code}</a>'
        for code, _n, _t, _p, folder in SA_CARDS)
    body = f"""
<h1>🧑‍🎓 Per a l'alumnat</h1>
<p class="lead">Tot el que fas servir tu: les fitxes de cada repte, com t'avaluaran
(sense sorpreses!) i el joc de carnets i insígnies.</p>
<h2>✏️ Les fitxes de cada SA</h2>
<div class="chips">{fitxes}</div>
<h2>Els teus documents</h2>
<div class="grid">{cards}</div>
"""
    (OUT / "alumnat.html").write_text(
        render_page("Alumnat", body, "alumnat.html",
                    [("Inici", "index.html"), ("Alumnat", None)]), encoding="utf-8")

    # Docent
    dest = "\n".join(card(PATH_MAP[rel], icon, t, d) for icon, t, rel, d in DOCENT_DESTACATS)
    sections = "\n".join(
        card(slugify(s) + "/index.html", SECTION_ICONS[s], s,
             {"Programació didàctica": "PD, temporització, temps-màquina, codocència, DUA…",
              "Classes": "Les 9 SA amb fitxa, rúbrica i exemple resolt",
              "Avaluació": "Criteris, rúbriques, full de progrés, instruments",
              "Normativa": "Seguretat, carnets, protocol VR, famílies",
              "Reptes": "Reptes express, passaport, projecte personal",
              "Simulacions": "Practicar sense material",
              "Memòria de treball": "Bitàcola, incidències, inventari, memòria",
              "Recursos": "Plantilles pròpies i enllaços validats"}[s])
        for s in SECTIONS)
    impresos = "\n".join([
        card("impressos/passaport.html", "🛠️", "Passaport maker",
             "A5 per alumne/a: carnets, insígnies i segells", "imprimible"),
        card("impressos/poster_grans_idees.html", "🧭", "Pòster de les 5 Grans Idees",
             "A4/A3 per penjar a les dues aules", "imprimible"),
        card("impressos/targetes_museu.html", "🏛️", "Targetes del Museu dels Errors",
             "4 per full, per deixar al costat del museu", "imprimible"),
        card("impressos/Quadern_digital_docent_plantilla.xlsx", "📊",
             "Plantilla del quadern digital", "Full de càlcul buit: pugeu-lo al Drive de centre",
             "xlsx"),
    ])
    body = f"""
<h1>👩‍🏫 Per al professorat</h1>
<p class="lead">El material complet de l'optativa: comença per la guia d'inici i tingues
sempre a mà la gestió del temps-màquina — és el que fa que tot rutlli.</p>
<h2>Imprescindibles</h2>
<div class="grid">{dest}</div>
<h2>🖨️ Impressos i plantilles</h2>
<div class="grid">{impresos}</div>
<h2>Tot el material, per carpetes</h2>
<div class="grid">{sections}</div>
"""
    (OUT / "docent.html").write_text(
        render_page("Docent", body, "docent.html",
                    [("Inici", "index.html"), ("Docent", None)]), encoding="utf-8")

    # SA (accés directe)
    shutil.copyfile(OUT / "classes/index.html", OUT / "sa.html")
    # arregla les rutes relatives del sa.html copiat (era dins classes/)
    sa_html = (OUT / "sa.html").read_text(encoding="utf-8")
    sa_html = sa_html.replace('href="../', 'href="').replace('src="../', 'src="')
    (OUT / "sa.html").write_text(sa_html, encoding="utf-8")

    # Famílies
    fam_cards = "\n".join([
        card(PATH_MAP["Normativa/Carta_families_inici_curs.md"], "✉️",
             "Carta d'inici de curs", "Què farà el vostre fill/a a l'Aula Maker"),
        card(PATH_MAP["Avaluació/Avaluacio_explicada_alumnat.md"], "🔍",
             "Com s'avalua l'optativa", "El sistema d'avaluació explicat en una pàgina"),
        card(PATH_MAP["Normativa/Autoritzacio_families_VR_360.md"], "📝",
             "Autorització VR i drets d'imatge", "El document que us demanarem signat"),
        card(PATH_MAP["Normativa/Protocol_us_VR.md"], "🥽",
             "Protocol d'ús de la realitat virtual", "Salut, temps d'ús i seguretat amb les ulleres"),
        card(PATH_MAP["Normativa/Normes_seguretat_taller.md"], "🛡️",
             "Normes de seguretat del taller", "Com treballem amb les màquines"),
    ])
    body = f"""
<h1>👨‍👩‍👧 Per a les famílies</h1>
<p class="lead">A l'Aula Maker el vostre fill/a <strong>dissenya i fabrica objectes reals</strong>
(talladora làser, impressió 3D) i crea contingut immersiu (360/VR), treballant en equip i amb
la seguretat com a norma número u. Aquí teniu els documents que us afecten directament.</p>
<div class="grid">{fam_cards}</div>
<blockquote><p>💡 Al final de curs, la <strong>Fira Aula Maker</strong> és oberta a les famílies:
hi veureu els projectes i hi podreu provar les experiències que han creat. Us hi esperem!</p></blockquote>
"""
    (OUT / "families.html").write_text(
        render_page("Famílies", body, "families.html",
                    [("Inici", "index.html"), ("Famílies", None)]), encoding="utf-8")

    # Cerca
    import json
    (OUT / "assets" / "cerca-index.json").write_text(
        json.dumps(SEARCH_INDEX, ensure_ascii=False), encoding="utf-8")
    body = """
<h1>🔍 Cerca al material</h1>
<p class="lead">Cerca per paraula: «kerf», «tolerància», «carnet», «rúbrica SA5»…</p>
<p><input id="q" type="search" placeholder="Escriu i prem Enter…" autofocus
   style="width:100%;padding:.8rem 1.2rem;font-size:1.1rem;border-radius:999px;
          border:2px solid var(--line);background:var(--bg-card);color:var(--ink)"></p>
<div id="res"></div>
<script>
let IDX=null;
const q=document.getElementById('q'), res=document.getElementById('res');
async function cerca(){
  if(!IDX) IDX=await (await fetch('assets/cerca-index.json')).json();
  const terms=q.value.toLowerCase().split(/\\s+/).filter(t=>t.length>1);
  if(!terms.length){res.innerHTML='';return;}
  const out=[];
  for(const p of IDX){
    const hay=(p.t+' '+p.x).toLowerCase();
    let score=0, ok=true;
    for(const t of terms){
      const n=hay.split(t).length-1;
      if(!n){ok=false;break;}
      score+=n+(p.t.toLowerCase().includes(t)?8:0);
    }
    if(ok) out.push([score,p,terms[0]]);
  }
  out.sort((a,b)=>b[0]-a[0]);
  res.innerHTML=out.slice(0,25).map(([s,p,t])=>{
    const i=p.x.toLowerCase().indexOf(t);
    const frag=i<0?p.x.slice(0,160):p.x.slice(Math.max(0,i-70),i+110);
    return `<a class="card" href="${p.u}"><div class="card-icon">📄</div>
      <div><h3>${p.t} <span class="badge">${p.s}</span></h3><p>…${frag}…</p></div></a>`;
  }).join('')||'<p>Cap resultat. Prova una paraula més curta o sense accents.</p>';
}
q.addEventListener('input',()=>{clearTimeout(q._d);q._d=setTimeout(cerca,250);});
</script>
"""
    (OUT / "cerca.html").write_text(
        render_page("Cerca", body, "cerca.html",
                    [("Inici", "index.html"), ("Cerca", None)]), encoding="utf-8")


def copy_assets():
    plant = ROOT / "Recursos" / "Plantilles_disseny"
    if plant.is_dir():
        dest = OUT / slugify("Recursos/Plantilles_disseny")
        dest.mkdir(parents=True, exist_ok=True)
        for f in plant.iterdir():
            if f.suffix in (".svg", ".py"):
                shutil.copyfile(f, dest / slugify(f.name))
    impresos = ROOT / "web_assets" / "impressos"
    if impresos.is_dir():
        dest = OUT / "impressos"
        dest.mkdir(parents=True, exist_ok=True)
        for f in impresos.iterdir():
            shutil.copyfile(f, dest / f.name)
    xlsx = ROOT / "Avaluació" / "Quadern_digital_docent_plantilla.xlsx"
    if xlsx.exists():
        (OUT / "impressos").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(xlsx, OUT / "impressos" / xlsx.name)
    if (ROOT / "LICENSE").exists():
        shutil.copyfile(ROOT / "LICENSE", OUT / "LICENSE")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copyfile(ROOT / "web_assets" / "style.css", OUT / "assets" / "style.css")
    pages = build_doc_pages()
    build_section_indexes(pages)
    build_home(pages)
    copy_assets()
    print(f"Web generada a {OUT} — {len(pages)} pàgines de contingut.")


if __name__ == "__main__":
    main()
