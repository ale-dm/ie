# Referencias: Supertécnicas y Transformaciones en los Juegos de Inazuma Eleven

Solo lo que dicen las fuentes, con enlace. Sirve para adaptar al Modo Fatal las supertécnicas y los estados especiales. Nada de esto es regla del juego hasta que se lleve al GDD.

## 1. Supertécnicas (Hissatsu)

### Coste y potencia
- **Juegos clásicos (DS/3DS):** cada técnica cuesta TP (puntos individuales de cada jugador) y su potencia base suele escalar con el TP que cuesta, aunque algunas son fuertes y baratas. [1]
- **Victory Road:** el TP se sustituye por **Tensión, compartida por todo el equipo**. Cada técnica cuesta una cantidad distinta de Tensión, relativa a su potencia. [2]
- **Victory Road:** la Tensión se gana en duelos de Focus y Scramble: **+60 por ganar y +30 por perder**, con un **máximo de 300**. [2]
- **Victory Road:** algunas mecánicas (Knockout, Shout) requieren al menos un 30 % de Tensión. [2]
- **Victory Road:** hay que elegir entre gastar mucha Tensión en el tiro del delantero o guardarla para que el portero aguante la siguiente ofensiva. [3]

> Nuestro GDD (5.1) sigue la misma idea a otra escala: Tensión compartida, 20/100, +25 al ganar y +10 al perder.

### Tipos
- Tiro, Regate (Offense), Bloqueo, Parada y **Habilidad (Skill)**. La Habilidad **no cuesta TP** y tiene efectos pasivos sobre jugadores, técnicas o el equipo. [1]

### Evolución
- **Juegos clásicos:** al usar una técnica con éxito un número de veces, **evoluciona** al siguiente nivel y sube su potencia. Cada técnica tiene un ritmo de crecimiento (rápido, medio o lento). [1]
- La evolución final tiene un coste de TP de 85 en paradas y bloqueos, y de 99 en regates y tiros. [1]
- Victory Road también tiene niveles de técnica. [3]

### Elementos
- Cuatro elementos: **Aire (Viento), Bosque, Fuego y Tierra (Montaña)**. [4][5]
- Ciclo de ventajas: **Fuego > Bosque > Aire > Tierra > Fuego**. [4][5]
- La ventaja elemental solo tiene en cuenta el **elemento del jugador**, no el de la técnica. [4]
- Si un jugador usa una técnica **de su mismo elemento**, recibe un pequeño aumento de potencia. [4][5]
- Victory Road añade el elemento **Vacío** en técnicas, neutro frente a los otros cuatro. [5]
- Las fuentes no publican el valor numérico de la ventaja. [5]

## 2. Estados Especiales

### Victory Road — Poderes Hiperdimensionales (tabla del PDF) [13]

Documento `IEVR_Hyper_Moves_Stat_Bonuses.pdf` (v1.0.5, WIP), aportado por el autor del proyecto y guardado en esta carpeta. Valores en % salvo duración y cooldown.

| Poder | AT | DF | Tiro AT | Poder Focus | Potencia hissatsu | CD hissatsu | Muro DF | KP | Bonus elemento | Mov. | Duración | Cooldown | Técnica extra | Pasiva extra |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Burning Overdrive (Despertar) | 30 | 30 | 20 | 20 | 30 | 50 | – | – | – | 45 | 30 s | 90 s | ✘ | ✘ |
| Keeper's Grit (Despertar) | 30 | 30 | – | – | 30 | 50 | – | 20 | – | 45 | 30 s | 90 s | ✘ | ✘ |
| Ironclad Guardian (Despertar) | 30 | 50 | – | – | 30 | 50 | 30 | – | – | 45 | 30 s | 90 s | ✘ | ✘ |
| Elemental Catalyst (Despertar) | 30 | 30 | – | 20 | 30 | 50 | – | – | ×2 | 45 | 30 s | 90 s | ✘ | ✘ |
| Instant Burst (Despertar) | 30 | 30 | – | 20 | 30 | 70 | – | – | – | 45 | 30 s | 90 s | ✘ | ✘ |
| Keshin | 50 | 50 | – | – | – | – | – | 15¹ | – | 30 | 45 s | 60 s | ✔ | ✔ |
| Keshin (Armadura) | 30 | 30 | – | – | 50 | 50 | – | 15¹ | – | 45 | 45 s | 60 s | ✘ | ✘ |
| Mixi-Max | 50 | 50 | – | – | 20 | 50 | – | 15¹ | – | 45 | 45 s | 60 s | ✔ | ✘ |
| Tótem | 35–75² | 35–75² | – | – | – | – | – | 15¹ | – | 45 | 60 s | 60 s | ✔ | ✘ |
| Kizuna Trans | 10 | 10 | – | – | 20 | 20 | – | – | – | 30 | 60 s | 90 s | ✔¹ | ✘ |
| Cambio de Forma (Mode Change) | 60 | 60 | – | – | – | 80 | – | – | – | – | 75 s | 60 s | ✔³ | ✘ |

