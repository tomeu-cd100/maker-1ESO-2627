# Vocabulari bàsic de l'Aula Maker — glossari del curs

> **Per a l'alumnat:** totes les paraules del curs en un sol lloc, explicades curt i clar.
> No cal memoritzar-les: les aprendràs **fent** — la columna «Quan» et diu a quina SA apareix
> cada una. **Per al docent:** és el word wall mestre; els word walls de cada SA en són
> subconjunts. A l'avaluació 0 (i al juny) l'alumnat marca quines coneix.

## 🛠️ Cultura maker (des del primer dia)

| Paraula | Què vol dir | Quan |
|---------|-------------|:----:|
| **maker** | Qui aprèn **fent**: dissenya, fabrica, s'equivoca i millora | SA0 |
| **fabricació digital** | Fabricar objectes reals a partir de dissenys fets a l'ordinador | SA0 |
| **fab lab / taller maker** | Espai amb màquines de fabricació digital compartides | SA0 |
| **prototip** | La primera versió d'una cosa, feta per **provar-la** (no per ser perfecta) | SA0 |
| **iteració** | Tornar-hi: provar → veure què falla → millorar → tornar a provar | SA3 |
| **criteris d'èxit** | La llista de què es mirarà en un repte — la tens des del primer dia | SA0 |
| **diari de taller** | La teva llibreta maker: què has fet, què has après, què has resolt | SA0 |
| **portafoli** | El recull de les teves evidències de tot el curs (diari + fotos + fitxes) | SA3 |
| **carnet de màquina** | La llicència que et guanyes per poder operar cada màquina | SA1 |
| **procés tecnològic** | El camí complet: necessitat → idea → disseny → fabricar → provar → millorar | SA3 |
| **requisit** | Una condició que la solució ha de complir **sí o sí** | SA3 |
| **rol d'equip** | La responsabilitat concreta que et toca dins l'equip (rota cada SA) | SA3 |

## 📐 Disseny 2D i làser (1r trimestre)

| Paraula | Què vol dir | Quan |
|---------|-------------|:----:|
| **disseny vectorial** | Dibuix fet de línies i corbes matemàtiques (es pot escalar sense perdre qualitat) | SA1 |
| **làser** | La màquina que talla i grava amb un feix de llum concentrada | SA1 |
| **seguretat** | Les normes que fan que treballar amb màquines no sigui perillós | SA1 |
| **node** | Cada punt que defineix una línia o corba d'un dibuix vectorial | SA2 |
| **camí** | La línia (recta o corba) que uneix nodes; el que la làser segueix | SA2 |
| **operació booleana** | Combinar formes: **unió** (sumar), **diferència** (restar), **intersecció** | SA2 |
| **vectoritzar** | Convertir una imatge normal (píxels) en camins que la làser entén | SA2 |
| **ompliment** | El "farcit" de color d'una forma (al nostre codi, negre = gravat) | SA2 |
| **capa** | "Pis" del dibuix: aquí separem què és **tall** i què és **gravat** | SA1 |
| **tall** | La làser **travessa** el material (línia fina, vermella al nostre codi) | SA1 |
| **gravat** | La làser **marca** la superfície sense travessar (negre) | SA1 |
| **kerf** | El material que la làser **"es menja"** en tallar (~0,1-0,2 mm) — compte amb els encaixos! | SA3 |
| **unió per encaix** | Peces que s'aguanten soles amb ranures a mida del gruix del material | SA3 |
| **nesting** | Col·locar molts dissenys junts en una planxa per aprofitar material i temps | SA2 |
| **batch** | Fabricar molts treballs d'una sola passada (tots els clauers junts!) | SA1 |

## 🧊 Disseny 3D i impressió (2n trimestre)

