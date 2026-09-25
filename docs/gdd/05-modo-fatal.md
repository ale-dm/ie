# 5. Modo Fatal: Combate 1vs1 (11 Rondas)

## 5.0 Referencia

Base tomada del Fatal de Madfut, con las mismas piezas: cada turno un jugador elige una carta y si la usa para **atacar, controlar o defender**; el rival responde con otra carta; gana la stat más alta y el desempate compara los demás atributos; los turnos se alternan hasta el final (10 en Madfut). También hay counters: si eliges la carta equivocada para el tipo de acción, te la contrarrestan. Pacybits usa el mismo principio en su modo Versus (stat contra stat).

Nuestra versión añade tres cosas: 11 rondas (una por jugador del once), supertécnicas con Tensión y transformaciones con Hiperenergía.

## 5.1 Preparación

- Cada equipo alinea 11 cartas. Se aplica el modificador de química (GDD 3.2) a sus stats antes de empezar; esas son sus **stats de partido**.
- Tensión: 20 / 100 para cada equipo. Hiperenergía: 0 cargas.
- Un sorteo decide quién ataca en la ronda 1.

## 5.2 Estructura de una Ronda

Cada carta se usa **una sola vez** por partido. Como en cada ronda cada equipo juega una carta, en 11 rondas se juega el once completo.

1. **Declaración (atacante):** elige una carta disponible y una acción:
   - **Tiro:** su ATT contra la DEF del defensor. Si gana, es **gol**.
   - **Jugada:** su CTL contra el CTL del defensor. Si gana, no marca, pero consigue **Ventaja** (ver 5.4).
2. **Respuesta (defensor):** viendo la carta y la acción, elige una carta disponible para defender.
3. **Potenciación oculta:** los dos eligen a la vez y en secreto si usan una supertécnica (5.5) y/o una transformación (5.6) con la carta que han jugado.
4. **Revelación y resolución** (5.3).
5. **Recursos:** el ganador suma +25 de Tensión y el perdedor +10 (máximo 100).
6. **Posesión:** ataca el otro equipo en la siguiente ronda (ver 5.7 para la ronda 11).

El paso 3 en secreto quita al defensor la ventaja de información de responder después: sabe a quién y cómo le atacan, pero no si el atacante va a gastar Tensión.

## 5.3 Resolución del Duelo

```
Valor = stat de partido + potencia de técnica + bonus de transformación + Ventaja
```

- Gana el valor más alto. **No hay aleatoriedad**: todo lo que decide el duelo es información que el jugador controla (alineación, química, gestión de recursos, lectura del rival).
- **Empate:** se compara la suma de las otras dos stats de partido de cada carta. Si sigue empatado, gana el defensor.

### Restricciones por posición

| Posición | Puede atacar | Puede defender |
|---|---|---|
| PR | No | Sí, contra Tiro o Jugada. Contra Tiro recibe **+5 DEF** (ventaja de portero). |
| DF, MC, DL | Sí | Sí |

Guardar al portero para parar un tiro fuerte es una decisión clave, porque solo se puede usar una vez.

## 5.4 Ventaja (Jugada ganada)

- El equipo que gana una Jugada obtiene **Ventaja: +5** a su próximo Tiro.
- Se pierde si no se usa en su siguiente ataque. No se acumula.
- Un defensor que gana cualquier duelo no obtiene Ventaja: su recompensa es evitar el gol y los +25 de Tensión.

## 5.5 Supertécnicas

- Máximo **1 técnica por carta y duelo**, de la categoría de la acción:

| Acción | Técnica del atacante | Técnica del defensor |
|---|---|---|
| Tiro | tiro | parada (PR) o bloqueo (resto) |
| Jugada | regate | bloqueo o parada |

- **Potencia** = puntos que se suman directamente a la stat:

| Tipo | Potencia base | Coste de Tensión |
|---|---|---|
| Supertécnica Estándar | 6 – 10 | 20 |
| Hipertécnica / Combinada | 12 – 16 | 40 |

- **Grado** (GDD 4.3): Grado 2 = potencia ×1,15 y Grado 3 = ×1,30, redondeado al entero más cercano. El coste no cambia.
- Si al revelar no hay Tensión suficiente, la técnica no se activa y no se gasta nada. La interfaz impide seleccionarla.
- Las **combinadas** solo se pueden activar si el compañero requerido está en el once, aunque ya se haya usado.

## 5.6 Hiperenergía y Transformaciones

- Cada 2 supertécnicas usadas en el partido (acumulado) = 1 carga. Máximo 2 cargas.
- Gastar 1 carga activa la transformación de la carta en ese duelo:

| Transformación | Bonus a las 3 stats en ese duelo |
|---|---|
| Básica (Keshin, Despertar) | +5 |
| Avanzada (Mixi-Max, Armadura, Tótem) | +8 |

- Se puede combinar con una supertécnica en el mismo duelo.

## 5.7 Final del Partido

- En las rondas 1–10 la posesión se alterna, así que cada equipo ataca 5 veces.
- **Ronda 11 (Duelo Final):** ataca el equipo que haya ganado más duelos. Si empatan, el que tenga más Tensión, y si sigue el empate, se sortea.
- **Victoria:** más goles tras 11 rondas.
- **Empate a goles:** en modos de liga, empate. En modos eliminatorios, gana quien haya ganado más duelos; después, el de mayor química de equipo; y, por último, el que tenga más Tensión restante.

## 5.8 Ejemplo

Ronda 1. A ataca con Axel Blaze (ATT 88, química 10 → 90) → Tiro. B responde con Mark Evans (DEF 84, química 9 → 84, +5 de portero = 89).
En secreto: A usa Tornado de Fuego Nv.2 (potencia 8 → 9, −20 de Tensión). B no usa nada.
Resultado: 99 contra 89, gol de A. A: 20 − 20 + 25 = 25 de Tensión. B: 20 + 10 = 30.
