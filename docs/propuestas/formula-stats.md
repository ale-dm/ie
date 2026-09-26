# Propuesta: Fórmula de ATT / CTL / DEF (v4)

Estado: **propuesta, no aprobada**. Script: `scripts/stats_cartas.py`. Datos: `data/fuentes/udb/jugadores-nivel99.csv` (Ultimate Database, IE1–IE3 y GO1–GO3; ver `referencias/ultimate-database.md`).

Resultados:
- `data/propuestas/stats-cartas.csv`: 9498 fichas, una por versión y juego.
- `data/propuestas/stats-media-personaje.csv`: media de las versiones base de cada personaje en todos los juegos en que aparece.

## Historial

- **v1:** escala 50–99 frente a todos. Demasiado alta y con porteros de ATT alto.
- **v2:** percentil. Exageraba diferencias con datos en saltos de 10.
- **v3:** proporcional. Diferencias demasiado grandes entre un delantero cualquiera y una estrella.
- **v4 (esta):** rango de Madfut fijado primero, una base con los 6 juegos y normalización por juego.

## Pasos

### 1. Normalizar cada juego

La saga GO usa casi el doble de escala que la original. Cada stat se convierte en "cuántas veces se aleja de la media de su juego" (puntuación z). Así un Kick alto en IE1 y un Tiro alto en GO3 valen lo mismo.

### 2. Stat bruta (con las stats normalizadas)

| Stat | Fórmula |
|---|---|
| ATT | 80 % tiro + 20 % técnica |
| CTL | 50 % regate + 25 % técnica + 25 % velocidad |
| DEF (campo) | 80 % defensa + 10 % técnica + 10 % aguante |
| DEF (portero) | 80 % parada + 20 % defensa |

### 3. Rango fijo de Madfut por posición

Escala lineal, con los 6 juegos juntos. El 2 % más flojo de cada posición queda en el mínimo y el 0,5 % mejor en el techo.

| Posición | ATT | CTL | DEF |
|---|---|---|---|
| PR | 25–45 | 25–45 | 60–89 |
| DF | 40–70 | 45–75 | 60–89 |
| MC | 55–86 | 60–89 | 40–80 |
| DL | 60–89 | 55–88 | 30–62 |

## Resultado

### El mismo personaje en distintos juegos

| Personaje | IE1 | IE2 | IE3 | GO1 | GO2 | GO3 | **Media** |
|---|---|---|---|---|---|---|---|
| Mark Evans (PR) | 44/45/82 | 43/45/81 | 32/32/88 | 33/33/84 | 37/34/83 | 35/34/83 | **37/37/84** |
| Axel Blaze (DL) | 84/84/54 | 83/82/53 | 85/81/49 | – | 82/75/45 | 81/75/45 | **83/79/49** |
| Jude Sharp (MC) | 78/89/80 | 76/89/80 | 80/82/57 | 76/71/56 | 76/80/61 | 76/83/61 | **77/82/65** |
| Kevin Dragonfly (DL) | 78/73/50 | 76/72/49 | 83/69/43 | 88/63/40 | 78/64/38 | – | **82/68/44** |
| Bobby Shearer (DF) | 70/67/84 | 70/65/83 | 54/63/86 | 50/51/71 | 51/60/78 | 51/62/81 | **57/62/81** |
| Victor Blade (DL) | – | – | – | 78/64/46 | 82/76/47 | 84/78/46 | **81/73/46** |
| Riccardo Di Rigo (MC) | – | – | – | 79/75/73 | 77/82/64 | 76/82/65 | **77/80/67** |
| Arion Sherwind (MC) | – | – | – | 66/82/61 | – | 72/81/59 | **69/82/60** |

Las versiones especiales van aparte y salen más altas: Axel adulto (GO2) 89/85/39, Axel Mixi-Max con Shawn (GO3) 87/86/42, Mark adulto (GO2) 35/36/87.

### Delanteros normales vs. estrellas (ATT de DL)

| Juego | Mínimo | Flojo (p25) | Normal (mediana) | Bueno (p75) | Máximo |
|---|---|---|---|---|---|
| IE1 | 60 | 66 | 70 | 73 | 84 |
| IE2 | 60 | 66 | 70 | 74 | 83 |
| IE3 | 60 | 66 | 70 | 74 | 89 |
| GO1 | 62 | 70 | 75 | 78 | 89 |
| GO2 | 65 | 73 | 76 | 78 | 89 |
| GO3 | 60 | 73 | 76 | 78 | 88 |

Un delantero normal sale en 70–76; Axel en 81–85. Los seis juegos quedan equivalentes.
