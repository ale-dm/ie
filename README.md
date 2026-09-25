# Burro — Inazuma Eleven Mobile

Juego móvil de coleccionismo, construcción de plantillas y combate táctico por turnos ambientado en el universo de Inazuma Eleven, con mecánicas al estilo Madfut / Pacybits (sobres, Draft, SBC y duelos 1vs1).

Sagas cubiertas: IE1, IE2, IE3, GO, GO2, GO3, ARES, ORION y VR (Victory Road).

## Estado

Fase de **definición de diseño**. Todavía no hay motor ni código elegido.

## Estructura

```
docs/
  gdd/                  Documento de Diseño de Juego, una sección por archivo
    01-vision.md
    02-cartas.md
    03-quimica.md
    04-tecnicas.md
    05-modo-fatal.md
    06-modos-de-juego.md
  decisiones.md         Registro de decisiones de diseño tomadas
  pendientes.md         Preguntas abiertas por definir
data/
  schemas/              JSON Schema de cartas y técnicas
  cards/                Cartas de ejemplo
  techniques/           Catálogo de técnicas de ejemplo
```

## Cómo seguir

1. Resolver las preguntas de `docs/pendientes.md`.
2. Anotar cada decisión en `docs/decisiones.md` y reflejarla en la sección del GDD correspondiente.
3. Ampliar `data/` con cartas y técnicas reales siguiendo los esquemas.
