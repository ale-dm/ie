# Documento de Diseño de Juego (GDD): Inazuma Eleven Mobile (Estilo Madfut / Pacybits)

## 1. Visión General del Proyecto

Juego móvil de simulación táctica, coleccionismo y construcción de plantillas ambientado en el universo de Inazuma Eleven. El juego traslada las mecánicas de Madfut / Pacybits (sobres, Drafts, SBCs y batallas por turnos) adaptándolas a la mitología del anime/videojuego, abarcando todas sus sagas oficiales: IE1, IE2, IE3, GO, GO2, GO3, ARES, ORION y VR (Victory Road).

## 2. Estructura y Ficha de las Cartas

### 2.1 Identificadores de Carta

- **Jugador / Personaje:** Nombre y versión correspondiente a una era específica (ej. Mark Evans - IE1 vs. Mark Evans - IE3).
- **Posición:** PR (Portero), DF (Defensa), MC (Centrocampista), DL (Delantero).
- **Equipo / Instituto:** Raimon, Royal Academy, Zeus, Alius, Inazuma Japón, Protocolo Omega, etc.
- **Afinidad / Elemento:** Fuego, Aire, Tierra, Bosque.
- **Juego / Era de Origen:** IE1, IE2, IE3, GO, GO2, GO3, ARES, ORION, VR.

### 2.2 Estadísticas para el Modo Fatal

Las cartas cuentan con tres estadísticas principales alineadas verticalmente en el lado derecho de la carta (estilo Madfut / Smoq Games), con una escala ajustada de 1 a 100:

| Atributo | Significado | Función en Duelo |
|---|---|---|
| ATT | Ataque / Tiro | Utilizado en acciones ofensivas y de disparo a puerta. |
| CTL | Control / Pase / Regate | Utilizado en disputas del centro del campo y movilidad. |
| DEF | Defensa / Parada | Utilizado para cortar avances o detener tiros en portería. |

## 3. Sistema de Química (0 a 100)

La química mide la cohesión de la plantilla y afecta directamente las estadísticas finales de las cartas durante los partidos del modo Fatal.

### 3.1 Cálculo de Química Individual (0 a 10)

Se calcula según los enlaces con los jugadores adyacentes en la formación táctica:

- **Enlace Verde (Fuerte):** Coinciden 2 o 3 parámetros (Equipo, Afinidad o Juego).
- **Enlace Naranja (Medio):** Coincide 1 parámetro.
- **Enlace Rojo (Nulo):** No coincide ningún parámetro.

### 3.2 Modificadores de Stats por Química

| Química del Jugador | Efecto en las Stats de Fatal (ATT, CTL, DEF) |
|---|---|
| 10 de Química | +1 en todas las estadísticas (Bonificador Máximo). |
| 9 de Química | 0 (Estadísticas base sin cambios). |
| 7 a 8 de Química | -1 en todas las estadísticas (Penalización leve). |
| 5 a 6 de Química | -3 en todas las estadísticas (Penalización media). |
| 1 a 4 de Química | -5 en todas las estadísticas (Penalización severa). |

## 4. Gestión de Huecos y Supertécnicas

Cada carta incluye una sección de Techniques Spéciales (inspirada en la interfaz de Inazuma Eleven 3DS). Los huecos determinan la versatilidad de la carta antes del encuentro:

### 4.1 Capacidad por Tipo de Carta

- **Cartas Base (Bronce, Plata, Oro):** 4 Huecos de técnica (estricto).
- **Cartas Especiales / Boosteadas:** 5 o 6 Huecos de técnica (representan momentos o partidos icónicos de la franquicia, como finales de torneo o despertares de personajes).
- **Huecos 5 y 6:** no tienen por qué ser hipertécnicas; pueden ser otras técnicas, o repetir una de las que ya tiene. Cada repetición suma **+1** a la potencia de esa técnica.

### 4.2 Ocupación de Huecos por Habilidad

| Tipo de Movimiento | Ocupación | Descripción |
|---|---|---|
| Supertécnica Estándar | 1 Hueco | Técnicas individuales básicas de tiro, regate o parada. |
| Hipertécnica / Combinada | 2 Huecos | Técnicas de alto poder que requieren 2 jugadores o gran potencia. |
| Transformación Básica | 1 Hueco | Habilita la activación de Espíritu Guerrero (Keshin) o Despertar. |
| Transformación Avanzada | 2 Huecos | Habilita la activación de Mixi-Max, Armadura de Keshin o Tótem. |

## 5. Modo Fatal: Sistema de Combate 1vs1 (10 Rondas + Desempate)

El modo Fatal se desarrolla a lo largo de 10 duelos individuales por turnos, más una ronda de desempate con la carta número 11 si hace falta, utilizando las dos barras de recursos compartidas por el equipo:

