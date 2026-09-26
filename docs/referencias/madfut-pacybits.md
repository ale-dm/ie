# Referencias: Madfut y Pacybits

Solo lo que dicen las fuentes consultadas, con enlace. Lo que no aparece documentado se indica como tal. Nada de este archivo es una regla del juego hasta que se lleve al GDD.

## Madfut — Modo Fatal

- Modo en el que construyes un equipo y lo usas para competir contra otro jugador o contra la IA. [1]
- En cada turno eliges un jugador y decides si lo usas para **controlar, atacar o defender**. [1]
- Si eliges defender, el rival elige un jugador para atacar, y el juego decide el ganador **por la valoración; después compara los otros atributos (defensa y control)**. [1]
- Después elige el rival y respondes tú; así se repite **diez veces** hasta que se decide el ganador. [1]
- En cada ronda gana el jugador con la valoración más alta, pero si eliges el jugador equivocado es fácil que te contrarresten, porque las valoraciones se dividen en ataque, defensa y pase. [3]
- En los modos de batalla cada jugador elige una carta y se enfrenta **tu ataque contra su defensa, tu defensa contra su ataque, o tu control contra su control**. [10]
- Jugar cartas fuera de su posición reduce sus stats; una buena química las aumenta. [10]
- Hay dos variantes: **Fatal My Club** (plantilla de tu colección) y **Fatal Draft** (equipo construido durante el partido). [3]
- Las "Fatal stats" dan bonus pasivos según la valoración Fatal o las estrellas del jugador (ej. MADFUT 25: 2 estrellas = +1 a todas las stats; 1 estrella = sin bonus). [2]

**No documentado en las fuentes:** cuánto se reducen las stats fuera de posición. Rondas, puntuación y desempate: ver la guía de r/MADFUT más abajo.

## Madfut — Guía de Fatal de r/MADFUT [11]

Guía para principiantes publicada por un moderador de r/MADFUT (hace ~4 años). La aportó el autor del proyecto copiando la traducción al español de Reddit.

### Modalidades
- **Fatal My Club:** construyes un equipo por serie que no supere la valoración requerida (ej. serie 75 → equipo de 75 o menos; igual para 82, 85…). Solo con cartas de tu club.
- **Fatal Draft:** equipo sacado de un draft; en el partido solo se usan los 11 titulares. Sin restricción de club.

### Rondas y resolución
- Si eliges una **stat de ataque**, el rival tiene que usar una **stat de defensa**, y al revés.
- La tercera opción es **control**: eliges control y el rival también responde con control.
- Si las dos stats enfrentadas son iguales, se **suman las stats totales de cada carta** y gana la más alta.
- Si también empatan las totales, **nadie se lleva el punto**.
- **10 rondas.** Gana quien tenga más puntos.

### Desempate
- Si tras 10 rondas el marcador está igualado (5-5, 4-4…), hay una **ronda de desempate**: se enfrenta la **última carta de cada equipo** y se suman todas sus stats. La más alta gana el partido.
- Si la diferencia en el desempate **no es mayor que 5**, el partido termina en **empate**.
- Deducción (la guía no lo dice explícitamente): con 11 cartas, 10 rondas y "la última carta" en el desempate, cada carta se juega una vez.

### Información durante la ronda
- Quien elige primero se decide **al azar**; según la guía, no es un factor importante.
- El que responde no ve la carta del rival, solo pistas: la guía pone de ejemplo "control con un centrocampista italiano" o "un delantero del Manchester United", y hay que adivinar quién es.
- Se puede **igualar** la carta del rival para no perder la ronda, o sacrificar una **carta "desechable"**: una carta floja que está para cuadrar química, valoración o impulsos, y que se gasta contra una carta que no puedes ganar para guardar las buenas.
- Consejo del autor de la guía: abrir con una carta de **"clase media"**.

### Impulsos Fatales
- Cada temporada hay impulsos distintos por serie (My Club) y por división (Draft).
- Ejemplo: +2 a todas las stats si el equipo tiene 6 o más tipos de cartas.

### Química
- **10 de química: +1** a las stats. **9:** la stat de la carta. **Menos de 9:** se pierden puntos, más cuanto menor es la química.
- Nota: nuestro GDD (3.2) da **+2** con 10 de química; Madfut da +1.

### Puntos de liga
| Rival | Victoria | Empate | Derrota |
|---|---|---|---|
| Online | 4 | 2 | 1 |
| IA | 3 | 1 | 0 |

Las recompensas por completar serie o división son las mismas online y contra la IA.

## Madfut — Calibración con Cartas Oro Top

Capturas aportadas por el autor (Madfut, Smoq Games): cartas oro únicas de media 87–91. Stats en el orden de la carta: verde (ATT), azul (CTL), rojo (DEF).

