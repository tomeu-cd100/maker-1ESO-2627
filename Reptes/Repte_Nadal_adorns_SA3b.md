# 🎄 SA3b — Mini-repte de Nadal: el meu adorn per a l'arbre

> Mini-repte de **2 setmanes** (setmanes 11-12, ≈ 2-3 h per alumne) entre el rusc (SA3) i la
> 🎪 Fira del T1. **No és una SA amb rúbrica pròpia**: es valora amb els **criteris constants**
> (CA1.4 · CA5.1 · CA5.2 · CA6.1: autonomia a la màquina, treball, diari i seguretat), sense
> criteris nous. Per això no surt a la matriu `Avaluació/Criteris_i_qualificacio.md` §4.
> El 3D (SA4) **no comença fins al T2** (8 de desembre).

## 🎯 El repte
> «Dissenya i talla **un adorn de Nadal** per penjar a l'arbre (el del centre o el de casa), amb
> el **teu nom o la teva inicial** i un **símbol teu**. Fes-lo prou bé perquè valgui per regalar.»

**Per què encaixa aquí:** fa servir **tot el que s'acaba d'aprendre** a la SA3 (plantilla amb
zona segura, capes tall/gravat/guia, símbol propi, semàfor de fabricació) en una peça petita i
ràpida, i **reaprofita el símbol de la rajola**: qui el té vectoritzat el pot posar a l'adorn en
dos minuts i dedicar el temps a fer-lo millor (no a començar de zero). L'⭐ ampliació (avet 3D
encaixat) torna a la **gran idea 1 — el material mana**: la ranura es calcula amb el **kerf**
de l'equip, com el connector del rusc.

## Criteris d'èxit (per a l'alumnat)
- [ ] He triat **una forma** (bola, estrella o avet) i **no he tocat** el forat ni la pestanya.
- [ ] Hi ha el meu **nom o inicial** (text convertit a camí) i un **símbol dins del cercle guia**.
- [ ] Ha passat el 🚦 **semàfor** i l'he **tallat jo** (amb el carnet 🔴).
- [ ] Hi he passat el **cordill** i **penja recte**.

## Seqüència (2 setmanes, amb el desdoblament de sempre)

| Setmana | 🔧 Estació Maker (amb el docent) | 💻 Aula ordinària (amb el co-docent) |
|---|---|---|
| **11** (17 i 19 nov) | **Acabar el rusc**: tallar rajoles + connectors, muntar la bresca i fer la prova | **SA3b · disseny**: obrir `adorns_nadal_SA3b.svg`, esborrar les 2 formes que no vull, nom + símbol dins del cercle, text a camí, GUIA amagada, desar `ElMeuNom_SA3b_v1.svg` |
| **12** (24 i 26 nov) | **SA3b · tall**: semàfor + batch de 8-10 adorns per tanda (≈ 6-8 min de làser) · iteració de la bresca si cal | Cordill i acabat · ⭐ avet 3D encaixat · targeta del rusc i **assaig de la frase de la Fira** · unir les bresques → el rusc sencer |

> ⏸️ **Mínim**: un adorn tallat amb nom + símbol, penjat amb cordill. Qui no hagi acabat la
> rajola del rusc té **prioritat de làser** a la setmana 12 (el rusc és el producte del T1).

## ⭐ Ampliacions (per a qui acaba abans)
- **Calat**: el símbol tallat (forat amb la seva forma) en lloc de gravat. Serveixen els motius
  d'una sola peça sense illes (`cor`, `estrella`, `llamp`, `lluna`, `pota`).
- **Avet 3D encaixat** (`avet_3d_SA3b.svg`): dues peces que s'encaixen en creu. La ranura fa
  **gruix − kerf** (3 − 0,15 = 2,85 mm). El docent regenera el fitxer amb el kerf de l'equip:
  `py -3.11 generador_adorns_nadal.py --tipus encaix --kerf 0.2`.
- **Un segon adorn per regalar** (a la família, a un altre professor…), amb un altre símbol.

## Material
- Plantilles (a `Recursos/Plantilles_disseny/`, generades amb `generador_adorns_nadal.py`):
  - `adorns_nadal_SA3b.svg`: bola (Ø70), estrella (Ø80) i avet (80 mm), amb pestanya i forat de
    Ø4 mm per al cordill, capa GUIA i `NOM`.
  - `avet_3d_SA3b.svg`: ⭐ les 2 peces de l'avet 3D (ranura amb kerf 0,15 mm per defecte).
- DM/contraxapat de 3 mm (retalls de la SA3: 4 adorns ≈ 1 rajola), cordill o cinta fina.
- 🖨️ Full de l'alumnat (1 pàgina): web → «Per imprimir» de la SA3, o en PDF amb
  `genera_pdf_impressos.py SA3`.
- Motius: el **banc de motius del rusc** (`Recursos/Banc_motius_SA3.md`); per a Nadal funcionen
  bé `estrella`, `pi`, `cor`, `lluna` i `somriure`, o un dibuix propi (floc de neu amb 3 línies
  creuades, campana, regal: un quadrat + un llaç).

## Per al docent
- **Abans de la setmana 11**: puja `adorns_nadal_SA3b.svg` a la carpeta de Drive de la SA3 i
  talla **un adorn de mostra** de cada forma (es passa de mà en mà, com la rajola).
- **Batch**: els adorns són petits i caben molts per planxa; aprofita els **retalls** de les
  planxes del rusc (CA6.2 — sostenibilitat, a la vista).
- ⚠️ **Vigila**: l'alumne que **escala** l'adorn sencer per fer-hi cabre el símbol: el forat
  també creix o s'encongeix i la pestanya es pot trencar. Es fa petit el símbol, no l'adorn.
- **On es pengen**: a l'arbre del centre (es pot fer una foto per al portafoli i per al web del
  centre, **sense cares d'alumnes**) o a casa. A la 🎪 Fira del T1 es poden ensenyar al costat
  del rusc.
