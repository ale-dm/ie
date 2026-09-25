# CLAUDE.md

Proyecto de diseño del juego "Inazuma Eleven Mobile" (repo `ie`). Idioma del proyecto: español.

- El GDD vive en `docs/gdd/`, una sección por archivo. Es la fuente de verdad del diseño.
- Toda decisión nueva se registra en `docs/decisiones.md` (fecha, decisión, motivo) y se aplica al GDD.
- Las dudas sin resolver van a `docs/pendientes.md`; al resolverlas se quitan de ahí.
- Los datos en `data/` deben validar contra `data/schemas/*.schema.json`. Los identificadores (`id`) van en kebab-case sin tildes.
- Nombres de personajes y técnicas: se usa la localización española de la franquicia cuando existe.
