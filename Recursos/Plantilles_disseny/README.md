# Plantilles de disseny — Aula Maker

Fitxers llestos per usar a l'aula. **Convenció de capes** per a la làser xTool S1:
- **TALL** → traç **vermell** (`#FF0000`), gruix de línia mínim (0,1 mm), sense ompliment.
- **GRAVAT** → elements **negres** (`#000000`).

> En obrir-los a Inkscape o a xTool Creative Space, comprova sempre les **mides en mm** i
> assigna cada element a l'operació correcta (tall / gravat) segons el color.

## Fitxers
| Fitxer | SA | Què és |
|--------|----|----|
| `clauer_SA1.svg` | SA1 | Clauer 60×25 mm amb forat i text gravat (canvia "NOM") |
| `marcapagines_SA2.svg` | SA2 | Marcapàgines 50×150 mm amb marc, missatge i zona d'imatge |
| `mostra_encaix_kerf_SA3.svg` | SA3 | **Mostra d'encaix + regle de kerf** (90×35 mm): 5 ranures de 2,6–3,4 mm per trobar el gruix real i mesurar el kerf abans de fabricar |
| `generador_caixa_encaix.py` | SA3 | Generador de **caixes amb encaix** (finger joints) en SVG |
| `caixa_exemple_80x80x50_g3.svg` | SA3 | Exemple generat: caixa 80×80×50 mm per a fusta de 3 mm |

## Generar una caixa a mida (SA3)
Requereix Python 3. Des d'aquesta carpeta:
```bash
python generador_caixa_encaix.py --ancho 100 --largo 60 --alto 40 --grosor 3 --salida la_meva_caixa.svg
```
Paràmetres:
- `--ancho` / `--largo` / `--alto`: dimensions en mm.
- `--grosor`: **gruix real del material** (clau perquè l'encaix quadri!).
- `--salida`: nom del fitxer SVG de sortida.

⚠️ **Talla sempre primer una mostra d'encaix** per validar que el gruix del material
coincideix amb el paràmetre `--grosor` abans de tallar la caixa sencera: fes servir la
`mostra_encaix_kerf_SA3.svg` (2 minuts de làser). La ranura que agafa la fusta *just* és el
gruix real; l'amplada mesurada de la ranura de 3,0 menys 3,0 és el **kerf**. Recorda
convertir els textos a camí (o esborrar-los) abans d'enviar-la a tallar.

## Alternatives en línia (sense codi)
- **MakerCase** i **boxes.py**: generadors web de caixes amb encaix (vegeu
  `Simulacions/Simuladors_disseny_2D_3D.md`).
