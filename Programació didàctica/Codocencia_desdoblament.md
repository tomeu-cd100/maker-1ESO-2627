# Codocència i desdoblament — «Aula Maker» (1r ESO)

> **Context organitzatiu:** grup de **20 alumnes** i **2 docents**; l'aforament de l'aula Maker
> és de **10 alumnes**. Es treballa en desdoblament: 10 a l'aula Maker i 10 a l'aula ordinària
> (propera, canvi d'espai viable en 10 minuts). Tot l'alumnat treballa amb **Chromebooks**.
>
> **La idea clau:** de les 2 h setmanals, només una part necessita l'aula Maker. El disseny, la
> documentació, la planificació i l'anàlisi es fan igual de bé (o millor) a l'aula ordinària.
> El desdoblament no és "la classe bona i la sala d'espera": són **dues estacions pedagògiques**
> (model de codocència per estacions, *station teaching*). I amb 10 alumnes per torn, la
> matemàtica del temps-màquina i les ràtios de seguretat **milloren**.

---

## 1. Model de rotació: dins de la mateixa sessió

Règim per defecte de cada sessió de 2 h:

| Franja | Grup A (10) | Grup B (10) |
|--------|-------------|-------------|
| 0–10' | **Obertura conjunta** a l'aula ordinària (hi cap tot el grup): 2' de *feed-forward* (recuperar l'objectiu personal del diari, si comença SA) + objectiu del dia + criteris d'èxit + Gran Idea del dia | |
| 10'–60' | 🔧 Aula Maker | 💻 Aula ordinària |
| 60'–70' | **Canvi d'espai** (rutina cronometrada: desar, moure's, seure) | |
| 70'–115' | 💻 Aula ordinària | 🔧 Aula Maker |
| 115'–120' | Tancament a l'espai on són: entrada al **diari de taller** | |

