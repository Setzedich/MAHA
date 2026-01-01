# ARCHIVO: UTILIDADES.py

import unicodedata
import re
from collections import Counter


def limpiar_texto(texto: str) -> str:
    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_sin_acentos = "".join(
        caracter for caracter in texto_normalizado if unicodedata.category(caracter) != "Mn"
    )
    return texto_sin_acentos.lower().replace(" ", "")


def es_respuesta_multiple(texto: str) -> bool:
    partes = [p.strip() for p in texto.split(",")]
    return ("," in texto) and len(partes) >= 2 and all(p != "" for p in partes)


def separar_respuestas_multiples(texto: str) -> list[str]:
    partes = texto.split(",")
    return [limpiar_texto(p) for p in partes if limpiar_texto(p) != ""]


def es_expresion_lineal(expresion: str) -> bool:
    texto_limpio = limpiar_texto(expresion)
    if any(caracter in texto_limpio for caracter in "=^π"):
        return False
    patron = r'[-+]?(?:\d*[a-z]+|\d+)(?:[-+](?:\d*[a-z]+|\d+))*$'
    return re.fullmatch(patron, texto_limpio) is not None


def descomponer_expresion_lineal(expresion: str) -> dict:
    texto_limpio = limpiar_texto(expresion).replace("-", "+-")
    partes = [p for p in texto_limpio.split("+") if p]

    coeficientes = {}
    for parte in partes:
        match = re.fullmatch(r'([-+]?\d*)([a-z]*)', parte)
        if not match:
            return {}

        coef_str, var = match.groups()

        if coef_str in ("", "+"):
            coef_num = 1
        elif coef_str == "-":
            coef_num = -1
        else:
            coef_num = int(coef_str)

        coeficientes[var] = coeficientes.get(var, 0) + coef_num

    return {v: c for v, c in coeficientes.items() if c != 0}


def son_expresiones_lineales_equivalentes(exp1: str, exp2: str) -> bool:
    return descomponer_expresion_lineal(exp1) == descomponer_expresion_lineal(exp2)


def esta_simplificada(expresion: str) -> bool:
    texto_limpio = limpiar_texto(expresion).replace("-", "+-")
    partes = [p for p in texto_limpio.split("+") if p]

    variables_vistas = set()
    for parte in partes:
        match = re.fullmatch(r'([-+]?\d*)([a-z]*)', parte)
        if not match:
            return False

        variable = match.group(2)
        if variable != "" and variable in variables_vistas:
            return False
        variables_vistas.add(variable)
    return True


def es_respuesta_factorizada(expresion: str) -> bool:
    texto_limpio = limpiar_texto(expresion)
    return re.fullmatch(r'^\(.*\).*\(.*\)$', texto_limpio) is not None


def extraer_factores(expresion: str) -> list[str]:
    factores_encontrados = re.findall(r'\((.*?)\)', expresion)
    return [limpiar_texto(f) for f in factores_encontrados]


def validar_respuesta(respuesta_usuario: str, respuesta_correcta: str) -> bool:
    if es_respuesta_multiple(respuesta_correcta):
        respuestas_usuario_lista = separar_respuestas_multiples(respuesta_usuario)
        respuestas_correcta_lista = separar_respuestas_multiples(respuesta_correcta)
        return Counter(respuestas_usuario_lista) == Counter(respuestas_correcta_lista)

    if es_respuesta_factorizada(respuesta_correcta):
        factores_usuario = extraer_factores(respuesta_usuario)
        factores_correctos = extraer_factores(respuesta_correcta)
        return Counter(factores_usuario) == Counter(factores_correctos)

    if es_expresion_lineal(respuesta_correcta):
        return (
                es_expresion_lineal(respuesta_usuario) and
                esta_simplificada(respuesta_usuario) and
                son_expresiones_lineales_equivalentes(respuesta_usuario, respuesta_correcta)
        )

    return limpiar_texto(respuesta_usuario) == limpiar_texto(respuesta_correcta)