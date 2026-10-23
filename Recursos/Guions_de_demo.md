# Guions de demo — les demostracions crítiques, pas a pas

> Una **demo curta abans de cada tècnica nova** és la rutina que més rendiment dona (guia
> docent §6) — i també el moment més fàcil d'espatllar: si s'allarga, es menja la sessió; si
> improvises, es perd el pas clau. Aquí tens **el guió de les 8 demos crítiques del curs**:
> què prepares, què fas i dius, l'error que veuràs segur i la frase que ha de quedar.
>
> Regles d'or de tota demo: **projectada i curta** (el temps indicat és un màxim), l'alumnat
> **mira sense teclat** (les mans venen després), i acabes sempre amb la frase clau escrita
> a la pissarra. Els tutorials per ampliar són a `Enllacos_i_tutorials.md`.
>
> Són **10 demos**: les 8 de tècnica de disseny/captura + la **9** (SVG→XCS→làser, el moment
> del carnet 🔴) i la **10** (muntar el tour), els dos passos amb màquina/publicació que abans
> quedaven sense guió.

---

## Demo 1 — Inkscape: el primer disseny (setmana 3 · SA1 · màx. 30')

**Prepara:** Inkscape obert i projectat; la plantilla `Plantilles_disseny/clauer_SA1.svg` a mà.
**El guió:**

1. Document nou → mides en **mm** (Propietats del document). Digues: «la làser no entén
   "més o menys": entén mil·límetres».

2. Dibuixa un rectangle arrodonit de **60×25 mm** amb la barra de mides (no a ull!).
3. Afegeix **text** (el teu nom) i col·loca'l dins. Canvia la tipografia una vegada, prou.
4. Dibuixa el **forat** de l'anella: cercle de 4-5 mm, a prop de la vora però no tocant-la.
5. **Anomena i desa**: `ElTeuNom_SA1_v1.svg` — «un fitxer sense nom no entra mai a la màquina».
**L'error que veuràs segur:** mides posades arrossegant el ratolí (surten 61,3×24,8) i el
forat massa a la vora (es trenca). Ensenya el camp de mides i la regla «forat a ≥3 mm de la vora».
**La frase que ha de quedar:** «El material mana: dissenyem amb les mides de veritat.»

## Demo 2 — Capes de tall i gravat + text a camí (setmanes 3 i 5 · SA1-SA2 · màx. 15')

**Prepara:** el clauer de la demo 1 acabat.
**El guió:**

1. Mostra les **dues capes**: TALL (traç **vermell**, línia fina, sense ompliment) i GRAVAT
   (**negre**, ompliment). «Vermell = la làser retalla; negre = la làser dibuixa.»

2. Mou el contorn a TALL i el nom a GRAVAT. Ensenya com es veu la capa activa.
3. Selecciona el text → **Camí → Objecte a camí**. Digues: «ara ja no és lletra: és dibuix.
   La làser no té les nostres tipografies — si no ho converteixes, et canviarà la lletra».

4. Comprova-ho: amb l'eina de nodes, el text mostra nodes (ja és camí).
**L'error que veuràs segur:** text sense convertir (a XCS surt amb una altra tipografia o no
surt) i línies de tall gruixudes «perquè es vegin» — el gruix no importa, el color sí.
**La frase que ha de quedar:** «Vermell talla, negre grava, i el text sempre a camí.»

## Demo 3 — Vectoritzar una imatge (setmana 6 · SA2 · màx. 15')

**Prepara:** dues imatges del banc: una **bona** (silueta simple, alt contrast) i una **dolenta**
(foto amb ombres).
**El guió:**

1. Importa la imatge bona → **Camí → Vectoritza el mapa de bits** → previsualització → D'acord.
2. Separa el vector de la foto original (mou-lo) i **esborra la foto**: «la làser no vol la
   foto, vol les línies».

3. Simplifica si cal (**Camí → Simplifica**): menys nodes = tall més net.
4. Ara la dolenta: vectoritza-la i deixa que vegin el monstre de taques. «Per això triem
   imatges simples.»
**L'error que veuràs segur:** vectoritzar fotos complexes i deixar la imatge original a sota
(la làser la grava com un borrissol gris).
**La frase que ha de quedar:** «Imatge simple i amb contrast, i la foto original s'esborra.»

