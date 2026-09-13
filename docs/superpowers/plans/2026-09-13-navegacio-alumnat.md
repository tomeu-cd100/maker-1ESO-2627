# Navegació separada per a l'alumnat — Pla d'implementació

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generar, dins de `web/`, un subarbre `alumnat/` amb un recorregut lineal i mínim (selector de SA → hub de SA → fitxa + documents transversals), separat físicament de la vista completa actual que continua servint docents/famílies/públic general sense cap canvi de comportament.

**Architecture:** Tot el treball és a `build_web.py` (únic generador del projecte, patró de fitxer únic ja establert — no es reestructura). S'afegeix una font única de veritat (`ALUMNAT_SPACE`) que decideix quins `.md` pertanyen al recorregut de l'alumnat, i cada funció de generació de pàgines es parametritza amb un `space: "full" | "alumnat"` que produeix una **còpia física** addicional sota `alumnat/` amb capçalera/breadcrumb/seqüència reduïts, reutilitzant tota la lògica HTML/CSS/JS ja existent.

**Tech Stack:** Python 3.11 (el `python` del PATH és el d'Inkscape — cal invocar l'intèrpret real, p. ex. `py -3.11` o la ruta completa), llibreria `markdown`, sense frameworks de test (el projecte es verifica regenerant `web/` i executant `verifica_web.py`/`verifica_enllacos.py`/`verifica_competencies.py`, no hi ha pytest al repo).

**Spec:** `docs/superpowers/specs/2026-09-13-navegacio-alumnat-design.md`

## Global Constraints