**Per què intra-sessió i no alternança setmanal:**
- Tothom toca màquines **cada setmana** (a 1r d'ESO, una setmana "sense Maker" desmotiva).
- Els dos grups avancen **sincronitzats** dins la mateixa SA: una sola programació.
- El co-docent sosté **50 minuts** de tasca pautada, no 2 hores.

**Excepcions (grup sencer, els dos docents junts, a l'aula ordinària o espai gran):**
- Sessió 1 de cada SA (presentació del repte i activació) — inclou la gimcana de seguretat de SA1.
- Galeries, coavaluacions i tancaments de SA.
- Presentacions de SA3 i SA6, i la **Fira** de SA9 (els visitants passen per l'aula Maker en
  grups de ≤10, respectant l'aforament).

## 2. Les dues estacions

| | 🔧 Estació Maker (docent Maker) | 💻 Estació de disseny i pensament (co-docent) |
|--|--|--|
| **Què s'hi fa** | Fabricació làser/3D, laminat, checkpoints del carnet, càmera 360, ulleres VR, postprocés, mostres d'encaix/tolerància | Disseny amb eines de navegador, esbossos amb mides, revisió v1→v2 per parelles, diari de taller, fitxes, reptes express, simulacions, anàlisi crítica VR, guions i assaig de presentacions |
| **Què demana del docent** | Expertesa tècnica i de seguretat | Gestió d'aula i acompanyament del pensament — **cap coneixement de màquines** |
| **Materials de suport** | Cada SA + `Gestio_temps_maquina_fabricacio.md` | `Fitxa_alumnat.md` i `Exemple_resolt.md` de cada SA, `Reptes/`, `Simulacions/`, `Avaluació/Diari_de_taller.md` |

> El material ja és autoportant per a l'estació de disseny: les fitxes són pas a pas, els
> criteris d'èxit són observables i l'exemple resolt mostra com és un treball ben fet. El
> co-docent no ensenya l'eina: fa que l'alumnat **segueixi la fitxa, es revisi per parelles i
> documenti**. Vegeu `00_Guia_inici_codocent.md`.

## 3. Chromebooks: què hi corre i què no

| Eina | Al Chromebook? | On s'usa |
|------|:--:|----------|
| **Tinkercad** (3D) | ✅ navegador | Estació de disseny |
| **CoSpaces Edu** (VR) | ✅ navegador | Estació de disseny |
| Diari / portafoli (Docs, Slides…) | ✅ | Les dues estacions |
| Visor de fotos 360 / tours | ✅ generalment navegador | Les dues estacions |
| **Inkscape** (2D) | ⚠️ només amb l'entorn **Linux** activat pel coordinador TIC | Vegeu els 2 escenaris ↓ |
| **xTool Creative Space** | ❌ | Ordinador del làser (aula Maker) |
| **Bambu Studio** | ❌ | Ordinador de la impressora (aula Maker) |

**Configuració del centre (decisió presa):** el coordinador TIC activa **Linux + Inkscape**
als Chromebooks. Per tant, **tot el disseny 2D es fa a l'estació ordinària** i el torn de
l'aula Maker queda net per a **fabricació** → més peces per sessió i cap alumne "esperant
màquina" davant d'un ordinador que podria ser a l'altra aula.

> Pla B (si algun Chromebook falla o Linux dona problemes): els ordinadors de la zona de
> disseny de l'aula Maker tenen Inkscape i fan de reserva dins el torn de 50'.
>
> Al 2n i 3r trimestre no hi ha dependència: Tinkercad i CoSpaces són de navegador, i el
> laminat amb Bambu Studio és una tasca curta de l'estació Maker.

## 4. Estacions per SA (que fa cada meitat de sessió)

| SA | 🔧 Estació Maker (50') | 💻 Estació de disseny (50') |
|----|------------------------|------------------------------|
| SA1 | Fabricació batch del clauer + checkpoint carnet 🔴 + repàs de fitxers a punt de tall | Esbós amb mides, **disseny Inkscape (Chromebook)**, contracte, vocabulari, diari |
| SA2 | Fabricació batch, preparació a XCS, postprocés | Esbós, **Inkscape: operacions de camí i vectorització (Chromebook)**, fitxa, diari |
| SA3 | Mostra d'encaix + mesura del kerf, fabricació, muntatge i ajust | Requisits, **disseny de peces i unions a Inkscape (Chromebook)**, rols (signatura de peça), guió de presentació |
| SA4 | Demo P2S + batch de placa de mostres + observació d'impressió | **Tot el modelatge Tinkercad** (navegador), reptes 3D, diari |
| SA5 | Laminat (Bambu Studio per torns), checkpoint carnet 🟠, kanban, primera capa, postprocés | Mesures reals, modelatge Tinkercad, revisió v1→v2 per parelles, fitxa tècnica |
| SA6 | Laminat i batches de placa, impressió, muntatge, proves amb l'usuari | Empatia i requisits, modelatge de cada peça, coordinació de mides, presentació |
| SA7 | Càmera 360 (torns de captura), checkpoint carnet 🟢, visualització VR | Pla de rodatge, guió i etiquetes del tour, selecció d'imatges, muntatge del tour (navegador) |
| SA8 | Exploració i proves amb ulleres (5 ulleres per a 10 = parelles usuari-guia perfectes), checkpoint carnet 🔵 | Fitxa d'anàlisi crítica, escena CoSpaces (navegador), preparació del debat |
| SA9 | Fabricació de l'estand (làser/3D) + prova del component immersiu | Pla de projecte, retolació, guions, CoSpaces/tour, assaig de presentació |

## 5. Grups i equips

- **Dos grups estables (A i B) heterogenis**, formats amb l'`Avaluació/Avaluacio_inicial.md`.
- Els **equips de 3-4 sencers dins del mateix grup**: mai un equip partit entre estacions.
- **Regla de sincronia:** cap grup comença una fase nova de la SA que l'altre no hagi tancat;
  els **reptes express** absorbeixen els desajustos de ritme.
- Alterneu **quin grup comença** a l'aula Maker (setmanes senars A, parelles B): que la fatiga
  del final de sessió no toqui sempre al mateix grup.

## 6. El co-docent: d'acompanyant a maker (arc del curs)

1. **Acollida (30 min de lectura):** només 3 documents — `00_Guia_inici_codocent.md`, les
   normes de seguretat i la fitxa + exemple resolt de la SA en curs. La resta s'aprèn fent.
2. **El profe també es treu els carnets** 🔴🟠🟢🔵 (`Normativa/Carnet_de_maquina.md`), davant
   de l'alumnat si cal: un adult que aprèn, s'equivoca i itera és la **cultura del prototip
   encarnada**, i el missatge d'equitat més potent que pot donar l'assignatura.
3. **Progressió de responsabilitat:**
   - **T1:** estació de disseny i pensament.
   - **T2:** a més, pot supervisar el **kanban** i els batches de placa (gestió visual, no
     tècnica) un cop tingui el carnet 🟠.
   - **T3:** pot dur l'**estació VR** (el protocol és de gestió: torns, temps, higiene, guies)
     amb el carnet 🔵.
4. **Repartiment de l'avaluació** — cadascú avalua allò que veu a la seva estació:

| Docent Maker | Co-docent |
|--------------|-----------|
| CA2 (qualitat tècnica del disseny) | CA1 (procés: requisits, idees, planificació, iteració v1→v2) |
| CA3 (fabricació) i CA4 (immersiu) | CA5 (equip, documentació, comunicació) |
| CA6.1 (seguretat) i CA6.2 (material) | CA6.3 (ètica digital) i **TE** (participació equitativa) |

> Cada docent duu el seu `Avaluació/Full_seguiment_grup.md` (codis +/-/!) i es posen en comú
> a la coordinació setmanal. El co-docent avalua justament les competències **transversals**,
> on la seva mirada externa és un actiu. Les rúbriques de SA es passen conjuntament.

## 7. Rituals de coordinació (el mínim imprescindible)

- **10 minuts setmanals** de traspàs entre docents (davant del kanban): qui va endarrerit,
  quin equip té prioritat de màquina, incidències, dubtes tècnics recollits (vegeu el
  mecanisme SOS de la guia del co-docent).
- **El diari de taller viatja amb l'alumne**: és el fil que cus les dues estacions.
- **Kanban compartit** visible (foto al final de cada sessió si cal).
- Un cop per trimestre, **intercanvi de mirada**: el co-docent passa una sessió a l'estació
  Maker (i tu a la seva) per calibrar l'observació i l'avaluació.
- Un cop per trimestre, **revisió d'equitat amb dades** (10'): recompte del registre de
  carnets i del kanban — qui ha operat màquines i quantes vegades
  (`Equitat_genere_STEAM.md` §3·bis).

## 8. Seguretat i aforament

- L'aforament de 10 és **normatiu**: cap alumne de més a l'aula Maker, tampoc "un moment".
- El docent Maker mai deixa la sala amb màquines en marxa (les normes ja ho recullen); si ha
  de sortir, s'atura la fabricació.
- A la Fira (SA9), els visitants entren a l'aula Maker en **grups de ≤10 comptats a la porta**
  (rol d'alumne/a "controlador d'aforament": responsabilitat real i avaluable).

> Relacionat amb: `00_Guia_inici_codocent.md`, `Gestio_temps_maquina_fabricacio.md` (la
> matemàtica del temps amb grups de 10), `Aprenentatge_cooperatiu.md`, `Normativa/Carnet_de_maquina.md`
> i `Avaluació/Criteris_i_qualificacio.md` (§2·bis, jerarquia d'instruments).
