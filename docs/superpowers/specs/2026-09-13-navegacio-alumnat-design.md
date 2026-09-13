# Disseny: separació de la navegació alumnat / vista completa

**Data:** 2026-09-13
**Estat:** aprovat pel docent, pendent d'implementació

## Problema

Després de la primera setmana d'ús real a l'aula, l'alumnat valora molt bé els
continguts però troba la navegació de la web molt difícil:

1. No sap per on començar cada sessió.
2. Es perd entre fitxa / rúbrica / exemple resolt / doc del docent dins d'una
   mateixa SA — massa material semblant barrejat a un sol hub.
3. No entén on és ni com tornar enrere (breadcrumbs i barra de context actuals
   pensats per a un ús "docent", amb massa nivells).

L'estructura de continguts (`.md`) és bona; el problema és exclusivament de
**navegació i presentació** generada per `build_web.py`.

## Objectiu

Separar físicament, dins de `web/`, un recorregut d'alumnat mínim i lineal
(`web/alumnat/...`) de la vista completa actual (que continua servint
docents, famílies i públic general amb tota la profunditat existent —
fitxa+rúbrica+exemple+doc, totes les seccions).

## Abast

- Només toca `build_web.py` (generador) i, si cal, `verifica_web.py`
  (verificació d'enllaços de la web generada).
- **Cap canvi als `.md` font**: `Fitxa_alumnat.md`, `Rubrica_SAx.md`,
  `SAx.md`, `Exemple_resolt.md` i la resta de continguts d'`ALUMNAT_LINKS`
  no es toquen.
- `web/` és artefacte generat (regla del CLAUDE.md): no es versiona a mà,
  només es regenera.

## Disseny

### 1. Dos espais dins de la mateixa web generada

- **Vista completa** (com ara): portada, `docent.html`, `families.html`,
  totes les seccions (`Classes/`, `Avaluació/`, etc.) amb el hub de SA
  complet (fitxa + rúbrica + exemple + doc), breadcrumbs de fins a 4 nivells,
  capçalera amb `Inici / Les 9 SA / Docent / Alumnat / Famílies / Cerca`.
- **Espai alumnat nou** (`web/alumnat/...`): subarbre separat, generat com a
  **còpies físiques** (no amb JS de mode) de només les pàgines que pertanyen
  al recorregut de l'alumne, amb capçalera i breadcrumbs reduïts.

La portada general (`index.html`) manté el tri de rols; el botó
"🧑‍🎓 Soc alumne/a" porta a `alumnat/index.html` en comptes de l'actual
`alumnat.html`. `alumnat.html` (l'índex actual, orientat a llistat de
documents) desapareix, fusionat dins del nou espai.

### 2. `ALUMNAT_SPACE`: font única de veritat

Nova estructura a `build_web.py` que decideix quins `.md` pertanyen al
recorregut de l'alumnat:

- Totes les `Fitxa_alumnat.md` de cada `Classes/SAx_*/`.
- Tots els `.md` ja referenciats a `ALUMNAT_LINKS` (diari de classe,
  vocabulari, diari de taller, primers auxilis, semàfor, avaluació explicada,
  rúbrica amigable, passaport, reptes express, projecte personal, normes de
  seguretat, protocol VR, grans idees, museu dels errors).
- **Explícitament fora**: `Rubrica_SAx.md`, `Exemple_resolt.md`, `SAx.md`
  (doc del docent) — només a la vista completa.

Cap fitxer es marca "és d'alumnat" en dos llocs diferents del codi; tot
consulta `ALUMNAT_SPACE`.

### 3. Contingut de l'espai alumnat

- **`alumnat/index.html`** — selector: 10 targetes SA0–SA9 (reaprofita
  `sa_cards()`). En triar-ne una: desa `localStorage.sa_actual = folder` i
  redirigeix al hub d'aquella SA. Enllaç petit i sempre visible "🔁 Veure-les
  totes" per tornar-hi.
- **`alumnat/classes/<slug>/index.html`** — hub mínim d'una SA: fitxa de
  l'alumnat destacada + imprimibles (`sa_printables_html`, ja existent) + pas
  anterior/pas següent. Sense targetes de rúbrica/exemple/doc.
- **`alumnat/classes/<slug>/fitxa_alumnat.html`** — la fitxa, amb capçalera i
  breadcrumb reduïts.
- **`alumnat/<ruta original>`** per a cada document d'`ALUMNAT_LINKS` (p. ex.
  `alumnat/avaluacio/diari-de-taller.html`), mateix criteri de capçalera
  reduïda.

### 4. Capçalera i breadcrumbs reduïts (dins d'`alumnat/`)

- Capçalera: `⌂ Inici (alumnat)` · xip persistent `📍 SAx` (llegit de
  `localStorage.sa_actual`, clicable → hub d'aquella SA) · `🔁 Canviar de SA`
  · `🔍 Cerca` · botons d'accessibilitat (es mantenen tal qual: A−/A+,
  espaiat, veu, tema, rellotge). **Sense** "Les 9 SA" / "Docent" /
  "Famílies".
