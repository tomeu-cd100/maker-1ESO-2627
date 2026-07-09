# Prova 2 interactiva (quiz de materials) — Pla d'implementació

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Afegir un quiz autocorrectiu «Permès o prohibit?» a la secció Prova 2 de la pàgina de material de la gimcana (SA0), que llegeix les preguntes de la taula de materials existent.

**Architecture:** Widget HTML + `<script>` en brut incrustat al Markdown font, just abans de la taula de materials. En carregar la pàgina, el JS parseja la taula (nom / emoji categoria / per què), l'embolcalla en un `<details>` plegable com a full de respostes, i mostra un quiz targeta a targeta. Estils scoped a `web_assets/style.css`. Cap canvi a `build_web.py`.

**Tech Stack:** Markdown (python-markdown), JavaScript vanilla (IIFE, sense dependències), CSS amb les variables de tema existents.

## Global Constraints

- **Build:** `python-markdown` via `build_web.py`. Executar-lo amb Python 3.11: `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" build_web.py` (el `python` del PATH és l'Inkscape).
- **`web/` és `.gitignore`:** no s'ha de fer commit; la construeix la GitHub Action `pages.yml`. Es build localment només per verificar.
- **Commits en català**, amb trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- **CI verd:** `verifica_enllacos.py` i `verifica_competencies.py` han de continuar passant (exit 0).
- **Accessibilitat:** feedback amb icona **+ text** (mai només color); botons `<button>` reals operables amb teclat; regió `aria-live="polite"`; usar variables CSS del tema (mode fosc/mida de lletra automàtics).
- **Aïllament:** tot el widget amb prefix `jp2-` / `id="joc-p2"` per no col·lidir amb l'script global de la plantilla.
- **Font única de veritat:** el quiz deriva les dades de la taula existent; no duplicar la llista de materials.
- **Sense framework de test JS al projecte:** la verificació és build + `grep` sobre l'HTML generat + comprovació al navegador (checklist explícita a cada tasca).

---

### Task 1: Widget del quiz (comportament) al Markdown

**Files:**
- Modify: `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md` (inserir el bloc just abans de la taula de Prova 2, entre el paràgraf «Retalleu una targeta per material…» i la línia `| Targeta | Resposta | …`)

**Interfaces:**
- Consumes: la taula Markdown de Prova 2 ja existent (12 files: col.1 material, col.2 emoji `✅`/`⚠️`/`❌`, col.3 per què).
- Produces: element `#joc-p2` amb el widget; en runtime, un `<details class="jp2-taula">` que embolcalla la taula. Classes CSS que la Task 2 estilitzarà: `jp2`, `jp2-inici`, `jp2-titol`, `jp2-sub`, `jp2-btn`, `jp2-comenca`, `jp2-joc`, `jp2-barra`, `jp2-barra-plena`, `jp2-progres`, `jp2-carta`, `jp2-material`, `jp2-opcions`, `jp2-op`, `jp2-ok`, `jp2-ko`, `jp2-feedback`, `jp2-fb-ok`, `jp2-fb-ko`, `jp2-seguent`, `jp2-final`, `jp2-resultat`, `jp2-repas`, `jp2-repas-tit`, `jp2-torna`, `jp2-taula`.

- [ ] **Step 1: Inserir el bloc del widget al Markdown**

Al fitxer `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md`, localitzar aquestes dues línies consecutives dins de «Prova 2»:

```markdown
Retalleu una targeta per material. L'equip les classifica en **PERMÈS / PROHIBIT / CAL
PREGUNTAR** i explica per què.
```

I inserir **després** (amb una línia en blanc abans i després) tot aquest bloc HTML+JS, de manera que quedi entre aquell paràgraf i la línia `| Targeta | Resposta | Per què (per al docent) |`:

```html
<div id="joc-p2" class="jp2">
  <div class="jp2-inici">
    <p class="jp2-titol">🎮 Joc: classifica els materials</p>
    <p class="jp2-sub">Tens <strong class="jp2-total-inici">12</strong> materials. Digues si cada un és <strong>permès</strong>, <strong>cal preguntar</strong> o <strong>prohibit</strong>… i mira'n el perquè.</p>
    <button type="button" class="jp2-btn jp2-comenca">Comença ▶</button>
  </div>

  <div class="jp2-joc" hidden>
    <div class="jp2-barra"><div class="jp2-barra-plena"></div></div>
    <p class="jp2-progres">Material <span class="jp2-n">1</span> de <span class="jp2-t">12</span> · encerts a la primera: <span class="jp2-encerts">0</span> · ratxa 🔥 <span class="jp2-ratxa">0</span></p>
    <div class="jp2-carta"><span class="jp2-material">—</span></div>
    <div class="jp2-opcions">
      <button type="button" class="jp2-btn jp2-op" data-cat="permes">✅ Permès</button>
      <button type="button" class="jp2-btn jp2-op" data-cat="cal-preguntar">⚠️ Cal preguntar</button>
      <button type="button" class="jp2-btn jp2-op" data-cat="prohibit">❌ Prohibit</button>
    </div>
    <div class="jp2-feedback" aria-live="polite"></div>
    <button type="button" class="jp2-btn jp2-seguent" hidden>Següent →</button>
  </div>

  <div class="jp2-final" hidden>
    <p class="jp2-titol">🏁 Fet!</p>
    <p class="jp2-resultat"></p>
    <div class="jp2-repas"></div>
    <button type="button" class="jp2-btn jp2-torna">↺ Torna a jugar</button>
  </div>
</div>

<script>
(function () {
  function init() {
    var arrel = document.getElementById('joc-p2');
    if (!arrel) return;

    var ETIQUETA = { 'permes': '✅ Permès', 'cal-preguntar': '⚠️ Cal preguntar', 'prohibit': '❌ Prohibit' };

    function trobaTaula(node) {
      var n = node.nextElementSibling;
      while (n && n.tagName !== 'TABLE') n = n.nextElementSibling;
      return n;
    }
    function categoria(text) {
      if (text.indexOf('✅') !== -1) return 'permes';
      if (text.indexOf('❌') !== -1) return 'prohibit';
      if (text.indexOf('⚠') !== -1) return 'cal-preguntar';
      return null;
    }
    function llegeixDades(taula) {
      var dades = [], files = taula.querySelectorAll('tbody tr');
      for (var i = 0; i < files.length; i++) {
        var cel = files[i].querySelectorAll('td');
        if (cel.length < 3) continue;
        var cat = categoria(cel[1].textContent);
        if (!cat) continue;
        dades.push({ nom: cel[0].textContent.trim(), cat: cat, perque: cel[2].innerHTML.trim() });
      }
      return dades;
    }
    function barreja(a) {
      for (var i = a.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
      }
      return a;
    }

    var taula = trobaTaula(arrel);
    if (!taula) return;
    var DADES = llegeixDades(taula);
    if (!DADES.length) return;

    // amaga la taula dins un desplegable (full de respostes del docent)
    var det = document.createElement('details');
    det.className = 'jp2-taula';
    var sum = document.createElement('summary');
    sum.textContent = 'Mostra el full de respostes (per al docent)';
    taula.parentNode.insertBefore(det, taula);
    det.appendChild(sum);
    det.appendChild(taula);

    var $ = function (s) { return arrel.querySelector(s); };
    var vistaInici = $('.jp2-inici'), vistaJoc = $('.jp2-joc'), vistaFinal = $('.jp2-final');
    var elMaterial = $('.jp2-material'), elFeedback = $('.jp2-feedback'), elSeguent = $('.jp2-seguent');
    var elN = $('.jp2-n'), elT = $('.jp2-t'), elEncerts = $('.jp2-encerts'), elRatxa = $('.jp2-ratxa');
    var elBarra = $('.jp2-barra-plena');
    var opcions = arrel.querySelectorAll('.jp2-op');
    $('.jp2-total-inici').textContent = DADES.length;

    var estat = { ordre: [], i: 0, encerts: 0, ratxa: 0, fallats: [] };

    function mostra(v) {
      vistaInici.hidden = v !== 'inici';
      vistaJoc.hidden = v !== 'joc';
      vistaFinal.hidden = v !== 'final';
    }
    function comenca() {
      estat.ordre = barreja(DADES.slice());
      estat.i = 0; estat.encerts = 0; estat.ratxa = 0; estat.fallats = [];
      elT.textContent = estat.ordre.length;
      elEncerts.textContent = '0'; elRatxa.textContent = '0';
      mostra('joc'); pinta();
    }
    function pinta() {
      var m = estat.ordre[estat.i];
      elMaterial.textContent = m.nom;
      elN.textContent = (estat.i + 1);
      elBarra.style.width = Math.round(estat.i / estat.ordre.length * 100) + '%';
      elFeedback.textContent = ''; elFeedback.className = 'jp2-feedback';
      elSeguent.hidden = true;
      for (var k = 0; k < opcions.length; k++) {
        opcions[k].disabled = false;
        opcions[k].classList.remove('jp2-ok', 'jp2-ko');
      }
      opcions[0].focus();
    }
    function respon(cat, boto) {
      var m = estat.ordre[estat.i], correcte = (cat === m.cat);
      for (var k = 0; k < opcions.length; k++) opcions[k].disabled = true;
      if (correcte) {
        boto.classList.add('jp2-ok');
        estat.encerts++; estat.ratxa++;
        elFeedback.className = 'jp2-feedback jp2-fb-ok';
        elFeedback.innerHTML = '✅ Molt bé! <strong>' + ETIQUETA[m.cat] + '</strong> — ' + m.perque;
      } else {
        boto.classList.add('jp2-ko');
        estat.ratxa = 0; estat.fallats.push(m);
        for (var j = 0; j < opcions.length; j++) {
          if (opcions[j].getAttribute('data-cat') === m.cat) opcions[j].classList.add('jp2-ok');
        }
        elFeedback.className = 'jp2-feedback jp2-fb-ko';
        elFeedback.innerHTML = '❌ Era <strong>' + ETIQUETA[m.cat] + '</strong> — ' + m.perque;
      }
      elEncerts.textContent = estat.encerts; elRatxa.textContent = estat.ratxa;
      elSeguent.hidden = false; elSeguent.focus();
    }
    function seguent() {
      estat.i++;
      if (estat.i >= estat.ordre.length) { acaba(); return; }
      pinta();
    }
    function acaba() {
      elBarra.style.width = '100%';
      mostra('final');
      var tot = estat.ordre.length;
      $('.jp2-resultat').innerHTML = 'Has encertat <strong>' + estat.encerts + ' de ' + tot + '</strong> a la primera.';
      var repas = $('.jp2-repas');
      if (estat.fallats.length) {
        var html = '<p class="jp2-repas-tit">📌 Repassa aquests:</p><ul>';
        for (var k = 0; k < estat.fallats.length; k++) {
          var f = estat.fallats[k];
          html += '<li><strong>' + f.nom + '</strong> → ' + ETIQUETA[f.cat] + ': ' + f.perque + '</li>';
        }
        repas.innerHTML = html + '</ul>';
      } else {
        repas.innerHTML = '<p class="jp2-repas-tit">🌟 Cap error. Coneixes bé els materials del taller!</p>';
      }
    }

    $('.jp2-comenca').addEventListener('click', comenca);
    $('.jp2-torna').addEventListener('click', comenca);
    elSeguent.addEventListener('click', seguent);
    for (var k = 0; k < opcions.length; k++) {
      (function (b) { b.addEventListener('click', function () { respon(b.getAttribute('data-cat'), b); }); })(opcions[k]);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
</script>
```

- [ ] **Step 2: Regenerar la web**

Run: `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" build_web.py`
Expected: `Web generada a …web — 96 pàgines de contingut.` (sense errors/traceback)

- [ ] **Step 3: Verificar que el widget és a l'HTML generat i la taula intacta**

Run (Grep sobre `web\classes\sa0_punt_de_partida\material_gimcana_seguretat.html`):
- `id="joc-p2"` → 1 coincidència
- `<script>` amb `function init()` i `getElementById('joc-p2')` present
- La taula de materials (`<td>Fusta DM 3 mm</td>`, `<td>PVC / vinil</td>` dins `<strong>`) continua present a l'HTML

Expected: totes presents; el `<table>` de Prova 2 amb les 12 files segueix al document (el `<details>` el crea el JS en runtime, així que a l'HTML estàtic la taula apareix normal).

- [ ] **Step 4: Verificar el comportament al navegador**

Obrir `web/classes/sa0_punt_de_partida/material_gimcana_seguretat.html` al navegador i comprovar la **checklist**:
1. A Prova 2 es veu la targeta d'inici amb «12 materials» i el botó **Comença ▶**; la taula apareix plegada dins «Mostra el full de respostes (per al docent)».
2. **Comença** mostra el primer material, «Material 1 de 12», barra de progrés i 3 botons.
3. Triar la categoria **correcta** → feedback verd «✅ Molt bé! …» amb el perquè; puja «encerts» i «ratxa».
4. Triar una **incorrecta** → feedback vermell «❌ Era <categoria correcta> — …», marca també el botó correcte, ratxa torna a 0.
5. **Següent →** avança; en fallar, el material es guarda per al resum.
6. En acabar les 12: pantalla final amb «Has encertat X de 12» i, si n'hi ha, la llista **📌 Repassa aquests**.
7. **↺ Torna a jugar** reinicia amb ordre diferent.
8. Tot operable amb **teclat** (Tab per moure's, Enter/Espai per activar).

Expected: els 8 punts es compleixen.

- [ ] **Step 5: Confirmar que els verificadors de la CI segueixen verds**

Run:
```
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" verifica_enllacos.py
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" verifica_competencies.py
```
Expected: tots dos `[OK] …` amb exit 0.

- [ ] **Step 6: Commit**

```
git add "Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md"
git commit -m "Quiz interactiu de materials a la Prova 2 de la gimcana (SA0)

Widget autocorrectiu targeta a targeta que llegeix les preguntes de la
taula de materials (una sola font de veritat) i la plega com a full de
respostes. Vanilla JS, accessible (teclat + aria-live), prefix jp2-.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 2: Estils del quiz (presentació + mode fosc)

**Files:**
- Modify: `web_assets/style.css` (afegir un bloc al final, o just després de la regla `.doc img { … }`)

**Interfaces:**
- Consumes: les classes `jp2-*` produïdes per la Task 1 i les variables de tema existents (`--accent`, `--accent-soft`, `--bg`, `--bg-card`, `--line`, `--ink`, `--ink-soft`, `--shadow`).
- Produces: aparença final del widget en clar i fosc.

- [ ] **Step 1: Afegir el CSS scoped**

Afegir a `web_assets/style.css` (per exemple després de la regla `.doc img { … }`):

```css
/* ── joc Prova 2: classifica els materials ─── */
.jp2 {
  border: 2px solid var(--line); border-radius: 16px;
  background: var(--bg-card); padding: 1.2rem 1.3rem;
  margin: 1.4rem 0; box-shadow: var(--shadow);
}
.jp2-titol { font-size: 1.25rem; font-weight: 700; margin: 0 0 .3rem; }
.jp2-sub { color: var(--ink-soft); margin: 0 0 1rem; }
.jp2-btn {
  font: inherit; font-weight: 600; cursor: pointer;
  border: 2px solid var(--line); border-radius: 999px;
  background: var(--bg-card); color: var(--ink); padding: .6rem 1.2rem;
}
.jp2-btn:hover { transform: translateY(-1px); transition: transform .15s; }
.jp2-btn:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
.jp2-comenca, .jp2-torna, .jp2-seguent {
  background: var(--accent); border-color: var(--accent); color: #fff; font-size: 1.05rem;
}
.jp2-barra { height: 8px; border-radius: 999px; background: var(--accent-soft); overflow: hidden; margin-bottom: .6rem; }
.jp2-barra-plena { height: 100%; width: 0; background: var(--accent); transition: width .3s; }
.jp2-progres { font-size: .9rem; color: var(--ink-soft); margin: 0 0 1rem; }
.jp2-carta {
  display: flex; align-items: center; justify-content: center;
  min-height: 5.5rem; padding: 1rem; margin-bottom: 1rem;
  border: 2px dashed var(--line); border-radius: 12px;
  background: color-mix(in srgb, var(--bg-card) 60%, var(--bg));
}
.jp2-material { font-size: 1.5rem; font-weight: 700; text-align: center; }
.jp2-opcions { display: flex; flex-wrap: wrap; gap: .6rem; }
.jp2-op { flex: 1 1 8rem; padding: .8rem; font-size: 1rem; }
.jp2-op:disabled { cursor: default; }
.jp2-op.jp2-ok { background: #128a4d; border-color: #128a4d; color: #fff; }
.jp2-op.jp2-ko { background: #c0392b; border-color: #c0392b; color: #fff; }
.jp2-feedback { margin: 1rem 0 .4rem; line-height: 1.5; }
.jp2-feedback.jp2-fb-ok, .jp2-feedback.jp2-fb-ko { padding: .8rem 1rem; border-radius: 10px; color: var(--ink); }
.jp2-fb-ok { background: color-mix(in srgb, #128a4d 15%, var(--bg-card)); border: 1px solid #128a4d; }
.jp2-fb-ko { background: color-mix(in srgb, #c0392b 15%, var(--bg-card)); border: 1px solid #c0392b; }
.jp2-seguent { margin-top: .4rem; }
.jp2-resultat { font-size: 1.1rem; }
.jp2-repas-tit { font-weight: 600; margin-bottom: .3rem; }
.jp2-repas ul { margin: 0 0 1rem; padding-left: 1.2rem; }
.jp2-repas li { margin: .3rem 0; }
.jp2-taula { margin: 1rem 0; }
.jp2-taula > summary { cursor: pointer; font-weight: 600; color: var(--accent); padding: .4rem 0; }
```

- [ ] **Step 2: Regenerar la web**

Run: `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" build_web.py`
Expected: build correcte; `web/assets/style.css` conté les regles `.jp2` (Grep `\.jp2-op\.jp2-ok`).

- [ ] **Step 3: Verificar l'aparença al navegador (clar i fosc)**

Obrir la pàgina i comprovar:
1. El widget es veu com una targeta amb vora arrodonida i ombra; botons de colors coherents amb la web.
2. En encertar/fallar, el botó correcte es marca verd i l'erroni vermell, i el requadre de feedback té fons verd/vermell suau **amb text llegible**.
3. Amb el botó **🌗** (mode fosc): els colors segueixen llegibles i el contrast es manté (verd/vermell sobre fons fosc, text feedback llegible).
4. El focus del teclat és **visible** (contorn) en tots els botons.
5. En mòbil/estret els 3 botons d'opció s'ajusten (wrap) sense desbordar.

Expected: els 5 punts es compleixen en clar i en fosc.

- [ ] **Step 4: Commit**

```
git add web_assets/style.css
git commit -m "Estils del quiz de materials de la Prova 2 (clar i fosc)

Regles scoped .jp2-* amb les variables de tema; feedback amb color +
icona i focus de teclat visible.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
```

---

### Task 3: Verificació final i desplegament

**Files:** cap (només build, verificació i push)

**Interfaces:**
- Consumes: els canvis de les Task 1 i 2 ja commitats.
- Produces: la web publicada a GitHub Pages amb la Prova 2 interactiva.

- [ ] **Step 1: Build net i verificadors**

Run:
```
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" verifica_enllacos.py
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" verifica_competencies.py
& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" build_web.py
```
Expected: els dos verificadors `[OK]` (exit 0) i el build correcte.

- [ ] **Step 2: Push (dispara el desplegament)**

> Confirmar amb l'usuari abans de fer push (desplega a producció).

```
git push origin main
```
Expected: push acceptat; s'engega la GitHub Action `pages.yml`.

- [ ] **Step 3: Confirmar el desplegament i la pàgina en directe**

Run: `gh run watch <ID> --exit-status` (o `gh run list --workflow pages.yml --limit 1` fins veure `completed success`).

> Si la run falla amb «not acquired by Runner of type hosted» (fallada transitòria d'infraestructura, no del codi), tornar-la a llançar: `gh run rerun <ID>`.

Després, verificar en directe que la pàgina respon i conté el widget:
`https://tomeu-cd100.github.io/maker-1ESO-2627/classes/sa0_punt_de_partida/material_gimcana_seguretat.html`
Expected: HTTP 200 i el joc apareix a la secció Prova 2.

---

## Notes de verificació (per què així)

- **No hi ha framework de test JS** al projecte (és un generador estàtic amb JS vanilla incrustat). Per això la verificació de cada tasca és build + `grep` sobre la sortida + checklist al navegador, en comptes de tests unitaris automàtics.
- **El plegat de la taula el fa el JS**, no el Markdown: `python-markdown` no processa taules dins de blocs HTML en brut (`<details>`) sense l'extensió `md_in_html`. Fer-ho en runtime evita tocar `build_web.py` i degrada bé sense JS (la taula es veu sencera).
- **`rewrite_links` de `build_web.py`** només actua sobre `href=`, `src=` i `<code>…</code>`; el widget no en conté cap, així que no s'hi veu afectat.
