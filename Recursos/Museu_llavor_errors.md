# Museu llavor — 5 errors canònics per obrir el Museu dels Errors

> El Museu dels Errors té una regla fundacional: **els adults l'obren**
> (`Programació didàctica/Museu_dels_errors.md`, regla 3). Aquest document explica com
> **fabricar expressament** les 5 peces fallides més instructives del curs abans de setembre,
> amb la **targeta de museu ja resolta** per a cadascuna. Així el dia 1 la lleixa no és buida:
> hi ha 5 peces per tocar, i el co-docent té material per presentar el museu encara que
> estigui aprenent les màquines.
>
> ⚠️ El museu és **tàctil per disseny**: aquest document no és un catàleg per mirar en
> pantalla, és la recepta per fabricar les peces físiques. Res no ensenya el *warping* com
> una peça amb *warping* a les mans.

**Temps total estimat:** una tarda (les dues impressions 3D poden anar en paral·lel als
talls de làser). Materials: retalls de DM/contraxapat 3 mm i ~30 g de PLA.

---

## Peça 1 — El *warping* (SA4-SA5, impressió 3D)

**Com fabricar-la expressament (~40'):** imprimiu una placa de 100×100×2 mm en PLA
**sense brim**, amb la base **freda** (anul·leu l'escalfament del llit al laminador) i, si
podeu, amb la base sense netejar. Les cantonades s'aixecaran soles. Atureu quan el warping
sigui ben visible: la peça a mig imprimir encara és més eloqüent.

```
PEÇA: placa de PLA amb les cantonades aixecades   SA: 4-5
QUÈ VA PASSAR: les cantonades s'han despegat de la base i s'han
corbat cap amunt; les capes de sobre han sortit tortes.
PER QUÈ: el plàstic es contreu en refredar-se; si la base no
l'aguanta (freda, bruta, sense brim), les vores estiren i guanyen.
COM S'EVITA: base neta i calenta, brim activat, i cantonades
arrodonides al disseny quan la peça és gran i plana.
Donada per: el/la docent (museu llavor)
```

## Peça 2 — L'encaix que balla (SA3, làser i *kerf*)

**Com fabricar-la expressament (~20'):** genereu una caixa petita amb
`Plantilles_disseny/generador_caixa_encaix.py` posant **kerf = 0** i talleu-la en DM 3 mm.
Les pestanyes ballaran. Guardeu al costat la mateixa cantonada tallada **amb el kerf
compensat** (la de `mostra_encaix_kerf_SA3.svg`): el contrast s'entén amb els dits.

```
PEÇA: cantonada de caixa amb les pestanyes que ballen   SA: 3
QUÈ VA PASSAR: les unions no aguanten; la caixa es desmunta sola.
PER QUÈ: el làser "es menja" ~0,15-0,2 mm a cada costat del tall
(kerf). Si dissenyes amb les mides exactes, cada encaix queda
0,3-0,4 mm massa fluix.
COM S'EVITA: mesura el kerf amb la mostra de prova i compensa'l al
disseny. Mesura dues vegades, fabrica una (Gran Idea 3).
Donada per: el/la docent (museu llavor)
```

## Peça 3 — El gravat cremat (SA1-SA2, làser)

**Com fabricar-la expressament (~15'):** graveu un text o logotip en cartró o DM amb la
**potència massa alta** (o la velocitat massa baixa): sortirà fosc, amb halos marrons i
vores menjades. Graveu al costat el mateix motiu amb els paràmetres correctes.

```
PEÇA: gravat cremat amb halos marrons   SA: 1-2
QUÈ VA PASSAR: el gravat ha quedat negre, borrós i amb la vora
socarrimada; el dibuix fi s'ha perdut.
PER QUÈ: massa potència (o massa lentitud) per a aquest material:
el làser crema en lloc de marcar.
COM S'EVITA: prova sempre els paràmetres en un racó del material
abans de la peça bona: la potència mínima que marca és la bona.
El material mana (Gran Idea 1).
Donada per: el/la docent (museu llavor)
```

## Peça 4 — El forat massa a prop de la vora (SA1, disseny)

**Com fabricar-la expressament (~10'):** talleu un clauer de la plantilla
`Plantilles_disseny/clauer_SA1.svg` movent el forat de l'anella a **menys d'1 mm** de la
vora. Poseu-hi una anella i forceu-la una mica: la paret es trenca. És l'error que més
apareixerà a la SA1 — tenir-lo al museu **abans** que passi el converteix en demo tàctil.

```
PEÇA: clauer amb la paret del forat trencada   SA: 1
QUÈ VA PASSAR: en posar l'anella, la paret entre el forat i la
vora s'ha trencat i el clauer ha quedat inservible.
PER QUÈ: quedava massa poc material: menys d'1 mm de paret no
aguanta l'esforç de l'anella.
COM S'EVITA: regla dels 3 mm: qualsevol forat, a 3 mm o més de
qualsevol vora. És a la fitxa de la SA1.
Donada per: el/la docent (museu llavor)
```

## Peça 5 — Els suports arrencats de cop (SA5, postprocés 3D)

**Com fabricar-la expressament (~45'):** imprimiu una peça petita amb un voladís que demani
suports (una L o una T invertida) i arrenqueu els suports **d'una estrebada, sense alicates**:
quedaran cicatrius, fils i probablement algun tros de la peça als dits.

```
PEÇA: peça 3D amb cicatrius de suports mal retirats   SA: 5
QUÈ VA PASSAR: en arrencar els suports de cop, la superfície ha
quedat rugosa i s'ha endut un tros de la peça.
PER QUÈ: els suports s'han de tallar a poc a poc amb alicates
(i ulleres!), no estirar: el PLA es trenca per on vol.
COM S'EVITA: postprocés amb calma i eines adequades — o millor:
redissenyar per evitar voladissos de més de 45° i no necessitar
suports. Petit i acabat guanya gran i a mitges (Gran Idea 2).
Donada per: el/la docent (museu llavor)
```

---

## Muntatge i ús

- Copieu cada targeta a mà (o imprimiu-la) en el format de targeta de museu de
  `Programació didàctica/Museu_dels_errors.md` i lligueu-la a la seva peça a la lleixa.
- El **co-docent** pot fabricar les peces 1 i 5 com a pràctica de màquina: són exactament
  el seu paper al museu («les del seu aprenentatge maker», regla 3).
- A la **SA0**, el recorregut pel taller passa per davant del museu: 5 peces que es poden
  tocar valen més que qualsevol discurs sobre «aquí equivocar-se és aprendre».
- Aquestes 5 peces són **llavor, no plantilla**: quan arribin les primeres donacions de
  l'alumnat, les llavors poden cedir el lloc (regla d'aforament d'una lleixa, §5 del museu).

> Relacionat amb: `Programació didàctica/Museu_dels_errors.md` (regles i usos),
> `Recursos/Guions_de_demo.md`, `Recursos/Plantilles_disseny/` i
> `Memòria de treball/Feines_pendents_docent.md` (tasca d'estiu).
