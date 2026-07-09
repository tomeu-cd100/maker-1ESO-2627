# Prova 2 interactiva — «Permès o prohibit?» (quiz de materials)

**Data:** 2026-07-09
**Pàgina afectada:** `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md`
→ es publica a `web/classes/sa0_punt_de_partida/material_gimcana_seguretat.html`

## Objectiu

Fer la **Prova 2** de la gimcana de seguretat (SA0) més interactiva: convertir la
taula estàtica de classificació de materials en un **quiz autocorrectiu** que
l'alumnat pugui fer de manera individual o en parelles al Chromebook, amb feedback
immediat i, sobretot, el **«per què»** de cada resposta (que és el que de veritat
s'aprèn).

## Context i restriccions

- Web estàtica generada per `build_web.py` des dels `.md`. Sense backend ni frameworks.
- Desplegament per GitHub Pages (Linux, sensible a majúscules).
- Públic: 1r ESO (~12 anys), en **Chromebooks** (touchpad; alguns tàctils).
- La web ja té ajustos d'accessibilitat (mida de lletra, espaiat dislèxia, TTS 🔊,
  mode fosc) basats en variables CSS i `data-*` a `<html>`.
- `python-markdown` deixa passar **HTML i `<script>` en brut** dins d'un `.md`, així
  que es pot incrustar el widget directament a la secció Prova 2.
- Aquesta pàgina és **material del docent**: la taula actual fa de full de respostes
  i és imprimible per retallar les targetes físiques. No s'ha de perdre.

## Decisions preses (brainstorming)

- **Ús principal:** individual/parelles al Chromebook, autocorrectiu.
- **Mecànica:** quiz **una targeta cada cop** amb 3 botons
  (✅ Permès · ⚠️ Cal preguntar · ❌ Prohibit). Descartat drag & drop (fràgil amb
  touchpad i pitjor per a accessibilitat/teclat).
- **La taula:** passa a `<details>` plegable sota el joc («full de respostes»).
- **En fallar (decisió A):** revela la resposta correcta + el perquè i avança; marca
  el material per repassar al final. No obliga a reintentar.
- **Toc de joc (decisió B):** lleuger — comptador d'encerts i ratxa 🔥, sense estats
  de «perdre» ni rànquings.
- **Ordre (decisió C):** materials **remesclats** cada partida.

## Disseny funcional

### Pantalles / estats

1. **Inici:** títol curt, botó gran **«Comença»**, comptador «12 materials».
2. **Jugant:** targeta gran amb el nom del material · «Material X de 12» · barra de
   progrés · 3 botons (✅ Permès · ⚠️ Cal preguntar · ❌ Prohibit).
3. **Feedback:** en triar, revela encert/error **amb icona + text** (mai només color)
   i **sempre el «per què»** ben visible. Botó **«Següent →»**.
4. **Final:** resum d'encerts a la primera + llista **«Repassa aquests»** amb els
   materials fallats i el seu perquè. Botó **«Torna a jugar»** (remescla i reinicia).

### Font de les dades (una sola font de veritat)

El quiz **llegeix les preguntes de la mateixa taula de materials** ja existent:
parseja cada fila de `<tbody>` per obtenir:

- **nom del material** (col. 1, es pot netejar de `<strong>`),
- **categoria** a partir de l'emoji de la col. 2: `✅ → Permès`, `⚠️ → Cal
  preguntar`, `❌ → Prohibit`,
- **«per què»** (col. 3, es conserva l'HTML `<strong>` per ressaltar).

Així, si el docent edita la taula al Markdown, el quiz s'actualitza sol. Cap
duplicació de dades. (Les 12 files actuals: 3 ✅ · 4 ⚠️ (paper, metacrilat, fusta amb
vernís, menjar) · 5 ❌ — però el joc s'adapta sigui quin sigui el recompte.)

### Accessibilitat

- Botons `<button>` reals: operables amb **teclat i touchpad**, focus visible.
- Feedback amb **icona + text**, mai només color (verd/ambre/vermell són reforç).
- Regió `aria-live="polite"` que anuncia el resultat + perquè (compatible amb el TTS).
- Hereta mode fosc / mida de lletra / espaiat dislèxia via **variables CSS existents**.

## Disseny tècnic

### Integració

- Bloc **HTML + `<script>` en brut** dins de `Material_gimcana_seguretat.md`, a la
  secció «Prova 2», **abans** de la taula.
- La taula existent s'embolcalla en `<details><summary>Mostra el full de
  respostes</summary>…</details>`.
- Tot l'HTML/JS/CSS del widget va amb **prefix propi** (`id="joc-p2"`, classes
  `jp2-…`) per no col·lidir amb l'script global de la plantilla (`build_web.py`
  `render_page`, que usa `el('theme')`, etc.).
- El `<script>` del widget s'auto-inicialitza en carregar (`DOMContentLoaded` o
  execució directa, ja que va al final del cos de l'article).

### Estils

- CSS nou **scoped** a `.jp2-…` afegit a `web_assets/style.css`, usant les variables
  del tema (`--accent`, `--accent-soft`, `--bg-card`, `--line`, `--ink`,
  `--ink-soft`, `--shadow`) perquè funcioni en clar i fosc.

### Riscos / punts de verificació

- **Parsing de la taula:** el `<script>` s'executa després que la taula existeixi al
  DOM. Com que el bloc del joc va **abans** de la taula, cal esperar el DOM
  (`DOMContentLoaded`) o seleccionar per un `id` a la taula.
- **`rewrite_links` de `build_web.py`** fa regex sobre `href=`, `<code>` i `src=`.
  El widget no ha d'usar `href`/`src` a rutes que es puguin reescriure per accident;
  si cal enllaçar, evitar patrons `.md`/`.svg`/`.png` no intencionats.
- **CI:** `verifica_enllacos.py` i `verifica_competencies.py` han de continuar en verd;
  el contingut nou no afegeix enllaços interns trencats.
- **Emoji com a clau:** el mapatge depèn dels emojis exactes de la taula
  (`✅`/`⚠️`/`❌`). Verificar que es detecten (l'emoji ⚠️ pot portar variant selector).

## Fora d'abast (YAGNI)

- Persistència de puntuació (localStorage), rànquings, temporitzador.
- Versió projectada per a tota la classe o mode multijugador.
- Reutilització del motor per a altres proves (Prova 3/4) — es podrà valorar després.

## Verificació d'acceptació

1. `python build_web.py` (Python 3.11) genera la pàgina sense errors.
2. A la pàgina publicada, la secció Prova 2 mostra el joc; «Comença» inicia el quiz.
3. Triar una categoria revela encert/error + el «per què»; «Següent» avança.
4. En acabar, es veu el resum i «Torna a jugar» reinicia remesclant.
5. Funciona amb **teclat** (tab + enter/espai) i en **mode fosc**.
6. `verifica_enllacos.py` i `verifica_competencies.py` continuen en verd.
