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
| `generador_rajola_hexagonal.py` | SA3 | Generador de la **rajola hexagonal**, dels **connectors**, de la **mostra de connectors** i de l'esquema del **rusc** |
| `rajola_hexagonal_SA3.svg` | SA3 | **Plantilla de la rajola** (100 mm entre costats): contorn i 6 osques en cua d'oronella (tall), `NOM` (gravat) i capa GUIA amb el cercle del símbol |
| `rajola_exemple_SA3.svg` | SA3 | Exemple resolt de rajola (nom + estrella) |
| `mostra_connectors_SA3.svg` | SA3 | **Mostra de connectors** (70×68 mm): 2 cupons amb osca + 4 connectors de kerf 0,0 / 0,1 / 0,2 / 0,3 mm |
| `connectors_SA3.svg` | SA3 | Full de 24 connectors en corbatí (kerf 0,15 mm) |
| `generador_motius_SA3.py` | SA3 | Generador del **banc de motius**: 26 siluetes de 56 mm (carpeta `motius_SA3/`) + `motius_SA3_galeria.svg`. Ús i idees: `Recursos/Banc_motius_SA3.md` |
| `rusc_esquema_SA3.svg` | SA3 | Esquema del rusc de 24 rajoles amb els connectors (per mirar, no per tallar) |
| `mostra_encaix_kerf_SA3.svg` | SA3 | **Mostra d'encaix + regle de kerf** (90×35 mm): 5 ranures de 2,6–3,4 mm per trobar el gruix real i mesurar el kerf abans de fabricar |
| `generador_caixa_encaix.py` | SA9 (opcional) | Generador de **caixes amb encaix** (finger joints) en SVG |
| `caixa_exemple_80x80x50_g3.svg` | SA9 (opcional) | Exemple generat: caixa 80×80×50 mm per a fusta de 3 mm |

## Rajoles i connectors del rusc (SA3)
Requereix Python 3. Des d'aquesta carpeta:
```bash
python generador_rajola_hexagonal.py --tipus connectors --kerf 0.2 --n 24 --salida connectors_equip1.svg
```
Paràmetres:

- `--tipus`: `rajola` (plantilla), `connectors` (full per tallar), `mostra` (mostra de
  connectors) o `rusc` (esquema per ensenyar).
- `--kerf`: el número del connector de la mostra que **entra amb el polze i no cau** (mm).
  Només afecta els connectors: la rajola no canvia mai.
- `--n`: nombre de connectors del full (o de rajoles de l'esquema del rusc).
- `--mida`: mida de la rajola entre costats (100 mm per defecte; si la canvies, canvia-la per a tothom).
- `--salida`: nom del fitxer SVG de sortida.

Comptar connectors: una bresca de 4 rajoles en fa servir **4 o 5** (segons la forma); el rusc sencer, unes
**2,2 per rajola** (24 rajoles → 53, vegeu `rusc_esquema_SA3.svg`). Talla'n un 10 % de més per a recanvis.

## Generar una caixa a mida
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
