# Diccionario de datos

Describe el esquema de las hojas originales del archivo de trabajo (`Dataset` y `Usuarios`). El archivo en sí **no se incluye** en este repositorio por confidencialidad — este documento describe únicamente la estructura, no los valores individuales.

## Hoja `Dataset` (evento de reproducción, 1 fila = 1 visualización)

| Columna | Tipo | Descripción |
|---|---|---|
| `DATE` | fecha | Fecha de la reproducción. |
| `CUSTOMER_ID` | entero | Identificador numérico del usuario (no personal — sin nombre, correo ni otro dato identificable). |
| `REGION` | texto | Ciudad del usuario. |
| `DEVICE` | texto | Dispositivo usado: `SMART TV`, `MOBILE`, `TABLET`, `WEB`. |
| `TITLE` | texto | Título del contenido visto. |
| `GENRE` | texto | Género/subgénero del contenido (ej. `Serie-Drama`, `Cine-Comedia`). |
| `SCREENTIME` | entero | Minutos vistos de esa reproducción. |
| `LENGTH` | entero | Duración total del contenido, en minutos. |
| `VIDEO_FORMAT` | texto | Formato del video (ej. `HD`). |
| `AUDIO_LANGUAGE` | texto | Idioma del audio. |
| `SEGMENTO` | texto | Segmento de cliente asignado (valores observados: `C`, `D`, `T`, `U` — definición exacta pendiente de documentar). |
| `SCREENTIME_HOUR` | decimal | `SCREENTIME` convertido a horas (columna calculada). |
| `GENRE_T` | texto | Género agrupado a nivel más general (columna calculada a partir de `GENRE`). |

## Hoja `Usuarios` (1 fila = 1 usuario)

| Columna | Tipo | Descripción |
|---|---|---|
| `CUSTOMER_ID` | entero | Identificador numérico del usuario. |
| `REGION` | texto | Ciudad del usuario. |
| `TV` | binario (0/1) | Si el usuario usó Smart TV en el periodo. |
| `MOBILE` | binario (0/1) | Si el usuario usó mobile en el periodo. |
| `TABLET` | binario (0/1) | Si el usuario usó tablet en el periodo. |
| `WEB` | binario (0/1) | Si el usuario usó web en el periodo. |
| `#_DISPOSITIVOS` | entero | Número total de dispositivos distintos usados por el usuario en el periodo. |

## Nota de privacidad

`CUSTOMER_ID` es un identificador numérico interno, no un dato personal directo (no incluye nombre, correo, teléfono ni ubicación exacta). Aun así, el archivo completo no se publica en este repositorio porque los datos me fueron compartidos por un tercero y no tengo confirmación explícita de autorización para redistribuirlos públicamente. Si vas a reutilizar este repositorio con tus propios datos, sustituye los archivos de `data/` por tus propios agregados.