| Carta | Media | Pos | ATT | CTL | DEF |
|---|---|---|---|---|---|
| Mbappé | 91 | ST | 89 | 83 | 42 |
| Hansen | 90 | RW | 86 | 88 | 50 |
| Kerr | 90 | ST | 88 | 79 | 47 |
| Vini Jr. | 90 | LW | 88 | 83 | 34 |
| De Bruyne | 90 | CM | 86 | 89 | 64 |
| Smith | 89 | ST | 87 | 81 | 50 |
| Ødegaard | 89 | CM | 84 | 87 | 64 |
| Donnarumma | 89 | GK | 39 | 34 | 88 |
| Alisson | 89 | GK | 41 | 43 | 88 |
| Courtois | 89 | GK | 36 | 29 | 88 |
| van Dijk | 89 | CB | 67 | 70 | 87 |
| ter Stegen | 89 | GK | 39 | 42 | 88 |
| Salah | 89 | RW | 87 | 83 | 49 |
| Kobel | 88 | GK | 35 | 33 | 87 |
| Wirtz | 88 | CAM | 83 | 86 | 50 |
| Katoto | 88 | ST | 86 | 78 | 43 |
| Debinha | 88 | CAM | 84 | 86 | 48 |
| Diani | 88 | RW | 86 | 82 | 58 |
| Patri Guijarro | 88 | CDM | 84 | 83 | 86 |
| Mead | 88 | RW | 86 | 83 | 66 |
| Renard | 88 | CB | 67 | 68 | 87 |
| Irene Paredes | 88 | CB | 61 | 66 | 86 |
| Endler | 88 | GK | 34 | 30 | 87 |
| Foden | 88 | RW | 87 | 85 | 55 |
| Messi | 88 | RW | 86 | 87 | 37 |
| Griezmann | 88 | ST | 86 | 86 | 61 |
| Lewandowski | 88 | ST | 86 | 80 | 48 |
| Bernardo Silva | 88 | CM | 84 | 87 | 68 |
| Oblak | 88 | GK | 38 | 35 | 87 |
| Rüdiger | 88 | CB | 67 | 70 | 86 |
| Osimhen | 87 | ST | 85 | 70 | 46 |
| Dybala | 87 | CAM | 85 | 84 | 44 |
| Saka | 87 | RW | 85 | 82 | 60 |
| Marquinhos | 87 | CB | 69 | 73 | 86 |
| Sommer | 87 | GK | 38 | 33 | 86 |
| Barella | 87 | CM | 82 | 85 | 78 |

Resumen:
- La stat principal nunca pasa de 89 en las oro normales.
- **Porteros:** ATT 34–41, CTL 29–43 y DEF 86–88.
- **Centrales:** ATT 61–69, CTL 66–73 y DEF 86–87.
- **Delanteros y extremos:** ATT 85–89, CTL 70–88 y DEF 34–66.
- **Mediocentros:** ATT 82–86, CTL 83–89 y DEF 44–78.

## Pacybits — Versus

- Modo **Versus** de "stat contra stat", en draft, contra la IA y contra otros jugadores. [4]
- Las cartas tienen en Versus tres stats: **Defense, Control y Attack**, las mismas que ATT / CTL / DEF de nuestro GDD. [5][6]
- La IA de la app usa los valores de ataque, defensa y centro del campo de cada equipo para simular el partido. [7]
- Modos online: Online Draft, Versus, Trading, DBC y LTMs. En SBC y Trading solo se pueden usar cartas **duplicadas**. [8]
- El ranking semanal es dinámico: bajas de puesto cuando otros jugadores te superan en puntos. [8]
- Incluye Draft, apertura de sobres, SBC con recompensas exclusivas y Trading. [9]

**No documentado en texto:** turnos, rondas, cómo se marcan goles y condición de victoria del Versus. Las explicaciones están en vídeos (canales de Pacybits en YouTube) y en la comunidad (subreddit y Discord), que no he podido consultar desde aquí: Reddit bloquea tanto el buscador como el acceso directo desde este entorno (403).

## Fuentes

1. [Madfut 24 – Ultimate Gameplay Guide (Talk Android)](https://www.talkandroid.com/33186-madfut-24-gameplay-guide/)
2. [MADFUT 26 – Strategies for Draft, Cup & Fatal Modes (apkfami)](https://apkfami.com/blog/madfut-26-top-strategies-for-draft-cup-fatal-modes/). Citado a partir del resumen del buscador; la página devuelve 404.
3. [MADFUT 25 (apkmody)](https://apkmody.com/games/madfut-25). Citado a partir del resumen del buscador.
4. [Pacybits FUT 20: Walkthrough, Tips and Strategy Guide (WriterParty)](https://writerparty.com/party/pacybits-fut-20-walkthrough-tips-cheats-and-strategy-guide/)
5. [Pacybits God Mode (GameGuardian)](https://gameguardian.net/forum/files/file/836-pacybits-god-mode-team-hack-always-win-versus-online-100/). Solo confirma los nombres de las stats.
6. [PACYBITS 20 TOTY versus stats (YouTube)](https://www.youtube.com/watch?v=KcUbQbrz5Xg)
7. [PACYBITS FUT 20 (Uptodown)](https://pacybits-fut-20.en.uptodown.com/android). Citado a partir del resumen del buscador.
8. [PACYBITS FAQ](https://www.pacybits.com/faq)
9. [PACYBITS FUT 19 (soft112)](https://pacybits-fut-19.soft112.com/). Descripción de la tienda de apps.
10. [MADFUT 23 – Tips, Cheats, Tricks and Strategy Guide (WriterParty)](https://writerparty.com/party/madfut-23-tips-cheats-tricks-and-strategy-guide/)
11. Guía de r/MADFUT "Fatal – Guía para principiantes y consejos" (u/tm4p29, moderador; texto facilitado por el autor del proyecto).
