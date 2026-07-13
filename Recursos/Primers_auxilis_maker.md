# 🧯 Primers auxilis maker — quan alguna cosa no funciona

> Guia de l'alumnat per **desencallar-se sol/a** abans de cridar el/la docent. El 90 % dels
> problemes de l'Aula Maker són aquí dins, amb la solució al costat. Busca la frase que
> s'assembla al teu problema i prova la solució. **Ordre per demanar ajuda:** 1️⃣ aquesta
> guia → 2️⃣ un company/a en verd (el **semàfor de com va cadascú**, no el del fitxer) → 3️⃣ el/la docent.
>
> 🧭 *Gran idea del curs:* qui es desencalla sol/a ha après **dues** coses: la solució i com
> trobar-la. Això també s'avalua (autonomia — nivell 💪 de la rúbrica amigable).

## On és el meu problema?

- Estic amb **Inkscape o la làser** → Bloc A
- Estic amb **Tinkercad o la impressora 3D** → Bloc B
- Es tracta de **fitxers, noms o el Drive** → Bloc C
- Tot em falla i no sé per què → final de la pàgina 🆘

---

## Bloc A — Inkscape i talladora làser (2D)

| 😖 Què em passa | 🔍 Per què passa | ✅ Solució |
|---|---|---|
| «He escrit un text però la làser **no el talla ni el grava**» | El text encara és una font tipogràfica, no un dibuix vectorial | Selecciona el text → menú **Camí → Objecte a camí** |
| «La peça surt **gegant** (o diminuta)» | El document està en píxels, no en mil·límetres | **Fitxer → Propietats del document** → unitats en **mm**. Després comprova la mida real de la peça amb la barra superior |
| «La línia que havia de ser de **tall** només s'ha **gravat**» | El color del traç no és el vermell pur del nostre codi | Traç **vermell pur (RGB 255, 0, 0)** i gruix fi (≈0,1 mm). Recorda el codi: **vermell = tall, negre = gravat** |
| «En moure una forma, **se m'enganxa on no vull**» | L'ajust automàtic (*snapping*, l'imant) està massa actiu | Prem **%** per desactivar l'imant (o desactiva'l a la barra), mou la peça, i torna'l a activar |
| «He esborrat una cosa **sense voler**» | Passa a tothom | **Ctrl+Z** desfà (i Ctrl+Y refà). Pots prémer-lo més d'un cop |
| «El meu dibuix té **línies dobles** i la làser passa dues vegades» | Formes duplicades una sobre l'altra (còpia accidental) | Selecciona-ho tot → mou-ho: veuràs les còpies. Esborra les que sobren |

## Bloc B — Tinkercad i impressora 3D

| 😖 Què em passa | 🔍 Per què passa | ✅ Solució |
|---|---|---|
| «La meva peça **flota** sobre el pla de treball» | La peça té alçada Z > 0: la impressora faria «espagueti» a l'aire | Selecciona la peça i prem la tecla **D** (*drop*: cau al pla de treball) |
| «He posat un **forat** (cos transparent) però **no forada**» | Falta agrupar: el forat només actua en unir-se amb la peça | Selecciona **peça + forat** (majúscula i clic) → **Agrupa (Ctrl+G)** |
| «He agrupat i ara **no puc editar** una part» | L'agrupació ho converteix en un sol cos | **Desagrupa (Ctrl+Maj+G)**, edita, i torna a agrupar |
| «M'han dit que la meva **paret és massa prima** per imprimir» | Per sota de ~1,2 mm les parets surten fràgils o no surten | Fes les parets d'un mínim de **2 mm** (comprova-ho amb el regle de Tinkercad) |
| «La peça impresa té les **vores aixecades** (warping)» | La primera capa s'ha refredat massa de pressa | No és culpa teva: mira la peça del **Museu dels Errors** i comenta-ho al torn de màquina (adhesió, base neta) |
| «La meva peça surt amb **fils** entre les parts» | *Stringing*: el filament degota en els desplaçaments | Es treu en el postprocés (amb compte!); si n'hi ha molt, apunta-ho al diari perquè es revisi la retracció |

## Bloc C — Fitxers, noms i Drive

| 😖 Què em passa | 🔍 Per què passa | ✅ Solució |
|---|---|---|
| «La màquina **no accepta** el meu fitxer» | Has desat el projecte, però no l'has **exportat** al format de màquina | Inkscape: desa'l **pla** (`.svg`); Tinkercad: **Exporta → .STL**. El fitxer de màquina és sempre l'exportat |
| «**No trobo** el meu fitxer al Drive de l'equip» | Desat a un altre lloc (Baixades, escriptori…) o amb un altre nom | Cerca el nom al Drive (🔍). Si no hi és, torna a l'aplicació i **exporta de nou a la carpeta de la SA** |
| «Tinc **cinc versions** i no sé quina és la bona» | Falta la numeració de versions | Reanomena seguint la convenció del curs: **`ElMeuNom_SAx_vN`** (ex.: `Marc_SA3_v2.svg`). La bona és la `vN` més alta |
| «He sobreescrit el fitxer d'un **company/a**» | Dos fitxers amb el mateix nom a la carpeta d'equip | Per això el nom porta **el teu nom** davant. Aviseu el/la docent: el Drive guarda l'historial de versions i es pot recuperar |

---

## 🆘 Si res d'això no ho arregla

1. **Atura't** (no cliquis més coses «a veure si sona la flauta»).
2. Mira el **semàfor** de l'aula: hi ha algú en 🟢? Demana-li **2 minuts** d'ajuda.
3. Si tampoc, aixeca la mà i, mentre esperes el/la docent, **escriu al diari** què passa i
   què has provat — així la consulta serà el doble de ràpida i tindràs mitja entrada feta. ♻️

> Connecta amb: `Recursos/Semafor_maker.md` (les 3 comprovacions **abans** de fabricar),
> `Programació didàctica/Museu_dels_errors.md` (els errors són material de museu, no vergonyes)
> i `Recursos/Enllacos_i_tutorials.md` (tutorials per anar més enllà).