| Paraula | Què vol dir | Quan |
|---------|-------------|:----:|
| **volum** | Que una cosa ocupa espai en 3 dimensions (té amplada, fondària i alçada) | SA4 |
| **eixos X/Y/Z** | Les tres direccions de l'espai: amplada, fondària i **alçada** | SA4 |
| **cos** | Cada peça bàsica amb volum (cub, cilindre…) que combines a Tinkercad | SA4 |
| **buit (forat)** | Un cos que en comptes d'afegir material, en **treu** | SA4 |
| **agrupar** | Fusionar cossos i forats en un sol objecte | SA4 |
| **escala** | Fer una cosa més gran o més petita mantenint-ne les proporcions | SA4 |
| **STL** | El format de fitxer del teu model 3D, a punt per laminar | SA4 |
| **batch de placa** | Imprimir moltes peces petites de diferents alumnes en una sola impressió | SA4 |
| **mida real** | La mida que fa una cosa de veritat (mesurada amb regle o peu de rei) | SA5 |
| **laminat** | Tallar el model en capes fines i convertir-lo en instruccions per a la impressora | SA5 |
| **alçada de capa** | El gruix de cada capa d'impressió (més fina = més detall, més temps) | SA5 |
| **farciment** | Quant de ple és l'interior de la peça (15-20 % sol ser prou) | SA5 |
| **suports** | Material extra que aguanta les parts "a l'aire" mentre s'imprimeixen (evita'ls!) | SA5 |
| **brim** | Vora extra a la primera capa perquè la peça s'enganxi bé a la placa | SA5 |
| **warping** | Quan una peça es **deforma** i s'aixeca de la placa (l'error més famós) | SA5 |
| **tolerància** | El marge extra que deixes perquè dues peces encaixin (res no és exacte!) | SA5 |
| **gruix de paret** | Com de gruixudes són les parets de la peça (mínim 3 mm o es trenca) | SA5 |
| **PLA** | El plàstic (d'origen vegetal) amb què imprimim | SA5 |
| **kanban** | El tauler de la cua d'impressió: *Per imprimir · Imprimint · Fet* | SA5 |

## 🤝 Disseny per a persones (2n trimestre)

| Paraula | Què vol dir | Quan |
|---------|-------------|:----:|
| **empatia** | Posar-te al lloc de qui farà servir el que dissenyes, per entendre què necessita | SA6 |
| **disseny centrat en l'usuari** | Dissenyar a partir del que necessita una persona real, no del que t'agrada a tu | SA6 |
| **assemblatge** | Un conjunt de peces que encaixen entre elles per formar una cosa | SA6 |
| **impacte** | La diferència real que la teva solució fa en la vida de qui la fa servir | SA6 |

## 🥽 Realitat immersiva (3r trimestre)

| Paraula | Què vol dir | Quan |
|---------|-------------|:----:|
| **360°** | Foto/vídeo que captura **tot** l'entorn alhora (no hi ha "fora de pla"!) | SA7 |
| **equirectangular** | La manera "desplegada" com es guarda una imatge 360 (com un mapamundi) | SA7 |
| **punt de captura** | On col·loques la càmera: des d'allà "estarà" qui miri la imatge | SA7 |
| **tour virtual** | Escenes 360 enllaçades que pots recórrer com si hi fossis | SA7 |
| **navegació** | Els punts que et deixen saltar d'una escena 360 a una altra dins el tour | SA7 |
| **realitat virtual (VR)** | Entorn digital que t'envolta del tot amb les ulleres | SA8 |
| **immersió** | La sensació de **ser dins** de l'experiència | SA8 |
| **escena** | L'espai 3D que construeixes (a CoSpaces) amb objectes i càmera | SA8 |
| **interacció** | Que l'escena **respongui**: cliques i passa alguna cosa | SA8 |
| **drets d'imatge** | Ningú pot sortir en una foto/vídeo publicat sense el seu permís | SA7 |
| **salut visual** | Tenir cura dels ulls amb la VR: sessions curtes i descansos | SA8 |
| **ètica digital** | Fer un ús responsable i respectuós de la tecnologia (privadesa, temps de pantalla) | SA8 |

## 📊 Avaluació i rutines (tot el curs)

| Paraula | Què vol dir | Quan |
|---------|-------------|:----:|
| **SA (situació d'aprenentatge)** | Cada "repte gran" del curs (SA0…SA9) | SA0 |
| **NA · AS · AN · AE** | Els 4 nivells: *encara no* 🌱 · *ho faig* 🙂 · *ho faig bé* 💪 · *ho domino* 🌟 | SA0 |
| **rúbrica** | La taula que descriu com és cada nivell — la veus des del primer dia | SA1 |
| **autoavaluació / coavaluació** | Valorar la teva feina / valorar la de l'equip (amb evidències, no simpaties!) | SA1 |
| **🎯 objectiu personal** | El que decideixes millorar a la propera SA (t'ho tornarem a preguntar!) | SA1 |
| **full de progrés** | La graella on el docent apunta la teva **trajectòria** — pots demanar veure'l | SA0 |
| **insígnia / passaport** | Els reconeixements del curs, tots al teu passaport maker | SA0 |
| **Gran Idea 🧭** | Els 5 principis que valen per a totes les màquines (són al pòster) | SA0 |
| **Museu dels Errors** | On les peces fallides ensenyen: aquí l'error val punts si n'aprenem | SA0 |
| **projecte integrador** | Un projecte que combina tot el que has après (làser + 3D + immersiu) | SA9 |
| **planificació** | Decidir abans qui fa què, quan i amb quin material | SA9 |
| **fita** | Un punt de control amb data: què ha d'estar acabat i quan | SA9 |
| **audiència** | Les persones per a qui fas una cosa i que la veuran (a la Fira!) | SA9 |
| **transferència** | Fer servir el que has après en situacions **noves** | SA9 |
