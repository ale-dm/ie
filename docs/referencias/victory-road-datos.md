# Referencias: Base de Datos de Victory Road

Fuente: `Inazuma_Eleven_VR_Document_v3.06` (última actualización 3-2-2026), hoja de cálculo comunitaria aportada por el autor del proyecto. Créditos del documento: Draak38 (fórmulas), TheToyo (stats por rareza), TKG, Lock, Weiss, Endou, Kazukii y otros.

Solo se han revisado las hojas **Main, Characters, Characters ATDF, Hero, Hyper Moves e Hissatsu**. Se exportaron a CSV en `data/fuentes/victory-road/`, sin las columnas de imagen ni de nombres en kanji/hiragana. El Excel original (8,8 MB) no se ha subido al repo.

## 1. Personajes (Characters)

- **5132 fichas:** 4986 jugadores, 92 entrenadores, 45 coordinadores y 9 coaches.
- **Por juego de origen:** IE1 1033, GO 917, Victory Road 896, IE2 646, IE3 634, GO2 Chrono Stone 402, GO Galaxy 386, Ares 218.
- **Posición:** DF 1505, MF 1504, FW 1311, GK 812. Cada uno tiene además una posición alternativa.
- **Elemento:** Bosque 1312, Aire 1310, Fuego 1280, Tierra 1230.
- **7 stats base:** Kick, Control, Technique, Pressure, Physical, Agility, Intelligence.
- **Estilo de juego preferido:** Bond, Counter, Breach, Justice, Tension, Rough Play. Cada estilo tiene una pasiva de equipo (hoja Main).
- **Total de stats base casi igual para todos:** entre 656 y 693, media de 666. Victory Road no da una rareza fija a cada personaje: todos parten de la misma base y la rareza se sube con Espíritus (ver `inazuma-eleven.md`). **La hoja no tiene columna de rareza.**
- Incluye las 3 primeras técnicas que aprende cada jugador y sus caminos del tablero de habilidades.

## 2. Fórmulas (Main)

Las stats de duelo de Victory Road salen de combinar las 7 stats base:

| Stat de duelo | Fórmula |
|---|---|
| Shoot AT | Kick + Control |
| Focus AT | (Control + Technique) + Kick × 0,5 |
| Focus DF | (Intelligence + Technique) + Agility × 0,5 |
| Scramble AT | Physical + Intelligence |
| Scramble DF | Pressure + Intelligence |
| Castle Wall DF | Physical + Pressure |
| KP (portero) | Agility × 4 + Physical × 3 + Pressure × 2 |
| Final Shot AT | (Shot AT × buffs) + (Potencia hissatsu × buffs de AT) |

La hoja **Characters ATDF** ya tiene calculadas estas stats de duelo para cada personaje.

## 3. Héroes (Hero)

- **126 fichas.** Un mismo personaje aparece con varios estilos de juego.
- **Total de stats:** entre 818 y 832, frente a unos 666 de la base (≈ +25 %).
- **Todos tienen 6 técnicas.**
- **124 de 126 repiten alguna técnica** dentro de esas 6: 110 repiten dos veces, 10 una y 4 tres. Es la misma regla de nuestro GDD (huecos 5 y 6 para repetir y subir de nivel).
- **85 de 126 tienen un Poder Hiperdimensional en el último hueco:** Despertar 66, Tótem 17, Keshin 2. Los otros 41 no tienen en su lista de técnicas ninguno de los poderes de la hoja Hyper Moves.
- Ejemplos:
  - Goenji Héroe: Fireball Screw, Maximum Fire, Grand Fire, Scorching Tackle, Ignited Steal, Burning Overdrive.
  - Fubuki Héroe: Eternal Blizzard ×2, Legendary Wolf, Snow Angel, Land of Ice, Elemental Catalyst.

## 4. Supertécnicas (Hissatsu)

- **691 técnicas.** Por tipo: Tiro 273, Bloqueo (Defense) 144, Regate (Offense) 140, Parada (Keep) 134.
- **Subtipos:** Tiro Largo 43, Tiro-Bloqueo 43, Contraataque 23.
- **Elemento:** Aire 172, Bosque 166, Fuego 164, Tierra 151, Vacío 19.
- **Potencia por escalones:** 30, 50, 60, 70, 85 y 100.
- **El coste de Tensión es casi igual a la potencia:**

| Potencia | Coste de Tensión | Nº de técnicas |
|---|---|---|
| 30 | 30 | 19 |
| 50 | 50 | 120 |
| 60 | 60 | 216 |
| 70 | 70 | 152 |
| 85 | 80 | 91 |
| 100 | 100 | 70 |

Hay pocas excepciones (ej. potencia 50 con coste 60).

## 5. Poderes Hiperdimensionales (Hyper Moves)

- **155 entradas:** Keshin 93, Tótem 56, Despertar 5 y Kizuna Trans 1. Mixi-Max, Armadura y Cambio de Forma no aparecen como entradas propias en esta hoja.
- **Keshin:** los 93 tienen **pasiva** y **técnica propia**, con potencia 100 (75), 85 (17) o 70 (1). Sus técnicas son de Tiro 39, Parada 19, Regate 18 y Bloqueo 17.
  - Pasivas más comunes: Focus AT y DF del equipo, Focus AT y DF propio, Tiro propio, Poder de Vínculo del equipo, Castle Wall DF, Tensión del equipo, menor coste de Tensión y % de paradas.
  - Ejemplos: Atlas (Tierra) → Majin the Hand (Parada, 85), pasiva "% de paradas +5 %"; Pegasus (Aire) → Pegasus Bolt (Regate, 100), pasiva "al pasar, Poder de Vínculo del equipo +50 %".
- **Tótem:** los 56 tienen **técnica propia de potencia 100** y **ninguno tiene pasiva**.
- **Despertar (5):** Burning Overdrive, Keeper's Grit, Ironclad Guardian, Elemental Catalyst e Instant Burst. Ninguno da técnica; solo dan bonus.
- **Kizuna Trans:** AT/DF propio +10 %; se transforma en un compañero y copia parte de sus stats y técnicas.
- **Duración** según la hoja: Despertares, Keshin, Tótem y Armadura 30 s; Mixi-Max 20 s.
- Otras notas de la hoja:
  - Mixi-Max: AT/DF +50 %, potencia hissatsu +20 %.
  - Keshin: AT/DF +40 %.
  - Armadura: AT/DF +20 %, potencia hissatsu +50 %.
  - Mixi-Max y Keshin dan una técnica adicional al activarse.

## 6. Estilos de Juego y sus Pasivas (Main)

| Estilo | Pasiva de equipo |
|---|---|
| Breach | Probabilidad de romper el Castle Wall del equipo +1,8 % (+2,7 % si se va empatando o perdiendo) |
| Counter | Al recuperar el balón (salvo paradas), Tiro AT del equipo +3 % (15 s) |
| Bond | Al pasar, Poder de Vínculo del equipo +5,5 % |
| Tension | Al ganar un Focus o Scramble, Tensión del equipo +4 % |
| Rough Play | Fuera de la zona, faltas del equipo −4 % |
| Justice | Hasta cometer falta, AT y DF del equipo +1,5 % |
