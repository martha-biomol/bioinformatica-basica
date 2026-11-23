# Bioinformática básica

Análisis de secuencias de ADN en Python puro (sin dependencias externas).
Proyecto de práctica para mi portafolio.

## Qué hace

`analisis_secuencias.py`:

- Valida que la secuencia solo tenga A, T, C y G
- Calcula el contenido GC
- Obtiene el complemento reverso
- Transcribe ADN a ARN
- Traduce ADN a proteína con el código genético estándar
- Cuenta los codones más frecuentes

## Cómo correrlo

```bash
python3 analisis_secuencias.py
```

## Ejemplo de salida

```
Secuencia: ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
Longitud: 39 nucleótidos
Contenido GC: 56.4%
Proteína (traducción): MAIVMGR
```

La secuencia de ejemplo es la secuencia clásica de los tutoriales de
NCBI/Biopython, usada solo para practicar.

## Qué sigue

- Leer secuencias desde archivos FASTA
- Traducir en los 6 marcos de lectura
- Alinear dos secuencias y calcular su identidad
