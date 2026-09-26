# Referencias: Inazuma Eleven Ultimate Database (IE1–IE3 y GO1–GO3)

Fuente: `Copy of Inazuma Eleven Ultimate Database Shared`, hoja de cálculo aportada por el autor del proyecto. Tiene una hoja por juego: IE1, IE2, IE3, GO1, GO2 y GO3. Se usan las **stats a nivel 99**. Exportadas y unificadas en `data/fuentes/udb/jugadores-nivel99.csv` (9498 fichas).

## Nombres unificados

Cada juego llama distinto a las stats. Así quedan agrupadas:

| Unificada | IE1–IE3 | GO1 | GO2 | GO3 (español) |
|---|---|---|---|---|
| tiro | Kick | Kick | Kick | Tiro |
| regate | Body | Dribbling | Dribble | Regate |
| técnica | Control | Technique | Technique | Técnica |
| defensa | Guard | Block | Block | Defensa |
| parada | Guard* | Catch | Catch | Control** |
| velocidad | Speed | Speed | Speed | Velocidad |
| aguante | Stamina | Stamina | Stamina | Aguante |
| extra | Guts | Lucky | Lucky | Suerte |

\* En IE1–IE3 no hay stat de parada separada: Guard vale para defender y para parar.
\*\* En GO3, "Control" es la parada: los porteros tienen de media 142 y los delanteros 73.

## Mínimo – máximo (media) por juego

| Juego | Fichas | Tiro | Regate | Técnica | Defensa | Parada | Velocidad | Aguante | Extra |
|---|---|---|---|---|---|---|---|---|---|
| IE1 | 1016 | 29–79 (55) | 28–79 (57) | 28–82 (55) | 29–79 (57) | 29–79 (57) | 28–79 (57) | 28–79 (59) | 28–82 (57) |
| IE2 | 1645 | 28–85 (57) | 28–82 (58) | 28–85 (57) | 29–82 (59) | 29–82 (59) | 28–79 (58) | 28–81 (60) | 28–82 (59) |
| IE3 | 2336 | 28–100 (55) | 30–100 (56) | 28–86 (55) | 33–99 (56) | 33–99 (56) | 30–97 (56) | 21–99 (55) | 28–103 (56) |
| GO1 | 1000 | 49–187 (93) | 60–187 (103) | 62–158 (103) | 61–188 (104) | 34–188 (72) | 73–197 (110) | 44–150 (100) | 64–145 (95) |
| GO2 | 1501 | 32–196 (96) | 45–196 (104) | 45–171 (102) | 9–196 (104) | 34–196 (85) | 50–178 (106) | 35–171 (96) | 30–178 (90) |
| GO3 | 2000 | 32–196 (100) | 45–196 (106) | 45–171 (105) | 42–191 (106) | 34–196 (89) | 50–197 (107) | 47–171 (98) | 35–178 (93) |

**La saga GO usa casi el doble de escala que la original** (medias de ~100 frente a ~57). Para compararlas hay que normalizar cada juego por separado (ver `propuestas/formula-stats.md`).

## Otros datos de la base

- **IE1–IE3:** stats a nivel 1 y a nivel 99, nivel en el que se maximiza cada stat, Freedom, 4 técnicas con el nivel en que se aprenden, y el ID hexadecimal.
- **GO1:** si tiene Keshin, GP, TP y Freedom.
- **GO2:** elemento, sexo y 4 técnicas.
- **GO3:** elemento ("Tipo"), método de fichaje y 4 técnicas.
- Hay versiones especiales como fichas propias. Ej.: "Mark Evans (Adult)", "Axel Blaze (MixMax ShawnFroste)", "Victor Blade (niño)".
