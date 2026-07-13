# 🔍 Auditoria profunda del curs — juliol 2026

> ✅ **ESTAT: IMPLEMENTADA (13-07-2026).** Les 7 fases (F1–F7) s'han aplicat i pujat a `main` en
> commits separats per fase. Cada fase va passar `verifica_enllacos.py` i
> `verifica_competencies.py`; el build final genera 104 pàgines sense errors. Aquest document
> es conserva com a registre del que es va detectar i corregir.

**Lent única:** què ajuda (o dificulta) que l'alumne aprengui.
**Abast:** les 10 SA senceres (guió docent, fitxa, rúbrica, exemple resolt), tota l'avaluació,
tota la programació didàctica, tota la normativa, el material transversal de l'alumne
(vocabulari, diari de classe, reptes, recursos, simulacions) i la progressió/càrrega
cognitiva transversal SA0→SA9.
**Mètode:** 7 revisions independents en paral·lel (T1, T2, T3, avaluació,
programació+normativa, material transversal, progressió cognitiva), ~180 troballes brutes,
deduplicades i verificades per mostreig (5/5 confirmades contra els fitxers).

---

## 1. Les 14 troballes crítiques (convergents o d'impacte alt)

Les marcades amb ✳️ van ser detectades independentment per 2 o més revisions.

### Errors tècnics i de seguretat (arreglar abans que res)

1. **«Les lletres cauen quan es talla» és fals amb el codi del curs** — `Classes/SA1_Benvinguts_Aula_Maker/SA1.md:93`.
   El nom va en negre = gravat, i el gravat no cau mai. El «truc maker» només aplica a les
   lletres calades (vermell). Contradicció tècnica al primer disseny del curs.
   → Reformular: «tot el que sigui VERMELL (tall) i quedi solt, cau; el negre gravat mai cau».

2. **Metacrilat transparent no es pot tallar amb la xTool S1** (làser de díode: el feix el
   travessa) — `SA1.md:150` i `Material_gimcana_seguretat.md:59` el proposen sense distingir.
   → «Metacrilat només opac/de colors, mai transparent» als dos llocs.

3. **Instrucció contradictòria en cas de flama** — `Normativa/Normes_seguretat_taller.md:26`
   diu «extintor / pot d'aigua» i la línia 46 diu «no apagar amb aigua aparells elèctrics».
   → L'alumne mai apaga res: para la màquina i avisa. Treure «pot d'aigua» del text d'alumne.

4. **Error de tolerància a l'exemple de SA6** — `Exemple_resolt.md:37-39`: llapis de 8 mm →
   «forat de 8 mm» que «va anar bé». En FDM un forat de Ø8 queda a ~7,6. Ensenya el contrari
   de la lliçó de tolerància de SA5. → «forat de 8,5 mm (tolerància!)».

### Risc normatiu real (RGPD / edat)

5. ✳️ **El consentiment d'imatge no cobreix la publicació del tour** —
   `Normativa/Autoritzacio_families_VR_360.md:27-28` autoritza ús «dins l'àmbit del centre»,
   però SA7 publica el tour a la web pública amb QR. → Casella específica «publicació al web
   del centre» a l'autorització, o norma dura: cap persona identificable a les captures.

6. **L'autorització VR no recull la data de naixement ni el criteri 13+** que el
   `Protocol_us_VR.md` declara aplicable (Quest 3, comptes de centre) —
   `Autoritzacio_families_VR_360.md:23`. La carta a famílies (línia 40) encara diu «alguns
   models recomanen 13 anys». → Alinear autorització i carta amb el protocol: pantalla com a
   via principal, ulleres condicionades a edat.

7. **L'exemple resolt de SA9 modela una infracció**: «la gent feia cua per provar les
   ulleres» a la Fira (públic de 6è = 11 anys, sense autorització) —
   `Classes/SA9_Projecte_final/Exemple_resolt.md:44`. → «la gent explorava el tour a la
   pantalla gran»; regla de Fira: visitants només pantalla.

### Forats de planificació que trencaran classes

8. ✳️ **L'eina per muntar el tour de SA7 no existeix enlloc** (4 revisions independents la
   van trobar): `SA7.md:97` diu «programari/visor de tours», `Enllacos_i_tutorials.md:74` en
   blanc, cap demo. 60' de muntatge amb eina fantasma. → Decidir eina (CoSpaces amb fons 360
   és la més coherent: ja la tenen de SA8… però SA8 va DESPRÉS; alternatives: Marzipano,
   H5P) + demo de 15' + xuleta de 5 passos.

