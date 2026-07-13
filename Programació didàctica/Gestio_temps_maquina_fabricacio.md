# Gestió del temps-màquina i de la fabricació — «Aula Maker» (1r ESO)

> **Per què aquest document?** El factor que més condiciona una aula maker no és el disseny:
> és el **temps-màquina**. El grup és de **20 alumnes** i el **règim per defecte és el
> desdoblament** (2 docents, **torns de 10 a l'aula Maker**, vegeu `Codocencia_desdoblament.md`):
> amb **1 làser i 1 impressora 3D**, cada torn de 10 ja és un **coll d'ampolla** que cal
> planificar perquè (a) la temporització sigui realista i (b) **tothom fabriqui** (equitat), no
> només els ràpids. Aquest document és el referent transversal de fabricació; les SA de
> fabricació (SA1, SA3, SA5, SA6, SA9) hi remeten. Al 3r trimestre el coll d'ampolla canvia de
> màquina: **1 càmera 360 i 5 ulleres VR** per al grup — vegeu el **§5 (temps-dispositiu)**.
>
> 📌 Les xifres d'aquest document estan calculades per al **torn de 10** (el règim real). Si
> algun dia treballeu amb el **grup sencer de 20** (sense desdoblament), dobleu la demanda
> simultània: la regla d'or i les quatre estratègies s'apliquen igual (el batch continua sent
> la diferència entre minuts i hores).

---

## 1. La matemàtica del temps (fes-la abans de cada SA)

Calcula sempre: **temps per peça × nre. d'alumnes del torn vs. minuts reals de la sessió.**

| Màquina | Temps orientatiu per treball | 10 alumnes (torn) "en sèrie" | Conclusió |
|---------|------------------------------|------------------------|-----------|
| Làser (gravat petit, p. ex. clauer) | 1–4 min + ~1 min de col·locació | 20–50 min | **No hi cap** còmodament si es fa un a un |
| Làser (projecte amb talls, SA3) | 5–15 min/equip | Per equips, sí (~3 equips/torn) | Viable **per equips**, no individual |
| Impressió 3D (peça petita <40 g) | 30–60 min | **Impossible** en sèrie a classe | Cal **cua** + impressió **fora d'horari** |
| Impressió 3D (peça mitjana) | 2–5 h | Dies | Disseny obligat a peça **petita i ràpida** |

> 📌 **Regla d'or:** si la suma "en sèrie" supera els minuts de la sessió, necessites una de les
> quatre estratègies de sota (batch de làser, batch de placa, cua o paral·lel). Normalment,
> **diverses alhora**.

---

## 2. Quatre estratègies (combina-les)

### A) Batch / *nesting* (làser) — la que més temps estalvia
- **Col·loca molts dissenys en una sola planxa i fes una única passada.** 25 clauers junts =
  una passada de pocs minuts, en comptes de 25 passades.

- A Inkscape/XCS: cada alumne/a lliura el seu disseny en una **mida i posició acordades**; el
  docent (o l'equip de "preparació de planxa") els munta en una sola làmina.

- Avantatge afegit: **optimitza material** (menys retalls) → connecta amb CE6.2 (sostenibilitat).
- A SA1 això converteix la fabricació de tot un torn en **15–20 min reals**, en lloc de 20–50.

### B) Batch de placa (impressió 3D) — el "nesting" de la impressora
- **Agrupa 4–8 peces petites de diversos alumnes en una sola placa** i llança-les com una única
  impressió. La placa de la P2S (256×256 mm) admet pràcticament tots els clauers de SA4 en
  **2–3 plaques**, i les peces petites de SA5 en 4–6 tandes.

- Com fer-ho a Bambu Studio: importa els STL a un mateix projecte, **Organitza automàticament**
  (*Arrange*) i revisa que cap peça no necessiti suports que toquin una altra. Anota al kanban
  **una targeta per placa** amb els noms de qui hi va.

- Condició de disseny: peces **petites i sense suports** (o amb suports mínims). Fes-ho part
  dels **criteris d'èxit** de la SA (vegeu §4): una peça que no cap al batch endarrereix tothom.

- Compte amb el risc compartit: si una peça del batch falla i arrossega la impressió, s'atura i
  es rellança sense la peça problemàtica. Explica-ho a l'alumnat: és un motiu més per validar
  la **imprimibilitat** abans d'enviar (vegeu la revisió v1→v2 a SA5).

- Converteix "25 impressions individuals impossibles" en **3–6 tandes viables** (algunes fora
  d'horari) i fa complible el compromís d'equitat de la cua (C).

### C) Cua d'impressió 3D visible (kanban)
- Full o pissarra amb tres columnes: **Per imprimir · Imprimint · Fet**. Cada peça és una
  targeta amb nom, temps estimat i grams.

- **Criteri d'ordre explícit i just** (decideix-lo i fes-lo públic): per ordre de validació del
  disseny, alternant equips, o per sorteig. Mai "qui crida més".

- **Compromís d'equitat:** ningú tanca la SA sense haver imprès. Qui no imprimeix avui, té
  **prioritat** la propera sessió (marca-ho al kanban).

- Programa les **impressions llargues fora d'horari** (pati, tarda, nit) i deixa per a classe
  només l'inici de la primera capa (el moment crític d'observar).

- Combina-la amb el **batch de placa (B)**: la unitat de la cua pot ser una placa sencera, no
  una peça — la cua avança molt més de pressa.

### D) Treball paral·lel amb propòsit (mentre s'espera torn)
Qui espera màquina **no perd el temps**; té tasques productives i avaluables:

- Entrada al **diari de taller** (procés, decisions, incidència observada).
- **Repte express** de `Reptes/` (fast finishers, nivells ⭐⭐⭐) o el seu **projecte personal
  longitudinal** (`Reptes/Projecte_personal.md`).

- Analitzar una peça del **Museu dels Errors** i escriure'n la targeta
  (`Museu_dels_errors.md`).

- **Millora del disseny** o preparació de la planxa de batch (rol d'equip).
- **Seguiment d'impressió** com a observació tècnica (primera capa, *warping*…).
- Practicar amb les **simulacions** (`Simulacions/`) sense ocupar màquina.

---

## 3. Rols de fabricació dins l'equip (rotatius)
Reparteix la pressió sobre la màquina i dona feina significativa a tothom. **No són rols nous:**
són el **barret de sessió de fabricació** dels mateixos rols d'equip de
`Aprenentatge_cooperatiu.md` §2 (l'alumne manté el seu rol de SA, i a la sessió de fabricar fa
aquesta funció):

| Barret de fabricació | = rol d'equip | Què fa | Connexió competencial |
|-----|-----|--------|-----------------------|
| **Preparador/a de planxa** | ✏️ Dissenyador/a | Munta el batch de làser, comprova mides i capes | CA2.1, CA2.3, CA6.2 |
| **Operador/a de màquina** | ⚙️ Operador/a | Envia el treball amb supervisió i segueix el protocol (🚦 semàfor) | CA3.1/3.2, CA6.1 |
| **Documentalista** | 📷 Documentalista | Registra paràmetres, temps, incidències al diari | CA5.2, CA3.3 |
| **Controlador/a de qualitat** | 🧭 Coordinador/a | Revisa el resultat i proposa millores (iteració) | CA1.4, CA3.3 |

> Per a alumnat amb dificultats motrius, el rol de **decisió/validació** (decideix paràmetres i
> col·locació, un altre executa el moviment fi) manté la responsabilitat sense la barrera física
> (vegeu `DUA_adaptacions_SA.md`).

---

## 4. Disseny orientat a la viabilitat (limita la frustració)
- **Peces petites i ràpides** al principi; "petit i acabat" motiva més que "gran i a mitges".
- Posa **límits de mida i de temps** explícits a cada repte (p. ex. "cap a < 60×40 mm a làser",
  "< 1 h d'impressió, < 40 g") i fes-los part dels **criteris d'èxit** (així ho fan SA4, SA5 i
  SA6): l'alumne els comprova ell mateix a la previsualització de Bambu Studio.

- En 3D, demana peces **sense suports o amb suports mínims**: és el que les fa aptes per al
  **batch de placa** (§2B) i el que més temps d'impressió estalvia.

- Tingues sempre **plantilles de partida** (`Recursos/Plantilles_disseny/`) per evitar el
  "full en blanc" i accelerar.

---

## 5. Temps-dispositiu al 3r trimestre (càmera 360 i ulleres VR)

Al 3r trimestre la mateixa matemàtica s'aplica a uns altres recursos escassos:

| Recurs | Disponible | Demanda típica (torn de 10) | Conclusió |
|--------|-----------|----------------|-----------|
| Càmera 360 | **1** | ~3 equips per torn a SA7 (torn de 50') | ~**15 min de càmera per equip**: cal reserva de torns i treball paral·lel |
| Ulleres VR | **5** | 10 alumnes per torn (`Normativa/Protocol_us_VR.md`) | **parelles usuari-guia perfectes** (5 parelles): 2–3 rondes de ~12' en un torn de 50' |

> 👥 El desdoblament (torns de 10, `Codocencia_desdoblament.md`) fa que 5 ulleres per a 10
> alumnes surtin a **parella usuari-guia** exacta — just el que demana el protocol. Amb el grup
> sencer de 20, dobleu les rondes o feu servir més la pantalla.

### Rotació per estacions (la clau del 3r trimestre)
Organitza la sessió en **estacions simultànies** per les quals roten els equips amb temps fixat
(temporitzador visible). Qui no té el dispositiu **també treballa en tasca avaluable**:

- **SA7, sessió de captura (torn de 50' ≈ 3 equips × ~15' de càmera):** un equip té la càmera
  (captura segons el seu pla de rodatge); la resta, a les estacions: *guió i etiquetes del tour*
  · *selecció i transferència de les captures fetes* · *repte immersiu*
  (`Reptes/Reptes_immersius_360_VR.md`). Full de **reserva de torns** públic (com el kanban):
  cap equip surt a capturar sense pla escrit.

- **SA8, exploració VR (torn de 50' ≈ 2–3 rondes de ~12'):** 5 alumnes amb ulleres (un guia per
  parella, vegeu el protocol); la resta a les estacions: *fitxa d'anàlisi crítica* · *exploració
  de l'experiència en pantalla* · *preparació del debat* · *primeres proves amb CoSpaces*.

- Encadena la rotació amb el **carnet de màquina** (`Normativa/Carnet_de_maquina.md`): el primer
  torn de cada equip inclou el checkpoint de càmera/VR.

> ⚠️ El mateix principi d'**equitat** que a la fabricació: registra qui ha passat per la càmera
> i per les ulleres; qui no hi ha passat té **prioritat** la sessió següent. L'alternativa en
> pantalla no és un càstig: a la VR és la **via principal** si el model d'ulleres ho requereix
> (vegeu `Normativa/Protocol_us_VR.md` §1).

---

## 6. Checklist abans d'una sessió de fabricació
- [ ] He fet la **matemàtica del temps** (§1) i la sessió és realista.
- [ ] Estratègia decidida: **batch** (làser), **batch de placa** i/o **cua** (3D), i/o **paral·lel**.
- [ ] **Kanban d'impressió** preparat amb criteri d'ordre públic i just.
- [ ] Tasques de **treball paral·lel** a punt (reptes, diari, simulacions).
- [ ] Consumibles i màquina comprovats; impressions llargues planificades **fora d'horari**.
- [ ] 5–10 min reservats per a **neteja i manteniment** al final.

---

## 7. Després: registra i millora
- Anota el **temps real** de fabricació a `Memòria de treball/Diari_docent_sessions.md`
  (és la millor dada per ajustar la `Temporitzacio_anual.md` el curs vinent).

- Registra incidències de màquina a `Memòria de treball/Registre_incidencies_i_manteniment.md`.

> Relacionat amb: `Temporitzacio_anual.md`, `DUA_adaptacions_SA.md`, `Aprenentatge_cooperatiu.md`,
> `Normativa/Carnet_de_maquina.md`, `Normativa/Protocol_us_VR.md`, `Reptes/`, `Simulacions/` i
> l'apartat de fabricació de cada `Classes/SAx/SAx.md`.
