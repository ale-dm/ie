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

**Stats individuales:** cada personaje tiene sus propias stats, como en los juegos de DS/3DS: hay jugadores mejores y peores. No se sigue el modelo de Victory Road, donde casi todos tienen la misma base.

**Cálculo de ATT / CTL / DEF:** con la fórmula de `formula-stats.md`, a partir de las stats a nivel 99 de IE1, IE2, IE3, GO1, GO2 y GO3, normalizadas por juego y llevadas al rango de Madfut de cada posición:

| Posición | ATT | CTL | DEF |
|---|---|---|---|
| PR | 25–45 | 25–45 | 60–89 |
| DF | 40–70 | 45–75 | 60–89 |
| MC | 55–86 | 60–89 | 40–80 |
| DL | 60–89 | 55–88 | 30–62 |

Cada personaje tiene **una carta por juego y versión** (estilo Strikers): p. ej. Axel Blaze IE1, Axel Blaze GO2 y Axel Blaze Adulto son cartas distintas. Por encima de 89 solo están las cartas Especiales.

### 2.3 Rareza

Como en Victory Road, las cartas base tienen 5 rarezas por color, en lugar de Bronce, Plata y Oro:

| Color | Rareza (Victory Road) |
|---|---|
| Verde | Normal (Common Player) |
| Azul | En Crecimiento (Growing Player) |
| Lila | Avanzado (Advanced Player) |
| Amarillo | Top (Top Player) |
| Naranja | Legendario (Legendary Player) |

Además están las cartas **Especiales / Boosteadas** (ver 4.1). Los nombres en español son provisionales. Pendiente: qué rarezas tienen 2 huecos y cuáles 4, y los rangos de valoración de cada una.

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

Los huecos forman el **árbol de habilidades** de la carta: la columna de técnicas de la ficha, como en la pantalla de atributos de Victory Road (ver `referencias/img/ievr-arbol-habilidades-goenji.jpg`).

### 4.1 Capacidad por Tipo de Carta

Los huecos del árbol se agrupan **de dos en dos** (grupos 1, 2 y 3, como en Victory Road):

| Tipo de carta | Grupos disponibles | Huecos |
|---|---|---|
| Cartas muy básicas | Grupo 1 | 2 |
| Cartas mejores | Grupos 1 y 2 | 4 |
| Cartas Especiales / Boosteadas | Grupos 1, 2 y 3 | 6 |

- Las cartas especiales representan momentos o partidos icónicos de la franquicia, como finales de torneo o despertares de personajes.
- Las cartas normales tienen como máximo 4 técnicas en el árbol.
- **Huecos del grupo 3 (5 y 6):** no tienen por qué ser hipertécnicas; pueden ser otras técnicas, o repetir una de las que ya tiene. Cada repetición suma **+1** a la potencia de esa técnica.
- **Cómo se ve una repetición:** el hueco gastado queda vacío en el árbol y la técnica mejorada muestra su nivel junto al nombre, con una única notación para todas las técnicas. Ejemplo (Goenji, carta especial): Jet Stream, Meteoric Fire Tornado +1, Prime Legend +1 y Burning Overdrive, con 2 huecos vacíos gastados en subir esas dos técnicas.
- **Técnica de un estado especial:** solo **Espíritu Guerrero (Keshin), Mixi-Max y Tótem** dan técnica. Al activar la Hiperenergía, su técnica sustituye el hueco del estado especial en el árbol y se muestra con un aspecto distinto al de las demás técnicas. Los demás estados (Armadura, Cambio de Forma, Despertar) solo dan boost de puntos.

### 4.2 Ocupación de Huecos por Habilidad

| Tipo de Movimiento | Ocupación | Descripción |
|---|---|---|
| Supertécnica Estándar | 1 Hueco | Técnicas individuales básicas de tiro, regate o parada. |
| Hipertécnica / Combinada | 1 Hueco | Técnicas de alto poder que requieren 2 jugadores o gran potencia. |
| Transformación Básica | 1 Hueco | Habilita la activación de Espíritu Guerrero (Keshin) o Despertar. |
| Transformación Avanzada | 1 Hueco | Habilita la activación de Mixi-Max, Armadura de Keshin, Tótem o Cambio de Forma. |

Todas las técnicas ocupan 1 hueco; no hay técnicas de dos huecos.

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
- Una supertécnica **suma puntos fijos** a la stat del duelo. Cada técnica tiene su propia potencia y su propio coste de Tensión, asignados técnica a técnica como en los juegos de DS/3DS (no por escalones como en Victory Road).
- Los estados especiales (Hiperenergía) también dan **bonus en puntos fijos**, no porcentajes.
- **Duración:** un estado especial y su técnica duran **solo esa ronda**. Excepción: el **Espíritu Guerrero dura 2 rondas**, por la pasiva o el boost que da al equipo.
- **Técnicas de Habilidad:** existen técnicas pasivas, como en los juegos. Cuando se activa la Hiperenergía, si el estado especial tiene técnica propia, esta se suma al árbol de habilidades de la carta (ver 4.1).
- Las técnicas **no evolucionan por uso**. Solo suben de potencia repitiéndolas en los huecos 5 y 6.
- También se pueden usar en la **ronda de desempate**.

### 5.5 Ventaja Elemental

- Ciclo: **Fuego > Bosque > Aire > Tierra > Fuego**. Cuenta el elemento del jugador, no el de la técnica.
- El valor de la ventaja está por definir.
- Bonus por usar una técnica del mismo elemento: de momento no.

### 5.6 Ronda de Desempate

- Si tras las 10 rondas el marcador está igualado, se enfrenta la última carta de cada equipo (la número 11) y se suman todas sus stats. La más alta gana el partido.
- Si la diferencia no es mayor que 5, el partido termina en empate.

### 5.7 Modalidades

- **Fatal Mi Club:** se construye un equipo por serie que no supere la valoración requerida (ej. serie 75 → equipo de 75 o menos). Solo con cartas del club.
- **Fatal Draft:** equipo formado en un Draft. Solo se usan los 11 titulares y no hay restricción de club.

### 5.8 Impulsos Fatales

Cada temporada hay un conjunto de impulsos por serie (Fatal Mi Club) y por división (Fatal Draft). Dan bonus a las stats si el equipo cumple unos requisitos (ej. +2 en todas las stats con 6 o más tipos de cartas).

### 5.9 Puntos por Partido

| Rival | Victoria | Empate | Derrota |
|---|---|---|---|
| Online | 4 | 2 | 1 |
| IA | 3 | 1 | 0 |

Las recompensas por completar una serie o división son las mismas online y contra la IA.

## 6. Modos de Juego Complementarios

- **Apertura de Sobres & Mercado:** Tienda diaria con sobres gratuitos y de monedas, y sistema de Trading con lista de deseos (Wishlist).
- **Modo Draft:** Selección aleatoria de 1 entre 5 cartas por casilla para formar alineaciones de alta química.
- **SBC (Desafíos de Creación de Plantillas):** Puzles temáticos donde se entregan cartas del inventario a cambio de versiones exclusivas.
