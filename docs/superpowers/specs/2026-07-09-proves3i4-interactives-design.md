# Proves 3 i 4 interactives — extensió del motor de quiz (SA0)

**Data:** 2026-07-09
**Pàgina afectada:** `Classes/SA0_Punt_de_partida/Material_gimcana_seguretat.md`
**Spec pare:** `2026-07-09-prova2-materials-interactiva-design.md` (motor validat i desplegat)

## Objectiu

Estendre el quiz autocorrectiu de la Prova 2 a les proves 3 i 4 de la gimcana de
seguretat, **amb el mateix motor** i el mateix llenguatge visual, per a ús
individual/parelles al Chromebook.

## Decisions preses

- **Prova 3 («Què faries si…»):** mecànica **pensa-i-revela** (triada per Tomeu entre
  3 opcions). Surt el cas → l'alumne pensa (o ho parlen en parella) → «👁 Mostra la
  resposta» → autoavaluació «✅ L'he encertat» / «🤔 M'ha faltat alguna cosa». El 🤔
  compta com a fallat i va a la llista «repassa» final. Descartada la tria entre 3
  respostes: les respostes llargues s'endevinen per paraules clau sense pensar.
- **Prova 4 (norma ↔ raó):** mode opcions del motor. Surt una **norma** i 3 **raons**
  (la correcta + 2 raons d'altres files com a distractors, remesclades). Botons en
  columna (raons llargues).
- **Refactor:** un únic `<script>` al final del `.md` amb un motor genèric
  `jocQuiz(cfg)` que munta el DOM del widget (cada secció només porta un
  `<div id="joc-pN" class="jqz"></div>`). Prefix CSS renombrat `jp2-` → `jqz-`
  (neutre, compartit pels 3 jocs); cap canvi funcional a la Prova 2.

## Disseny funcional

- Els tres jocs conserven: inici amb recompte i «Comença ▶», barra de progrés,
  comptador d'encerts + ratxa 🔥, resum final amb llista de repàs, «↺ Torna a jugar»
  amb remescla. Sense «perdre» ni rànquings.
- **Fonts de veritat** (cap duplicació de dades):
  - P2: la taula de materials (com fins ara).
  - P3: la llista `<ol>` de casos (negreta = cas, cursiva = resposta esperada);
    en runtime es plega dins `<details>` «per al docent», com la taula de P2.
  - P4: la taula norma|raó; també es plega en `<details>`.
- **P3, flux:** en autoavaluar-se s'avança directament (la resposta ja s'ha llegit;
  no cal un «Següent» extra).
- **P4, distractors:** es trien una vegada per càrrega de pàgina (recarregar en dona
  de nous). Acceptat com a simplificació (YAGNI).

## Accessibilitat

Igual que P2: botons reals amb focus visible, feedback amb icona + text,
`aria-live="polite"`, variables CSS del tema (mode fosc / mida de lletra / espaiat).

## Fora d'abast

Persistència, rànquings, temporitzador, mode projectat, reutilitzar el motor fora
d'aquesta pàgina.

## Verificació d'acceptació

1. Build correcte (Python311) i verificadors CI en verd.
2. **P2 sense regressió**: funciona exactament igual que la versió desplegada.
3. **P3**: cas → revela → autoavaluació → resum amb «torna a llegir aquests casos».
4. **P4**: norma + 3 raons remesclades; en fallar marca la bona; resum de parelles.
5. Tot operable amb teclat i llegible en mode fosc.
