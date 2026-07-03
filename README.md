# Aula Maker — Optativa de 1r d'ESO (curs 2026-2027)

Materials complets de l'assignatura optativa **«Aula Maker»**: anual, 2 h/setmana, enfocament
STEAM i maker, currículum de Catalunya (Decret 175/2022, LOMLOE).

**Maquinari:** impressora 3D Bambu Lab P2S · talladora làser xTool S1 · càmera 360 · 5 ulleres VR.

> 👉 **Comença per la [Guia d'inici docent](00_Guia_inici_docent.md).**
> Si fas codocència en desdoblament, el teu company/a té la seva pròpia
> [guia d'inici del co-docent](00_Guia_inici_codocent.md) (no cal saber de màquines).

## Estructura

| Carpeta | Contingut |
|---------|-----------|
| [`Programació didàctica/`](Programació%20didàctica/) | PD, temporització, **gestió del temps-màquina**, **codocència/desdoblament**, **les 5 Grans Idees**, **Museu dels Errors**, **mapatge competencial oficial**, cooperatiu, equitat/gènere, interdisciplinarietat/APS i adaptacions DUA |
| [`Classes/`](Classes/) | Les **9 SA** desenvolupades (SA1–SA9) amb exemple resolt |
| [`Avaluació/`](Avaluació/) | Avaluació inicial, criteris + **mapa operatiu per SA**, rúbriques, **full de progrés competencial**, **quadern digital del docent**, **l'avaluació explicada a l'alumnat**, instruments formatius, diari, auto/coavaluació |
| [`Normativa/`](Normativa/) | Seguretat, **carnet de màquina**, protocol VR, reglament, marc normatiu, **carta i autoritzacions de famílies** |
| [`Reptes/`](Reptes/) | Reptes curts 2D / 3D / immersius + insígnies + **projecte personal longitudinal** |
| [`Simulacions/`](Simulacions/) | Eines virtuals per practicar sense material |
| [`Memòria de treball/`](Memòria%20de%20treball/) | Bitàcola, incidències, inventari, memòria final |
| [`Recursos/`](Recursos/) | Plantilles de disseny pròpies i enllaços/tutorials validats |

## Les 9 situacions d'aprenentatge

| SA | Títol | Trim. | Eix | Producte final |
|----|-------|:----:|-----|----------------|
| SA1 | Benvinguts a l'Aula Maker | 1 | Cultura maker + làser | Clauer gravat |
| SA2 | Dissenyem en 2D | 1 | Inkscape + làser | Marcapàgines/etiqueta |
| SA3 | Projecte làser: la meva identitat | 1 | Projecte làser | Objecte d'identitat ⭐T1 |
| SA4 | Del 2D al 3D | 2 | Tinkercad | Figura/clauer 3D |
| SA5 | Modelatge 3D funcional | 2 | 3D + impressió | Peça útil impresa |
| SA6 | Repte de disseny 3D | 2 | Repte 3D | Solució a un problema ⭐T2 |
| SA7 | Captura el món en 360 | 3 | Càmera 360 | Tour virtual |
| SA8 | Explorem la Realitat Virtual | 3 | VR / CoSpaces | Escena VR |
| SA9 | Projecte final Aula Maker | 3 | Integrador | Estand a la Fira ⭐curs |

## Llicència
Material original sota **[CC BY-SA 4.0](LICENSE)** (Reconeixement-CompartirIgual): el podeu
reutilitzar i adaptar citant l'autoria i compartint-lo amb la mateixa llicència.
ℹ️ La carpeta `Recursos/` **no redistribueix material de tercers**: només conté material propi
(plantilles i enllaços). La formació de tercers s'enllaça a la font (vegeu
`Recursos/Enllacos_i_tutorials.md`) per respectar-ne l'autoria i la llicència.

## 🌐 Versió web

Tot el material té una **versió web navegable** (disseny net, mode fosc, cercador,
imprimible), amb portades per a **docents**, **alumnat** i **famílies**:

**https://tomeu-cd100.github.io/maker-1ESO-2627/**

- La web **es construeix sola**: a cada push, el workflow `.github/workflows/pages.yml`
  verifica els enllaços (`verifica_enllacos.py`), regenera la web des dels `.md`
  (`build_web.py`) i la publica a GitHub Pages. **No cal fer res més que editar els `.md`.**
- Per a ús **offline**: `pip install markdown` + `python build_web.py` i obriu
  `web/index.html` (la carpeta `web/` no es versiona: és un producte generat).
- L'estil viu a `web_assets/style.css`; les pàgines imprimibles (passaport, pòster,
  targetes), a `web_assets/impressos/`.

> ⚠️ **Protecció de dades:** el repositori és públic. Els fitxers amb noms d'alumnat
> (quadern digital emplenat, exportacions) **no s'hi pugen mai** — deseu-los a `dades/`
> (ignorada per git) o al Drive de centre.

## Notes
- Tot el material està en **Markdown**, editable i convertible a Word/Google Docs/PDF.
- Adapteu les referències normatives i els models d'autorització al vostre centre cada curs.
