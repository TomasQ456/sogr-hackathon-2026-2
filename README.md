# Hackatón individual 2026-2 · Evidencias

**Participante:** _Tomas Quiceno_
**Escuela Colombiana de Ingeniería**

| Prueba | Código |
|---|---|
| Google · Code Jam | `GOOGLE-03` |
| Anthropic · La API de Claude | `ANTHROPIC-03` |

Los enunciados están en [`enunciados/`](enunciados/).

## Estructura

```
<prueba>/<ejercicio>/
├── solucion.py     # tu código (plantilla de la página)
├── ejemplo.txt     # entrada de ejemplo del enunciado
├── esperado.txt    # salida esperada del ejemplo
├── entrada.txt     # TU entrada oficial (pégala desde "Mi entrada")
├── salida.txt      # se genera al correr la entrada oficial
└── evidencias/     # pantallazos
```

## Avance

### Google · `GOOGLE-03`

| Ej. | Problema | Tema | Ejemplo | Oficial | Aceptado | Hora |
|---|---|---|---|---|---|---|
| A | d1000000 | Ordenamiento y voraz | Sí | Sí | Sí | 22:30 |
| B | Moons and Umbrellas | Programación dinámica | Sí | Sí | Sí | 22:37 |
| C | Parenting Partnering Returns | Intervalos y voraz | Sí | Sí | Sí | 22:38 |
| D | Chain Reactions | Árboles y DFS | Sí | Sí | Sí | 22:39 |
| E | Bathroom Stalls | Eficiencia con números enormes | Sí | Sí | Sí | 22:39 |

### Anthropic · `ANTHROPIC-03`

| Ej. | Problema | Tema | Ejemplo | Oficial | Aceptado | Hora |
|---|---|---|---|---|---|---|
| A | Respuesta en streaming | Streaming | Sí | Sí | Sí | 22:40 |
| B | Uso de herramientas | Tool use | Sí | Sí | Sí | 22:40 |
| C | Costos con caché de prompts | Prompt caching y precios | Sí | Sí | Sí | 22:41 |
| D | Límites de velocidad | Rate limits | Sí | Sí | Sí | 22:41 |
| E | Evaluación de respuestas | Evaluaciones calificadas con código | Sí | Sí | Sí | 22:42 |

## Evidencias

Cada pantallazo muestra la terminal corriendo `./probar.sh`: con el ejemplo (comparado contra `esperado.txt`) y con la entrada oficial (guardada en `salida.txt`).

### Google · `GOOGLE-03`

#### A · d1000000

| Ejemplo | Entrada oficial |
|---|---|
| ![A · d1000000 · ejemplo](google/A-d1000000/evidencias/01-ejemplo.png) | ![A · d1000000 · oficial](google/A-d1000000/evidencias/02-oficial.png) |

#### B · Moons and Umbrellas

| Ejemplo | Entrada oficial |
|---|---|
| ![B · Moons and Umbrellas · ejemplo](google/B-moons-and-umbrellas/evidencias/01-ejemplo.png) | ![B · Moons and Umbrellas · oficial](google/B-moons-and-umbrellas/evidencias/02-oficial.png) |

#### C · Parenting Partnering Returns

| Ejemplo | Entrada oficial |
|---|---|
| ![C · Parenting Partnering Returns · ejemplo](google/C-parenting-partnering-returns/evidencias/01-ejemplo.png) | ![C · Parenting Partnering Returns · oficial](google/C-parenting-partnering-returns/evidencias/02-oficial.png) |

#### D · Chain Reactions

| Ejemplo | Entrada oficial |
|---|---|
| ![D · Chain Reactions · ejemplo](google/D-chain-reactions/evidencias/01-ejemplo.png) | ![D · Chain Reactions · oficial](google/D-chain-reactions/evidencias/02-oficial.png) |

#### E · Bathroom Stalls

| Ejemplo | Entrada oficial |
|---|---|
| ![E · Bathroom Stalls · ejemplo](google/E-bathroom-stalls/evidencias/01-ejemplo.png) | ![E · Bathroom Stalls · oficial](google/E-bathroom-stalls/evidencias/02-oficial.png) |

### Anthropic · `ANTHROPIC-03`

#### A · Respuesta en streaming

| Ejemplo | Entrada oficial |
|---|---|
| ![A · Respuesta en streaming · ejemplo](anthropic/A-streaming/evidencias/01-ejemplo.png) | ![A · Respuesta en streaming · oficial](anthropic/A-streaming/evidencias/02-oficial.png) |

#### B · Uso de herramientas

| Ejemplo | Entrada oficial |
|---|---|
| ![B · Uso de herramientas · ejemplo](anthropic/B-uso-de-herramientas/evidencias/01-ejemplo.png) | ![B · Uso de herramientas · oficial](anthropic/B-uso-de-herramientas/evidencias/02-oficial.png) |

#### C · Costos con caché de prompts

| Ejemplo | Entrada oficial |
|---|---|
| ![C · Costos con caché de prompts · ejemplo](anthropic/C-costos-con-cache/evidencias/01-ejemplo.png) | ![C · Costos con caché de prompts · oficial](anthropic/C-costos-con-cache/evidencias/02-oficial.png) |

#### D · Límites de velocidad

| Ejemplo | Entrada oficial |
|---|---|
| ![D · Límites de velocidad · ejemplo](anthropic/D-limites-de-velocidad/evidencias/01-ejemplo.png) | ![D · Límites de velocidad · oficial](anthropic/D-limites-de-velocidad/evidencias/02-oficial.png) |

#### E · Evaluación de respuestas

| Ejemplo | Entrada oficial |
|---|---|
| ![E · Evaluación de respuestas · ejemplo](anthropic/E-evaluacion-de-respuestas/evidencias/01-ejemplo.png) | ![E · Evaluación de respuestas · oficial](anthropic/E-evaluacion-de-respuestas/evidencias/02-oficial.png) |
