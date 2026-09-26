# Referencias: Stats de Jugadores en los Juegos de DS/3DS (IE1, IE2, IE3)

En los juegos clásicos **cada jugador tiene sus propias stats**: hay jugadores mejores y peores. Victory Road, en cambio, da casi la misma base a todos (ver `victory-road-datos.md`). Por decisión del autor, este proyecto sigue el modelo clásico.

Fuente principal: [watashiwa7 – Inazuma Eleven database](http://watashiwa7.altervista.org/). Stats a nivel 99 de IE1 (igual en IE2), IE2 e IE3, y fórmulas de IE2.

## Datos exportados

`data/fuentes/ds/ie1-ie2-ie3-nivel99.csv`: **2270 fichas** (IE1 512, IE2 1355, IE3 403), con los campos:

- juego, equipo, nombre, posición (PR/DF/MC/DL), elemento;
- FP, TP;
- Kick, Body, Control, Guard, Speed, Stamina, Guts;
- 4 técnicas.

Hay jugadores repetidos entre juegos y en IE2 los nombres llevan el apodo entre paréntesis. En algunas tablas de IE2 la columna "equipo" es el apartado de la página (p. ej. "Scouting by name").

### Dispersión de stats (nivel 99)

| Juego | Rango de cada stat | Total de las 7 stats: mín – media – máx |
|---|---|---|
| IE1 | 28 – 82 | 232 – 400 – 520 |
| IE2 | 28 – 93 | 232 – 414 – 592 |
| IE3 | 28 – 103 | 327 – 412 – 479 |

Comparación: en Victory Road el total base va de 656 a 693 para casi todos.

Ejemplos (IE1, nivel 99):

| Jugador | Pos | Kick | Body | Control | Guard | Speed | Stamina | Guts |
|---|---|---|---|---|---|---|---|---|
| Mark Evans | PR | 72 | 72 | 70 | 77 | 68 | 69 | 79 |
| Axel Blaze | DL | 79 | 66 | 76 | 64 | 72 | 68 | 60 |
| Jude Sharp | MC | 63 | 79 | 79 | 79 | 76 | 76 | 68 |
| Tod Ironside | DF | 54 | 55 | 53 | 56 | 59 | 56 | 65 |
| William Glass | DL | 56 | 51 | 68 | 57 | 56 | 53 | 60 |

## Significado de cada stat (definición oficial, IE2)

- **Kick:** potencia y velocidad del tiro.
- **Body:** probabilidad de conservar el balón al regatear.
- **Control:** precisión de pases y tiros.
- **Guard:** defensa contra regates y tiros.
- **Speed:** velocidad de carrera.
- **Stamina:** cuanto más alta, menos FP se pierden.
- **Guts:** capacidad para disputar el balón.

## Peso de cada stat en cada acción (IE2)

| Acción | Kick | Body | Control | Guard | Speed | Stamina | Guts | Intervalo aleatorio |
|---|---|---|---|---|---|---|---|---|
| Parada / despeje | – | – | – | 80 % | – | 10 % | 10 % | 20 |
| Parada (supertécnica) | – | 10 % | – | 80 % | – | – | 10 % | 20 |
| Defensa (normal) | – | – | 10 % | 80 % | – | – | 10 % | 30 |
| Defensa (supertécnica) | – | – | 10 % | 70 % | – | 10 % | 10 % | 20 |
| Regate (normal) | – | 80 % | 10 % | – | – | – | 10 % | 40 |
| Regate (supertécnica) | – | 70 % | 10 % | – | – | 10 % | 10 % | 20 |
| Tiro (normal) | 80 % | – | 10 % | – | – | – | 10 % | 20 |
| Tiro con vaselina | 20 % | – | 70 % | – | – | – | 10 % | 20 |
| Volea / cabezazo | 60 % | – | – | – | 30 % | – | 10 % | 20 |
| Tiro (supertécnica) | 80 % | – | – | – | – | 10 % | 10 % | 20 |
| Disputa: robar | – | – | – | 60 % | – | 20 % | 20 % | 20 |
| Disputa: conservar | – | 60 % | – | – | – | 20 % | 20 % | 20 |
| Disputa con el portero | – | 30 % | 40 % | 30 % | – | – | – | 40 |
| Bloquear tiro con técnica defensiva | – | – | – | 70 % | – | 10 % | 20 % | 20 |
| Bloquear tiro con otro tiro | 70 % | – | 20 % | – | – | 10 % | – | 20 |

La fuente también menciona un bonus de "fase ardiente" por acción (15–20). La potencia del tiro sube cuanto más cerca de la portería, hasta un 160 %.

## Strikers (Wii) y Strikers 2013

No se han podido consultar sus stats: las páginas de GameFAQs, MrGuider y la wiki bloquean el acceso desde aquí. Las guías de watashiwa7 sobre Strikers tratan de cómo desbloquear jugadores y técnicas, no de stats.

## Fuentes

1. [IE1 – Stats and movesets of players at level 99](http://watashiwa7.altervista.org/ie/1/stats_ie1.htm)
2. [IE2 – Level 99 stats](http://watashiwa7.altervista.org/ie/2/stats_ie2.htm)
3. [IE3 – Stats of players at level 99](http://watashiwa7.altervista.org/ie/3/inazuma-eleven-3-stats-players-level-99.htm)
4. [IE2 – Game mechanics and formulas](http://watashiwa7.altervista.org/ie/2/inazuma-eleven-2-game-mechanics-formula.htm)
