# Inazuma Eleven Mobile

Juego móvil de coleccionismo, construcción de plantillas y combate táctico por turnos ambientado en el universo de Inazuma Eleven, con mecánicas al estilo Madfut / Pacybits.

## Estructura

```
docs/
  GDD.md                        Documento de Diseño de Juego
  decisiones.md                 Decisiones de diseño tomadas
  pendientes.md                 Preguntas abiertas
  referencias/                  Madfut, Pacybits, juegos de Inazuma y datos de Victory Road
  formula-stats.md              Fórmula de ATT / CTL / DEF
  ejemplos-cartas.md            Ejemplos de cartas calculadas
data/
  schemas/                      JSON Schema de cartas y técnicas
  fuentes/victory-road/         CSV de personajes, héroes, técnicas y poderes de Victory Road
  fuentes/ds/                   Stats a nivel 99 de IE1, IE2 e IE3
  fuentes/strikers/             Jugadores y técnicas de GO Strikers 2013 Xtreme
  fuentes/udb/                  Ultimate Database: IE1–IE3 y GO1–GO3 a nivel 99, unificados
  stats/                        ATT / CTL / DEF de todas las fichas de la base
  cartas/                       Cartas cribadas (las que entran en el juego), con técnicas
  config/                       Plantillas de la línea del Raimon
scripts/                        stats_cartas.py → cribar_cartas.py → ejemplos_cartas.py
```