```
┌─────────────────────────────────────────────────────────┐
│               SISTEMA DE RECURSOS FATAL                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  [ Duelos 1vs1 ] ────> Generan TENSIÓN (20 a 100)       │
│                             │                           │
│                             ▼                           │
│  [ Supertécnicas ] ───> Gastan TENSIÓN                  │
│                         Cargan HIPERENERGÍA             │
│                             │                           │
│                             ▼                           │
│  [ Hiperenergía ] ───>  Gastas Cargas (Máx. 2)          │
│                         Activas Transformación Especial │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 5.1 Barra Global de Tensión

- **Inicio de Partido:** 20 / 100 de Tensión.
- **Ganar un Duelo:** Suma +25 de Tensión.
- **Perder un Duelo:** Suma +10 de Tensión.
- **Uso:** Se consume para activar las Supertécnicas asignadas en la carta durante el turno seleccionado.

### 5.2 Barra de Hiperenergía (Máximo 2 Cargas)

- **Condición de Carga:** Se obtiene 1 Carga cada vez que el jugador utiliza acumulativamente 2 Supertécnicas en el partido.
- **Uso:** Gastar 1 carga permite activar el estado especial de la carta (Keshin, Mixi-Max, Armadura, Tótem, Cambio de Forma o Despertar) en esa ronda, aplicando sus respectivos modificadores.

### 5.3 Estructura del Partido (igual que Madfut)

- **Alineación:** se juega con los 11 titulares. Cada carta se usa una vez.
- **Quién empieza:** se sortea. Después, los equipos se alternan: en cada ronda uno elige primero y el otro responde.
- **Elección:** el que elige primero escoge una carta y una stat:
  - Si elige **ATT**, el rival responde con la **DEF** de una de sus cartas.
  - Si elige **DEF**, el rival responde con el **ATT** de una de sus cartas.
  - Si elige **CTL**, el rival responde con el **CTL** de una de sus cartas.
- **Información oculta:** el que responde no ve la carta elegida, solo la stat y pistas de la carta.
- **Ganador de la ronda:** la stat más alta gana y suma **1 punto**.
  - Si las stats son iguales, se suman las stats totales (ATT + CTL + DEF) de cada carta y gana la más alta.
  - Si también son iguales, nadie obtiene el punto.
- **10 rondas.** Gana quien tenga más puntos.

### 5.4 Supertécnicas y Transformaciones en la Ronda

- **Los dos jugadores** pueden usarlas: el que elige primero y el que responde.
- Se deciden **al elegir la carta**, de forma **oculta**, y se revelan al resolver la ronda.
- Una supertécnica **suma puntos fijos** a la stat del duelo. Cada técnica tiene su propia potencia y su propio coste de Tensión (valores por definir técnica a técnica).
- Algunas técnicas y estados especiales (p. ej. Espíritu Guerrero) pueden dar **efectos pasivos** en lugar de, o además de, puntos. Por definir tomando como referencia los juegos de la saga.
- También se pueden usar en la **ronda de desempate**.

### 5.5 Ronda de Desempate

- Si tras las 10 rondas el marcador está igualado, se enfrenta la última carta de cada equipo (la número 11) y se suman todas sus stats. La más alta gana el partido.
- Si la diferencia no es mayor que 5, el partido termina en empate.

### 5.6 Modalidades

- **Fatal Mi Club:** se construye un equipo por serie que no supere la valoración requerida (ej. serie 75 → equipo de 75 o menos). Solo con cartas del club.
- **Fatal Draft:** equipo formado en un Draft. Solo se usan los 11 titulares y no hay restricción de club.

### 5.7 Impulsos Fatales

Cada temporada hay un conjunto de impulsos por serie (Fatal Mi Club) y por división (Fatal Draft). Dan bonus a las stats si el equipo cumple unos requisitos (ej. +2 en todas las stats con 6 o más tipos de cartas).

### 5.8 Puntos por Partido

| Rival | Victoria | Empate | Derrota |
|---|---|---|---|
| Online | 4 | 2 | 1 |
| IA | 3 | 1 | 0 |

Las recompensas por completar una serie o división son las mismas online y contra la IA.

## 6. Modos de Juego Complementarios

- **Apertura de Sobres & Mercado:** Tienda diaria con sobres gratuitos y de monedas, y sistema de Trading con lista de deseos (Wishlist).
- **Modo Draft:** Selección aleatoria de 1 entre 5 cartas por casilla para formar alineaciones de alta química.
- **SBC (Desafíos de Creación de Plantillas):** Puzles temáticos donde se entregan cartas del inventario a cambio de versiones exclusivas.
