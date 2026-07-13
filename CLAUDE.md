# CLAUDE.md — Curs Aula Maker 1r ESO

Material docent en **català** (optativa maker 1r ESO, LOMLOE). El markdown és la font única;
`build_web.py` genera la web estàtica que GitHub Pages publica a cada push a `main`.

## Regles

- **Tot en català**, amb ortografia completa (accents inclosos).
- **`web/` és artefacte generat**: no s'edita ni es versiona. Regenera amb `build_web.py`.
- **Python**: el `python` del PATH és el d'Inkscape. Usa el Python 3.11 real per executar
  `build_web.py`, `verifica_*.py` i `genera_quadern.py`.

- **Abans de committar**: `verifica_enllacos.py` i `verifica_competencies.py` han de passar
  (el CI els executa i bloqueja la publicació si fallen).

- **RGPD**: repo públic. Cap dada d'alumnat real; les dades van a `dades/` (gitignored,
  patró `*_DADES.*`).

- **`Quadern_digital_docent_plantilla.xlsx` no s'edita a mà**: es genera amb
  `genera_quadern.py` (openpyxl).

- **Llicència CC BY-SA 4.0**; `Recursos/` només enllaça material de tercers, mai el copia.

## Estructura d'unitats

Cada `Classes/SAx_Nom/` conté `SAx.md` + `Fitxa_alumnat.md` + `Rubrica_SAx.md` +
`Exemple_resolt.md` (SA0 és diagnòstica: sense rúbrica ni exemple). Les seccions de `SAx.md`
segueixen plantilla fixa (§1–§8, pregunta guia, criteris d'èxit, ⏸️ mínims). El §2 de cada SA
ha de quadrar amb la matriu `Avaluació/Criteris_i_qualificacio.md` §4 — ho verifica
`verifica_competencies.py` (atenció: usa `range(1,10)`; amplia'l si crees SA10+).

## Convencions

- Referències creuades amb backticks, p. ex. `Avaluació/Diari_de_taller.md` (+ `§N` per seccions).
- Emojis semàntics: 🎯 objectiu · 🧭 gran idea · ⏸️ mínim del dia · ♻️ una reflexió/sessió ·
  ⭐ ampliació · 🌱🙂💪🌟 nivells amigables · 🖨️ imprimible.

- Noms de fitxer en Snake_Case; docs de nivell curs amb prefix `00_`.
- Commits en català, tipus Conventional Commits.
- Accessibilitat web: icona+text (mai només color), navegable per teclat.