1. Solo si el poder base aporta una técnica de portero extra.
2. Empieza en 35 %; +20 % de AT/DF por cada duelo de Focus ganado, hasta un máximo del 75 %. El AT/DF extra se conserva al reutilizar el Tótem.
3. Sustituye todas o parte de las técnicas equipadas. Los Cambios de Forma tienen tableros de habilidades (Abilearn Boards) predefinidos.

- La columna "Tension Cost" del PDF está vacía en v1.0.5: según su historial de cambios, se eliminó el coste de Tensión de Armadura, Mixi-Max y Despertares.
- El historial menciona una v1.0.6 (06/08/2026) que actualiza el AT/DF de la Armadura; el PDF aportado muestra los valores de la v1.0.5.

### Victory Road — Otras fuentes

| Estado | Bonus AT/DF | Otros efectos | Fuente |
|---|---|---|---|
| Espíritu Guerrero (Keshin) | +40 % | Técnicas exclusivas. Pasiva de equipo propia de cada Keshin (ej. +20 % al tiro). Gana los duelos de Focus. | [6][7] |
| Armadura (Keshin Armed) | +20 % | Refuerza las supertécnicas normales. Sin pasiva. Duración corta. | [6][7] |
| Mixi-Max | +50 % | Técnica exclusiva. Sin pasiva de equipo. Solo en ciertos jugadores; no combinable con Keshin ni Tótem. | [6][7][8] |
| Despertar | +30 % | Más velocidad. Cinco variantes. | [6][7] |
| Kizuna Trans | +10 % | Transformarse en un compañero y usar sus técnicas. | [2][6][7] |

Estas fuentes son anteriores al PDF, y sus valores de Keshin y Armadura no coinciden con él (el PDF recoge actualizaciones posteriores).

- Activar Keshin, Mixi-Max o Aura requiere la barra azul de Tensión llena y la consume. [9]
- Las pasivas se muestran en la esquina inferior izquierda durante el partido. [7]

### Juegos de 3DS (GO, Chrono Stone, Galaxy)

- **Keshin:** gasta KP (Keshin Points) en técnicas de Keshin y en acciones; el KP baja según la resistencia del jugador. Mientras está activo, mejora tiro, regate, bloqueo y demás. [10]
- **Habilidades de Keshin:** ej. Kick Force X, que da +30 de Tiro a todo el equipo (Chrono Stone) o +50 (Galaxy) mientras el Keshin está activo. [10]
- **Armadura (Galaxy):** las técnicas cuestan el **70 % del TP** original, y además da más velocidad y más poder en los duelos. No se pueden usar las técnicas ni la habilidad del Keshin, y el KP se agota con el tiempo. [10][11]
- **Mixi-Max:** dos personajes transfieren su aura; el jugador se convierte en un híbrido y usa el poder de su pareja. [11]
- **Tótem (Soul, Galaxy):** el jugador se transforma en un animal o criatura, sube su poder y desbloquea una **Soul Strike** exclusiva, normalmente más potente que sus supertécnicas. El TP pasa a ser **SP**, con el que las técnicas normales cuestan un **50 %**. [11][12]

