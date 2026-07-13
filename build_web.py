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

def trim_num(trim: str) -> int:
    """1/2/3 segons el trimestre de la SA; 0 si no n'és cap (SA0)."""
    if trim.startswith("1r"):
        return 1
    if trim.startswith("2n"):
        return 2
    if trim.startswith("3r"):
        return 3
    return 0


# imprimibles (a web_assets/impressos/) que toca mostrar a la pàgina de cada SA
SA_PRINTABLES = {
    "SA0_Punt_de_partida": [
        ("avaluacio_inicial.html", "📝 Avaluació 0 (full de l'alumnat)"),
        ("passaport.html", "🛠️ Passaport maker"),
    ],
    "SA1_Benvinguts_Aula_Maker": [
        ("clauer_paper_SA1.html", "🔑 El clauer en paper (full de disseny)"),
    ],
    "SA2_Dissenyem_en_2D": [
        ("marcapagines_paper_SA2.html", "📑 El marcapàgines en paper (full de disseny)"),
    ],
}

ALUMNAT_LINKS = [
    ("📅", "El curs, dia a dia", "00_Diari_de_classe_alumnat.md", "Una targeta per setmana: què farem i què no pots oblidar"),
    ("📖", "Vocabulari bàsic del curs", "Classes/SA0_Punt_de_partida/Vocabulari_basic.md", "Totes les paraules maker, explicades curt i clar"),
    ("📔", "El diari de taller", "Avaluació/Diari_de_taller.md", "La teva llibreta maker: una entrada per sessió"),
    ("🧯", "Primers auxilis maker", "Recursos/Primers_auxilis_maker.md", "Alguna cosa no funciona? Desencalla't sol/a amb aquesta guia"),
    ("🚦", "Semàfor de fabricació", "Recursos/Semafor_maker.md", "Les 3 comprovacions abans d'enviar res a una màquina"),
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

    # 3) imatges: <img src="ruta/relativa/al/repo"> → còpia dins web/
    def fix_src(m):
        src = m.group(1)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        asset = src.replace("%20", " ").lstrip("./")
        cand = asset if (ROOT / asset).exists() else f"{current_rel_dir}/{asset}"
        if (ROOT / cand).exists():
            return f'src="{prefix}{slugify(cand)}"'
        return m.group(0)

    html_text = re.sub(r'src="([^"]+)"', fix_src, html_text)
    return html_text


def checkboxify(html_text: str, page_key: str) -> str:
    counter = [0]

    def task_li(m: re.Match) -> str:
        tid = f"{page_key}_task_{counter[0]}"
        counter[0] += 1
        return (f'<li class="task-item"><label class="task-label">'
                f'<input type="checkbox" class="task-check" data-task-id="{tid}">'
                f'<span class="task-text">{m.group(1).strip()}</span></label></li>')

    html_text = re.sub(r"<li>\[ \](.*?)</li>", task_li, html_text)
    html_text = re.sub(r"<li>\[x\](.*?)</li>", r'<li class="task-item done">☑\1</li>',
                        html_text, flags=re.I)
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
<a class="skip" href="#contingut">Salta al contingut ↓</a>
<header class="site-header">
  <a class="brand" href="{prefix}index.html">🛠️ <strong>Aula Maker</strong> <span>1r ESO</span></a>
  <nav>
    <a href="{prefix}index.html">Inici</a>
    <a href="{prefix}sa.html">Les 9 SA</a>
    <a href="{prefix}docent.html">Docent</a>
    <a href="{prefix}alumnat.html">Alumnat</a>
    <a href="{prefix}families.html">Famílies</a>
    <a href="{prefix}cerca.html" title="Cerca">🔍</a>
    <span class="a11y" role="group" aria-label="Ajustos de lectura">
      <button id="fmenys" title="Lletra més petita" aria-label="Lletra més petita">A−</button>
      <button id="fmes" title="Lletra més gran" aria-label="Lletra més gran">A+</button>
      <button id="espaiat" title="Lectura fàcil: més espai entre lletres i línies"
              aria-label="Lectura fàcil (més espaiat)" aria-pressed="false">Aa↔</button>
      <button id="llegir" title="Escolta aquesta pàgina en veu alta"
              aria-label="Escolta aquesta pàgina en veu alta">🔊</button>
      <button id="rellotge" title="Rellotge Maker (temporitzador de 50′)"
              aria-label="Obre el Rellotge Maker">⏱️ Rellotge</button>
      <button id="theme" title="Canvia el tema" aria-label="Canvia el tema">🌗</button>
    </span>
  </nav>
</header>
<div class="clock-panel" id="clock-panel" role="dialog" aria-label="Rellotge Maker">
  <div class="clock-label">Torn d'estació (50′)</div>
  <div class="clock-time" id="clock-time">50:00</div>
  <div class="clock-actions">
    <button id="clock-start">▶️ Inicia</button>
    <button id="clock-reset">↺ 50′</button>
  </div>
</div>
<div class="crumb">{crumb_html}</div>
<main class="content" id="contingut" tabindex="-1">
{body}
</main>
<footer class="site-footer">
  <p>«Aula Maker» · optativa de 1r d'ESO · curs 2026-2027 · material sota
  <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.ca">CC BY-SA 4.0</a></p>
</footer>
<script>
const R=document.documentElement, LS=localStorage;
const el=id=>document.getElementById(id);
// tema
if(LS.getItem('theme'))R.dataset.theme=LS.getItem('theme');
el('theme').onclick=()=>{{R.dataset.theme=(R.dataset.theme==='dark')?'light':'dark';
LS.setItem('theme',R.dataset.theme);}};
// mida de lletra (0=normal, 1=gran, 2=molt gran)
let fs=+(LS.getItem('fs')||0);
const aplicaFs=()=>{{R.dataset.fs=fs;LS.setItem('fs',fs);}};aplicaFs();
el('fmes').onclick=()=>{{fs=Math.min(2,fs+1);aplicaFs();}};
el('fmenys').onclick=()=>{{fs=Math.max(0,fs-1);aplicaFs();}};
// lectura fàcil (espaiat ampli, columna estreta)
const esp=el('espaiat');
const aplicaEsp=v=>{{if(v)R.dataset.espaiat='1';else delete R.dataset.espaiat;
esp.setAttribute('aria-pressed',v?'true':'false');LS.setItem('espaiat',v?'1':'0');}};
aplicaEsp(LS.getItem('espaiat')==='1');
esp.onclick=()=>aplicaEsp(R.dataset.espaiat!=='1');
// escolta la pàgina (veu en català si n'hi ha)
const veu=el('llegir');
if(!('speechSynthesis' in window))veu.style.display='none';
else veu.onclick=()=>{{const s=speechSynthesis;
if(s.speaking){{s.cancel();veu.textContent='🔊';return;}}
const u=new SpeechSynthesisUtterance(document.querySelector('main').innerText);
u.lang='ca-ES';const v=s.getVoices().find(v=>v.lang&&v.lang.toLowerCase().startsWith('ca'));
if(v)u.voice=v;u.rate=.95;u.onend=()=>veu.textContent='🔊';
veu.textContent='⏹';s.speak(u);}};
// checklists persistents (localStorage)
document.querySelectorAll('.task-check').forEach(chk=>{{
const key='maker_chk_'+chk.dataset.taskId;
chk.checked=LS.getItem(key)==='true';
chk.closest('.task-item').classList.toggle('completed',chk.checked);
chk.addEventListener('change',()=>{{LS.setItem(key,chk.checked);
chk.closest('.task-item').classList.toggle('completed',chk.checked);}});
}});
// Rellotge Maker (temporitzador de torn, 50')
const cp=el('clock-panel'),ctime=el('clock-time'),cstart=el('clock-start'),
creset=el('clock-reset'),crell=el('rellotge'),DUR=50*60;
let clockTimer=null;
const fmt=s=>{{s=Math.max(0,s);return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0');}};
const clockRender=()=>{{
const end=+LS.getItem('clock_end');
let remain=end?Math.round((end-Date.now())/1000):DUR;
if(remain<=0){{remain=0;clearInterval(clockTimer);clockTimer=null;LS.removeItem('clock_end');cstart.textContent='▶️ Inicia';}}
ctime.textContent=fmt(remain);
cp.classList.toggle('warn',remain>0&&remain<=600);
}};
crell.onclick=()=>cp.classList.toggle('open');
cstart.onclick=()=>{{
if(LS.getItem('clock_end')){{LS.removeItem('clock_end');clearInterval(clockTimer);clockTimer=null;
cstart.textContent='▶️ Inicia';return;}}
const m=/^(\d+):(\d+)$/.exec(ctime.textContent);
const remain=m?(+m[1])*60+(+m[2]):DUR;
LS.setItem('clock_end',Date.now()+remain*1000);
cstart.textContent='⏸ Pausa';
clockTimer=setInterval(clockRender,1000);
}};
creset.onclick=()=>{{clearInterval(clockTimer);clockTimer=null;LS.removeItem('clock_end');
cstart.textContent='▶️ Inicia';ctime.textContent='50:00';cp.classList.remove('warn');}};
if(LS.getItem('clock_end')){{cstart.textContent='⏸ Pausa';clockTimer=setInterval(clockRender,1000);clockRender();}}
</script>
</body>
</html>
"""


SEARCH_INDEX = []  # {t: títol, u: url, s: secció, x: text pla}


# ── navegació entre SA i hub per SA ────────────────────────────────────────
def sa_idx(folder: str):
    for i, c in enumerate(SA_CARDS):
        if c[4] == folder:
            return i
    return None


def sa_siblings(folder: str):
    """Pàgines d'una SA, ordenades: (etiqueta amb emoji, basename html, kind)."""
    order = {"fitxa": 0, "doc": 1, "rubrica": 2, "exemple": 3, "extra": 5}
    out = []
    for p in MD_FILES:
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        if not rel.startswith(f"Classes/{folder}/"):
            continue
        fn = rel.rsplit("/", 1)[-1]
        base = PATH_MAP[rel].rsplit("/", 1)[-1]
        if fn.startswith("Fitxa"):
            lbl, kind = "✏️ Fitxa de l'alumnat", "fitxa"
        elif re.match(r"SA\d", fn):
            lbl, kind = "📖 La SA (docent)", "doc"
        elif fn.startswith("Rubrica"):
            lbl, kind = "📊 Rúbrica", "rubrica"
        elif fn.startswith("Exemple"):
            lbl, kind = "🌟 Exemple resolt", "exemple"
        elif fn.startswith("Dinamica"):
            lbl, kind = "🤝 Dinàmica de cohesió", "extra"
        elif fn.startswith("Material_gimcana"):
            lbl, kind = "🛡️ Gimcana de seguretat", "extra"
        elif fn.startswith("Vocabulari"):
            lbl, kind = "📖 Vocabulari bàsic", "extra"
        else:
            lbl, kind = "📄 " + fn[:-3].replace("_", " "), "extra"
        out.append((order[kind], lbl, base, kind))
    out.sort()
    return [(lbl, base, kind) for _o, lbl, base, kind in out]


# Seqüència lineal única del recorregut de l'alumne: dins de cada SA es passa pels seus passos
# (hub → fitxa → exemple → activitats) i només al final se salta a la SA següent. Les pàgines
# de referència del docent (la SA completa i la rúbrica) NO són passos de l'alumne.
_WALK_PRIO = {"hub": -1, "fitxa": 0, "exemple": 1, "extra": 2}
SA_SEQUENCE = []            # [{folder, base, label, kind}] en ordre de recorregut
SEQ_INDEX = {}              # (folder, base) → posició a SA_SEQUENCE


def build_sequence():
    SA_SEQUENCE.clear()
    SEQ_INDEX.clear()
    for code, name, _trim, _product, folder in SA_CARDS:
        SA_SEQUENCE.append({"folder": folder, "base": "index.html", "kind": "hub",
                            "label": f"{code} · {html.escape(name)}"})
        sibs = [s for s in sa_siblings(folder) if s[2] in _WALK_PRIO]
        for lbl, base, kind in sorted(sibs, key=lambda s: _WALK_PRIO[s[2]]):
            SA_SEQUENCE.append({"folder": folder, "base": base, "kind": kind,
                                "label": f"{code} · {lbl}"})
    for i, e in enumerate(SA_SEQUENCE):
        SEQ_INDEX[(e["folder"], e["base"])] = i


def step_nav(folder: str, base: str) -> str:
    """Pas anterior / següent del recorregut de l'alumne per a la pàgina (folder, base)."""
    i = SEQ_INDEX.get((folder, base))
    if i is None:
        return ""

    def rel_href(e):
        return e["base"] if e["folder"] == folder else f'../{slugify(e["folder"])}/{e["base"]}'

    prev = SA_SEQUENCE[i - 1] if i > 0 else None
    nxt = SA_SEQUENCE[i + 1] if i < len(SA_SEQUENCE) - 1 else None
    if prev:
        left = (f'<a class="sa-prev" href="{rel_href(prev)}">'
                f'<small>← pas anterior</small><strong>{prev["label"]}</strong></a>')
    else:
        left = '<span class="sa-prev sa-dis"><small>← pas anterior</small><strong>—</strong></span>'
    if nxt:
        right = (f'<a class="sa-next" href="{rel_href(nxt)}">'
                 f'<small>pas següent →</small><strong>{nxt["label"]}</strong></a>')
    else:
        right = '<span class="sa-next sa-dis"><small>pas següent →</small><strong>fi del curs 🎉</strong></span>'
    return f'<nav class="sa-nav" aria-label="Pas anterior i següent">{left}{right}</nav>'


def sa_printables_html(folder: str) -> str:
    items = SA_PRINTABLES.get(folder, [])
    if not items:
        return ""
    links = " · ".join(f'<a href="../../impressos/{f}">{lbl}</a>' for f, lbl in items)
    return (f'<div class="sa-print">🖨️ <strong>Per imprimir i repartir a l\'alumnat:</strong> '
            f'{links}</div>')


def sa_context_bar(folder: str, current_base: str) -> str:
    """Peu discret de cada pàgina d'una SA: germanes + imprimibles + prev/next (a sota de tot)."""
    chips = [f'<a class="sa-hublink" href="index.html">⌂ Aquesta SA</a>']
    for lbl, base, _kind in sa_siblings(folder):
        if base == current_base:
            chips.append(f'<span class="sa-chip cur">{lbl}</span>')
        else:
            chips.append(f'<a class="sa-chip" href="{base}">{lbl}</a>')
    return (f'<div class="sa-sib">{"".join(chips)}</div>'
            f'{sa_printables_html(folder)}'
            f'{step_nav(folder, current_base)}')


def sa_cards(prefix: str) -> str:
    """Graella de targetes de SA que porten al hub (compartida per portada i índex de Classes)."""
    return "\n".join(
        f'<a class="card sa" data-trim="{trim_num(trim)}" '
        f'href="{prefix}classes/{slugify(folder)}/index.html">'
        f'<div class="card-icon">{product.split()[0]}</div>'
        f'<div><h3>{code} · {html.escape(name)} <span class="badge badge-t{trim_num(trim)}">{trim}</span></h3>'
        f'<p>{html.escape(product.split(" ", 1)[1])}</p></div></a>'
        for code, name, trim, product, folder in SA_CARDS)


def build_sa_hubs():
    """Una pàgina hub per SA: entrada única igual des de tot arreu."""
    for code, name, trim, product, folder in SA_CARDS:
        slug = slugify(folder)
        out_rel = f"classes/{slug}/index.html"
        sibs = sa_siblings(folder)
        fitxa = next((b for lbl, b, k in sibs if k == "fitxa"), None)
        primary = ""
        if fitxa:
            primary = (f'<a class="sa-primary" href="{fitxa}"><span class="sa-primary-ic">✏️</span>'
                       f'<span><strong>Fitxa de l\'alumnat</strong>'
                       f'<small>el full amb què treballes aquesta SA</small></span></a>')
        others = [(lbl, b, k) for lbl, b, k in sibs if k != "fitxa"]
        cards = "\n".join(
            f'<a class="card" href="{b}"><div class="card-icon">{lbl.split(" ", 1)[0]}</div>'
            f'<div><h3>{html.escape(lbl.split(" ", 1)[1])}</h3></div></a>'
            for lbl, b, k in others)
        body = f"""
<h1>{code} · {html.escape(name)} <span class="badge badge-t{trim_num(trim)}">{trim}</span></h1>
<p class="product">{html.escape(product)}</p>
{primary}
{sa_printables_html(folder)}
<h2>Tot el material d'aquesta SA</h2>
<div class="grid">{cards}</div>
<footer class="sa-foot">{step_nav(folder, "index.html")}</footer>
"""
        crumb = [("Inici", "index.html"), ("Classes", "classes/index.html"),
                 (f"{code} · {name}" if len(f"{code} · {name}") < 60 else f"{code}", None)]
        (OUT / out_rel).parent.mkdir(parents=True, exist_ok=True)
        (OUT / out_rel).write_text(
            render_page(f"{code} · {name}", body, out_rel, crumb), encoding="utf-8")


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
        page_key = re.sub(r"[^a-z0-9]+", "_", out_rel[:-5].lower()).strip("_")
        body = checkboxify(body, page_key)
        plain_src = body  # sense la barra de navegació (per a l'índex de cerca)
        parts = rel.split("/")
        if len(parts) >= 3 and parts[0] == "Classes" and sa_idx(parts[1]) is not None:
            foot = sa_context_bar(parts[1], out_rel.rsplit("/", 1)[-1])
            body = f'<article class="doc">{body}<footer class="sa-foot">{foot}</footer></article>'
        else:
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
        plain = re.sub(r"<[^>]+>", " ", plain_src)
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
            body_html = (f"<h1>{icon} El curs, SA a SA (SA0 + les 9 SA)</h1>"
                         f"<p class=\"lead\">Clica una SA per obrir-la: hi trobaràs la fitxa de "
                         f"l'alumnat, el material del docent i tot el que cal imprimir, amb "
                         f"navegació a la SA anterior i la següent.</p>"
                         f"<div class='grid'>{sa_cards('../')}</div>")
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
    sa_grid = sa_cards("")
    body = f"""
<section class="hero">
  <h1>🛠️ Aula Maker</h1>
  <p class="tagline">Optativa de 1r d'ESO · imaginar, dissenyar i <strong>fabricar de veritat</strong>:
  talladora làser, impressió 3D, càmera 360 i realitat virtual.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="sa.html">🧩 Les 9 SA</a>
    <a class="btn" href="docent.html">👩‍🏫 Soc docent</a>
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
        f'<a class="chip" href="classes/{slugify(folder)}/index.html">{code}</a>'
        for code, _n, _t, _p, folder in SA_CARDS)
    body = f"""
<h1>🧑‍🎓 Per a l'alumnat</h1>
<p class="lead">Tot el que fas servir tu: les fitxes de cada repte, com t'avaluaran
(sense sorpreses!) i el joc de carnets i insígnies.</p>
<blockquote><p><strong>Com fer servir aquesta web (3 passos):</strong>
1️⃣ Mira <a href="00_diari_de_classe_alumnat.html">què toca aquesta setmana</a> ·
2️⃣ Obre la <strong>fitxa de la SA</strong> que estem fent (aquí sota) ·
3️⃣ Si no entens una paraula, busca-la al
<a href="classes/sa0_punt_de_partida/vocabulari_basic.html">vocabulari</a>.</p>
<p>💡 <strong>Fes-te la web teva</strong> amb els botons de dalt: <strong>A−/A+</strong> per la
mida de la lletra, <strong>Aa↔</strong> per llegir amb més espai (va molt bé si les lletres
«es mouen»), <strong>🔊</strong> perquè la pàgina es llegeixi sola en veu alta i <strong>🌗</strong>
pel mode fosc. La web ho recorda per al pròxim dia.</p></blockquote>
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
        card("impressos/avaluacio_inicial.html", "📝", "Avaluació 0 (full de l'alumnat)",
             "A4, 2 pàgines: autopercepció + vocabulari + esbós del clauer. Per a la SA0 "
             "(sense ordinador), amb espai per escriure a mà", "imprimible"),
        card("impressos/clauer_paper_SA1.html", "🔑", "Clauer en paper (full de disseny SA1)",
             "A4, 2 pàgines: ruta de disseny amb caselles + tauler mil·limetrat a mida real. "
             "Per a la sessió 1 de la SA1 (en paper, sense ordinador)", "imprimible"),
        card("impressos/diari_taller_T1.html", "📓", "Diari de taller en paper (T1)",
             "16 pàgines per alumne/a: les 12 entrades del trimestre ja etiquetades + "
             "tancaments de SA", "imprimible"),
        card("impressos/diari_taller_T2.html", "📓", "Diari de taller en paper (T2)",
             "SA4-SA6, setmanes 13-24: opció paper (DUA) i pla B del portafoli digital",
             "imprimible"),
        card("impressos/diari_taller_T3.html", "📓", "Diari de taller en paper (T3)",
             "SA7-SA9 + tancament de curs, setmanes 25-35: opció paper i pla B",
             "imprimible"),
        card("impressos/poster_grans_idees.html", "🧭", "Pòster de les 5 Grans Idees",
             "A4/A3 per penjar a les dues aules", "imprimible"),
        card("impressos/targetes_museu.html", "🏛️", "Targetes del Museu dels Errors",
             "4 per full, per deixar al costat del museu", "imprimible"),
        card("impressos/targetes_kanban.html", "🖨️", "Targetes de kanban d'impressió",
             "8 per full: una per placa, de la SA5 fins a la Fira", "imprimible"),
        card("impressos/torns_camera.html", "🎥", "Reserva de torns de càmera 360",
             "1 full per sessió de captura (SA7) amb les 4 regles del rodatge", "imprimible"),
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
<blockquote><p>💡 Cada trimestre hi ha <strong>Fira Aula Maker</strong> oberta a les famílies
(us farem arribar les dates): hi veureu els projectes del trimestre i, a la <strong>gran
Fira</strong> de final de curs, hi podreu provar les experiències que han creat. Us hi
esperem!</p></blockquote>
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
    imatges = ROOT / "Recursos" / "imatges"
    if imatges.is_dir():
        dest = OUT / slugify("Recursos/imatges")
        dest.mkdir(parents=True, exist_ok=True)
        for f in imatges.iterdir():
            if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"):
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
    build_sequence()
    pages = build_doc_pages()
    build_sa_hubs()
    build_section_indexes(pages)
    build_home(pages)
    copy_assets()
    print(f"Web generada a {OUT} — {len(pages)} pàgines de contingut.")


if __name__ == "__main__":
    main()
