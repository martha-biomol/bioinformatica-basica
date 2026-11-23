#!/usr/bin/env python3
"""Análisis básico de secuencias de ADN (proyecto de práctica).

Funciones:
- validar una secuencia (solo A, T, C, G)
- contenido GC
- complemento reverso
- transcripción ADN -> ARN
- traducción ADN -> proteína (código genético estándar)
- conteo de codones

Uso:
    python3 analisis_secuencias.py

La secuencia de ejemplo es la secuencia clásica de los tutoriales
de NCBI/Biopython, usada solo para practicar.
"""

from collections import Counter

# Código genético estándar, construido a partir de las bases TCAG.
_BASES = "TCAG"
_AMINOACIDOS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
_CODONES = [a + b + c for a in _BASES for b in _BASES for c in _BASES]
TABLA_CODONES = dict(zip(_CODONES, _AMINOACIDOS))

_COMPLEMENTO = str.maketrans("ATCG", "TAGC")


def validar_secuencia(seq):
    """Devuelve True si la secuencia solo tiene A, T, C y G."""
    return set(seq.upper()) <= set("ATCG")


def contenido_gc(seq):
    """Porcentaje de G y C en la secuencia."""
    seq = seq.upper()
    return 100.0 * (seq.count("G") + seq.count("C")) / len(seq)


def complemento_reverso(seq):
    """Complemento reverso de la secuencia."""
    return seq.upper().translate(_COMPLEMENTO)[::-1]


def transcribir(seq):
    """Transcripción ADN -> ARN (T se cambia por U)."""
    return seq.upper().replace("T", "U")


def traducir(seq):
    """Traducción en el marco +1. Se detiene en el primer codón de paro."""
    seq = seq.upper()
    proteina = []
    for i in range(0, len(seq) - 2, 3):
        aminoacido = TABLA_CODONES[seq[i:i + 3]]
        if aminoacido == "*":
            break
        proteina.append(aminoacido)
    return "".join(proteina)


def contar_codones(seq):
    """Cuenta cuántas veces aparece cada codón."""
    seq = seq.upper()
    return Counter(seq[i:i + 3] for i in range(0, len(seq) - 2, 3))


if __name__ == "__main__":
    secuencia = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

    print(f"Secuencia: {secuencia}")
    print(f"Longitud: {len(secuencia)} nucleótidos")
    print(f"Secuencia válida: {validar_secuencia(secuencia)}")
    print(f"Contenido GC: {contenido_gc(secuencia):.1f}%")
    print(f"Complemento reverso: {complemento_reverso(secuencia)}")
    print(f"ARN (transcripción): {transcribir(secuencia)}")
    print(f"Proteína (traducción): {traducir(secuencia)}")
    print("Codones más frecuentes:")
    for codon, veces in contar_codones(secuencia).most_common(5):
        print(f"  {codon}: {veces}")