## Demo 4 — La cua d'oronella, el connector i el kerf (setmana 10 · SA3 · màx. 25')

**Prepara:** dues rajoles hexagonals tallades, connectors de kerf 0,0 i 0,2, la
`mostra_connectors_SA3.svg` tallada i el peu de rei.
**El guió:**

1. Uneix dues rajoles amb un connector i aixeca-les per una: «cap cola. El truc: l'osca és
   **més ampla per dins** que a la vora, i el connector no pot sortir estirant».

2. Prova el connector 0,0: entra sol i cau. «Per què, si l'hem dibuixat exacte?» Mesura'n la
   cintura amb el peu de rei davant de tothom (10,0 dibuixat → 9,8 tallat?).

3. «El làser es menja material a cada tall: és el **kerf**. El connector s'aprima i l'osca
   s'eixampla.» Prova el 0,2: entra amb el polze i aguanta.

4. Presenta la **mostra de connectors**: «abans de tallar 24 connectors, tallem això de 2
   minuts. El número del que aguanta és el vostre kerf».
**L'error que veuràs segur:** alumnes que escalen la rajola (les osques canvien i el connector
no hi entra), i equips que volen saltar-se la mostra per anar de pressa.
**La frase que ha de quedar:** «L'error barat de 2 minuts evita l'error car de 20.»

## Demo 5 — Tinkercad: cossos, forats i agrupar (setmanes 14-15 · SA4 · màx. 20')

**Prepara:** compte de classe obert; un objecte simple pensat (un got: cilindre + cilindre forat).
**El guió:**