## 3. Ficha de Jugador en Victory Road (Árbol de Habilidades)

Captura aportada por el autor: `img/ievr-arbol-habilidades-goenji.jpg`.

- Jugador: Shuya Goenji (Axel Blaze), FW, elemento Fuego, "Legendary Player", nivel 88.
- Stats de la ficha: Kick 536, Control 528, Technique 372, Intelligence 190, Pressure 180, Agility 173, Physical 173.
- Columna de técnicas con 6 huecos, numerados por parejas (1, 2, 3):
  - Jet Stream — AT 579
  - Meteoric Fire Tornado **+1** — AT 537
  - Prime Legend **L2** — AT 637
  - Burning Overdrive (Despertar)
  - 2 huecos vacíos
- Según el autor, los 2 huecos vacíos se gastaron en subir el nivel de dos técnicas (Meteoric Fire Tornado y Prime Legend).
- El Despertar (Burning Overdrive) ocupa un hueco en la misma columna que las técnicas.

## 4. Nombres en Español

- **Tótem** es el nombre en español de *Soul* (también llamado *Poder Animal*, y *Alma* en el manga). [12]
- **Cambio de Forma** = *Mode Change* de Victory Road. [13]
- La *Kizuna Trans* (Bond Transform) queda descartada para nuestro juego.

## Fuentes

1. [Hissatsu technique – Inazuma Eleven Wiki](https://inazuma-eleven.fandom.com/wiki/Hissatsu_technique). Citado a partir del resumen del buscador.
2. [Tension – Inazuma Eleven Wiki](https://inazuma-eleven.fandom.com/wiki/Tension) y [Kizuna Trans – Inazuma Eleven Wiki](https://inazuma-eleven.fandom.com/wiki/Kizuna_Trans). Citados a partir del resumen del buscador.
3. [Inazuma Eleven: Victory Road Hissatsu and Every New Special Move (allthings.how)](https://allthings.how/inazuma-eleven-victory-road-hissatsu-and-every-new-special-move/)
4. [Elements – Inazuma Eleven Wiki](https://inazuma-eleven.fandom.com/wiki/Elements). Citado a partir del resumen del buscador.
5. [Inazuma Eleven Victory Road Elements Guide (Operation Sports)](https://www.operationsports.com/inazuma-eleven-victory-road-elements-guide-all-advantages-and-disadvantages-explained/)
6. [Super Dimensional Move Guide – Keshin or Keshin Armed? (note.com)](https://note.com/manners_inaire/n/n7f211528e90e?hl=en)
7. [Differences between hyper moves? (Steam, Victory Road)](https://steamcommunity.com/app/2799860/discussions/0/684112827030450569/)
8. [Mixi Max – Inazuma Eleven Wiki](https://inazuma-eleven.fandom.com/wiki/Mixi_Max). Citado a partir del resumen del buscador.
9. [Inazuma Eleven: Victory Road Beginner's Guide (NoobFeed)](https://www.noobfeed.com/articles/inazuma-eleven-victory-road-beginners-guide-gameplay-tips)
10. [Keshin – Inazuma Eleven GO Galaxy Wiki](https://inazuma-eleven-go-galaxy.fandom.com/wiki/Keshin), [Kick Force X – Inazuma Eleven Wiki](https://inazuma-eleven.fandom.com/wiki/Kick_Force_X). Citados a partir del resumen del buscador.
11. [Keshin Armed](https://inazuma-eleven.fandom.com/wiki/Keshin_Armed), [Soul](https://inazuma-eleven.fandom.com/wiki/Soul), [Mixi Max](https://inazuma-eleven.fandom.com/wiki/Mixi_Max) – Inazuma Eleven Wiki. Citados a partir del resumen del buscador.
12. [Tótem – Wiki Inazuma Eleven (es)](https://inazuma.fandom.com/es/wiki/T%C3%B3tem). Citado a partir del resumen del buscador.
13. `IEVR_Hyper_Moves_Stat_Bonuses.pdf` (v1.0.5), en esta misma carpeta. Aportado por el autor del proyecto.
