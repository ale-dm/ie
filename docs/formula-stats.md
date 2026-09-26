# Fórmula de ATT / CTL / DEF (v4)

Estado: **aprobada** (2026-09-26). Las cartas usan la **versión por juego**, al estilo Strikers: cada personaje tiene una carta por cada juego y versión en que aparece. Script: `scripts/stats_cartas.py`. Datos: `data/fuentes/udb/jugadores-nivel99.csv` (Ultimate Database, IE1–IE3 y GO1–GO3; ver `referencias/ultimate-database.md`).

**Conocido:** no es perfecta; algunos valores concretos pueden ajustarse a mano carta a carta.

Resultados:
- `data/stats/stats-por-juego.csv`: 9498 fichas, una por versión y juego. **Es la que se usa para las cartas.**
- `data/stats/stats-media-personaje.csv`: media de las versiones base de cada personaje (solo como referencia).

Ejemplos de cartas: `ejemplos-cartas.md`.

## Historial

- **v1:** escala 50–99 frente a todos. Demasiado alta y con porteros de ATT alto.
- **v2:** percentil. Exageraba diferencias con datos en saltos de 10.
- **v3:** proporcional. Diferencias demasiado grandes entre un delantero cualquiera y una estrella.
- **v4 (esta):** rango de Madfut fijado primero, una base con los 6 juegos y normalización por juego. Revisión: se fija también el valor del jugador normal de cada posición para equilibrar los duelos (porteros por encima de defensas, delantero vs. portero ~35 %).

## Pasos

### 1. Stats de cada juego (nivel 99)

| Para calcular | IE1, IE2, IE3 | GO1, GO2 | GO3 (español) |
|---|---|---|---|
| ATT | 80 % Kick + 20 % Control | 80 % Kick + 20 % Technique | 80 % Tiro + 20 % Técnica |
| CTL | 50 % Body + 25 % Control + 25 % Speed | 50 % Dribble + 25 % Technique + 25 % Speed | 50 % Regate + 25 % Técnica + 25 % Velocidad |
| DEF de campo | 80 % Guard + 10 % Control + 10 % Stamina | 80 % Block + 10 % Technique + 10 % Stamina | 80 % Defensa + 10 % Técnica + 10 % Aguante |
| DEF de portero | 100 % Guard (IE no tiene stat de parada) | 80 % Catch + 20 % Block | 80 % Control (parada) + 20 % Defensa |

### 2. Normalizar cada juego

La saga GO usa casi el doble de escala que la original. Antes del paso 1, cada stat se convierte en "cuántas veces se aleja de la media de su juego" (puntuación z). Así un Kick alto en IE1 y un Tiro alto en GO3 valen lo mismo.

### 3. Rango por posición (mínimo · jugador normal · máximo)

Escala lineal por tramos, con los 6 juegos juntos:
- el 2 % más flojo de cada posición → mínimo;
- el jugador mediano → valor normal;
- el 0,5 % mejor → máximo.

| Posición | ATT | CTL | DEF |
|---|---|---|---|
| PR | 25 · 33 · 45 | 25 · 33 · 45 | 69 · 78 · 89 |
| DF | 40 · 54 · 70 | 45 · 60 · 75 | 58 · 71 · 86 |
| MC | 58 · 72 · 86 | 62 · 76 · 89 | 45 · 62 · 80 |
| DL | 62 · 76 · 89 | 55 · 70 · 86 | 28 · 42 · 58 |

Balance de duelos con cartas al azar:

| Duelo | Gana el primero |
|---|---|
| Delantero (ATT) vs. defensa (DEF) | 68 % |
| Delantero (ATT) vs. portero (DEF) | 35 % (hay muchos delanteros y un solo portero por equipo) |
| Medio (ATT) vs. defensa (DEF) | 50 % |
| Portero (DEF) más alta que defensa (DEF) | 80 % |

## Resultado

Ejemplos de muchos personajes en todos los juegos: `ejemplos-cartas.md` (se genera con `scripts/ejemplos_cartas.py`).