1. Navegació 3D primer: orbita, zoom, el **cub de vistes**. «En 3D, mirar és una habilitat.»
2. Arrossega un **cilindre**; mides amb els quadradets (números, no a ull).
3. Arrossega un segon cilindre més petit → marca'l com a **forat** → col·loca'l dins.
4. **Alinear** (eina d'alineació, mai a ull!) → selecciona-ho tot → **Agrupa**: el got apareix.
5. Desagrupa i torna a agrupar: «el forat no esborra res fins que agrupes — i sempre pots
   tornar enrere».
**L'error que veuràs segur:** peces «alineades» a ull que queden tortes, i forats que no
traspassen del tot (fes el forat sempre més llarg que el cos).
**La frase que ha de quedar:** «Cos + forat + agrupar: amb això es construeix quasi tot.»

## Demo 6 — Laminar amb Bambu Studio (setmana 18 · SA5 · màx. 20')

**Prepara:** un STL d'exemple ja pujat; la impressora visible des d'on projectes.
**El guió:**

1. Importa l'STL → gira'l perquè la **cara més plana toqui la placa**. «La impressora
   construeix de baix a dalt: cada capa necessita una de sota.»

2. Paràmetres que toquem nosaltres (i prou): alçada de capa, **farciment 15-20 %**, *brim* si
   la base és petita, suports només si hi ha parts a l'aire.

3. **Lamina** → ensenya la previsualització capa a capa (és el moment màgic: deixa'ls-la veure).
4. Assenyala **temps i grams**: «aquí es decideix si entres a la cua: **menys d'1 h i menys
   de 40 g**. Si et passes, no demanes permís: redissenyes» (més petit, menys farciment, sense
   suports).
**L'error que veuràs segur:** la peça orientada amb la cara bona a la placa (queda marcada) i
el «només són 65 minuts, va…» — el límit és el límit.
**La frase que ha de quedar:** «Els límits no són un càstig: són el que fa que tothom imprimeixi.»

## Demo 7 — Càmera 360: la captura estable (setmana 26 · SA7 · màx. 15')

**Prepara:** la càmera carregada + trípode/perxa; una captura d'exemple bona i una de moguda.
**El guió:**

1. Ensenya la càmera: **dos objectius, ho veu TOT** — «no hi ha "fora de pla": si hi ets, surts».
2. On s'amaga el fotògraf: sota la càmera no serveix; **darrere un obstacle o lluny** després
   de prémer (temporitzador).

3. Trípode, altura d'ulls, llum de cara als espais, i **3 segons quiet** abans i després.
4. Mostra la captura bona i la moguda costat a costat: «quina posaríeu al tour del centre?»
5. Recorda els **drets d'imatge**: ningú sense permís al pla — és criteri d'avaluació (CA6.3).
**L'error que veuràs segur:** el fotògraf sortint a la foto (tothom hi cau el primer dia) i
captures caminant.
**La frase que ha de quedar:** «La càmera ho veu tot — planifica on ets tu i qui surt.»

## Demo 8 — CoSpaces: l'escena mínima explorable (setmana 30 · SA8 · màx. 20')

**Prepara:** compte de classe; una escena d'exemple mig feta (3 objectes + un text).
**El guió:**

1. Escena nova → arrossega **3-4 objectes** de la biblioteca → col·loca'ls amb sentit (no
   flotant!).

2. Un **text** que orienti el visitant («Benvinguts al museu de…»).
3. La **càmera**: on comença el visitant i què veu primer. «La càmera és els ulls del visitant:
   posa-la a alçada de persona.»

4. **Play** → explora en pantalla → ensenya com es veu en mode VR.
5. Digues: «això ja és una escena explorable — tot el que afegiu a partir d'aquí és ampliació
   (⭐ interaccions amb blocs de codi per a qui vagi ràpid)».
**L'error que veuràs segur:** equips que passen 40 minuts triant objectes sense col·locar la
càmera — l'escena «gran» que no s'acaba.
**La frase que ha de quedar:** «Petit i acabat guanya gran i a mitges.»

## Demo 9 — De l'SVG a la làser amb XCS (setmana 5 · SA1 · màx. 15')

**Prepara:** el fitxer `ElTeuNom_SA1_v1.svg` d'un alumne; la xTool S1 i XCS oberts i projectats.
**El guió:**

1. **Importa l'SVG** a XCS. Comprova que la **mida** és la de veritat (mm), no s'ha escalat.
2. Assigna els **modes** per color: el **vermell** = *Tallar*; el **negre** = *Gravar*. «El
   color que vam triar a Inkscape aquí es converteix en l'ordre a la màquina.»

3. **Enquadra** sobre el material (marc de posició/*framing*): la peça ha de caure damunt la
   planxa, no fora. Comprova la posició amb la llum de referència.

4. Materials i seguretat: material de la llista verda, tapa tancada, ventilació. **Botó
   d'aturada localitzat.** (És el contingut del carnet 🔴.)

5. **Enviar**: primer una peça de prova o el batch del torn. Ningú es queda sol amb la màquina.
**L'error que veuràs segur:** l'SVG importat a una mida diferent (s'ha escalat) i colors mal
assignats (tot a gravar, o el gravat a tallar). Ensenya a comprovar mida i modes **abans** d'enviar.
**La frase que ha de quedar:** «El vermell talla i el negre grava — també dins la màquina.»

## Demo 10 — Muntar i publicar el tour (setmana 28 · SA7 · màx. 15')

**Prepara:** CoSpaces obert amb **2 fotos 360** ja transferides; una escena d'exemple mig feta.
**El guió (els 5 passos del tour):**

1. **Escena nova** → posa la **foto 360 com a fons** (entorn 360 / *360 image*). «Ara ets dins
   la foto: gira i mira al voltant.»

2. Crea una **segona escena** amb l'altra foto.
3. Afegeix un **punt de navegació** (un objecte/fletxa) que porti de l'escena 1 a la 2. «Això
   és el que fa que el visitant pugui passejar.»

4. Posa un **títol/etiqueta** a cada escena (on som).
5. **Prova-ho** en pantalla i digues on es revisen els **drets d'imatge** abans de publicar, i
   com es genera el **QR** (coordinació TIC).
**L'error que veuràs segur:** equips que fan una escena preciosa però **sense punt de
navegació** (no es pot passejar) i títols oblidats.
**La frase que ha de quedar:** «Un tour és escenes connectades: la fletxa és el que el fa tour.»

---

> **Després de cada demo:** els criteris d'èxit del dia a la vista i les mans al teclat.
> Recorda l'exemple resolt de cada SA: es mostra **després** del primer intent, no abans.