9. ✳️ **El carnet 🔵 de VR arriba una setmana DESPRÉS del primer ús real de VR** (SA7 S3,
   setmana 28 vs SA8 S1, setmana 29) — trenca la regla «sense carnet no s'opera» des de dins.
   → Avançar el mini-checkpoint 🔵 als torns de visualització de SA7 S3.

10. ✳️ **`Gestio_temps_maquina_fabricacio.md` calcula tot amb ~25 alumnes** quan la decisió
    presa és grup de 20 amb torns de 10 (`Codocencia_desdoblament.md:3`). Les matemàtiques
    del coll d'ampolla estan sobredimensionades; el full de torns de càmera no funciona amb
    desdoblament. → Reescriure §1 i §5 amb 20/10.

11. **La «vàlvula de contingència» del calendari no allibera temps real** —
    `Temporitzacio_anual.md:97`: la sessió ⭐ de SA8 no ocupa cap setmana. Quan es perdi una
    setmana, l'única vàlvula real és comprimir SA9 i es descobrirà al juny. → Corregir la
    taula de contingències.

12. ✳️ **SA9 demana crear el component immersiu en 100'** (SA7 hi va dedicar 3 sessions,
    SA8 dues) sense dir enlloc que reutilitzar el tour de SA7 o l'escena de SA8 és legítim.
    → Explicitar la reutilització + ⏸️ mínim a la S3.

### Contractes d'avaluació trencats (patró transversal)

13. ✳️ **El pacte «criteri d'èxit = nivell AN de la rúbrica» es trenca a 6 SA**:
    - SA2: AN exigeix «operacions de camí» que cap criteri d'èxit demana (`Rubrica_SA2.md:7`).
    - SA3: «iterar» és criteri d'èxit però a la rúbrica és AE (`Rubrica_SA3.md:9`).
    - SA4: el nom en relleu és requisit a la fitxa però ampliació al guió (`Fitxa:9` vs `SA4.md:81`).
    - SA6: «prova amb usuari» és criteri d'èxit però AE a la rúbrica (`Rubrica_SA6.md:10`).
    - SA7/SA8: §2 declara CA focals (CA3.3, CA4.3, CA6.3) que cap fila de rúbrica ni evidència recull.
    - SA1: CA1.1 focal sense instrument (`SA1.md:57`).
    → Passada sistemàtica de coherència per SA (quadre criteri↔AN↔fitxa) — és el bloc amb més
    impacte directe en la confiança de l'alumne en el sistema.

14. ✳️ **Triple autoavaluació al tancament de cada SA** (diari + rúbrica amigable + full A,
    més B/B·bis/diana/galeria/tiquet a SA3/6/9) i **5 escales conviuen** (1-4, NA/AS/AN/AE,
    🌱🙂💪🌟, 😟🙂😀🤩 del diari, semàfor) — `Avaluació/Autoavaluacio_coavaluacio.md:23-38`,
    `Diari_de_taller.md:54`. El principi ♻️ protegeix la sessió però no el tancament.
    → UNA autoavaluació de tancament (la rúbrica amigable absorbeix la resta), escala emoji
    única 🌱🙂💪🌟, i el termòmetre d'autonomia amb iconografia pròpia (no 🌱🙂💪🌟).

---

## 2. Totes les troballes, per àmbit

Format: `fitxer` — problema → proposta. **[A]**lta / **[M]**itjana / **[B]**aixa.

### 2.1 SA0–SA3 (T1)

