# Proves 3 i 4 interactives (motor compartit) — Pla d'implementació

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactoritzar el quiz de la Prova 2 en un motor genèric i fer interactives les proves 3 (pensa-i-revela) i 4 (norma ↔ raó) de la pàgina de la gimcana (SA0).

**Architecture:** Un únic `<script>` al final de `Material_gimcana_seguretat.md` amb el motor `jocQuiz(cfg)` (modes `opcions` i `revela`) que munta el DOM de cada widget dins `<div id="joc-pN" class="jqz"></div>`. Cada joc parseja la seva font (taula P2, `<ol>` P3, taula P4) i la plega en `<details>`. CSS: prefix `jp2-` renombrat a `jqz-` + 4 regles noves.

**Tech Stack:** Markdown (python-markdown, HTML/script en brut), JavaScript vanilla (IIFE), CSS amb variables de tema.

## Global Constraints

- **Build:** `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" build_web.py` (el `python` del PATH és l'Inkscape).
- **`web/` és `.gitignore`**; la publica la GitHub Action `pages.yml`. Build local només per verificar.
- **Previsualització local:** servir amb `python -m http.server <port> --bind 127.0.0.1 --directory web` des de l'arrel del repo (mai amb el CWD dins `web/`: bloqueja el `rmtree` del build). Matar el servidor abans de reconstruir.
- **Commits en català** amb trailer `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
- **CI verd:** `verifica_enllacos.py` i `verifica_competencies.py` (exit 0).
- **Accessibilitat:** feedback icona + text, `aria-live`, focus visible, variables de tema.
- **Sense framework de test JS:** verificació = build + grep + checklist al navegador.

---

### Task 1: Motor genèric `jocQuiz` + Prova 2 refactoritzada (sense regressió)

**Files:**
- Modify: `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md` (substituir el bloc `<div id="joc-p2">…</script>` per un div buit; afegir el script del motor al final del fitxer)
- Modify: `web_assets/style.css` (renombrar `jp2-` → `jqz-` i afegir regles noves)

**Interfaces:**
- Consumes: la taula de materials de P2 (12 files: material | emoji | per què).
- Produces: funció `jocQuiz(cfg)` amb `cfg = { id, titol, sub, item, marcador, tipus: 'opcions'|'revela', vertical?, resultat, repasTitol, perfecte, dades }`; targeta mode opcions `= { enunciat, opcions: [{html, ok}], perque, perqueKo, repas }`; targeta mode revela `= { enunciat, resposta, repas }`. Helpers globals de l'IIFE: `barreja(a)`, `seguentElement(node, tag)`, `plega(el, resum)`, `categoria(text)`. Les tasques 2 i 3 afegeixen parsers i configs dins el mateix script.

- [ ] **Step 1: Substituir el widget de P2 per un div buit**

Al `.md`, substituir tot el bloc des de `<div id="joc-p2" class="jp2">` fins a `</script>` (inclosos) per:

```html
<div id="joc-p2" class="jqz"></div>
```

- [ ] **Step 2: Afegir el script del motor al final del fitxer**

Afegir al final del `.md` (després de la secció «Dinàmica i tancament»):

```html
<script>
(function () {
  // ── utilitats ──
  function barreja(a) {
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function seguentElement(node, tag) {
    var n = node && node.nextElementSibling;
    while (n && n.tagName !== tag) n = n.nextElementSibling;
    return n;
  }
  function plega(el, resum) {
    var det = document.createElement('details');
    det.className = 'jqz-taula';
    var sum = document.createElement('summary');
    sum.textContent = resum;
    el.parentNode.insertBefore(det, el);
    det.appendChild(sum);
    det.appendChild(el);
  }

  // ── motor genèric: una targeta cada cop ──
  function jocQuiz(cfg) {
    var arrel = document.getElementById(cfg.id);
    if (!arrel || !cfg.dades.length) return;

    arrel.innerHTML =
      '<div class="jqz-inici">' +
        '<p class="jqz-titol">' + cfg.titol + '</p>' +
        '<p class="jqz-sub">' + cfg.sub.replace('{n}', cfg.dades.length) + '</p>' +
        '<button type="button" class="jqz-btn jqz-comenca">Comença ▶</button>' +
      '</div>' +
      '<div class="jqz-joc" hidden>' +
        '<div class="jqz-barra"><div class="jqz-barra-plena"></div></div>' +
        '<p class="jqz-progres"></p>' +
        '<div class="jqz-carta"><span class="jqz-material"></span></div>' +
        '<div class="jqz-opcions' + (cfg.vertical ? ' jqz-vertical' : '') + '"></div>' +
        '<div class="jqz-feedback" aria-live="polite"></div>' +
        '<button type="button" class="jqz-btn jqz-seguent" hidden>Següent →</button>' +
      '</div>' +
      '<div class="jqz-final" hidden>' +
        '<p class="jqz-titol">🏁 Fet!</p>' +
        '<p class="jqz-resultat"></p>' +
        '<div class="jqz-repas"></div>' +
        '<button type="button" class="jqz-btn jqz-torna">↺ Torna a jugar</button>' +
      '</div>';

    var $ = function (s) { return arrel.querySelector(s); };
    var vInici = $('.jqz-inici'), vJoc = $('.jqz-joc'), vFinal = $('.jqz-final');
    var elCarta = $('.jqz-material'), elOpcions = $('.jqz-opcions');
    var elFeedback = $('.jqz-feedback'), elSeguent = $('.jqz-seguent');
    var elProgres = $('.jqz-progres'), elBarra = $('.jqz-barra-plena');
    var estat = { ordre: [], i: 0, encerts: 0, ratxa: 0, fallats: [] };

    function mostra(v) {
      vInici.hidden = v !== 'inici'; vJoc.hidden = v !== 'joc'; vFinal.hidden = v !== 'final';
    }
    function boto(html, classe) {
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'jqz-btn ' + classe; b.innerHTML = html;
      return b;
    }
    function progres() {
      elProgres.textContent = cfg.item + ' ' + (estat.i + 1) + ' de ' + estat.ordre.length +
        ' · ' + cfg.marcador + ': ' + estat.encerts + ' · ratxa 🔥 ' + estat.ratxa;
      elBarra.style.width = Math.round(estat.i / estat.ordre.length * 100) + '%';
    }
    function comenca() {
      estat.ordre = barreja(cfg.dades.slice());
      estat.i = 0; estat.encerts = 0; estat.ratxa = 0; estat.fallats = [];
      mostra('joc'); pinta();
    }
    function pinta() {
      var c = estat.ordre[estat.i];
      elCarta.innerHTML = c.enunciat;
      elFeedback.innerHTML = ''; elFeedback.className = 'jqz-feedback';
      elSeguent.hidden = true;
      elOpcions.innerHTML = '';
      progres();
      if (cfg.tipus === 'revela') pintaRevela(c); else pintaOpcions(c);
    }
    function pintaOpcions(c) {
      for (var k = 0; k < c.opcions.length; k++) {
        (function (op) {
          var b = boto(op.html, 'jqz-op');
          if (op.ok) b.setAttribute('data-ok', '1');
          b.addEventListener('click', function () { respon(c, op, b); });
          elOpcions.appendChild(b);
        })(c.opcions[k]);
      }
      elOpcions.firstChild.focus();
    }
    function respon(c, op, b) {
      var botons = elOpcions.querySelectorAll('button');
      for (var k = 0; k < botons.length; k++) botons[k].disabled = true;
      if (op.ok) {
        b.classList.add('jqz-ok');
        estat.encerts++; estat.ratxa++;
        elFeedback.className = 'jqz-feedback jqz-fb-ok';
        elFeedback.innerHTML = '✅ Molt bé! ' + c.perque;
      } else {
        b.classList.add('jqz-ko');
        estat.ratxa = 0; estat.fallats.push(c);
        for (var j = 0; j < botons.length; j++)
          if (botons[j].getAttribute('data-ok') === '1') botons[j].classList.add('jqz-ok');
        elFeedback.className = 'jqz-feedback jqz-fb-ko';
        elFeedback.innerHTML = '❌ ' + c.perqueKo;
      }
      progres();
      elSeguent.hidden = false; elSeguent.focus();
    }
    function pintaRevela(c) {
      var b = boto('👁 Mostra la resposta', 'jqz-comenca');
      b.addEventListener('click', function () {
        b.hidden = true;
        elFeedback.className = 'jqz-feedback jqz-fb-rev';
        elFeedback.innerHTML = '→ ' + c.resposta +
          '<p class="jqz-repas-tit">Com t\'ha anat?</p>';
        var caixa = document.createElement('div');
        caixa.className = 'jqz-opcions';
        var bOk = boto('✅ L\'he encertat', 'jqz-op');
        var bKo = boto('🤔 M\'ha faltat alguna cosa', 'jqz-op');
        bOk.addEventListener('click', function () { estat.encerts++; estat.ratxa++; seguent(); });
        bKo.addEventListener('click', function () { estat.ratxa = 0; estat.fallats.push(c); seguent(); });
        caixa.appendChild(bOk); caixa.appendChild(bKo);
        elFeedback.appendChild(caixa);
        bOk.focus();
      });
      elOpcions.appendChild(b);
      b.focus();
    }
    function seguent() {
      estat.i++;
      if (estat.i >= estat.ordre.length) acaba(); else pinta();
    }
    function acaba() {
      elBarra.style.width = '100%';
      mostra('final');
      $('.jqz-resultat').innerHTML =
        cfg.resultat.replace('{x}', estat.encerts).replace('{n}', estat.ordre.length);
      var repas = $('.jqz-repas');
      if (estat.fallats.length) {
        var html = '<p class="jqz-repas-tit">📌 ' + cfg.repasTitol + '</p><ul>';
        for (var k = 0; k < estat.fallats.length; k++) html += '<li>' + estat.fallats[k].repas + '</li>';
        repas.innerHTML = html + '</ul>';
      } else {
        repas.innerHTML = '<p class="jqz-repas-tit">🌟 ' + cfg.perfecte + '</p>';
      }
    }

    $('.jqz-comenca').addEventListener('click', comenca);
    $('.jqz-torna').addEventListener('click', comenca);
    elSeguent.addEventListener('click', seguent);
  }

  // ── Prova 2: la taula de materials ──
  var NOMCAT = { 'permes': 'Permès', 'cal-preguntar': 'Cal preguntar', 'prohibit': 'Prohibit' };
  var EMOJICAT = { 'permes': '✅ Permès', 'cal-preguntar': '⚠️ Cal preguntar', 'prohibit': '❌ Prohibit' };
  function categoria(text) {
    if (text.indexOf('✅') !== -1) return 'permes';
    if (text.indexOf('❌') !== -1) return 'prohibit';
    if (text.indexOf('⚠') !== -1) return 'cal-preguntar';
    return null;
  }
  function dadesMaterials() {
    var taula = seguentElement(document.getElementById('joc-p2'), 'TABLE');
    if (!taula) return [];
    plega(taula, 'Mostra el full de respostes (per al docent)');
    var files = taula.querySelectorAll('tbody tr'), dades = [];
    for (var i = 0; i < files.length; i++) {
      var cel = files[i].querySelectorAll('td');
      if (cel.length < 3) continue;
      var cat = categoria(cel[1].textContent);
      if (!cat) continue;
      var nom = cel[0].textContent.trim(), perque = cel[2].innerHTML.trim();
      dades.push({
        enunciat: nom,
        opcions: [
          { html: '✅ Permès', ok: cat === 'permes' },
          { html: '⚠️ Cal preguntar', ok: cat === 'cal-preguntar' },
          { html: '❌ Prohibit', ok: cat === 'prohibit' }
        ],
        perque: '<strong>' + NOMCAT[cat] + '</strong> — ' + perque,
        perqueKo: 'Era <strong>' + NOMCAT[cat] + '</strong> — ' + perque,
        repas: '<strong>' + nom + '</strong> → ' + EMOJICAT[cat] + ': ' + perque
      });
    }
    return dades;
  }

  function init() {
    jocQuiz({
      id: 'joc-p2',
      titol: '🎮 Joc: classifica els materials',
      sub: "Tens <strong>{n}</strong> materials. Digues si cada un és <strong>permès</strong>, <strong>cal preguntar</strong> o <strong>prohibit</strong>… i mira'n el perquè.",
      item: 'Material', marcador: 'encerts a la primera', tipus: 'opcions',
      resultat: 'Has encertat <strong>{x} de {n}</strong> a la primera.',
      repasTitol: 'Repassa aquests:',
      perfecte: 'Cap error. Coneixes bé els materials del taller!',
      dades: dadesMaterials()
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
</script>
```

- [ ] **Step 3: Renombrar el prefix CSS i afegir les regles noves**

A `web_assets/style.css`, dins el bloc «joc Prova 2», substituir totes les ocurrències de `jp2` per `jqz` (el comentari passa a «jocs de la gimcana (quiz targeta a targeta)»), i afegir al final del bloc:

```css
.jqz-opcions.jqz-vertical { flex-direction: column; }
.jqz-opcions.jqz-vertical .jqz-op { flex: none; text-align: left; }
.jqz-fb-rev { background: var(--accent-soft); border: 1px solid var(--accent); padding: .8rem 1rem; border-radius: 10px; }
.jqz-feedback .jqz-opcions { margin-top: .6rem; }
```

- [ ] **Step 4: Build + grep**

Run: `& "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe" build_web.py`
Expected: build correcte. Grep sobre l'HTML generat: `id="joc-p2"` present, `function jocQuiz` present, cap `jp2` restant ni a l'HTML ni a `web/assets/style.css`.

- [ ] **Step 5: Verificar P2 al navegador (regressió)**

Servir `web/` (`--directory web`, port lliure) i comprovar la checklist de P2: inici «12 materials» → Comença → encert (verd + perquè) → error (vermell + marca la bona) → Següent → final amb resum i repàs → Torna a jugar. Taula plegada dins «Mostra el full de respostes».

- [ ] **Step 6: Commit**

```
git add "Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md" web_assets/style.css
git commit -m "Motor generic de quiz (jqz) compartit; Prova 2 refactoritzada sense canvis funcionals" (+ trailer)
```

---

### Task 2: Prova 3 — pensa-i-revela

**Files:**
- Modify: `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md`

**Interfaces:**
- Consumes: `jocQuiz`, `seguentElement`, `plega` (Task 1); l'`<ol>` de casos de P3 (negreta = cas, cursiva = resposta).
- Produces: `dadesCasos()` i el widget `#joc-p3`.

- [ ] **Step 1: Inserir el div del widget**

Després de la línia «Un cas per targeta; l'equip acorda la resposta en 1 minut. Resposta esperada en cursiva.» (amb línia en blanc abans i després):

```html
<div id="joc-p3" class="jqz"></div>
```

- [ ] **Step 2: Afegir el parser i la config**

Dins el script, després de `dadesMaterials()`:

```js
  // ── Prova 3: la llista de casos ──
  function dadesCasos() {
    var llista = seguentElement(document.getElementById('joc-p3'), 'OL');
    if (!llista) return [];
    plega(llista, 'Mostra tots els casos amb resposta (per al docent)');
    var items = llista.children, dades = [];
    for (var i = 0; i < items.length; i++) {
      var cas = items[i].querySelector('strong'), resp = items[i].querySelector('em');
      if (!cas || !resp) continue;
      dades.push({
        enunciat: cas.textContent.trim(),
        resposta: resp.innerHTML.trim(),
        repas: '<strong>' + cas.textContent.trim() + '</strong> → ' + resp.innerHTML.trim()
      });
    }
    return dades;
  }
```

I dins `init()`, després del `jocQuiz` de P2:

```js
    jocQuiz({
      id: 'joc-p3',
      titol: '🎮 Joc: què faries tu?',
      sub: 'Tens <strong>{n}</strong> casos. Llegeix la situació, pensa què faries (o parleu-ho en parella) i compara-ho amb la resposta del taller.',
      item: 'Cas', marcador: 'encertats', tipus: 'revela',
      resultat: "T'has puntuat <strong>{x} de {n}</strong>.",
      repasTitol: 'Torna a llegir aquests casos:',
      perfecte: 'Tots encertats. Bons reflexos de taller!',
      dades: dadesCasos()
    });
```

- [ ] **Step 3: Build + verificar P3 al navegador**

Checklist: inici «7 casos» → Comença → cas a la targeta + «👁 Mostra la resposta» → resposta visible + «Com t'ha anat?» amb els 2 botons → «✅» puja encerts i avança directe; «🤔» va al repàs → final amb «T'has puntuat X de 7» i la llista → la llista de casos original queda plegada.

- [ ] **Step 4: Commit** («Prova 3 interactiva: pensa-i-revela amb autoavaluació (SA0)» + trailer)

---

### Task 3: Prova 4 — cada norma amb la seva raó

**Files:**
- Modify: `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md`

**Interfaces:**
- Consumes: `jocQuiz`, `seguentElement`, `plega`, `barreja` (Task 1); la taula norma|raó de P4.
- Produces: `dadesNormes()` i el widget `#joc-p4`.

- [ ] **Step 1: Inserir el div del widget**

Després de la línia «Retalleu les normes i les raons per separat; l'equip les aparella.» (amb línia en blanc abans i després):

```html
<div id="joc-p4" class="jqz"></div>
```

- [ ] **Step 2: Afegir el parser i la config**

Dins el script, després de `dadesCasos()`:

```js
  // ── Prova 4: la taula norma ↔ raó (2 distractors per targeta) ──
  function dadesNormes() {
    var taula = seguentElement(document.getElementById('joc-p4'), 'TABLE');
    if (!taula) return [];
    plega(taula, 'Mostra les parelles norma ↔ raó (per al docent)');
    var files = taula.querySelectorAll('tbody tr'), tot = [];
    for (var i = 0; i < files.length; i++) {
      var cel = files[i].querySelectorAll('td');
      if (cel.length < 2) continue;
      tot.push({ norma: cel[0].innerHTML.trim(), rao: cel[1].innerHTML.trim() });
    }
    var dades = [];
    for (var i = 0; i < tot.length; i++) {
      var altres = [];
      for (var j = 0; j < tot.length; j++) if (j !== i) altres.push(tot[j].rao);
      barreja(altres);
      dades.push({
        enunciat: tot[i].norma,
        opcions: barreja([
          { html: tot[i].rao, ok: true },
          { html: altres[0], ok: false },
          { html: altres[1], ok: false }
        ]),
        perque: tot[i].rao,
        perqueKo: 'La raó de veritat: ' + tot[i].rao,
        repas: tot[i].norma + ' → ' + tot[i].rao
      });
    }
    return dades;
  }
```

I dins `init()`, després del `jocQuiz` de P3:

```js
    jocQuiz({
      id: 'joc-p4',
      titol: '🎮 Joc: cada norma té una raó',
      sub: 'Tens <strong>{n}</strong> normes. Per a cada una, tria la seva raó de veritat entre tres.',
      item: 'Norma', marcador: 'encerts a la primera', tipus: 'opcions', vertical: true,
      resultat: 'Has aparellat bé <strong>{x} de {n}</strong> a la primera.',
      repasTitol: 'Repassa aquestes parelles:',
      perfecte: 'Cap error. Les normes ja tenen tot el sentit!',
      dades: dadesNormes()
    });
```

- [ ] **Step 3: Build + verificar P4 al navegador**

Checklist: inici «10 normes» → norma a la targeta + 3 raons en columna → encert verd; error marca la raó bona → final amb parelles per repassar → taula plegada. Comprovar també **mode fosc** i que P2 i P3 segueixen funcionant.

- [ ] **Step 4: Commit** («Prova 4 interactiva: aparella norma i raó amb distractors (SA0)» + trailer)

---

### Task 4: Verificació final i desplegament

- [ ] **Step 1:** `verifica_enllacos.py` + `verifica_competencies.py` + `build_web.py` — tot exit 0. Matar servidors de prova.
- [ ] **Step 2:** **Confirmar amb l'usuari** i `git push origin main`.
- [ ] **Step 3:** `gh run watch` fins a `success` (si falla amb «not acquired by Runner», `gh run rerun`). Verificar la pàgina en directe (HTTP 200, `function jocQuiz`, `joc-p3`, `joc-p4` presents).