- **Cap canvi als `.md` font** (Fitxa_alumnat.md, Rubrica_SAx.md, SAx.md, Exemple_resolt.md, documents d'`ALUMNAT_LINKS`) — tot l'esforç és al generador.
- `web/` és artefacte generat: mai s'edita a mà, només amb `python build_web.py`.
- Tot text nou visible (capçaleres, avisos, etiquetes) ha d'estar en català amb ortografia completa (accents inclosos).
- La vista completa actual (portada, `docent.html`, `families.html`, hubs de SA amb fitxa+rúbrica+exemple+doc, breadcrumbs de 4 nivells) **no ha de canviar de comportament**.
- Després de cada tasca: `py -3.11 build_web.py` ha d'acabar sense excepcions i `py -3.11 verifica_web.py` ha de sortir amb `[OK]` (codi de sortida 0).
- Accessibilitat: tota icona nova porta text al costat (mai només color), navegable per teclat (és a dir, elements interactius nous són `<a>`/`<button>`, mai `<div onclick>`).

---

## Mapa de fitxers

- **Modify:** `build_web.py` — únic fitxer tocat en totes les tasques (858 línies actuals; les tasques hi afegeixen/divideixen funcions, sense extreure'l a mòduls nous, seguint el patró existent).
- **No es toca:** `verifica_web.py` (és genèric: recorre tots els `.html` de `web/` i comprova que els `href`/`src` locals resolen a fitxers reals — no té cap lògica de "duplicat" que calgui adaptar; les còpies noves sota `alumnat/` només han de tenir enllaços que resolguin, cosa que cobreixen les tasques 6-8).
- **No es toca:** `verifica_enllacos.py`, `verifica_competencies.py` (operen sobre els `.md` font, no es veuen afectats).

---

### Task 1: `ALUMNAT_SPACE` — font única de veritat

**Files:**
- Modify: `build_web.py:82-98` (just després de la llista `ALUMNAT_LINKS`)

**Interfaces:**
- Produces: `ALUMNAT_SPACE: set[str]` — conjunt de rutes `.md` relatives a `ROOT` (amb `/` com a separador, format idèntic a les claus de `PATH_MAP`, p. ex. `"Classes/SA2_Dissenyem_en_2D/Fitxa_alumnat.md"`, `"Avaluació/Diari_de_taller.md"`) que pertanyen al recorregut de l'alumnat. Les tasques 2-9 hi consulten pertinença amb `rel in ALUMNAT_SPACE`.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

Crea un fitxer temporal `check_task1.py` (fora de `web/`, a l'arrel del repo, esborrable després):

```python
# check_task1.py
import build_web as bw

assert hasattr(bw, "ALUMNAT_SPACE"), "Falta ALUMNAT_SPACE"
assert isinstance(bw.ALUMNAT_SPACE, set)

# Totes les fitxes d'alumnat hi són
fitxes = {rel for rel in bw.PATH_MAP if rel.rsplit("/", 1)[-1] == "Fitxa_alumnat.md"}
assert fitxes and fitxes <= bw.ALUMNAT_SPACE, f"Falten fitxes: {fitxes - bw.ALUMNAT_SPACE}"

# Tots els ALUMNAT_LINKS hi són
for _icon, _t, rel, _d in bw.ALUMNAT_LINKS:
    assert rel in bw.ALUMNAT_SPACE, f"Falta a ALUMNAT_SPACE: {rel}"

# Rúbrica, exemple i doc de SA NO hi són
for rel in bw.PATH_MAP:
    fn = rel.rsplit("/", 1)[-1]
    if fn.startswith("Rubrica") or fn.startswith("Exemple"):
        assert rel not in bw.ALUMNAT_SPACE, f"No hi hauria de ser: {rel}"

print("OK task 1")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task1.py`
Expected: `AttributeError: module 'build_web' has no attribute 'ALUMNAT_SPACE'`

- [ ] **Step 3: Implementa `ALUMNAT_SPACE`**

Afegeix a `build_web.py`, immediatament després del tancament de la llista `ALUMNAT_LINKS` (línia 98, abans de `DOCENT_DESTACATS`):

```python
# ALUMNAT_SPACE es calcula més avall, un cop existeix PATH_MAP (necessita conèixer
# totes les fitxes reals). Es declara aquí com a marcador de disseny; el valor
# real s'assigna a build_alumnat_space(), cridada després de construir PATH_MAP.
ALUMNAT_SPACE: set[str] = set()


def build_alumnat_space() -> None:
    """Omple ALUMNAT_SPACE: totes les Fitxa_alumnat.md + tots els ALUMNAT_LINKS."""
    ALUMNAT_SPACE.clear()
    for rel in PATH_MAP:
        if "%20" in rel:
            continue
        if rel.rsplit("/", 1)[-1] == "Fitxa_alumnat.md":
            ALUMNAT_SPACE.add(rel)
    for _icon, _title, rel, _desc in ALUMNAT_LINKS:
        ALUMNAT_SPACE.add(rel)
```

Després, a `main()` (línia 842-853), crida `build_alumnat_space()` just després de `build_sequence()`:

```python
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copyfile(ROOT / "web_assets" / "style.css", OUT / "assets" / "style.css")
    build_sequence()
    build_alumnat_space()
    pages = build_doc_pages()
    build_sa_hubs()
    build_section_indexes(pages)
    build_home(pages)
    copy_assets()
    print(f"Web generada a {OUT} — {len(pages)} pàgines de contingut.")
```

- [ ] **Step 4: Executa la comprovació i confirma que passa**

Com que `build_alumnat_space()` només s'omple dins `main()`, ajusta temporalment `check_task1.py` perquè la cridi abans dels asserts:

```python
import build_web as bw
bw.build_alumnat_space()
# ... (resta d'asserts igual)
```

Run: `py -3.11 check_task1.py`
Expected: `OK task 1`

- [ ] **Step 5: Neteja i verifica la build sencera**

Run: `rm check_task1.py && py -3.11 build_web.py && py -3.11 verifica_web.py`
Expected: build sense errors, `verifica_web.py` acaba amb `[OK] ... tots els enllacos locals resolen.`

- [ ] **Step 6: Commit**

```bash
git add build_web.py
git commit -m "feat: afegeix ALUMNAT_SPACE com a font única del recorregut d'alumnat"
```

---

### Task 2: `render_page` amb capçalera reduïda per l'espai alumnat

**Files:**
- Modify: `build_web.py:264-382` (`render_page`)

**Interfaces:**
- Consumes: res nou (només l'esquelet HTML existent).
- Produces: `render_page(title, body, out_rel, crumb, space="full")`. Quan `space="alumnat"`, la `<nav>` de capçalera es redueix i s'afegeix el xip `📍 SAx` + botó `🔁 Canviar de SA`, llegint/escrivint `localStorage.sa_actual` (nom exacte de la clau que fan servir totes les tasques posteriors).

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task2.py
import build_web as bw

html_full = bw.render_page("Prova", "<p>cos</p>", "prova.html", [("Inici", "index.html"), ("Prova", None)])
assert 'href="docent.html"' in html_full, "La vista full ha de mantenir l'enllaç a Docent"

html_alu = bw.render_page("Prova", "<p>cos</p>", "alumnat/prova.html", [("Alumnat", "index.html"), ("Prova", None)], space="alumnat")
assert 'href="docent.html"' not in html_alu, "La vista alumnat no ha de mostrar l'enllaç a Docent"
assert 'href="../docent.html"' not in html_alu
assert 'sa_actual' in html_alu, "Falta la lectura de localStorage.sa_actual"
assert 'Canviar de SA' in html_alu

print("OK task 2")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task2.py`
Expected: `AssertionError` (space no existeix encara com a paràmetre, o l'enllaç a Docent hi és igualment)

- [ ] **Step 3: Implementa el paràmetre `space`**

Substitueix la signatura i el bloc `<nav>` de `render_page` (`build_web.py:264-302`):

```python
def render_page(title: str, body: str, out_rel: str, crumb: list[tuple[str, str | None]],
                 space: str = "full") -> str:
    prefix = rel_prefix(out_rel)
    crumb_html = " <span class=\"sep\">›</span> ".join(
        f'<a href="{prefix}{href}">{html.escape(text)}</a>' if href else f"<span>{html.escape(text)}</span>"
        for text, href in crumb
    )
    if space == "alumnat":
        brand_href = f"{prefix}alumnat/index.html"
        nav_links = (
            f'<a href="{prefix}alumnat/index.html">Inici</a>'
            f'<a href="{prefix}alumnat/cerca.html" title="Cerca">🔍</a>'
            f'<span class="sa-actual-chip"><a id="sa-actual-link" href="#">📍 <span id="sa-actual-label">…</span></a>'
            f'<a class="sa-canvia" href="{prefix}alumnat/index.html">🔁 Canviar de SA</a></span>'
        )
    else:
        brand_href = f"{prefix}index.html"
        nav_links = (
            f'<a href="{prefix}index.html">Inici</a>'
            f'<a href="{prefix}sa.html">Les 9 SA</a>'
            f'<a href="{prefix}docent.html">Docent</a>'
            f'<a href="{prefix}alumnat/index.html">Alumnat</a>'
            f'<a href="{prefix}families.html">Famílies</a>'
            f'<a href="{prefix}cerca.html" title="Cerca">🔍</a>'
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
  <a class="brand" href="{brand_href}">🛠️ <strong>Aula Maker</strong> <span>1r ESO</span></a>
  <nav>
    {nav_links}
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
const m=/^(\\d+):(\\d+)$/.exec(ctime.textContent);
const remain=m?(+m[1])*60+(+m[2]):DUR;
LS.setItem('clock_end',Date.now()+remain*1000);
cstart.textContent='⏸ Pausa';
clockTimer=setInterval(clockRender,1000);
}};
creset.onclick=()=>{{clearInterval(clockTimer);clockTimer=null;LS.removeItem('clock_end');
cstart.textContent='▶️ Inicia';ctime.textContent='50:00';cp.classList.remove('warn');}};
if(LS.getItem('clock_end')){{cstart.textContent='⏸ Pausa';clockTimer=setInterval(clockRender,1000);clockRender();}}
{"""
// xip "SA actual" (només a l'espai alumnat)
const saLbl=el('sa-actual-label'), saLink=el('sa-actual-link');
if(saLbl){{
  const cur=LS.getItem('sa_actual');
  if(cur){{saLbl.textContent=cur;saLink.href=cur+'/index.html';}}
  else{{saLink.parentElement.style.display='none';}}
}}
""" if space == "alumnat" else ""}
</script>
</body>
</html>
"""
```

Nota: `sa_actual` es desa com el **slug** de la SA (p. ex. `sa2_dissenyem_en_2d`), no com el nom de carpeta original — és el format que fan servir les rutes de sortida. `saLink.href=cur+'/index.html'` funciona perquè totes les pàgines d'`alumnat/classes/<slug>/...` són germanes al mateix nivell (`../<slug>/index.html` es resol bé només si estem ja dins `alumnat/classes/`; com que el xip apareix a **totes** les pàgines d'`alumnat/`, incloent les que no són de `classes/` — cal un enllaç absolut des de l'arrel d'`alumnat/`). Corregeix-ho fent que `saLink.href` es construeixi amb el prefix relatiu correcte: substitueix la línia per:

```javascript
if(cur){{saLbl.textContent=cur;saLink.href='{prefix}alumnat/classes/'+cur+'/index.html';}}
```

(el `{prefix}` de Python s'incrusta igual que a la resta del bloc `<script>`, ja fora de l'`if` de space perquè és una f-string sencera).

- [ ] **Step 4: Executa la comprovació i confirma que passa**

Run: `py -3.11 check_task2.py`
Expected: `OK task 2`

- [ ] **Step 5: Neteja i verifica la build sencera**

Run: `rm check_task2.py && py -3.11 build_web.py && py -3.11 verifica_web.py`
Expected: `[OK]` (l'espai alumnat encara no genera pàgines pròpies — aquesta tasca només canvia la funció compartida — així que la build ha de comportar-se exactament igual que abans per a totes les pàgines existents, totes `space="full"` per defecte).

- [ ] **Step 6: Commit**

```bash
git add build_web.py
git commit -m "feat: render_page admet una capçalera reduïda per a l'espai alumnat"
```

---

### Task 3: `sa_cards` amb base configurable + selector `alumnat/index.html`

**Files:**
- Modify: `build_web.py:495-503` (`sa_cards`)
- Modify: `build_web.py:613-643` (`build_home`, per cridar la nova funció)

**Interfaces:**
- Consumes: `render_page(..., space=)` (Task 2), `ALUMNAT_LINKS`, `SA_CARDS`, `card()` (`build_web.py:580-583`, sense canvis).
- Produces: `sa_cards(prefix, base="classes/")`; `build_alumnat_home()` que escriu `web/alumnat/index.html`.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task3.py
import build_web as bw
from pathlib import Path

out = bw.sa_cards("../", base="alumnat/classes/")
assert "alumnat/classes/sa2_dissenyem_en_2d/index.html" in out, out[:200]

assert hasattr(bw, "build_alumnat_home"), "Falta build_alumnat_home"
print("OK task 3 (part 1: sa_cards)")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task3.py`
Expected: `AssertionError` o `TypeError: sa_cards() got an unexpected keyword argument 'base'`

- [ ] **Step 3: Implementa `sa_cards` amb `base`**

Substitueix `build_web.py:495-503`:

```python
def sa_cards(prefix: str, base: str = "classes/") -> str:
    """Graella de targetes de SA que porten al hub (compartida per portada i índex de Classes)."""
    return "\n".join(
        f'<a class="card sa" data-trim="{trim_num(trim)}" '
        f'href="{prefix}{base}{slugify(folder)}/index.html">'
        f'<div class="card-icon">{product.split()[0]}</div>'
        f'<div><h3>{code} · {html.escape(name)} <span class="badge badge-t{trim_num(trim)}">{trim}</span></h3>'
        f'<p>{html.escape(product.split(" ", 1)[1])}</p></div></a>'
        for code, name, trim, product, folder in SA_CARDS)
```

Els dos usos existents (`build_web.py:614` `sa_cards("")` i `build_web.py:599` `sa_cards('../')`) no canvien: `base` per defecte és `"classes/"`, idèntic al comportament actual.

- [ ] **Step 4: Implementa `build_alumnat_home()`**

Afegeix una funció nova, després de `build_home()` (abans de `copy_assets()`, `build_web.py:812`):

```python
def build_alumnat_home() -> None:
    """Selector de SA de l'alumnat + documents transversals del curs."""
    out_rel = "alumnat/index.html"
    sa_grid = sa_cards("", base="alumnat/classes/")
    # els documents transversals viuen sota alumnat/ (Task 6 els hi genera); aquí ja
    # apuntem a la seva ruta final dins alumnat/
    docs = "\n".join(
        card(f"alumnat/{PATH_MAP[rel]}", icon, t, d)
        for icon, t, rel, d in ALUMNAT_LINKS
    )
    body = f"""
<h1>🧑‍🎓 Quina SA esteu fent ara?</h1>
<p class="lead">Tria la teva SA per obrir-ne la fitxa. Si un altre dia vols
tornar-hi, aquesta pàgina et recordarà quina és — sempre pots canviar-la amb
el botó «🔁 Canviar de SA» de dalt.</p>
<div class="grid">{sa_grid}</div>
<h2>Documents del curs</h2>
<div class="grid">{docs}</div>
"""
    (OUT / "alumnat").mkdir(parents=True, exist_ok=True)
    (OUT / out_rel).write_text(
        render_page("Alumnat", body, out_rel, [("Alumnat", None)], space="alumnat"),
        encoding="utf-8")
```

- [ ] **Step 5: Crida `build_alumnat_home()` des de `main()`**

A `build_web.py:842-853`, afegeix la crida just després de `build_home(pages)`:

```python
    build_home(pages)
    build_alumnat_home()
    copy_assets()
```

(Les rutes `alumnat/<...>` dins `docs` encara no existeixen com a fitxers — es generaran a la Task 6 — així que `verifica_web.py` fallarà momentàniament amb enllaços trencats fins llavors. És **esperat**: aquesta tasca es verifica de manera aïllada mirant el contingut HTML, no encara amb `verifica_web.py` en verd.)

- [ ] **Step 6: Executa la comprovació i confirma que passa**

Run: `py -3.11 check_task3.py`
Expected: `OK task 3 (part 1: sa_cards)`

- [ ] **Step 7: Comprova el contingut generat**

Run: `py -3.11 build_web.py && grep -c 'card sa' web/alumnat/index.html`
Expected: `10` (una targeta per SA0-SA9)

Run (PowerShell equivalent si `grep` no és disponible): `Select-String -Path web/alumnat/index.html -Pattern 'card sa'`

- [ ] **Step 8: Neteja i commit**

```bash
rm check_task3.py
git add build_web.py
git commit -m "feat: selector de SA per a l'espai alumnat (alumnat/index.html)"
```

(No s'executa `verifica_web.py` aquí a posta — quedarà en vermell fins la Task 6; és coherent amb l'ordre de dependències del pla.)

---

### Task 4: Seqüència i navegació pas-a-pas per a l'espai alumnat

**Files:**
- Modify: `build_web.py:427-470` (`SA_SEQUENCE`/`SEQ_INDEX`/`build_sequence`/`step_nav`)

**Interfaces:**
- Consumes: `sa_siblings()` (sense canvis, `build_web.py:396-424`).
- Produces: `ALUMNAT_SEQUENCE: list[dict]`, `ALUMNAT_SEQ_INDEX: dict`, `build_alumnat_sequence()`; `step_nav(folder, base, sequence=SA_SEQUENCE, seq_index=SEQ_INDEX, base_prefix="")`.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task4.py
import build_web as bw

bw.build_sequence()
bw.build_alumnat_space()
bw.build_alumnat_sequence()

kinds = {e["kind"] for e in bw.ALUMNAT_SEQUENCE}
assert kinds <= {"hub", "fitxa"}, f"L'espai alumnat no hauria de tenir: {kinds - {'hub', 'fitxa'}}"

# Ha de tenir 2 entrades per SA (hub + fitxa) x 10 SA = 20
assert len(bw.ALUMNAT_SEQUENCE) == 20, len(bw.ALUMNAT_SEQUENCE)

nav = bw.step_nav("SA2_Dissenyem_en_2D", "index.html",
                   sequence=bw.ALUMNAT_SEQUENCE, seq_index=bw.ALUMNAT_SEQ_INDEX)
assert "pas següent" in nav
assert "🌟" not in nav and "exemple" not in nav.lower(), "No hi ha d'haver pas cap a l'exemple resolt"

print("OK task 4")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task4.py`
Expected: `AttributeError: module 'build_web' has no attribute 'build_alumnat_sequence'`

- [ ] **Step 3: Implementa la seqüència d'alumnat i parametritza `step_nav`**

Substitueix el bloc `build_web.py:427-470`:

```python
# Seqüència lineal única del recorregut de l'alumne: dins de cada SA es passa pels seus passos
# (hub → fitxa → exemple → activitats) i només al final se salta a la SA següent. Les pàgines
# de referència del docent (la SA completa i la rúbrica) NO són passos de l'alumne.
_WALK_PRIO = {"hub": -1, "fitxa": 0, "exemple": 1, "extra": 2}
SA_SEQUENCE = []            # [{folder, base, label, kind}] en ordre de recorregut (vista completa)
SEQ_INDEX = {}              # (folder, base) → posició a SA_SEQUENCE

# Recorregut mínim de l'alumnat: només hub i fitxa, sense exemple/rúbrica/doc.
_WALK_PRIO_ALUMNAT = {"hub": -1, "fitxa": 0}
ALUMNAT_SEQUENCE = []
ALUMNAT_SEQ_INDEX = {}


def _build_sequence_generic(walk_prio: dict) -> list[dict]:
    seq = []
    for code, name, _trim, _product, folder in SA_CARDS:
        seq.append({"folder": folder, "base": "index.html", "kind": "hub",
                    "label": f"{code} · {html.escape(name)}"})
        sibs = [s for s in sa_siblings(folder) if s[2] in walk_prio]
        for lbl, base, kind in sorted(sibs, key=lambda s: walk_prio[s[2]]):
            seq.append({"folder": folder, "base": base, "kind": kind,
                        "label": f"{code} · {lbl}"})
    return seq


def build_sequence():
    SA_SEQUENCE.clear()
    SEQ_INDEX.clear()
    SA_SEQUENCE.extend(_build_sequence_generic(_WALK_PRIO))
    for i, e in enumerate(SA_SEQUENCE):
        SEQ_INDEX[(e["folder"], e["base"])] = i


def build_alumnat_sequence():
    ALUMNAT_SEQUENCE.clear()
    ALUMNAT_SEQ_INDEX.clear()
    ALUMNAT_SEQUENCE.extend(_build_sequence_generic(_WALK_PRIO_ALUMNAT))
    for i, e in enumerate(ALUMNAT_SEQUENCE):
        ALUMNAT_SEQ_INDEX[(e["folder"], e["base"])] = i


def step_nav(folder: str, base: str, sequence: list[dict] = None,
             seq_index: dict = None) -> str:
    """Pas anterior / següent del recorregut (SA_SEQUENCE per defecte; passa
    ALUMNAT_SEQUENCE/ALUMNAT_SEQ_INDEX per generar-lo dins l'espai alumnat."""
    if sequence is None:
        sequence = SA_SEQUENCE
    if seq_index is None:
        seq_index = SEQ_INDEX
    i = seq_index.get((folder, base))
    if i is None:
        return ""

    def rel_href(e):
        return e["base"] if e["folder"] == folder else f'../{slugify(e["folder"])}/{e["base"]}'

    prev = sequence[i - 1] if i > 0 else None
    nxt = sequence[i + 1] if i < len(sequence) - 1 else None
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
```

`rel_href` no canvia: com que totes les pàgines d'alumnat viuen a `alumnat/classes/<slug>/...` amb la mateixa fondària relativa entre elles que les de `classes/<slug>/...`, el càlcul `../<slug>/<base>` és vàlid sense tocar-lo per cap dels dos espais.

Actualitza també la crida existent a `sa_context_bar` (`build_web.py:490-492`, es toca a la Task 6 quan es diferenciï per espai; de moment deixa-la intacta cridant `step_nav(folder, current_base)` — seguirà fent servir `SA_SEQUENCE`/`SEQ_INDEX` per defecte, comportament idèntic al d'abans).

Actualitza `main()` per cridar `build_alumnat_sequence()` just després de `build_alumnat_space()`:

```python
    build_sequence()
    build_alumnat_space()
    build_alumnat_sequence()
    pages = build_doc_pages()
```

- [ ] **Step 4: Executa la comprovació i confirma que passa**

Run: `py -3.11 check_task4.py`
Expected: `OK task 4`

- [ ] **Step 5: Verifica que la vista completa no ha canviat**

Run: `py -3.11 build_web.py && grep -A1 'sa-next' web/classes/sa2_dissenyem_en_2d/index.html`
Expected: el mateix contingut de pas següent que abans de la tasca (ha de continuar incloent l'exemple resolt al recorregut complet, ja que `sa_context_bar`/hub complet encara criden `step_nav` sense arguments extra).

- [ ] **Step 6: Neteja i commit**

```bash
rm check_task4.py
git add build_web.py
git commit -m "feat: seqüència de navegació pas-a-pas pròpia per a l'espai alumnat"
```

---

### Task 5: Hub mínim de SA per a l'alumnat

**Files:**
- Modify: `build_web.py:506-537` (`build_sa_hubs`)

**Interfaces:**
- Consumes: `sa_siblings()`, `sa_printables_html()` (sense canvis), `step_nav(..., sequence=ALUMNAT_SEQUENCE, seq_index=ALUMNAT_SEQ_INDEX)` (Task 4), `render_page(..., space="alumnat")` (Task 2).
- Produces: `build_sa_hub_full(...)`, `build_sa_hub_alumnat(...)`; `build_sa_hubs()` esdevé l'orquestrador que crida totes dues per cada SA.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task5.py
import build_web as bw
from pathlib import Path

bw.build_sequence(); bw.build_alumnat_space(); bw.build_alumnat_sequence()
bw.OUT.mkdir(exist_ok=True)
(bw.OUT / "assets").mkdir(exist_ok=True)
bw.build_doc_pages()
bw.build_sa_hubs()

alu_hub = Path("web/alumnat/classes/sa2_dissenyem_en_2d/index.html").read_text(encoding="utf-8")
assert "Fitxa de l'alumnat" in alu_hub
assert "Rúbrica" not in alu_hub, "El hub d'alumnat no ha de mostrar la rúbrica"
assert "Exemple resolt" not in alu_hub, "El hub d'alumnat no ha de mostrar l'exemple resolt"

full_hub = Path("web/classes/sa2_dissenyem_en_2d/index.html").read_text(encoding="utf-8")
assert "Rúbrica" in full_hub, "El hub complet ha de seguir mostrant la rúbrica (regressió)"

print("OK task 5")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task5.py`
Expected: `FileNotFoundError` (encara no existeix `web/alumnat/classes/.../index.html`)

- [ ] **Step 3: Divideix `build_sa_hubs`**

Substitueix `build_web.py:506-537`:

```python
def build_sa_hub_full(code, name, trim, product, folder):
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


def build_sa_hub_alumnat(code, name, trim, product, folder):
    slug = slugify(folder)
    out_rel = f"alumnat/classes/{slug}/index.html"
    sibs = sa_siblings(folder)
    fitxa = next((b for lbl, b, k in sibs if k == "fitxa"), None)
    primary = ""
    if fitxa:
        primary = (f'<a class="sa-primary" href="{fitxa}"><span class="sa-primary-ic">✏️</span>'
                   f'<span><strong>Fitxa de l\'alumnat</strong>'
                   f'<small>el full amb què treballes aquesta SA</small></span></a>')
    body = f"""
<h1>{code} · {html.escape(name)} <span class="badge badge-t{trim_num(trim)}">{trim}</span></h1>
<p class="product">{html.escape(product)}</p>
{primary}
{sa_printables_html(folder)}
<footer class="sa-foot">{step_nav(folder, "index.html", sequence=ALUMNAT_SEQUENCE, seq_index=ALUMNAT_SEQ_INDEX)}</footer>
"""
    crumb = [("Alumnat", "index.html"), (f"{code} · {name}" if len(f"{code} · {name}") < 60 else code, None)]
    (OUT / out_rel).parent.mkdir(parents=True, exist_ok=True)
    (OUT / out_rel).write_text(
        render_page(f"{code} · {name}", body, out_rel, crumb, space="alumnat"), encoding="utf-8")


def build_sa_hubs():
    """Una pàgina hub per SA a cada espai: entrada única igual des de tot arreu."""
    for code, name, trim, product, folder in SA_CARDS:
        build_sa_hub_full(code, name, trim, product, folder)
        build_sa_hub_alumnat(code, name, trim, product, folder)
```

Nota: el xip `sa_actual` de la capçalera (Task 2) desa/llegeix el **slug**; caldria que en entrar al hub d'una SA es desés automàticament com a "SA actual" (a més de fer-ho des del selector). Afegeix-ho amb un petit script inline al `body` del hub d'alumnat, just abans del `footer`:

```python
    body = f"""
<h1>{code} · {html.escape(name)} <span class="badge badge-t{trim_num(trim)}">{trim}</span></h1>
<p class="product">{html.escape(product)}</p>
{primary}
{sa_printables_html(folder)}
<footer class="sa-foot">{step_nav(folder, "index.html", sequence=ALUMNAT_SEQUENCE, seq_index=ALUMNAT_SEQ_INDEX)}</footer>
<script>try{{localStorage.setItem('sa_actual','{slug}')}}catch(e){{}}</script>
"""
```

(el `try/catch` evita trencar la pàgina si `localStorage` no és disponible, p. ex. mode privat estricte).

- [ ] **Step 4: Executa la comprovació i confirma que passa**

Run: `py -3.11 check_task5.py`
Expected: `OK task 5`

- [ ] **Step 5: Build completa (encara amb `verifica_web.py` en vermell, esperat)**

Run: `py -3.11 build_web.py`
Expected: sense excepcions.

- [ ] **Step 6: Neteja i commit**

```bash
rm check_task5.py
git add build_web.py
git commit -m "feat: hub mínim de SA per a l'espai alumnat (fitxa + imprimibles + pas ant/seg)"
```

---

### Task 6: Còpia física de pàgines dins `alumnat/` amb enllaços conscients de l'espai

**Files:**
- Modify: `build_web.py:190-245` (`rewrite_links`)
- Modify: `build_web.py:539-577` (`build_doc_pages`)

**Interfaces:**
- Consumes: `ALUMNAT_SPACE` (Task 1), `render_page(..., space=)` (Task 2).
- Produces: `rewrite_links(html_text, out_rel, current_rel_dir, space="full")`; `ALUMNAT_TARGETS: set[str]` (calculat dins `build_doc_pages`, out-paths de l'espai alumnat); `build_doc_pages()` genera també la còpia sota `alumnat/` per cada `.md` d'`ALUMNAT_SPACE`.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task6.py
import build_web as bw
from pathlib import Path

bw.build_sequence(); bw.build_alumnat_space(); bw.build_alumnat_sequence()
bw.OUT.mkdir(exist_ok=True)
(bw.OUT / "assets").mkdir(exist_ok=True)
bw.build_doc_pages()

fitxa_full = Path("web/classes/sa2_dissenyem_en_2d/fitxa_alumnat.html")
fitxa_alu = Path("web/alumnat/classes/sa2_dissenyem_en_2d/fitxa_alumnat.html")
assert fitxa_full.exists(), "Regressió: la còpia completa ha de seguir existint"
assert fitxa_alu.exists(), "Falta la còpia dins alumnat/"

diari_alu = Path("web/alumnat/avaluacio/diari-de-taller.html")
assert diari_alu.exists(), "Falta la còpia alumnat d'un ALUMNAT_LINKS"

text = fitxa_alu.read_text(encoding="utf-8")
assert 'href="../../../docent.html"' not in text and 'Docent</a>' not in text.split("<main")[0]

print("OK task 6")
```

(Ajusta el nom exacte de `diari-de-taller.html` al valor real de `PATH_MAP["Avaluació/Diari_de_taller.md"]` — comprova'l abans amb `py -3.11 -c "import build_web as bw; print(bw.PATH_MAP['Avaluació/Diari_de_taller.md'])"`.)

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task6.py`
Expected: `AssertionError: Falta la còpia dins alumnat/`

- [ ] **Step 3: Parametritza `rewrite_links` amb `space`**

A `build_web.py:190-245`, afegeix el paràmetre i la lògica de prefix. Substitueix la signatura i `fix_href`/`fix_code`/`fix_src`:

```python
def rewrite_links(html_text: str, out_rel: str, current_rel_dir: str, space: str = "full") -> str:
    prefix = rel_prefix(out_rel)

    def maybe_alumnat(target: str) -> str:
        """Dins l'espai alumnat, redirigeix el target cap a la seva còpia alumnat/
        si hi pertany; si no hi pertany, cau a la vista completa (comportament acceptat)."""
        if space == "alumnat" and target in ALUMNAT_TARGETS and not target.startswith("alumnat/"):
            return f"alumnat/{target}"
        return target

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
            target = "impressos/" + href.rsplit("/", 1)[-1]
        if target:
            return f'href="{prefix}{maybe_alumnat(target)}"'
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
            return f'<a class="doclink" href="{prefix}{maybe_alumnat(target)}"><code>{inner}</code></a>'
        return m.group(0)

    html_text = re.sub(r"<code>([^<]+)</code>", fix_code, html_text)

    # 3) imatges: <img src="ruta/relativa/al/repo"> → còpia dins web/ (no depèn de l'espai:
    #    els assets es comparteixen, no es dupliquen sota alumnat/)
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
```

`ALUMNAT_TARGETS` es defineix com a variable global (a prop d'`ALUMNAT_SPACE`, Task 1) però es calcula dins `build_doc_pages()` (Step 4) perquè necessita `PATH_MAP` complet i els slugs dels hubs de SA.

- [ ] **Step 4: Genera la còpia alumnat a `build_doc_pages`**

Afegeix, després de la declaració d'`ALUMNAT_SPACE` (Task 1), la variable global buida:

```python
ALUMNAT_TARGETS: set[str] = set()
```

Substitueix `build_web.py:539-577` (`build_doc_pages`):

```python
def build_doc_pages():
    ALUMNAT_TARGETS.clear()
    ALUMNAT_TARGETS.update(PATH_MAP[rel] for rel in ALUMNAT_SPACE)
    ALUMNAT_TARGETS.update(f"classes/{slugify(folder)}/index.html" for *_r, folder in SA_CARDS)

    pages = {}  # rel md → (title, out_rel)
    for p in MD_FILES:
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        out_rel = PATH_MAP[rel]
        text = p.read_text(encoding="utf-8")
        title = page_title(text, p.stem.replace("_", " "))
        MD.reset()
        body_md = MD.convert(text)
        current_dir = rel.rsplit("/", 1)[0] if "/" in rel else ""
        page_key = re.sub(r"[^a-z0-9]+", "_", out_rel[:-5].lower()).strip("_")

        # ── còpia completa (vista docent/general) ──
        body = rewrite_links(body_md, out_rel, current_dir, space="full")
        body = checkboxify(body, page_key)
        plain_src = body
        parts = rel.split("/")
        if len(parts) >= 3 and parts[0] == "Classes" and sa_idx(parts[1]) is not None:
            foot = sa_context_bar(parts[1], out_rel.rsplit("/", 1)[-1])
            body_full = f'<article class="doc">{body}<footer class="sa-foot">{foot}</footer></article>'
        else:
            body_full = f'<article class="doc">{body}</article>'
        crumb = [("Inici", "index.html")]
        if "/" in rel:
            section = rel.split("/")[0]
            crumb.append((section, slugify(section) + "/index.html"))
            if rel.count("/") > 1:
                crumb.append((rel.split("/")[1].replace("_", " "), None))
        crumb.append((title if len(title) < 60 else title[:57] + "…", None))
        out = OUT / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(title, body_full, out_rel, crumb), encoding="utf-8")
        pages[rel] = (title, out_rel)
        plain = re.sub(r"<[^>]+>", " ", plain_src)
        plain = re.sub(r"\s+", " ", html.unescape(plain)).strip()
        SEARCH_INDEX.append({"t": title, "u": out_rel,
                              "s": rel.split("/")[0] if "/" in rel else "Inici",
                              "x": plain[:4000], "sp": "full"})

        # ── còpia dins l'espai alumnat, només si el .md hi pertany ──
        if rel not in ALUMNAT_SPACE:
            continue
        MD.reset()
        body_alu = MD.convert(text)
        alu_out_rel = f"alumnat/{out_rel}"
        body_alu = rewrite_links(body_alu, alu_out_rel, current_dir, space="alumnat")
        body_alu = checkboxify(body_alu, "alu_" + page_key)
        plain_alu_src = body_alu
        if len(parts) >= 3 and parts[0] == "Classes" and sa_idx(parts[1]) is not None:
            foot = sa_context_bar(parts[1], out_rel.rsplit("/", 1)[-1], space="alumnat")
            body_alu = f'<article class="doc">{body_alu}<footer class="sa-foot">{foot}</footer></article>'
        else:
            body_alu = f'<article class="doc">{body_alu}</article>'
        alu_crumb = [("Alumnat", "index.html")]
        if len(parts) >= 3 and parts[0] == "Classes" and sa_idx(parts[1]) is not None:
            code, name, *_r = SA_CARDS[sa_idx(parts[1])]
            alu_crumb.append((f"{code} · {name}" if len(f"{code} · {name}") < 60 else code,
                              f"../index.html"))
        alu_crumb.append((title if len(title) < 60 else title[:57] + "…", None))
        alu_out = OUT / alu_out_rel
        alu_out.parent.mkdir(parents=True, exist_ok=True)
        alu_out.write_text(render_page(title, body_alu, alu_out_rel, alu_crumb, space="alumnat"),
                            encoding="utf-8")
        plain_alu = re.sub(r"<[^>]+>", " ", plain_alu_src)
        plain_alu = re.sub(r"\s+", " ", html.unescape(plain_alu)).strip()
        SEARCH_INDEX.append({"t": title, "u": alu_out_rel, "s": rel.split("/")[0] if "/" in rel else "Inici",
                              "x": plain_alu[:4000], "sp": "alumnat"})
    return pages
```

`sa_context_bar` encara no accepta `space=` — s'implementa a continuació.

- [ ] **Step 5: Fes que `sa_context_bar` sigui conscient de l'espai**

Substitueix `build_web.py:482-492`:

```python
def sa_context_bar(folder: str, current_base: str, space: str = "full") -> str:
    """Peu discret de cada pàgina d'una SA: germanes + imprimibles + prev/next (a sota de tot)."""
    if space == "alumnat":
        return (f'{sa_printables_html(folder)}'
                f'{step_nav(folder, current_base, sequence=ALUMNAT_SEQUENCE, seq_index=ALUMNAT_SEQ_INDEX)}')
    chips = [f'<a class="sa-hublink" href="index.html">⌂ Aquesta SA</a>']
    for lbl, base, _kind in sa_siblings(folder):
        if base == current_base:
            chips.append(f'<span class="sa-chip cur">{lbl}</span>')
        else:
            chips.append(f'<a class="sa-chip" href="{base}">{lbl}</a>')
    return (f'<div class="sa-sib">{"".join(chips)}</div>'
            f'{sa_printables_html(folder)}'
            f'{step_nav(folder, current_base)}')
```

(A l'espai alumnat s'omet la barra de "germanes" — fitxa/rúbrica/exemple/doc — perquè només hi ha una pàgina d'alumnat per SA, la fitxa; mostrar-la seria una llista d'un sol element sense sentit.)

- [ ] **Step 6: Executa la comprovació i confirma que passa**

Run: `py -3.11 check_task6.py`
Expected: `OK task 6`

- [ ] **Step 7: Build completa i `verifica_web.py`**

Run: `py -3.11 build_web.py && py -3.11 verifica_web.py`
Expected: `[OK]` — a partir d'aquesta tasca, tots els enllaços generats fins ara (selector, hubs, fitxes, documents transversals) han de resoldre; si `verifica_web.py` reporta trencats, revisa el nom exacte generat per `slugify()` per a `Avaluació/Diari_de_taller.md` i similar abans de continuar.

- [ ] **Step 8: Neteja i commit**

```bash
rm check_task6.py
git add build_web.py
git commit -m "feat: genera còpies físiques de fitxes i documents dins web/alumnat/"
```

---

### Task 7: Avís "material del professorat" a les pàgines docents d'una SA

**Files:**
- Modify: `build_web.py:539-577` (`build_doc_pages`, bloc de la còpia "full")

**Interfaces:**
- Consumes: `sa_idx()` (sense canvis), `ALUMNAT_TARGETS`/slug de la SA (Task 6).
- Produces: cap interfície nova cap a altres tasques — és l'última peça visible de la vista completa.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task7.py
import build_web as bw
from pathlib import Path

bw.build_sequence(); bw.build_alumnat_space(); bw.build_alumnat_sequence()
bw.OUT.mkdir(exist_ok=True); (bw.OUT / "assets").mkdir(exist_ok=True)
bw.build_doc_pages()

rubrica = next(p for p in Path("web/classes/sa2_dissenyem_en_2d").glob("rubrica*.html"))
text = rubrica.read_text(encoding="utf-8")
assert "material del professorat" in text.lower(), "Falta l'avís a la rúbrica"
assert 'href="../../alumnat/classes/sa2_dissenyem_en_2d/index.html"' in text

fitxa = Path("web/classes/sa2_dissenyem_en_2d/fitxa_alumnat.html").read_text(encoding="utf-8")
assert "material del professorat" not in fitxa.lower(), "La fitxa no ha de portar l'avís"

print("OK task 7")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 check_task7.py`
Expected: `AssertionError: Falta l'avís a la rúbrica`

- [ ] **Step 3: Afegeix l'avís al bloc "full" de `build_doc_pages`**

Dins `build_doc_pages()` (Task 6, Step 4), al tram on es construeix `body_full` per a pàgines de `Classes/<slug>/...`, distingeix entre la fitxa (sense avís) i la resta (rúbrica/exemple/doc, amb avís):

```python
        parts = rel.split("/")
        if len(parts) >= 3 and parts[0] == "Classes" and sa_idx(parts[1]) is not None:
            foot = sa_context_bar(parts[1], out_rel.rsplit("/", 1)[-1])
            notice = ""
            if not rel.endswith("Fitxa_alumnat.md"):
                slug = slugify(parts[1])
                notice = (f'<p class="teacher-notice">📖 Això és material del professorat — '
                          f'<a href="../../alumnat/classes/{slug}/index.html">torna a la teva SA</a></p>')
            body_full = f'<article class="doc">{notice}{body}<footer class="sa-foot">{foot}</footer></article>'
        else:
            body_full = f'<article class="doc">{body}</article>'
```

Nota: l'enllaç `../../alumnat/classes/{slug}/index.html` assumeix que la pàgina origen és `classes/<slug>/<fitxer>.html` (fondària 2, `rel_prefix` = `../../`); com que `notice` s'insereix literalment sense passar per `rewrite_links`, cal fer-lo servir amb el prefix ja calculat en comptes d'un valor fix. Substitueix per:

```python
                prefix_here = rel_prefix(out_rel)
                notice = (f'<p class="teacher-notice">📖 Això és material del professorat — '
                          f'<a href="{prefix_here}alumnat/classes/{slug}/index.html">torna a la teva SA</a></p>')
```

- [ ] **Step 4: Afegeix estil mínim per a `.teacher-notice` (accessibilitat: icona + text, ja inclosos)**

Comprova si `web_assets/style.css` ja té una classe d'avís reutilitzable:

Run: `grep -n "notice\|alert\|warn" web_assets/style.css | head -20`

Si no n'hi ha cap, afegeix al final de `web_assets/style.css`:

```css
.teacher-notice{background:var(--bg-card);border:2px solid var(--accent,#c0392b);
border-radius:.6rem;padding:.7rem 1rem;margin-bottom:1.2rem;font-weight:600}
.teacher-notice a{margin-left:.4rem}
```

(Ajusta els noms de variables CSS (`--bg-card`, `--accent`) als que ja fa servir el full d'estils — comprova'ls abans amb `grep -n "^\s*--" web_assets/style.css`.)

- [ ] **Step 5: Executa la comprovació i confirma que passa**

Run: `py -3.11 check_task7.py`
Expected: `OK task 7`

- [ ] **Step 6: Build completa i verificació**

Run: `py -3.11 build_web.py && py -3.11 verifica_web.py`
Expected: `[OK]`

- [ ] **Step 7: Neteja i commit**

```bash
rm check_task7.py
git add build_web.py web_assets/style.css
git commit -m "feat: avís de material del professorat a rúbrica/exemple/doc de cada SA"
```

---

### Task 8: Cerca separada per espai

**Files:**
- Modify: `build_web.py:767-809` (bloc de cerca dins `build_home`)

**Interfaces:**
- Consumes: `SEARCH_INDEX` amb camp `"sp"` (Task 6).
- Produces: `web/cerca.html` (vista completa, sense filtrar per `sp`) i `web/alumnat/cerca.html` (filtra `sp == "alumnat"`), compartint el mateix `assets/cerca-index.json`.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task8.py
import json
from pathlib import Path

idx = json.loads(Path("web/assets/cerca-index.json").read_text(encoding="utf-8"))
assert all("sp" in e for e in idx), "Totes les entrades han de tenir el camp 'sp'"
assert any(e["sp"] == "alumnat" for e in idx)
assert any(e["sp"] == "full" for e in idx)

assert Path("web/alumnat/cerca.html").exists(), "Falta cerca.html dins alumnat/"
alu_cerca = Path("web/alumnat/cerca.html").read_text(encoding="utf-8")
assert "sp===" in alu_cerca.replace(" ", "") or "sp==" in alu_cerca, "La cerca d'alumnat ha de filtrar per 'sp'"

print("OK task 8")
```

(Aquesta comprovació assumeix que ja s'ha executat `py -3.11 build_web.py` sencer abans — a diferència de les tasques anteriors, aquí cal la build completa perquè `cerca-index.json` es genera a `build_home`.)

- [ ] **Step 2: Executa `build_web.py` i la comprovació per confirmar que falla**

Run: `py -3.11 build_web.py && py -3.11 check_task8.py`
Expected: `AssertionError: Totes les entrades han de tenir el camp 'sp'` (encara no, `build_home` no ho escriu així) — de fet ja ho té gràcies a la Task 6 (`SEARCH_INDEX` ja porta `"sp"`); el que falla és `Falta cerca.html dins alumnat/`.

- [ ] **Step 3: Extreu el cos de cerca a una funció parametritzada**

Substitueix el bloc de cerca dins `build_home` (`build_web.py:767-809`):

```python
    # Cerca
    import json
    (OUT / "assets" / "cerca-index.json").write_text(
        json.dumps(SEARCH_INDEX, ensure_ascii=False), encoding="utf-8")
    build_search_page("cerca.html", [("Inici", "index.html"), ("Cerca", None)], space="full")
    build_search_page("alumnat/cerca.html", [("Alumnat", "index.html"), ("Cerca", None)], space="alumnat")
```

Afegeix la nova funció `build_search_page`, abans de `build_home` (per exemple just després de `card()`, `build_web.py:583`):

```python
def build_search_page(out_rel: str, crumb: list[tuple[str, str | None]], space: str) -> None:
    filter_js = "" if space == "full" else ".filter(p=>p.sp==='alumnat')"
    body = f"""
<h1>🔍 Cerca al material</h1>
<p class="lead">Cerca per paraula: «kerf», «tolerància», «carnet», «rúbrica SA5»…</p>
<p><input id="q" type="search" placeholder="Escriu i prem Enter…" autofocus
   style="width:100%;padding:.8rem 1.2rem;font-size:1.1rem;border-radius:999px;
          border:2px solid var(--line);background:var(--bg-card);color:var(--ink)"></p>
<div id="res"></div>
<script>
let IDX=null;
const q=document.getElementById('q'), res=document.getElementById('res');
async function cerca(){{
  if(!IDX) IDX=(await (await fetch('{rel_prefix(out_rel)}assets/cerca-index.json')).json()){filter_js};
  const terms=q.value.toLowerCase().split(/\\s+/).filter(t=>t.length>1);
  if(!terms.length){{res.innerHTML='';return;}}
  const out=[];
  for(const p of IDX){{
    const hay=(p.t+' '+p.x).toLowerCase();
    let score=0, ok=true;
    for(const t of terms){{
      const n=hay.split(t).length-1;
      if(!n){{ok=false;break;}}
      score+=n+(p.t.toLowerCase().includes(t)?8:0);
    }}
    if(ok) out.push([score,p,terms[0]]);
  }}
  out.sort((a,b)=>b[0]-a[0]);
  res.innerHTML=out.slice(0,25).map(([s,p,t])=>{{
    const i=p.x.toLowerCase().indexOf(t);
    const frag=i<0?p.x.slice(0,160):p.x.slice(Math.max(0,i-70),i+110);
    return `<a class="card" href="{rel_prefix(out_rel)}${{p.u}}"><div class="card-icon">📄</div>
      <div><h3>${{p.t}} <span class="badge">${{p.s}}</span></h3><p>…${{frag}}…</p></div></a>`;
  }}).join('')||'<p>Cap resultat. Prova una paraula més curta o sense accents.</p>';
}}
q.addEventListener('input',()=>{{clearTimeout(q._d);q._d=setTimeout(cerca,250);}});
</script>
"""
    (OUT / out_rel).parent.mkdir(parents=True, exist_ok=True)
    (OUT / out_rel).write_text(render_page("Cerca", body, out_rel, crumb, space=space),
                                encoding="utf-8")
```

Nota important sobre `${p.u}`: com que `p.u` per a l'espai "full" ja és una ruta arrel-relativa vàlida (p. ex. `classes/sa2.../rubrica.html`) i per a "alumnat" les entrades filtrades tenen `u` amb el prefix `alumnat/...` (perquè la Task 6 hi guarda `alu_out_rel = f"alumnat/{out_rel}"`), l'enllaç final `href="{prefix}${{p.u}}"` funciona igual en ambdós espais sense lògica addicional.

- [ ] **Step 4: Executa la comprovació i confirma que passa**

Run: `py -3.11 build_web.py && py -3.11 check_task8.py`
Expected: `OK task 8`

- [ ] **Step 5: `verifica_web.py`**

Run: `py -3.11 verifica_web.py`
Expected: `[OK]` (el codi JS de cerca és dins `<script>`, que `verifica_web.py` ja exclou explícitament — `build_web.py` comentari a `verifica_web.py:39`).

- [ ] **Step 6: Neteja i commit**

```bash
rm check_task8.py
git add build_web.py
git commit -m "feat: cerca separada per espai (alumnat/cerca.html filtra només el seu contingut)"
```

---

### Task 9: Portada apunta al nou selector; retira `alumnat.html` antic

**Files:**
- Modify: `build_web.py:613-670` (`build_home`, secció de portada i de l'antiga pàgina `alumnat.html`)

**Interfaces:**
- Consumes: `build_alumnat_home()` (Task 3).
- Produces: cap interfície nova — és l'últim cablejat visible des de la portada general.

- [ ] **Step 1: Escriu la comprovació que ha de fallar**

```python
# check_task9.py
from pathlib import Path

home = Path("web/index.html").read_text(encoding="utf-8")
assert 'href="alumnat/index.html"' in home, "El botó 'Soc alumne/a' ha d'apuntar al selector"
assert not Path("web/alumnat.html").exists(), "L'antiga alumnat.html ja no s'ha de generar"

print("OK task 9")
```

- [ ] **Step 2: Executa-la per confirmar que falla**

Run: `py -3.11 build_web.py && py -3.11 check_task9.py`
Expected: `AssertionError: El botó 'Soc alumne/a' ha d'apuntar al selector` (ara apunta a `alumnat.html`)

- [ ] **Step 3: Actualitza l'enllaç de la portada i elimina el bloc antic**

A `build_web.py:613-643` (`build_home`, secció hero), canvia:

```python
    <a class="btn" href="alumnat.html">🧑‍🎓 Soc alumne/a</a>
```

per:

```python
    <a class="btn" href="alumnat/index.html">🧑‍🎓 Soc alumne/a</a>
```

Elimina completament el bloc que genera l'antiga `web/alumnat.html` (`build_web.py:644-669`, des del comentari `# Alumnat` fins abans del comentari `# Docent`):

```python
    # Alumnat
    cards = "\n".join(card(PATH_MAP[rel], icon, t, d) for icon, t, rel, d in ALUMNAT_LINKS)
    fitxes = "\n".join(
        f'<a class="chip" href="classes/{slugify(folder)}/index.html">{code}</a>'
        for code, _n, _t, _p, folder in SA_CARDS)
    body = f"""
...
"""
    (OUT / "alumnat.html").write_text(
        render_page("Alumnat", body, "alumnat.html",
                    [("Inici", "index.html"), ("Alumnat", None)]), encoding="utf-8")
```

(Elimina tot el bloc; `build_alumnat_home()`, ja cridada a `main()` des de la Task 3, cobreix la mateixa necessitat amb el nou selector.)

Comprova que cap altra part de `build_web.py` referenciï `"alumnat.html"` (a diferència d'`"alumnat/index.html"`):

Run: `grep -n '"alumnat\.html"' build_web.py`
Expected: cap resultat.

- [ ] **Step 4: Executa la comprovació i confirma que passa**

Run: `py -3.11 build_web.py && py -3.11 check_task9.py`
Expected: `OK task 9`

- [ ] **Step 5: `verifica_web.py` sencer**

Run: `py -3.11 verifica_web.py`
Expected: `[OK]` — comprova especialment que cap enllaç antic cap a `alumnat.html` (p. ex. des de `docent.html` o algun `.md`) hagi quedat penjant. Si `verifica_web.py` reporta un trencat cap a `alumnat.html`, localitza'l amb:

Run: `grep -rn "alumnat\.md\]\|Alumnat\.md" --include="*.md" .`

i redirigeix aquella referència cap a un dels documents concrets d'`ALUMNAT_LINKS` (mai cap a l'antiga pàgina eliminada).

- [ ] **Step 6: Neteja i commit**

```bash
rm check_task9.py
git add build_web.py
git commit -m "feat: la portada porta al nou selector d'alumnat; retira l'antiga alumnat.html"
```

---

### Task 10: Verificació final completa i revisió manual

**Files:** cap modificació — tasca de verificació.

- [ ] **Step 1: Build neta des de zero**

Run: `rm -rf web && py -3.11 build_web.py`
Expected: acaba amb `Web generada a ... — N pàgines de contingut.` sense excepcions.

- [ ] **Step 2: Els tres verificadors del CI, en l'ordre del `CLAUDE.md`**

Run:
```bash
py -3.11 verifica_enllacos.py
py -3.11 verifica_competencies.py
py -3.11 verifica_web.py
```
Expected: els tres surten amb `[OK]` / codi 0.

- [ ] **Step 3: Inspecció manual del recorregut sencer de l'alumne**

Obre `web/index.html` en un navegador (o `python -m http.server` des de `web/`) i recorre:
1. Portada → «🧑‍🎓 Soc alumne/a» → ha d'obrir el selector amb 10 targetes SA0-SA9 i, a sota, "Documents del curs".
2. Tria "SA2" → ha d'obrir el hub mínim (només fitxa + imprimibles si n'hi ha + pas ant/seg), sense rúbrica ni exemple.
3. Clica la fitxa → capçalera reduïda, xip "📍 sa2_dissenyem_en_2d" visible, breadcrumb de 2 nivells.
4. Clica "pas següent" diverses vegades → ha d'anar SA0→SA1→SA2→...→SA9 saltant-se exemple/rúbrica/doc, i acabar amb "fi del curs 🎉".
5. Clica "🔁 Canviar de SA" → torna al selector.
6. Vés a la vista completa (`web/docent.html` o `web/classes/sa2.../index.html`) → ha de continuar mostrant fitxa+rúbrica+exemple+doc com sempre.
7. Obre la rúbrica o l'exemple resolt d'una SA des de la vista completa → ha d'aparèixer l'avís "📖 Això és material del professorat" amb enllaç de tornada al hub d'alumnat d'aquella SA.
8. Prova la cerca dins `alumnat/cerca.html` amb una paraula que només existeixi a una rúbrica (p. ex. un criteri d'avaluació) → no ha d'aparèixer als resultats. Prova la mateixa paraula a `web/cerca.html` (vista completa) → sí ha d'aparèixer.

- [ ] **Step 4: Neteja del directori de treball**

Run: `git status`
Expected: només canvis a `build_web.py`, `web_assets/style.css` i els fitxers de spec/pla dins `docs/superpowers/`; `web/` no s'ha de commitejar (regla del CLAUDE.md: és artefacte generat, hauria d'estar gitignored — comprova `.gitignore` si `git status` mostra `web/` com a "untracked").

- [ ] **Step 5: Commit final (si queda alguna cosa pendent de les tasques anteriors)**

```bash
git status
git add -A -- build_web.py web_assets/style.css
git commit -m "chore: verificació final de la navegació separada per a l'alumnat" --allow-empty-message
```

(Només si `git status` mostra canvis pendents; si totes les tasques anteriors ja s'han comès individualment, aquest pas pot no generar cap commit nou.)