- **[A]** `SA2.md:37-40`+`Rubrica_SA2.md:7` — criteris d'èxit sense operacions de camí però AN les exigeix → afegir criteri «forma nova amb unió o diferència» (→ crítica 13).
- **[A]** `Rubrica_SA3.md:9` — «itera» a AE quan és criteri d'èxit → AN = «millora el prototip almenys un cop» (→ crítica 13).
- **[A]** `SA1.md:57` — CA1.1 focal sense fila de rúbrica ni evidència → treure'l o lligar-lo a l'esbós (→ crítica 13).
- **[A]** `SA2.md:51-53` — CA1.1/CA1.2/CA3.3 focals sense evidència; la rúbrica demana «diverses idees» que la fitxa mai fa produir → afegir «idees provades (mín. 2)» a la fitxa.
- **[A]** `SA1.md:93-94` — truc de les lletres fals (→ crítica 1).
- **[A]** `Fitxa SA1:18` — «forat prop d'una vora» sense distància mínima, indueix l'error del contraexemple → «centre a ~6 mm; vora del forat a ≥3 mm».
- **[A]** `SA1.md:122-125` — S3 sense ⏸️ ni camí per a qui falla el checkpoint del carnet → «el disseny entra igualment al batch; el checkpoint es repeteix als torns o a SA2».
- **[A]** `SA1.md:150`+gimcana — metacrilat transparent (→ crítica 2).
- **[M]** `Fitxa SA1:32-46` — esbós de la fitxa duplica i contradiu el full mil·limetrat de S1 → referenciar el full imprès.
- **[M]** `SA2.md:40`+`Rubrica_SA2.md:11` — «aprofitar bé la planxa» no observable → quantificar (≤10 mm entre peces).
- **[M]** `SA3.md:41-44` — criteris tots d'equip → afegir criteri individual «puc ensenyar LA MEVA peça».
- **[M]** `Fitxa SA1:19-20` — la convenció de capes «te l'explica el profe» però no és escrita → escriure-la (vermell #FF0000 0,1 mm / negre ompliment).
- **[M]** `Fitxa SA2:16`+exemple — «llindar» no definit → definir en línia i al word wall.
- **[M]** `Exemple SA2:10-23` — sense SVG real descarregable (SA1 en té) → crear `marcapagines_exemple.svg` amb capes.
- **[M]** `SA3.md:82-83` — encaixos: única bastida és demo de 25' → fitxa visual «Com dibuixo una ranura de 3 mm».
- **[M]** `SA3.md:74-79` — S1 suma 110' i sense temps de diari → esbós 40' + diari 10'.
- **[M]** `SA0.md:79-80`+gimcana:4 — gimcana 50' vs 35' (i 33' reals) → unificar a 50', Prova 2 amb 8 targetes.
- **[M]** `SA0.md:86` — «cap barrera de lectoescriptura» però proves 2-4 són text dens → lectura en veu alta per un membre + pictogrames.
- **[M]** `SA3.md:86-87` — només S2 té ⏸️ en 5 sessions → afegir a S1, S3, S4.
- **[M]** `Rubrica_SA1:8-9` (i SA2, SA3) — AS definit per «amb ajuda» penalitza demanar ajuda → redefinir AS pel producte.
- **[M]** `SA3.md:104-107` — Fira sense pla B per a equips inacabats → «prototip + mostra + què falta: el procés també és producte».
- **[B]** `SA2.md:69-73` — S1 suma 110' i sense ⏸️ → ajustar i afegir mínim.
- **[B]** `Rubrica_SA2:8` — NA sense «Encara no» → corregir.
- **[B]** `SA0.md:71` — 5' per a la primera entrada de diari de la vida → 10-15' i modelar-la en veu alta.
- **[B]** `Rubrica_SA3:10` — fila «Funcionalitat» sense codi CA → assignar CA3.3.

### 2.2 SA4–SA6 (T2)

- **[A]** `Fitxa SA4:9` vs `SA4.md:81` — nom en relleu: requisit o ampliació? → decidir (⭐) i alinear els 3 documents (→ crítica 13).
- **[A]** `Exemple SA4:18` — exemple de 55 mm amb criteri de màx ~50 mm → exemple a 45 mm + línia «comprovo el límit».
- **[A]** `SA6.md:41` — «hem entès la necessitat» no verificable → «≥3 requisits i ≥1 restricció sortits de parlar amb l'usuari».
- **[A]** `Rubrica_SA6:10` — prova amb usuari a AE quan és criteri d'èxit → AN (→ crítica 13).
- **[A]** `Fitxa SA6:9-13` — fase d'empatia sense bastida d'entrevista → miniguió de 4-5 preguntes.
- **[A]** `SA6.md:104` — prova amb usuari real en horari de classe sense pla B → prova delegada amb evidència (foto/vídeo) o usuari-proxy.
- **[A]** `SA5.md:79-83` — la v2 no té temps de modelatge assignat → 20-25' a l'inici de S2.
- **[A]** `SA5.md:42` — laminat individual impossible en 1 estació (4-5'/alumne) → laminar per parelles + Bambu Studio «en fred» a 2-3 PCs.
- **[A]** `Exemple SA6:37-39` — error de tolerància Ø8 (→ crítica 4).
- **[M]** `SA4.md:37` — «gruix suficient» no quantificat i 3 formulacions diferents → «≥3 mm» pertot.
- **[M]** `SA4.md:38-39` — «sense suports» sense regla de comprovació → «mira-la de costat: res en l'aire».
- **[M]** `Fitxa SA5:38` vs `:62` — gruix «2-3 mm» vs «≥2 mm» vs «≥3 mm» a SA4 → un únic llindar de curs.
- **[M]** `Rubrica_SA4:8` — límits de batch (50 mm, pla, sense suports) fora de la rúbrica → a la cel·la AN.
- **[M]** `Rubrica_SA6:13` — Comunicació AN «Clara» / AE «Clara i convincent» → ancorar en fets.
- **[M]** `SA6.md:22-23` — opcions «joc» i «peça per al centre» sense usuari real evident → assignar usuari per opció.
- **[M]** `Exemple SA6:9-16` — una sola peça per a 4 persones: no modela conjunt coordinat → exemple amb 3-4 peces que encaixen.
- **[M]** `SA5`/`SA6` — ⏸️ absents a SA5 S2-S4 i SA6 S1/S3-S5 → afegir-ne (laminat comprovat, usuari+requisits, feedback anotat).
- **[M]** `SA5.md:106-109` — 90' de «treball paral·lel» sense tasca → fitxa tècnica + rutina del Museu.
- **[M]** `SA5.md:38-43` — CA3.3 focal sense criteri d'èxit → «sé explicar una incidència: què/per què/com l'evito».
- **[M]** `Fitxa SA5:71-80` — taula «Com m'avaluaran» omet el diari → afegir fila.
- **[M]** `SA5.md:46` — «tolerància» mai definida en material d'alumne → definició d'una línia a la fitxa.
- **[B]** `SA4.md:83` — ⏸️ trenca la numeració de la llista → moure'l.
- **[B]** `Fitxa SA4:21-30` — 3 vistes sense mini-exemple → afegir-ne un.
- **[B]** `SA6.md:85-100` — S2 i S3 sense temps de diari → 5-10' de tancament.
- **[B]** `Fitxa SA6:13` — límits 1h/40g no apareixen fins a la Fase 3 → preimprimir a la Fase 1.

### 2.3 SA7–SA9 (T3)

- **[A]** `SA7.md:97` — eina de tour fantasma (→ crítica 8).
- **[A]** `SA9.md:96`+fitxa — portafoli final sense guió ni índex → guió-checklist (1 evidència/trimestre + reflexió) construït a S2-S4.
- **[A]** `SA9.md:84-85` — component immersiu en 100' (→ crítica 12).
- **[A]** `SA7.md:53-57` vs rúbrica — CA3.3/CA4.3 declarats i no avaluats (→ crítica 13).
- **[A]** `SA8.md:52-57` vs rúbrica — CA3.3/CA6.3 idem (→ crítica 13).
- **[A]** `Autoritzacio:27-28` vs SA7 — RGPD publicació (→ crítica 5).
- **[A]** `Exemple SA9:44` — cua per provar ulleres a la Fira (→ crítica 7).
- **[A]** `SA9.md:41-44` — «presentació clara i atractiva» i «portafoli complet» no observables → mini-guió de presentació d'1-2 min + guió del portafoli.
- **[M]** `SA7.md:40-41` — criteri «publicat» depèn del centre, no de l'alumne → «a punt de publicar (revisat + QR generat)».
- **[M]** `SA7.md:84-89` — torns de càmera de 12' amb desplaçament + checkpoint → espais propers, carnet a S1, màx 2 espais/torn.
- **[M]** `SA7.md:81-89` — equip fora de l'aula amb càmera sense supervisió definida → un codocent acompanya sempre.
- **[M]** `SA7.md:92-94`+`SA8.md:90-92` — cap pla B de maquinari (càmera/CoSpaces) → photo sphere de mòbil + banc d'imatges 360 + storyboard en paper.
- **[M]** `SA7.md:103-105` — ulleres a SA7 sense carnet 🔵 (→ crítica 9).
- **[M]** `SA7.md:98-102` — revisió de drets d'imatge en 10' per a 6-7 equips → checklist per equip dins del muntatge.
- **[M]** `Fitxa SA7:38-46` — taula d'avaluació omet diari i coavaluació → afegir files.
- **[M]** `SA7.md:37`+rúbrica — «estables i ben il·luminades» no observable → 3 checks (horitzó recte, sense borrós, detalls a l'ombra).
- **[M]** `SA8.md:38-41`+rúbrica — «explorable» no reutilitza la definició del ⏸️ (3-4 objectes + text + càmera) → copiar-la al criteri i a AN.
- **[M]** `SA8.md:117` — CoSpaces Pro necessari per a CoBlocks i grups, no dit → anotar requisit de llicència a §7.
- **[M]** `SA9.md:77-96` — només S2 té ⏸️ → afegir a S3 i S4.
- **[M]** `SA9.md:81-82` — sense pla B si la fabricació falla la setmana 33-34 → reimprimir reduït o adaptar peça de SA1-SA6 documentant la incidència.
- **[M]** `Rubrica_SA8:9` — AS «Idea única» sona a elogi → «proposa una sola idea, sense comparar».
- **[B]** `Rubrica_SA7:11`+SA8 — nivells de Comunicació d'una paraula → ancorar AE en conductes.
- **[B]** `Rubrica_SA9:10` — fila sense codi CA → assignar-lo.
- **[B]** `SA8.md:60-61` — «graus de llibertat» declarat i mai treballat → treure o convertir en pregunta de la fitxa.
- **[B]** `SA8.md:72-84` — S1 sense ⏸️ → «Part B completa + tema triat».

### 2.4 Avaluació

- **[A]** `Criteris_i_qualificacio.md:165-168` — cap revisió docent contra rúbrica ABANS del tancament → revisió intermèdia obligatòria a la sessió central de SA3/6/9 amb «següent pas» escrit.
- **[A]** `Rubrica_alumnat_amigable.md:39-43` — falta la fila d'ètica digital (CA6.3) → afegir «Respecto drets d'imatge i llicències».
- **[A]** `Autoavaluacio_coavaluacio.md:23-38` — triple autoavaluació al tancament (→ crítica 14).
- **[A]** `Diari_de_taller.md:54` — escala 😟🙂😀🤩 diferent de la canònica i 😟 contradiu el «encara no» → 🌱🙂💪🌟.
- **[A]** `Full_seguiment_grup.md:8` — «Autonomia» i «Actitud» sense descriptors (20 % de la nota) → ancorar al termòmetre + conductes observables.
- **[M]** `Avaluacio_explicada_alumnat.md:56-57` — el Museu dels Errors promès com a «no resta» sense mecanisme → evidència de CA1.4 a la fila «Procés i iteració».
- **[M]** `Autoavaluacio:3`+`Full_seguiment:3` — «10 %/20 % de la nota» contradiu el «no és mitjana ponderada» → «pes orientatiu dins el judici».
- **[M]** `Autoavaluacio:42-49` — graella B sense descriptors ni evidència → ancoratges 1-4 + casella «on ho he vist».
- **[M]** `Criteris:37` — promet versió curta d'auto/coavaluació que no existeix → afegir secció «A·curta».
- **[M]** `Instruments_formatius:27-35` — termòmetre reutilitza 🌱🙂💪🌟 amb semàntica diferent → iconografia pròpia.
- **[M]** `Rubrica_general:14-18` — CA1.3 (planificar) sense indicadors → afegir fila.
- **[M]** `Criteris:113` — TA marcat a SA3/5/7 sense instrument → nota TA a Rubrica_SA3 o treure ●.
- **[M]** `Criteris:109-110` — CA6.1/CA6.2 sense fila a rúbriques SA3/SA6 → afegir CA6.2 o nota al peu.
- **[M]** `Rubrica_SA3:10-13` — files duplicades amb Rubrica_producte_final → repartir àmbits.
- **[M]** `Rubrica_producte_final:12` — «Creativitat» 15 % sense CA → vincular a CA1.2 en clau de procés.
- **[M]** `Diari_de_taller:88` — «nota que mereixo» contradiu «no hi ha notes» → «quin nivell 🌱🙂💪🌟 i quina evidència».
- **[M]** `Rubrica_amigable:51` — «marca cada fila» = 14 files per SA → només les files de la SA.
- **[M]** `Questionaris_repas.md:59-63` — distractor SA0 parcialment cert → resposta bona «…i formar equips equilibrats».
- **[M]** escales — 5 escales conviuen (→ crítica 14).
- **[M]** `Instruments:5` — «trieu 1-2» + diari = 3 reflexions/dia possibles → el diari compta com un dels 1-2; tiquet 3-2-1 → 1-1-1.
- **[M]** `Full_seguiment:8` vs `Quadern:27-30` vs `Criteris:35` — 3 estructures per al mateix registre d'observació → unificar codis +/-/! amb regla de conversió.
- **[B]** `Quadern:56` — cita §9 inexistent → §8.
- **[B]** `Questionaris_repas:9-10` — banc duplicat generador/md sense regla de sincronització → declarar font i nota.
- **[B]** `Full_progres:71` — TE/TA tractats com a files equivalents a CE → aclarir que maticen, no sumen.

### 2.5 Programació didàctica i normativa

- **[A]** `Gestio_temps:4,24,57,120` — càlculs amb ~25 alumnes (→ crítica 10).
- **[A]** `Temporitzacio:74,97` — vàlvula de contingència fantasma (→ crítica 11).
- **[A]** `Temporitzacio:48`+`Codocencia:118` — VR a SA7 sense carnet 🔵 (→ crítica 9).
- **[A]** `Codocencia:150` — el docent Maker avalua CA2 (disseny) que passa tot a l'estació del codocent → repartir CA2.1/2.2 al codocent.
- **[A]** `Programacio:166-168` — forquilles de trimestre no quadren amb les Fires (13/25/35) → corregir a 1-13/14-25/26-35.
- **[A]** `Carnet:31` vs `Temporitzacio:33-34` — setmana del carnet 🟠 ambigua (laminat a S2 o S3?) → alinear temporització amb SA5.md.
- **[A]** `Autoritzacio:23` — sense data de naixement ni criteri 13+ (→ crítica 6).
- **[A]** `Autoritzacio:27-28` — àmbit del consentiment (→ crítica 5).
- **[A]** `Carta_families:47-48` — falta la mini-taula de dates de les 3 Fires → afegir placeholder.
- **[M]** `Gestio_temps:88-93` vs cooperatiu — dos sistemes de rols de 4 sense mapa → «barrets de fabricació» mapats sobre els rols de SA.
- **[M]** `DUA_adaptacions:130-140` — falta la fila SA0 → afegir (avaluació 0 oral/gràfica, agenda visual).
- **[M]** `Carta_families` — no menciona la web del curs ni la barra DUA → afegir punt amb URL.
- **[M]** `Carta_families:40` — «recomanen 13 anys» desalineat amb el protocol → reformular.
- **[M]** `Museu_errors:41-53` — votació 🏆 i «5' al museu» sense slot al calendari → fites a les setmanes 13/25/35 i 1a sessió de fabricació.
- **[M]** `Normes_seguretat:26` vs `:46` — aigua i flama (→ crítica 3).
- **[M]** `Reglament_aula` — ni aforament 10 ni «sense carnet no s'opera» al document d'alumne → afegir 2 punts.
- **[M]** `Gestio_temps:119` — matemàtica de SA7 per a grup sencer → recalcular per a desdoblament (3 equips × 15').
- **[M]** `Temporitzacio:38` — iteració de SA6 no cap en 1 setmana d'impressió → 1a tanda fora d'horari a la setmana 22.
- **[M]** `Gestio_temps:50` — impressió dels clauers de SA4 sense setmana assignada → «fora d'horari setmanes 16-17, es reparteix a SA5».
- **[M]** `Codocencia:112` — «contracte» a SA1 quan es signa a SA0 → «repàs del contracte».
- **[M]** `Protocol_VR:6-23` — §1 en llenguatge d'adult, sense resum de les 4 regles per a l'alumne → quadre «🥽 Les 4 regles VR».
- **[B]** `Codocencia:24` — segon torn és de 45', no 50' → dir-ho.
- **[B]** `Temporitzacio:97` — contingència cita setmana 33 (immersiu) per a muntatge → corregir a 34.
- **[B]** `Marc_normatiu:21-27` — falten CCEC i CP → remetre al Mapatge.
- **[B]** `Gestio_temps:26,43,124` — xifres internes inconsistents (rangs, 15-20 vs 75, 2 vs 3 equips) → unificar.
- **[B]** `Museu_errors:11` — peces del museu a l'aula Maker però s'analitzen a l'estació de disseny (aula ordinària) → capsa de préstec viatgera.

### 2.6 Material transversal de l'alumne

- **[A]** `Vocabulari_basic.md` — cap terme de SA6 ni SA9; ~10 termes de word walls absents; columna «Quan» amb 5-6 errors → completar i corregir.
- **[A]** `Simulacions/Experiencies_VR_360:11`+`Enllacos:74` — eina de tour i càmera 360 indefinides (→ crítica 8).
- **[A]** `Index_reptes:20` — «repte completat» sense definició de validació → «compta quan és al diari amb foto i algú l'ha vist funcionar».
- **[A]** `Guions_de_demo:5` — falten les 2 demos més crítiques: SVG→XCS→làser (setmana 5) i muntatge del tour (setmana 28) → Demo 9 i Demo 10.
- **[M]** `Guions_de_demo:14,42,67` — demos 1, 3 i 4 desfasades una setmana respecte del diari/temporització → corregir setmanes.
- **[M]** `Temporitzacio:33` vs diari vs SA5 — setmanes 17-19 de SA5 no quadren entre documents (→ crítica de coherència; unificar amb el carnet 🟠).
- **[M]** `Diari_alumnat:70` — text a camí presentat com a novetat la setmana 6 quan el semàfor l'exigeix la 5 → requisit a la targeta 5, consolidació a la 6.
- **[M]** `Diari_alumnat:25` — setmanes 6, 8, 14, 19, 24, 28 sense «què no pots oblidar» → afegir ⏸️/recordatoris.
- **[M]** `Primers_auxilis:33` — falten 3 errors freqüents (làser marca però no talla; primera capa/espagueti en directe; STL exportat a mitges) → afegir files.
- **[M]** `Projecte_personal:22` — sense checkpoints datats → 3 checkpoints a les setmanes 13/25/35 lligats al passaport.
- **[M]** `Enllacos:14` — secció d'impressió 3D amb 🟢 (que és càmera) → 🟠.
- **[M]** `Enllacos:10,26,27,60-61` — 4 enllaços fràgils (xtec personal, blogs, id numèric) → revisió de setembre + substituts estables.
- **[M]** `Capsules_inspirat:59` — un sol referent femení amb nom; cap jove/local → afegir 2-3 noms concrets.
- **[M]** `Laboratoris_virtuals` — fitxer orfe sense cap referència des de les SA → enllaçar des de SA3/SA4 o fusionar.
- **[M]** `Reptes_immersius:8` — reptes «mentre esperes» que necessiten la càmera per la qual s'espera → reformular amb imatges ja capturades.
- **[B]** `Index_reptes:19` — «(suggeriment)» vs passaport imprès → treure.
- **[B]** `Reptes_express_2D:15` — reptes ⭐⭐⭐ sense «des de SA_x» → afegir.
- **[B]** `Reptes_3D:3` — «no ocupen impressora» però 2 reptes només es validen imprimint → validació digital o batch de sobrants.
- **[B]** `Primers_auxilis:6` — «company en verd» ambigu amb 2 semàfors → aclarir.
- **[B]** `Passaport:32` — segells de trimestre sense criteri → «es posa el dia de la Fira si s'ha presentat».
- **[B]** `Capsules_inspirat:65` — cerques suggerides poc segures per projectar → concretar.

### 2.7 Progressió i càrrega cognitiva

- **[A]** SA0→SA1 — formació d'equips anunciada i sense sessió → 10' a la S1 de SA1.
- **[A]** SA1 S2 (setmana 4) — 5 novetats simultànies el primer dia de Chromebook → rutina de 15' «arrenco i trobo la meva carpeta».
- **[A]** SA3→SA9 — Inkscape 21 setmanes sense ús ni reactivació → repàs exprés de 15' a SA9 + xuletari enllaçat.
- **[A]** SA5→SA6 — encaixos 3D exigits com a criteri sense haver-se ensenyat com a base → mostra de tolerància obligatòria a SA5 o criteri de SA6 rebaixat.
- **[M]** `Fitxa SA8` — única fitxa sense «El repte» → afegir bloc.
- **[M]** `Fitxa SA5` — única fitxa sense «Reflexió» etiquetada → afegir.
- **[M]** Fitxes SA3/SA9 — el 🚦 semàfor desapareix justament on el cost d'error és màxim → afegir bloc.
- **[M]** `Diari_de_taller:91-92` — el 🎯 «el recuperaràs» no té moment a cap seqüència → 5' al punt 1 de la S1 de cada SA.
- **[M]** SA3 — «portafoli» avaluat des de la setmana 13 però definit al word wall de SA9 → moure a SA3 + definició d'una línia.
- **[M]** `Fitxa SA6:29` — «operador/a» mai definit en material d'alumne → llista breu de rols a la fitxa.
- **[M]** Fitxes SA4/SA5 — «batch de placa» no definit → word wall SA4 + frase.
- **[M]** SA5 S2 — Bambu Studio + 5 paràmetres + carnet + kanban + tolerància en 2h → kanban a la S3.
- **[M]** Fitxes SA1/SA4/SA5 — instrucció de lliurament de 35 paraules i 4 accions → mini-checklist de 3 caselles.
- **[M]** SA1→SA9 — convenció `Nom_SAx_vN` intermitent (desapareix a SA2-3 i SA6-9) → casella fixa a cada fitxa amb fabricació.
- **[M]** SA9 — límits <1h/<40g desapareixen → mantenir-los al checklist i al ⏸️ de S2.
- **[M]** SA8 — tota la creació CoSpaces en 1 sessió i la ⭐ és alhora vàlvula de retallada → demo al final de S1.
- **[M]** SA9 S3 — (→ crítica 12).
- **[M]** `Fitxa SA1:13-46` — ordre de la fitxa inverteix l'ordre de les sessions → reordenar (repte → esbós → seguretat → Inkscape).
- **[M]** `Fitxa SA1:25-26` — normes en negatiu sense conducta positiva → reformular en positiu.
- **[B]** `Fitxa SA5:62` — «tecla D» mai ensenyada → afegir al xuletari de SA4.
- **[B]** `SA0.md:63-70` — 6 sistemes administratius presentats en 25' el dia 1 → presentar-ne 3 i diferir la resta al primer ús.
- **[B]** Fitxes — caixa d'esbós canvia de lloc i desapareix a SA3/SA6 → posició fixa després d'«El repte».
- **[B]** SA2 — vectoritzar s'aprèn i mai més es demana → ⭐ a SA3 i opció de retolació a SA9.

---

## 3. Què NO s'ha auditat

- Enllaços externs per xarxa (només marcats els fràgils per patró).
- Renderitzat visual de la web (CSS, responsive, mode fosc) i interactius JS.
- Els fitxers SVG de `Recursos/Plantilles_disseny/` (existència sí, contingut no).
- El quadern digital `.xlsx` (només la seva documentació).
- Contingut factual dels enllaços/tutorials de tercers.

## 4. Pla d'implementació proposat

| Fase | Contingut | Troballes |
|---|---|---|
| **F1 — Errors tècnics i seguretat** | lletres/gravat, metacrilat, flama/aigua, tolerància SA6, exemple SA4 fora de límit | 5 · totes [A] |
| **F2 — Normativa i RGPD** | autorització (casella web + edat), carta famílies, exemple SA9, reglament (aforament+carnets), protocol VR per a alumnes | 6 |
| **F3 — Contractes d'avaluació** | passada criteri↔AN↔fitxa a les 9 SA, CA focals orfes, files sense codi, escala única d'emojis, autoavaluació única de tancament, descriptors d'observació | ~20 |
| **F4 — Coherència de planificació** | Gestio_temps a 20/10, temporització (SA5, contingències, trimestres), carnets 🔵/🟠, demos desfasades, formació d'equips | ~12 |
| **F5 — Bastides noves d'alumne** | eina del tour + demo 9/10, guió del portafoli, miniguió d'entrevista SA6, fitxa de ranures SA3, guió de presentació SA9, primer dia de Chromebook, reactivació Inkscape SA9 | ~10 |
| **F6 — ⏸️ mínims i fitxes** | mínims que falten (12 sessions), seccions absents (repte SA8, reflexió SA5, semàfor SA3/SA9), checklists de lliurament, vocabulari complet | ~20 |
| **F7 — Polits** | totes les [B] restants | ~25 |

> Generat per l'auditoria profunda del 13-07-2026 (7 revisions paral·leles + verificació per
> mostreig). Les troballes es tanquen marcant-les aquí o traslladant-les a commits.
