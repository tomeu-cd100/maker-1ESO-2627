# Material de la gimcana de seguretat — SA0 (setmana 1)

> Tot el que cal per muntar les **4 proves** de la gimcana de la **SA0**
> (`Classes/SA0_Punt_de_partida/SA0.md`): 35', equips de 4-5, rotació de
> ~7' per prova + 5' de posada en comú. Imprimiu i retalleu les targetes; les respostes per
> al docent van al final de cada prova. Contingut alineat amb
> `Normativa/Normes_seguretat_taller.md` (que és el que s'avalua al checkpoint del carnet).

---

## Prova 1 — 🔎 Troba els perills

**Preparació (abans del curs):** fotografieu 3-4 **escenes muntades a l'aula Maker amb errors
plantats** (o representeu-les en làmines). Escenes suggerides amb els errors a plantar:

**Escena A — «La pressa»** (5 errors)
1. Làser en marxa amb la **tapa oberta**.
2. **Ningú** davant de la màquina.
3. Una **motxilla** a terra al mig del pas.
4. Un **got de batut** al costat del teclat.
5. Retalls i restes **acumulats dins** la làser.

![Escena A «La pressa»: fotografia de l'aula Maker amb els 5 perills plantats per trobar-los.](Recursos/imatges/A.jpg)

**Escena B — «El look perillós»** (4 errors)
1. Alumne/a amb els **cabells llargs solts** inclinat sobre la màquina.
2. **Mànigues amples** penjant / cordó de la dessuadora sobre la zona de treball.
3. Toca la peça acabada de tallar **amb els dits** (encara crema).
4. **Corre** entre les taules amb unes tisores a la mà.

![Escena B «El look perillós»: fotografia de l'aula Maker amb els 4 perills plantats per trobar-los.](Recursos/imatges/B.jpg)

**Escena C — «El material misteriós»** (4 errors)
1. Una planxa de **PVC/vinil** a punt de posar a la làser.
2. Material **sense etiquetar** («això que he trobat al garatge»).
3. **Esprai inflamable** a la lleixa de sobre la làser.
4. La **finestra tancada** i l'extractor apagat amb la làser preparada.

![Escena C «El material misteriós»: fotografia de l'aula Maker amb els 4 perills plantats per trobar-los.](Recursos/imatges/C.jpg)

**Consigna:** «Quants perills veieu? Anoteu-los i digueu QUÈ pot passar per culpa de cadascun.»
*(Puntua trobar-los, però sobretot saber-ne la conseqüència.)*

---

## Prova 2 — ✅❌ Permès o prohibit? (targetes de materials)

Retalleu una targeta per material. L'equip les classifica en **PERMÈS / PROHIBIT / CAL
PREGUNTAR** i explica per què.

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
    var NOM = { 'permes': 'Permès', 'cal-preguntar': 'Cal preguntar', 'prohibit': 'Prohibit' };

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
        elFeedback.innerHTML = '✅ Molt bé! <strong>' + NOM[m.cat] + '</strong> — ' + m.perque;
      } else {
        boto.classList.add('jp2-ko');
        estat.ratxa = 0; estat.fallats.push(m);
        for (var j = 0; j < opcions.length; j++) {
          if (opcions[j].getAttribute('data-cat') === m.cat) opcions[j].classList.add('jp2-ok');
        }
        elFeedback.className = 'jp2-feedback jp2-fb-ko';
        elFeedback.innerHTML = '❌ Era <strong>' + NOM[m.cat] + '</strong> — ' + m.perque;
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

| Targeta | Resposta | Per què (per al docent) |
|---------|:--------:|--------------------------|
| Fusta DM 3 mm | ✅ | El material estàndard del taller |
| Contraxapat 3-4 mm | ✅ | Talla i grava bé |
| Cartró / cartolina gruixuda | ✅ | Vigilar potència: s'encén fàcil — mai sense vigilància |
| Paper | ⚠️ | Només gravats/talls ràpids i vigilats: molt inflamable |
| Metacrilat (acrílic) | ⚠️ | Es pot tallar amb cura (es fon); només amb el docent |
| **PVC / vinil** | ❌ | Allibera **clor** (gas tòxic i corrosiu: fa malbé pulmons i màquina) |
| **Policarbonat** | ❌ | Es crema i fa fum tòxic, no talla bé |
| **ABS** | ❌ | Fum tòxic i es fon malament |
| Material desconegut sense etiqueta | ❌ | Si no saps què és, **no entra a la làser** |
| Fusta amb vernís/pintura desconeguda | ⚠️ | El recobriment pot ser tòxic en cremar: preguntar sempre |
| Mirall / metall | ❌ | Reflecteix el làser (perillós) i no es talla |
| Menjar («em gravés una galeta?») | ⚠️ | Tècnicament possible… però mai sense el docent i mai amb la màquina de materials |

**Consigna:** «Classifiqueu i justifiqueu. Una targeta ben classificada sense el perquè només
val mig punt.»

---

## Prova 3 — 🚨 Què faries si… (casos)

Un cas per targeta; l'equip acorda la resposta en 1 minut. Resposta esperada en cursiva.

1. **Veus una flama petita dins la làser.** → *Avisar el docent IMMEDIATAMENT (crit d'avís,
   sense córrer). No obrir la tapa d'entrada; el docent atura la màquina i actua segons el
   protocol del centre. Mai aigua sobre un aparell elèctric.*
2. **La impressora fa una olor estranya i un soroll nou.** → *No tocar res; avisar el docent;
   apuntar-ho després al registre d'incidències.*
3. **El teu company posa la mà dins la impressora en marxa per treure un fil.** → *Aturar-lo
   de paraula («para!»), no estirar-lo físicament; el broquet crema (~200 °C) i la màquina es
   pausa des de la pantalla, no amb les mans dins.*
4. **Trobes la làser funcionant i no hi ha ningú a la vora.** → *Quedar-t'hi tu mirant-la i
   avisar (o fer avisar) el docent. Una làser MAI es queda sola: és la norma número u.*
5. **Et talles lleugerament amb un cúter al postprocés.** → *Rentar amb aigua, avisar el
   docent → farmaciola. Encara que sembli poca cosa, sempre s'avisa.*
6. **Un company vol gravar el logotip d'una marca famosa per vendre clauers.** → *Tema de
   llicències i ús comercial: parlar-ho amb el docent (connecta amb CA6.3 — al taller
   respectem drets i llicències).*
7. **Sona l'alarma d'evacuació mentre la làser està tallant.** → *El docent atura la màquina
   (botó de pausa/stop); tothom segueix el pla d'evacuació del centre. Les coses es queden;
   les persones surten.*

---

## Prova 4 — 🧩 Cada norma té una raó (aparellar)

Retalleu les normes i les raons per separat; l'equip les aparella.

| Norma | Raó |
|-------|-----|
| No es toca cap màquina sense autorització | Les màquines tallen, cremen o atrapen: primer cal saber-ne el funcionament (per això hi ha el **carnet**) |
| Cabells recollits i res penjant | Qualsevol cosa que penja pot quedar **atrapada** per parts mòbils |
| No menjar ni beure a les zones de màquines | Un líquid vessat sobre electrònica = màquina morta (i perill elèctric) |
| La làser mai funciona sola | Si es cala foc, els **primers 10 segons** ho decideixen tot |
| Comprovar la ventilació abans d'engegar | El fum del tall porta partícules i gasos que **no s'han de respirar** |
| Només materials autoritzats | Alguns plàstics alliberen **gasos tòxics** en cremar (el PVC, clor!) |
| Mantenir la porta de la impressora tancada | El broquet va a ~200 °C i les parts mòbils **pessiguen** |
| Cada eina al seu lloc en acabar | El següent equip ha de trobar el taller **segur i a punt** (i les eines perdudes costen diners) |
| Avisar de seguida de qualsevol incidència | Un problema petit ignorat es converteix en un **accident** o una màquina avariada |
| Es respecten els torns i el kanban | Sense torns justos, la màquina la guanya **qui crida més** — i això no és un taller, és una jungla |

---

## Dinàmica i tancament

- **Rotació:** 4 estacions (una per prova), ~7 min per estació, un docent itinerant per
  resoldre dubtes (en desdoblament, la gimcana es fa en **grup sencer** a la sessió 1).
- **Puntuació lleugera** (opcional): un punt per resposta raonada; l'equip guanyador tria
  la primera cançó del taller o similar — el premi és simbòlic.
- **Posada en comú (5'):** un error de cada escena, el material que més ha sorprès (el PVC!),
  i el cas més discutit.
- **Tancament:** signatura del **contracte d'aula** (ara amb coneixement de causa) i
  presentació del **carnet de màquina** (`Normativa/Carnet_de_maquina.md`): «el checkpoint del
  carnet 🔴 (SA1, sessió 2) pregunta exactament aquestes coses».
