# 4. Gestión de Huecos y Supertécnicas

Cada carta incluye una sección de *Techniques Spéciales* (inspirada en la interfaz de Inazuma Eleven 3DS). Los huecos determinan la versatilidad de la carta antes del encuentro.

## 4.1 Capacidad por Tipo de Carta

- **Cartas Base (Bronce, Plata, Oro):** 4 huecos (estricto).
- **Cartas Especiales / Boosteadas:** 5 o 6 huecos (momentos o partidos icónicos: finales de torneo, despertares de personajes…). Los huecos extra son de uso libre (ver 4.3).

## 4.2 Ocupación de Huecos por Habilidad

| Tipo de Movimiento | Ocupación | Descripción |
|---|---|---|
| Supertécnica Estándar | 1 | Técnicas individuales básicas de tiro, regate o parada. |
| Hipertécnica / Combinada | 2 | Técnicas de alto poder que requieren 2 jugadores o gran potencia. |
| Transformación Básica | 1 | Habilita Espíritu Guerrero (Keshin) o Despertar. |
| Transformación Avanzada | 2 | Habilita Mixi-Max, Armadura de Keshin o Tótem. |
| Mejora de Grado | 1 | Repite una supertécnica ya equipada para subir su grado y potencia. |

## 4.3 Uso de los Huecos Extra (5 y 6)

Los huecos 5 y 6 **no están reservados a Hipertécnicas**. Admiten:

1. **Técnicas adicionales:** cualquier movimiento de la tabla 4.2, respetando su ocupación.
2. **Mejora de Grado:** repetir una supertécnica ya equipada para subirle un grado.

### Grados de Técnica

Nomenclatura de la franquicia (Nv.1 → Nv.2 → Nv.3 → Final / G1–G5 / Shin, Kai, Z…) unificada en tres grados:

| Grado | Cómo se obtiene | Potencia |
|---|---|---|
| 1 (Base) | Técnica equipada una vez | Base |
| 2 | + 1 Mejora de Grado | Base +15 % |
| 3 / Final | + 2 Mejoras de Grado | Base +30 % |

**Reglas:**

- Cada Mejora de Grado ocupa 1 hueco, aunque la técnica mejorada ocupe 2.
- Grado máximo: 3 / Final (hasta 2 repeticiones).
- Subir de grado no cambia el coste de Tensión.
- Las Transformaciones no suben de grado; su evolución se representa con otras versiones de carta.
- En la carta, la técnica mejorada se muestra una vez con su grado (ej. *Mano Celestial Nv.3*) y los huecos de mejora aparecen enlazados a ella.

El modelo de datos de una técnica está en `data/schemas/technique.schema.json`.