- Breadcrumb: màxim 2 nivells amb sentit —
  `🧑‍🎓 Alumnat › SA2 · Dissenyem en 2D › Fitxa` — mai "Classes" ni la resta
  de jerarquia de carpetes real.
- Barra de pas anterior/següent (`step_nav`, ja existent): la seqüència
  `_WALK_PRIO` per a aquest espai es redueix a `{"hub": -1, "fitxa": 0}` —
  s'elimina "exemple"/"extra" del recorregut de l'alumne (aquest material ja
  no hi és present).

### 5. Avís en arribar per error a una pàgina docent

Si un alumne obre (per URL compartida, resultat de cerca antic, etc.) una
pàgina de la vista completa que pertany a una SA (rúbrica, exemple, doc), la
pàgina mostra un avís discret sobre l'`<article class="doc">`: "📖 Això és
material del professorat — torna a la teva SA" amb enllaç directe a
`alumnat/classes/<slug>/index.html`. No s'aplica a la resta de la vista
completa (docent.html, families.html, seccions no lligades a una SA).

### 6. Implementació tècnica a `build_web.py`

- `render_page(title, body, out_rel, crumb, space="full")`: paràmetre nou
  `space` que tria quina capçalera/nav HTML es genera. L'esquelet HTML, CSS,
  i el bloc `<script>` (tema, mida de lletra, espaiat, veu, rellotge,
  checklists) es comparteixen sense duplicar-se; només s'hi afegeix la
  lectura/escriptura de `localStorage.sa_actual` amb el mateix patró ja
  existent per `theme`/`fs`.
- `build_doc_pages()`: per cada `.md` d'`ALUMNAT_SPACE`, després de generar
  la còpia "full" com ara, genera una segona crida a `render_page(...,
  space="alumnat")` desada sota `alumnat/<ruta relativa>`. `resolve_ref()` ha
  de resoldre els enllaços interns d'una pàgina que ja és dins `alumnat/`
  cap a una altra pàgina `alumnat/` quan el target pertany a `ALUMNAT_SPACE`,
  i només caure cap a la vista completa quan el target no hi pertany (p. ex.
  un enllaç puntual des d'una fitxa cap a una rúbrica, si n'hi hagués).
- `build_sa_hubs()` es divideix en `build_sa_hub_full()` (comportament actual
  intacte) i `build_sa_hub_alumnat()` (nou, descrit al punt 3).
- Cerca: un únic `cerca-index.json` amb un camp `space` per entrada
  (`"full"` o `"alumnat"`). Es genera `cerca.html` en totes dues variants
  (full i alumnat); cada variant filtra pel seu propi `space` (l'alumnat mai
  veu resultats docents; la vista completa continua veient-ho tot, sense
  filtrar, com ara).
- `copy_assets()`: sense canvis (els assets es referencien amb rutes
  relatives ja calculades per `rel_prefix`, vàlides també des d'`alumnat/`).

### 7. Verificació

- `verifica_web.py` (enllaços de la web generada, ja al CI) haurà de
  travessar també `web/alumnat/**` i entendre que hi ha dues còpies
  legítimes de moltes pàgines — no ha de marcar-ho com a duplicat erroni.
- `verifica_enllacos.py` i `verifica_competencies.py` (sobre els `.md` font)
  no es veuen afectats: no es toca cap `.md`.

## Fora d'abast (YAGNI)

- No es crea cap sistema de rols/login; la separació és purament d'estructura
  de navegació generada, com fins ara amb `docent.html`/`alumnat.html`.
- No es canvia el contingut de cap `.md`, ni l'estil visual (`style.css`) més
  enllà del que calgui per a la capçalera reduïda.
- No es toca el recorregut de la vista completa (`SA_SEQUENCE` "full" amb
  hub→fitxa→exemple→extra) — es manté intacte per a ús docent.
- No s'introdueix detecció automàtica de "quina SA toca per data"; la
  selecció és manual i persistent via `localStorage`.

## Testing

- Regenerar amb `python build_web.py` (Python 3.11, no el del PATH) i
  verificar manualment:
  - `alumnat/index.html` mostra les 10 SA i desa la selecció.
  - El hub d'una SA a `alumnat/` només mostra fitxa + imprimibles + pas
    ant/seg.
  - Els enllaços interns de les pàgines d'`alumnat/` no s'escapen mai cap a
    `classes/...` (vista completa) llevat del cas explícit de l'avís de
    "material del professorat".
  - La vista completa (`docent.html`, hubs de SA complets) no ha canviat de
    comportament.
- Executar `verifica_web.py` i confirmar que no reporta cap enllaç trencat
  ni cap falç positiu de duplicat a `alumnat/`.
- Executar `verifica_enllacos.py` i `verifica_competencies.py` (no haurien
  de veure's afectats, però formen part del gate de pre-commit/CI).
