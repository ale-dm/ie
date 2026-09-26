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
| 10 de Química | +2 en todas las estadísticas (Bonificador Máximo). |
| 9 de Química | 0 (Estadísticas base sin cambios). |
| 7 a 8 de Química | -1 en todas las estadísticas (Penalización leve). |
| 5 a 6 de Química | -3 en todas las estadísticas (Penalización media). |
| 1 a 4 de Química | -5 en todas las estadísticas (Penalización severa). |

## 4. Gestión de Huecos y Supertécnicas

Cada carta incluye una sección de Techniques Spéciales (inspirada en la interfaz de Inazuma Eleven 3DS). Los huecos determinan la versatilidad de la carta antes del encuentro:

### 4.1 Capacidad por Tipo de Carta

- **Cartas Base (Bronce, Plata, Oro):** 4 Huecos de técnica (estricto).
- **Cartas Especiales / Boosteadas:** 5 o 6 Huecos de técnica (representan momentos o partidos icónicos de la franquicia, como finales de torneo o despertares de personajes).

### 4.2 Ocupación de Huecos por Habilidad

| Tipo de Movimiento | Ocupación | Descripción |
|---|---|---|
| Supertécnica Estándar | 1 Hueco | Técnicas individuales básicas de tiro, regate o parada. |
| Hipertécnica / Combinada | 2 Huecos | Técnicas de alto poder que requieren 2 jugadores o gran potencia. |
| Transformación Básica | 1 Hueco | Habilita la activación de Espíritu Guerrero (Keshin) o Despertar. |
| Transformación Avanzada | 2 Huecos | Habilita la activación de Mixi-Max, Armadura de Keshin o Tótem. |

## 5. Modo Fatal: Sistema de Combate 1vs1 (11 Rondas)

El modo Fatal se desarrolla a lo largo de 11 duelos individuales por turnos utilizando las dos barras de recursos compartidas por el equipo:

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
- **Uso:** Gastar 1 carga permite activar el estado especial de la carta (Keshin, Mixi-Max, Armadura, Tótem o Despertar) en esa ronda, aplicando sus respectivos modificadores.

## 6. Modos de Juego Complementarios

- **Apertura de Sobres & Mercado:** Tienda diaria con sobres gratuitos y de monedas, y sistema de Trading con lista de deseos (Wishlist).
- **Modo Draft:** Selección aleatoria de 1 entre 5 cartas por casilla para formar alineaciones de alta química.
- **SBC (Desafíos de Creación de Plantillas):** Puzles temáticos donde se entregan cartas del inventario a cambio de versiones exclusivas.
