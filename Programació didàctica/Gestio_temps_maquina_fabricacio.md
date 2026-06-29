# Gestió del temps-màquina i de la fabricació — «Aula Maker» (1r ESO)

> **Per què aquest document?** El factor que més condiciona una aula maker no és el disseny:
> és el **temps-màquina**. Amb **1 làser i 1 impressora 3D per a ~25 alumnes**, la fabricació és
> un **coll d'ampolla** que cal planificar conscientment perquè (a) la temporització sigui
> realista i (b) **tothom fabriqui** (equitat), no només els ràpids. Aquest document és el
> referent transversal de fabricació; les SA de fabricació (SA1, SA3, SA5, SA6, SA9) hi remeten.

---

## 1. La matemàtica del temps (fes-la abans de cada SA)

Calcula sempre: **temps per peça × nre. d'alumnes vs. minuts reals de la sessió.**

| Màquina | Temps orientatiu per treball | 25 alumnes "en sèrie" | Conclusió |
|---------|------------------------------|------------------------|-----------|
| Làser (gravat petit, p. ex. clauer) | 1–4 min + ~1 min de col·locació | 50–125 min | **No hi cap** en una sessió si es fa un a un |
| Làser (projecte amb talls, SA3) | 5–15 min/equip | Per equips, sí (6–7 equips) | Viable **per equips**, no individual |
| Impressió 3D (peça petita <40 g) | 30 min – 1.5 h | **Impossible** en sèrie a classe | Cal **cua** + impressió **fora d'horari** |
| Impressió 3D (peça mitjana) | 2–5 h | Dies | Disseny obligat a peça **petita i ràpida** |

> 📌 **Regla d'or:** si la suma "en sèrie" supera els minuts de la sessió, necessites una de les
> tres estratègies de sota (batch, cua o paral·lel). Normalment, les **tres alhora**.

---

## 2. Tres estratègies (combina-les)

### A) Batch / *nesting* (làser) — la que més temps estalvia
- **Col·loca molts dissenys en una sola planxa i fes una única passada.** 25 clauers junts =
  una passada de pocs minuts, en comptes de 25 passades.
- A Inkscape/XCS: cada alumne/a lliura el seu disseny en una **mida i posició acordades**; el
  docent (o l'equip de "preparació de planxa") els munta en una sola làmina.
- Avantatge afegit: **optimitza material** (menys retalls) → connecta amb CE6.2 (sostenibilitat).
- A SA1 això converteix la fabricació de tot el grup en **15–20 min reals**, no 75.

### B) Cua d'impressió 3D visible (kanban)
- Full o pissarra amb tres columnes: **Per imprimir · Imprimint · Fet**. Cada peça és una
  targeta amb nom, temps estimat i grams.
- **Criteri d'ordre explícit i just** (decideix-lo i fes-lo públic): per ordre de validació del
  disseny, alternant equips, o per sorteig. Mai "qui crida més".
- **Compromís d'equitat:** ningú tanca la SA sense haver imprès. Qui no imprimeix avui, té
  **prioritat** la propera sessió (marca-ho al kanban).
- Programa les **impressions llargues fora d'horari** (pati, tarda, nit) i deixa per a classe
  només l'inici de la primera capa (el moment crític d'observar).

### C) Treball paral·lel amb propòsit (mentre s'espera torn)
Qui espera màquina **no perd el temps**; té tasques productives i avaluables:
- Entrada al **diari de taller** (procés, decisions, incidència observada).
- **Repte express** de `Reptes/` (fast finishers, nivells ⭐⭐⭐).
- **Millora del disseny** o preparació de la planxa de batch (rol d'equip).
- **Seguiment d'impressió** com a observació tècnica (primera capa, *warping*…).
- Practicar amb les **simulacions** (`Simulacions/`) sense ocupar màquina.

---

## 3. Rols de fabricació dins l'equip (rotatius)
Reparteix la pressió sobre la màquina i dona feina significativa a tothom:

| Rol | Què fa | Connexió competencial |
|-----|--------|-----------------------|
| **Preparador/a de planxa** | Munta el batch de làser, comprova mides i capes | CA2.1, CA2.3, CA6.2 |
| **Operador/a de màquina** | Envia el treball amb supervisió i segueix el protocol | CA3.1/3.2, CA6.1 |
| **Documentalista** | Registra paràmetres, temps, incidències al diari | CA5.2, CA3.3 |
| **Controlador/a de qualitat** | Revisa el resultat i proposa millores (iteració) | CA1.4, CA3.3 |

> Per a alumnat amb dificultats motrius, el rol de **decisió/validació** (decideix paràmetres i
> col·locació, un altre executa el moviment fi) manté la responsabilitat sense la barrera física
> (vegeu `DUA_adaptacions_SA.md`).

---

## 4. Disseny orientat a la viabilitat (limita la frustració)
- **Peces petites i ràpides** al principi; "petit i acabat" motiva més que "gran i a mitges".
- Posa **límits de mida i de temps** explícits a cada repte (p. ex. "cap a < 60×40 mm a làser",
  "< 1 h d'impressió, < 40 g") i fes-los part dels criteris d'èxit.
- Tingues sempre **plantilles de partida** (`Recursos/Plantilles_disseny/`) per evitar el
  "full en blanc" i accelerar.

---

## 5. Checklist abans d'una sessió de fabricació
- [ ] He fet la **matemàtica del temps** (§1) i la sessió és realista.
- [ ] Estratègia decidida: **batch** (làser) i/o **cua** (3D) i/o **paral·lel**.
- [ ] **Kanban d'impressió** preparat amb criteri d'ordre públic i just.
- [ ] Tasques de **treball paral·lel** a punt (reptes, diari, simulacions).
- [ ] Consumibles i màquina comprovats; impressions llargues planificades **fora d'horari**.
- [ ] 5–10 min reservats per a **neteja i manteniment** al final.

---

## 6. Després: registra i millora
- Anota el **temps real** de fabricació a `Memòria de treball/Diari_docent_sessions.md`
  (és la millor dada per ajustar la `Temporitzacio_anual.md` el curs vinent).
- Registra incidències de màquina a `Memòria de treball/Registre_incidencies_i_manteniment.md`.

> Relacionat amb: `Temporitzacio_anual.md`, `DUA_adaptacions_SA.md`, `Aprenentatge_cooperatiu.md`,
> `Reptes/`, `Simulacions/` i l'apartat de fabricació de cada `Classes/SAx/SAx.md`.
