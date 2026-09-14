# Instal·lació d'Inkscape als Chromebooks (Linux/Crostini) — pas a pas

> **Per a qui és:** el coordinador TIC (tu mateix). És la tasca pendent marcada a
> `Memòria de treball/Feines_pendents_docent.md` («Activar Linux + Inkscape als Chromebooks»)
> i la peça que fa possible l'escenari de disseny 2D descrit a
> `Codocencia_desdoblament.md` §3 (tot el disseny 2D es fa a l'estació ordinària amb
> Inkscape, i el torn de l'aula Maker queda net per a fabricació).

Hi ha dues fases: **(A)** una única vegada, des de la consola d'administració del centre, i
**(B)** a cada Chromebook del grup (es pot fer en bloc si el centre distribueix una política
d'inici de sessió, o manualment el primer dia que hi ha Chromebooks a l'aula — setmana 4).

---

## A. Habilitar Linux als dispositius gestionats (consola d'administració de Google)

Als Chromebooks d'un centre educatiu, l'entorn Linux (Crostini) està **desactivat per
defecte** i només un administrador de l'organització el pot activar — no apareix l'opció a
l'alumnat fins que no ho fas des d'aquí.

1. Entra a **admin.google.com** amb el teu compte d'administrador (o demana-ho a qui tingui
   aquest rol al centre, si no ets tu qui hi té accés).
2. Ves a **Dispositius → Chrome → Configuració → Configuració del dispositiu**.
3. Selecciona la **unitat organitzativa (OU)** que correspon als Chromebooks del grup (per
   exemple, «1r ESO» o l'OU específica del vostre grup-classe). Si tot el centre comparteix
   una sola OU, valora crear-ne una de pròpia per no activar Linux a tots els cursos.
4. Al cercador intern de la pàgina de configuració (la lupa o `Ctrl+F` del navegador), escriu
   **«Linux»**: et portarà directament a la secció de màquines virtuals.
5. Activa l'opció **«Linux (Beta)»** / **«Permet que els usuaris facin servir Linux»** per a
   aquesta OU.
6. Desa. El canvi es propaga als Chromebooks la propera vegada que sincronitzin política
   (normalment en minuts si estan engegats i connectats).

> 📌 Si el centre ja gestiona els Chromebooks amb un altre perfil TIC, aquest pas és l'únic
> que necessites demanar-los explícitament: la resta (B) el pot fer cada docent o el mateix
> alumnat la primera vegada.

---

## B. Activar Linux i instal·lar Inkscape a cada Chromebook

### 1. Activar l'entorn Linux
1. **Configuració** (icona d'engranatge) → **Avançada** → **Desenvolupadors**.
2. A l'apartat **«Entorn de desenvolupament Linux»**, prem **Activa**.
3. Accepta l'assignació d'espai (per defecte reserva uns 10 GB; és suficient per a Inkscape i
   uns quants projectes SVG). Prem **Instal·la** i espera — pot trigar uns minuts la primera
   vegada.
4. Quan acabi, s'obre una finestra de **Terminal**: és des d'aquí que instal·larem Inkscape.

### 2. Instal·lar Inkscape (via APT — opció recomanada per a l'aula)
A la finestra de Terminal, escriu (una línia i Enter, després l'altra):

```bash
sudo apt update
sudo apt install inkscape
```

Baixa uns 150 MB i triga entre 3 i 8 minuts segons la xarxa del centre. En acabar, Inkscape
apareix a l'app drawer (calaix d'aplicacions) dins la carpeta **Linux**; pots arrossegar-lo a
l'estant (shelf) perquè quedi fix.

> ⚠️ **Versió:** `apt install inkscape` instal·la la versió empaquetada a Debian (la base de
> Crostini), que sol anar 1-2 versions per darrere de l'última d'Inkscape. Per a les
> operacions que fem servir a les SA (nodes, unir/restar camins, text→camí, capes de
> tall/gravat) és de sobres. Si algun dia calgués la versió més recent, hi ha l'alternativa
> Flatpak de sota.

### 3. (Opcional) Versió més recent via Flatpak
Només si es necessita una funció que la versió d'APT no té:

```bash
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.inkscape.Inkscape
```

Per obrir-lo després: `flatpak run org.inkscape.Inkscape` (o cercar-lo a l'app drawer un cop
instal·lat).

---

## C. Comprovació ràpida (fes-ho abans de la setmana 4)

- [ ] Linux activat a la OU correcta (consola d'administració).
- [ ] En un Chromebook de prova: `sudo apt update && sudo apt install inkscape` s'executa
  sense error.
- [ ] Inkscape obre, es pot crear un document nou i desar un `.svg` a l'espai de Linux.
- [ ] El fitxer `.svg` desat des de Linux és accessible/exportable cap al Drive del grup
  (comprova que la carpeta de Linux Files es pot veure des de l'app Fitxers de ChromeOS).
- [ ] Fitxa provada amb la plantilla `Recursos/plantilles_disseny/clauer_sa1.svg` (obre-la des
  d'Inkscape sense errors de capes).

Si algun Chromebook falla o Linux dona problemes el dia de la sessió, recorda el **Pla B**
que ja recull `Codocencia_desdoblament.md` §3: els ordinadors de la zona de disseny de l'aula
Maker tenen Inkscape instal·lat de reserva.

---

## Vídeos de suport (material de tercers — no es copia, només s'enllaça)

- [How to Use Inkscape on Chromebook — Beginners Guide 2026 (YouTube)](https://www.youtube.com/watch?v=iFV5zny_r1E)
- [How to install Inkscape and Ink Stitch on a Chromebook (YouTube)](https://www.youtube.com/watch?v=h4QcgKJtAug)
- [How to Install Inkscape on a Chromebook — ChromeReady (guia escrita, pas a pas amb captures)](https://chromeready.com/13115/install-inkscape-chromebook/)

> ⚠️ Vídeos de tercers: mira'ls sencers abans de posar-los a l'alumnat o d'enllaçar-los a la
> web pública del curs — poden incloure anuncis o contingut no rellevant a l'inici/final.

---

Relacionat amb: `Codocencia_desdoblament.md` §3, `00_Guia_inici_docent.md` (checklist de
comptes i programari), `Memòria de treball/Feines_pendents_docent.md`.
