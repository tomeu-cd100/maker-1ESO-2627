# Quadern digital del docent — un sol full de càlcul per a tota la gestió

> **El problema que resol:** el sistema d'avaluació i seguiment genera cinc registres
> paral·lels (2 fulls de seguiment, 20 fulls de progrés, registre de carnets amb usos,
> recompte d'equitat, kanban) que en paper s'han de creuar a mà a cada coordinació. La
> solució: **un únic full de càlcul compartit** (Google Sheets, compte de centre) amb una
> pestanya per registre — les dades s'entren una sola vegada i els recomptes surten sols.
> El paper queda per a l'alumnat (diari, fitxes, passaport); la gestió docent, digital.

> 📥 **Plantilla llesta per usar:** [`Quadern_digital_docent_plantilla.xlsx`](Quadern_digital_docent_plantilla.xlsx)
> (generada amb `genera_quadern.py`; també descarregable des del portal docent de la web).
> Pugeu-la al Drive de centre, poseu-hi els noms **allà** i llestos.

## Estructura del full de càlcul (pestanyes)

### 1. `Alumnat` (la taula mestra)
| Columna | Contingut |
|---------|-----------|
| Nom | — |
| Grup | A / B |
| Equip T1 / T2 / T3 | nom d'equip de cada trimestre (es re-formen!) |
| Perfil | notes d'avaluació inicial, NESE, adaptacions |

Totes les altres pestanyes referencien aquesta columna de noms (rang amb nom `ALUMNES`).

### 2. `Seguiment` (substitueix els dos fulls de paper)
Una fila per observació: **Data · Alumne/a (desplegable) · Docent (Maker/Co) · Codi (+/-/!) ·
CA · Nota breu**. En codocència, els dos docents escriuen a la mateixa pestanya des del seu
dispositiu — la posada en comú setmanal ja està feta quan arribeu a la coordinació.

### 3. `Progrés` (el full de progrés competencial, digital)
Files = alumnes; columnes = CE1…CE6, TE, TA **per SA** (SA1-CE1, SA1-CE2… o una columna per
SA amb el detall en comentari). Valors: NA/AS/AN/AE amb **format condicional** (vermell →
verd): la trajectòria de cada alumne es veu d'un cop d'ull, i ensenyar-li «la seva fila» al
trimestre és girar la pantalla. La versió paper (`Full_progres_competencial.md`) queda com a
alternativa per a qui la prefereixi.

### 4. `Carnets` (registre + usos)
Files = alumnes; columnes: data de cada carnet (🔴🟠🟢🔵) + **una columna d'usos per màquina i
trimestre** (s'hi suma 1 cada vegada que l'alumne opera). D'aquí mengen dues coses:
- El **passaport maker** de l'alumne (`Reptes/Passaport_maker.md`) — el registre oficial és aquest.
- La **revisió trimestral d'equitat** ↓

### 5. `Equitat` (es calcula sola)
Taula dinàmica o fórmules sobre `Carnets`: usos per màquina desagregats per gènere/perfil i
trimestre. La revisió trimestral (`Programació didàctica/Equitat_genere_STEAM.md` §3·bis)
passa de «recompte a mà» a **llegir una taula que ja està feta** i decidir la correcció.

### 6. `Kanban` (opcional)
Columnes: Peça/Placa · Alumnes · Estat (Per imprimir/Imprimint/Fet) · Temps · Grams · Data.
El kanban físic a la paret continua manant a l'aula; aquesta pestanya és el registre
(i la font de la matemàtica del temps real per ajustar la temporització el curs vinent).

### 7. `Valoracions` (veu de l'alumnat)
Enllaç als resultats del **tiquet trimestral de valoració de l'assignatura**
(`Instruments_formatius.md` §9, per Google Forms) — al costat de les vostres dades, les seves.

## Regles d'ús

- ⚠️ **RGPD — regla d'or:** el quadern **emplenat conté dades personals d'alumnes** i aquest
  repositori és **públic**. El quadern viu **només al Drive de centre** (o a la carpeta local
  `dades/`, que git ignora): **mai es comiteja** cap fitxer amb noms. Al repositori només hi
  ha aquesta especificació i la plantilla buida.
- **Compartit entre els dos docents** amb edició; l'alumnat no hi té accés (RGPD: dades
  d'avaluació — compte de centre, no personal).
- **Menys és més:** si una pestanya no s'omple en dues setmanes, elimineu-la — el quadern ha
  de treure feina, no afegir-ne.
- Còpia de seguretat trimestral (Fitxer → Fes una còpia) abans de cada tancament.
- En el **traspàs de co-docent** (vegeu `Programació didàctica/Codocencia_desdoblament.md`
  §7), el quadern és l'única cosa que cal traspassar: tot el seguiment hi és.

> Relacionat amb: `Full_progres_competencial.md` (versió paper), `Full_seguiment_grup.md`
> (codis), `Normativa/Carnet_de_maquina.md`, `Equitat_genere_STEAM.md` §3·bis i
> `Reptes/Passaport_maker.md`.
