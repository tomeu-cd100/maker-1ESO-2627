# SA5 — «Modelatge 3D funcional»

| | |
|---|---|
| **Matèria** | Aula Maker (optativa) |
| **Nivell** | 1r ESO |
| **Trimestre** | 2n |
| **Temporització** | 4 sessions de 2 h (setmanes 16–19) |
| **Eix** | Disseny 3D funcional + impressió (Bambu Lab P2S) |
| **Producte final** | Una **peça útil impresa en 3D** (portamòbil, ganxo, suport d'auriculars, organitzador…) |

---

## 1. Descripció (context + repte)

Ara el 3D resol un problema real. L'alumnat dissenya una **peça funcional** pensada per a una
necessitat concreta i la fabrica amb la impressora 3D, aprenent tot el flux: disseny → laminat
→ impressió → postprocés → avaluació.

> **Repte:** «Detecta una petita molèstia del teu dia a dia i dissenya una **peça útil** que la
> resolgui (un suport per al mòbil, un ganxo, un organitzador de cables, un topall…). Ha de
> complir mides reals i imprimir-se correctament.»

## 🎯 Pregunta guia
> «Com dissenyo i imprimeixo una peça que resolgui una necessitat real?»

> 🧭 **Gran idea 3 — Mesura dues vegades, fabrica una** (mides reals, v1→v2) **+ 4 — L'error
> és informació** (anàlisi d'incidències, Museu dels Errors)
> (`Programació didàctica/Grans_idees_maker.md`).

## 👁️ Aprenentatge visible (per a l'alumnat)
**En acabar aquesta SA seré capaç de…**
- Mesurar la realitat amb precisió.
- Dissenyar amb mides i gruixos adequats a la impressió.
- Laminar amb Bambu Studio.
- Detectar i resoldre incidències d'impressió.

**Sabré que ho he aconseguit si… (criteris d'èxit)**
- [ ] He pres mides reals de l'objecte/espai.
- [ ] La peça és imprimible (gruixos i suports correctes) i he fet una **versió 2** després de
  la revisió amb la parella (i sé dir què hi he canviat).
- [ ] He laminat triant els paràmetres, i Bambu Studio diu **menys d'1 h i menys de 40 g**.
- [ ] La peça **funciona** per al que la vaig pensar.

## 🔑 Vocabulari clau (word wall)
`mida real` · `tolerància` · `gruix de paret` · `laminat` · `farciment` · `suport` · `adherència (brim)`

## 2. Competències específiques i criteris avaluats
- **CE1** → CA1.1, CA1.4
- **CE2** → CA2.2, CA2.3
- **CE3** → CA3.2, CA3.3
- **CE5** → CA5.2
- **CE6** → CA6.1, CA6.2

## 3. Sabers
- Disseny 3D funcional: mesures reals, toleràncies, gruixos mínims.
- **Revisió d'imprimibilitat i iteració digital** (v1 → retorn → v2) abans de fabricar.
- Impressió 3D: filament (PLA), **laminat** amb Bambu Studio (alçada de capa, farciment,
  adherència, suports), temps i material; límits de temps/material com a requisit de disseny.
- Postprocés i control de qualitat; incidències típiques (warping, no adherència, *stringing*).

## 4. Seqüència de sessions

### Sessió 1 — Detectar i dissenyar (2 h)
1. **Repte + mesurar el problema (30')**: identificar la necessitat i prendre **mides reals**
   (regle/peu de rei) de l'objecte/espai on anirà la peça. Recordar els **límits del repte**:
   la peça ha d'imprimir-se en **< 1 h i < 40 g** (ho comprovarem a Bambu Studio).
2. **Disseny a Tinkercad — versió 1 (65')**: modelar la peça amb les mides correctes; gruix
   mínim 2-3 mm; evitar suports si és possible.
3. **Revisió d'imprimibilitat per parelles (15')**: intercanvi de dissenys amb el **checklist
   d'imprimibilitat** de la fitxa (mides reals, gruixos, parts a l'aire, mida/temps). Cadascú fa
   la **versió 2** a partir del retorn rebut: aquesta iteració **en digital** és la cultura del
   prototip sense gastar filament, i és evidència de CA1.4.
4. **Diari (10')**: incloure captura de la v1 i la v2 amb una frase: "què he canviat i per què".

> ⏸️ **Mínim d'avui**: mides reals preses + v1 modelada (encara que sigui tosca). Si la revisió
> per parelles no hi cap, obre la sessió 2 amb ella — la v2 abans de laminar és el que no es
> pot saltar.

### Sessió 2 — Del model a la impressora (2 h)
1. **Exportar STL + Bambu Studio (40')**: importar, orientar la peça, paràmetres bàsics
   (alçada de capa, farciment 15-20 %, suports si cal, *brim* per a l'adherència).
2. **Comprendre el laminat (30')**: previsualització de capes, temps i grams estimats —
   **comprovar el límit del repte (< 1 h, < 40 g)**; si se supera, redissenyar (una iteració més!).
3. **Checkpoint del carnet 🟠 d'impressora 3D** (integrat en els torns): 3 preguntes de
   seguretat + enviar la impressió amb supervisió (`Normativa/Carnet_de_maquina.md`). Qui té el
   carnet pot operar la P2S la resta del curs.
4. **Cua d'impressió (40')**: agrupar les peces petites compatibles en **batches de placa**
   (4-8 peces per placa) i gestionar-los amb un **kanban visible** (Per imprimir · Imprimint ·
   Fet, una targeta per placa) i un criteri d'ordre **just** perquè tothom imprimeixi; les
   plaques que no caben a classe van **fora d'horari** (vegeu
   `Programació didàctica/Gestio_temps_maquina_fabricacio.md` §2B i §2C). Si la peça té un
   **encaix**, l'equip imprimeix primer una petita **mostra de tolerància** compartida (com la
   mostra d'encaix de SA3). Comencen les primeres plaques; reptes express mentre s'imprimeix.
5. **Diari (10')**.

### Sessió 3 — Impressió i seguiment (2 h)
1. **Seguiment d'impressions (continu)**: observar la primera capa (clau!), detectar problemes.
2. **Treball paral·lel (90')**: millorar el disseny, ajudar altres equips, reptes 3D.
3. **Diari (15')**.

### Sessió 4 — Postprocés i avaluació (2 h)
1. **Postprocés (40')**: retirar suports/*brim*, llimar, provar la funcionalitat real.
2. **Control de qualitat i iteració (40')**: funciona? què refaríem? (cultura del prototip).
3. **Galeria i avaluació (40')**: coavaluació i tancament al diari.

## 5. Producte final
Peça funcional impresa que resol una necessitat real + fitxa tècnica (mides, paràmetres) al
portafoli.

## 6. Atenció a la diversitat (DUA)
> 📌 Adaptacions completes (per barrera i per màquina) i la fila d'aquesta SA:
> `Programació didàctica/DUA_adaptacions_SA.md`.
- Banc de "problemes-tipus" amb diferent dificultat per a qui no trobi idea.
- Plantilles de mides i de paràmetres de laminat.
- Repte base (peça d'un sol cos) i ampliació ⭐ (peça amb encaix o moviment).

## 7. Recursos i materials
- Tinkercad; Bambu Studio; impressora **Bambu Lab P2S**; filament PLA; regle/peu de rei;
  eines de postprocés (alicates de tall, llima).
- `Normativa/Normes_seguretat_taller.md` (apartat 3D). `Fitxa_alumnat.md` · `Rubrica_SA5.md`.

## 🧠 Metacognició i tiquet de sortida
> ♻️ **Una sola reflexió per sessió:** la rutina o el tiquet **s'integren al diari** (ocupen
> una de les seves preguntes) — trieu-ne una per sessió, mai totes.
**Rutina d'anàlisi d'errors:** *Què ha passat / Per què / Com ho evito* davant una impressió
fallida (pròpia o d'un altre equip) — l'error com a font d'aprenentatge. Les peces fallides
instructives es **donen al Museu dels Errors** amb la seva targeta
(`Programació didàctica/Museu_dels_errors.md`).

**Tiquet de sortida:**
1. La decisió de laminat de què estic més content/a: …
2. Una incidència que he après a evitar: …
3. Com em sento amb la impressió 3D? 🔴 🟡 🟢

## 8. Avaluació — què s'avalua, amb què i qui

> SA curta → **rúbrica reduïda** (`Avaluació/Criteris_i_qualificacio.md` §2·bis). La versió
> per a l'alumnat és a la fitxa («Com m'avaluaran?»).

| Evidència (sessió d'on surt) | Instrument | Qui avalua | Criteris |
|------------------------------|-----------|------------|----------|
| **Peça impresa que funciona** per a la seva necessitat (S4) | Checklist de criteris d'èxit + fila «Funcionalitat» de `Rubrica_SA5.md` | Docent + autoaval. | CA1.1, CA2.2, CA3.2 |
| **Iteració digital v1→v2** amb el retorn de la parella (S1) | Fila «Iteració digital» de la rúbrica + captures al diari | Docent + parella | CA1.4 |
| **Laminat dins els límits** (< 1 h, < 40 g) + carnet 🟠 (S2) | Previsualització de Bambu Studio + checkpoint | Docent | CA3.2, CA6.1 |
| **Fitxa tècnica** (mides, paràmetres) (S1-S4) | Fitxa de l'alumnat completada | Docent | CA2.3, CA5.2 |
| **Gestió d'incidències** (primera capa, postprocés) (S3-S4) | Observació + rutina d'anàlisi d'errors (Museu) | Docents | CA3.3 |
| **Diari** (1 entrada/sessió + tancament amb 🎯) | Pauta del diari | Docent | CA5.2 |

**En tancar la SA:** nivell de les CE treballades → `Avaluació/Full_progres_competencial.md`.
