# ARCHIVO: main.py

import time
import json
from TEMA import Tema
from UTILIDADES import limpiar_texto
from CONTENIDO import (
    RUTAS_POR_MATERIA,
    NOMBRES_DE_TEMAS,
    BANCO_PREGUNTAS_MAESTRO,
    CONTENIDO_MAESTRO
)
# --- NUEVA IMPORTACIÓN ---
from PERFILES import (
    obtener_lista_perfiles,
    cargar_perfil,
    guardar_perfil,
    crear_perfil_nuevo
)

# --- Constantes del Sistema ---
UMBRAL_APROBACION = 0.8
PREREQUISITOS_DEL_JSON = {}

MODO_ADMIN = False
CLAVE_ADMIN = "MAHA-ADMIN"

def cargar_datos_prerrequisitos():
    """Carga el JSON con los prerrequisitos y lo fusiona con el contenido maestro."""
    global CONTENIDO_MAESTRO, PREREQUISITOS_DEL_JSON

    # 1. Cargar el JSON de prerrequisitos
    json_path = "PREREQUISITOS.json"
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            PREREQUISITOS_DEL_JSON = json.load(f)
        print(f"✅ Prerrequisitos cargados de: {json_path}")
    except FileNotFoundError:
        print(f"❌ Error: Archivo {json_path} no encontrado.")
        return
    except json.JSONDecodeError:
        print(f"❌ Error: Archivo {json_path} dañado.")
        return

    # 2. Fusionar los prerrequisitos con CONTENIDO_MAESTRO
    # Esto asegura que CONTENIDO_MAESTRO tenga la clave 'prerequisitos' actualizada
    for tema_id, datos_req in PREREQUISITOS_DEL_JSON.items():
        if tema_id not in CONTENIDO_MAESTRO:
            # Si un tema está en el JSON pero no en CONTENIDO_MAESTRO (de CONTENIDO.py)
            CONTENIDO_MAESTRO[tema_id] = {}

            # Sobreescribir solo la clave 'prerequisitos' para mantener el contenido original.
        CONTENIDO_MAESTRO[tema_id]['prerequisitos'] = datos_req.get('prerequisitos', [])

    print("✅ Fusión de prerrequisitos completa.")

cargar_datos_prerrequisitos()


def obtener_materia_de_id(id_tema: str) -> str:
    """Extrae el nombre legible de la materia a partir del ID del tema."""
    if id_tema.startswith("FIS-"):
        return "FÍSICA"
    elif id_tema.startswith("QUIM-"):
        return "QUÍMICA"
    elif id_tema.startswith("PROG-"):
        return "PROGRAMACIÓN"
    else:
        return "MATEMÁTICAS"


def obtener_resumen_progreso(progreso_estudiante: dict) -> dict:
    """
    Calcula las métricas de progreso total y por materia.
    Devuelve un diccionario con las métricas y el detalle por materia.
    """
    total_temas_curriculum = len(CONTENIDO_MAESTRO.keys())
    temas_dominados = len(progreso_estudiante)
    porcentaje_progreso = (temas_dominados / total_temas_curriculum) * 100 if total_temas_curriculum > 0 else 0

    resumen_por_materia = {}
    for id_tema in CONTENIDO_MAESTRO.keys():
        materia = obtener_materia_de_id(id_tema)
        if materia not in resumen_por_materia:
            resumen_por_materia[materia] = {"total": 0, "dominados": 0}

        resumen_por_materia[materia]["total"] += 1

        if id_tema in progreso_estudiante:
            resumen_por_materia[materia]["dominados"] += 1

    return {
        "total": total_temas_curriculum,
        "dominados": temas_dominados,
        "restantes": total_temas_curriculum - temas_dominados,
        "porcentaje": round(porcentaje_progreso, 1),
        "detalle_materias": resumen_por_materia
    }


def mostrar_resumen_progreso(nombre_estudiante: str, resumen: dict):
    """Muestra el saludo, el ánimo y el progreso total y por materia."""
    print("\n" + "=" * 60)
    print(f"👋 ¡Bienvenido/a de nuevo, {nombre_estudiante}!")
    print("=" * 60)

    # Muestra el progreso global
    print(f"📈 Progreso General: **{resumen['porcentaje']}%** Dominado.")
    print(f"Te quedan **{resumen['restantes']} temas** por dominar. ¡Vamos por ello! 🚀")

    # Muestra el detalle por materia
    print("\n--- Desglose por Materia ---")
    for materia, detalle in sorted(resumen["detalle_materias"].items()):
        porcentaje_materia = round((detalle["dominados"] / detalle["total"]) * 100, 1)
        barra = "█" * int(porcentaje_materia / 10)  # Barra de 10 caracteres
        espacios = "░" * (10 - len(barra))

        print(
            f"  {materia.ljust(15)}: [{barra}{espacios}] {porcentaje_materia}% ({detalle['dominados']}/{detalle['total']})")

    print("-" * 60)
    time.sleep(1.5)
# ==========================================================================
# --- FUNCIÓN DE BIENVENIDA ---
# ==========================================================================

def mostrar_bienvenida_maha():

    print("      BIENVENIDO AL PROYECTO MAHA")
    print(" (MAuricio Helping Assistant Project)")
    print("\nMAHA es un sistema de aprendizaje personalizado diseñado")
    print("para estudiantes de ingeniería.")
    print("\n¿Cómo funciona?")
    print("1. Evaluaremos tus conocimientos actuales (Diagnóstico).")
    print("2. Identificaremos los temas que necesitas reforzar.")
    print("3. Te guiaremos con lecciones y ejemplos prácticos.")
    print("4. Lo más importante: Te mostraremos por qué cada tema")
    print("   es vital para tu futura carrera en ingeniería.")
    print("\n¡Vamos a empezar!")



# ==========================================================================
# --- (NUEVO) FUNCIÓN DE INICIO DE SESIÓN ---
# ==========================================================================

def gestionar_inicio_sesion() -> dict | None:
    """
    Maneja el login o registro del estudiante.
    Devuelve el diccionario del perfil del estudiante (nuevo o cargado).
    """
    global MODO_ADMIN  # Necesario para cambiar la variable global
    perfiles_existentes = obtener_lista_perfiles()

    while True:
        print("\n¿Eres un usuario (N)uevo o (E)xistente?")
        opcion = input("> ").lower().strip()

        # --- Flujo de Usuario Existente (E) ---
        if opcion == "e":
            # ... (Lógica de listado de perfiles) ...

            nombre_usuario = input("Escribe tu nombre de perfil para cargar tu progreso: ")


            if nombre_usuario.upper() == CLAVE_ADMIN:
                print("\n!Modo Administrador Activado!")
                MODO_ADMIN = True
                # Crea un perfil temporal que ha dominado todos los temas
                return {
                    "nombre": "Administrador",
                    "carrera": "sistemas",
                    "progreso": {id_t: "dominado_por_admin" for id_t in CONTENIDO_MAESTRO.keys()}
                }


            datos_perfil = cargar_perfil(nombre_usuario)

            if datos_perfil:
                print(f"¡Bienvenido de nuevo, {datos_perfil['nombre']}!")
                print(f"Cargando perfil de Ing. {datos_perfil['carrera'].title()}...")
                return datos_perfil
            else:
                print(f"Error: No se encontró un perfil con el nombre '{nombre_usuario}'.")

        # --- Flujo de Usuario Nuevo (N) ---
        elif opcion == "n":
            nombre_usuario = input("\nPerfecto, vamos a crear tu perfil.\nIngresa tu nombre: ")

            # Validar si el nombre ya existe
            perfil_existente = cargar_perfil(nombre_usuario)
            if perfil_existente:
                print(f"Error: El nombre '{nombre_usuario}' ya existe. Intenta iniciar sesión (E).")
                continue

            # Pedir carrera
            carreras_validas = [
                "sistemas", "mecanica", "civil", "electrica",
                "quimica", "mecatronica", "aeronautica"
            ]
            print("\nPara personalizar tus ejemplos, ¿cuál es tu ingeniería?")
            print(f"Opciones: {', '.join(carreras_validas)}")

            while True:
                carrera_usuario = input("> ").lower().strip()
                if carrera_usuario in carreras_validas:
                    break
                else:
                    print(f"'{carrera_usuario}' no es una opción válida. Intenta de nuevo.")

            # Crear y guardar el perfil
            datos_perfil = crear_perfil_nuevo(nombre_usuario, carrera_usuario)
            return datos_perfil

        else:
            print("Opción no válida. Escribe 'N' o 'E'.")


# ==========================================================================
# --- EL CONSTRUCTOR DE TEMAS (LA "FÁBRICA") ---
# ==========================================================================

def construir_tema(id_tema: str) -> Tema | None:
    # 1. Validar que el tema exista
    if id_tema not in NOMBRES_DE_TEMAS or id_tema not in CONTENIDO_MAESTRO:
        print(f"ERROR FATAL: El tema_id '{id_tema}' no está bien definido en CONTENIDO.py")
        return None

    nombre_legible = NOMBRES_DE_TEMAS[id_tema]
    tema = Tema(id_tema=id_tema, nombre_tema=nombre_legible, requiere_diagnostico=True)

    # 2. Cargar Cuestionario Diagnóstico
    preguntas_diagnostico_bruto = [
        q for q in BANCO_PREGUNTAS_MAESTRO if q.get("tema_id") == id_tema
    ]

    cuestionario_formateado = []
    for q in preguntas_diagnostico_bruto:
        cuestionario_formateado.append({
            "enunciado": q.get("pregunta", "Error: pregunta no definida"),
            "respuesta_correcta": q.get("respuesta", "Error: respuesta no definida"),
            "opciones": q.get("opciones", [])
        })

    if cuestionario_formateado:
        tema.asignar_cuestionario(cuestionario_formateado)
    else:
        # print(f"Aviso: Tema '{nombre_legible}' no tiene preguntas de diagnóstico.")
        tema.requiere_diagnostico = False

    # 3. Cargar Contenido de Reforzamiento (CON SIMILARES)
    datos_reforzamiento_bruto = CONTENIDO_MAESTRO[id_tema].get("refuerzo", [])

    reforzamiento_formateado = []
    for lec_bruta in datos_reforzamiento_bruto:
        leccion_nueva = lec_bruta.copy()

        ejercicio_final = {
            "enunciado": "Ejercicio no definido",
            "respuesta_correcta": "",
            "opciones": [],
            "similares": []  # <--- AGREGADO: Lista vacía por defecto
        }

        if "ejercicio" in lec_bruta:
            data_ejercicio = lec_bruta["ejercicio"]

            # 1. Cargar Ejercicio Principal
            if "principal" in data_ejercicio:
                principal = data_ejercicio["principal"]
                ejercicio_final["enunciado"] = principal.get("pregunta", "")
                ejercicio_final["respuesta_correcta"] = principal.get("respuesta_correcta") or principal.get(
                    "respuesta", "")
                ejercicio_final["opciones"] = principal.get("opciones", [])
            else:
                # Soporte para estructura simple antigua
                ejercicio_final["enunciado"] = data_ejercicio.get("pregunta", "")
                ejercicio_final["respuesta_correcta"] = data_ejercicio.get("respuesta_correcta", "")
                ejercicio_final["opciones"] = data_ejercicio.get("opciones", [])

            # 2. Cargar Ejercicios Similares (ESTO ES LO NUEVO IMPORTANTE)
            # Se busca la clave "similares" al mismo nivel que "principal"
            raw_similares = data_ejercicio.get("similares", [])
            similares_procesados = []

            for sim in raw_similares:
                # Normalizamos la estructura de cada similar
                similares_procesados.append({
                    "pregunta": sim.get("pregunta", ""),
                    "respuesta_correcta": sim.get("respuesta_correcta") or sim.get("respuesta", ""),
                    "opciones": sim.get("opciones", [])
                })

            ejercicio_final["similares"] = similares_procesados

        leccion_nueva["ejercicio"] = ejercicio_final
        reforzamiento_formateado.append(leccion_nueva)

    tema.asignar_reforzamiento(reforzamiento_formateado)

    # 4. Cargar Prerrequisitos
    prerequisitos_brutos = CONTENIDO_MAESTRO[id_tema].get("prerequisitos", [])
    tema.asignar_prerequisitos(prerequisitos_brutos)

    return tema


def generar_temas_disponibles(progreso_estudiante: dict) -> list[str]:
    """
    Genera una lista de IDs de temas que el estudiante puede cursar
    comparando su progreso con los prerrequisitos de todos los temas.
    """
    global MODO_ADMIN  # 🔥 Usar la variable global

    if MODO_ADMIN:
        # 🔥 En modo admin, TODOS los temas están disponibles
        return list(CONTENIDO_MAESTRO.keys())

    temas_disponibles_ids = []

    # 1. Creamos un set de temas dominados (solo IDs) para búsquedas rápidas
    temas_dominados_ids = set(progreso_estudiante.keys())

    # 2. Iteramos sobre *todos* los temas definidos en el contenido maestro
    for id_tema, datos_tema in CONTENIDO_MAESTRO.items():

        # Ignorar si el tema ya fue dominado
        if id_tema in temas_dominados_ids:
            continue

        prerequisitos_requeridos = set(datos_tema.get("prerequisitos", []))

        # Lógica central del DAG: ¿Los prerrequisitos son un subconjunto del progreso?
        # Si un tema no tiene prerrequisitos (set vacío), issubset() es True.
        if prerequisitos_requeridos.issubset(temas_dominados_ids):
            temas_disponibles_ids.append(id_tema)

    return temas_disponibles_ids


def calcular_avance_a_meta(progreso_estudiante: dict, meta_id: str) -> dict:
    """
    Calcula cuántos temas faltan para llegar a una meta específica
    recorriendo el Grafo Dirigido Acíclico (DAG) de prerrequisitos.
    """
    temas_dominados = set(progreso_estudiante.keys())

    # 2. Verificar si la meta es válida y ya fue alcanzada
    if meta_id not in CONTENIDO_MAESTRO:
        return {"error": "Meta no válida."}
    if meta_id in temas_dominados:
        return {"restantes": 0, "modulos": 0, "completado": True}

    # 3. Construir la lista de prerrequisitos necesarios (recorriendo el grafo)
    #    Se utiliza una cola de revisión para encontrar todos los temas necesarios
    #    en la ruta (dependencias transitivas).
    temas_requeridos_en_ruta = set()
    cola_revision = set([meta_id])

    while cola_revision:
        tema_actual = cola_revision.pop()

        if tema_actual not in temas_dominados:
            temas_requeridos_en_ruta.add(tema_actual)

            # Añadir los prerrequisitos de este tema a la cola de revisión
            datos_tema = CONTENIDO_MAESTRO.get(tema_actual, {})
            prerequisitos = datos_tema.get("prerequisitos", [])

            for prereq_id in prerequisitos:
                if prereq_id not in temas_dominados:
                    cola_revision.add(prereq_id)

    # 4. Calcular métricas finales
    temas_pendientes_reales = len(temas_requeridos_en_ruta)

    return {
        "restantes": temas_pendientes_reales,
        "modulos": temas_pendientes_reales,  # 1 módulo = 1 tema
        "completado": False
    }


# --------------------------------------------------------------------------

def mostrar_avance_a_metas(progreso_estudiante: dict):
    """Muestra el resumen motivacional de cuánto falta para las metas grandes (en módulos)."""

    METAS_GRANDES = {
        "CÁLCULO INTEGRAL": "CALCULO INTEGRAL",
        "ÁLGEBRA LINEAL": "ALGEBRA LINEAL",
        "DINÁMICA": "FIS-03",
        "ESTEQUIOMETRÍA": "QUIM-03",
    }

    print("\n💡 PROYECCIÓN Y METAS CLAVE:")

    for nombre_meta, id_meta in METAS_GRANDES.items():
        resumen_meta = calcular_avance_a_meta(progreso_estudiante, id_meta)

        if resumen_meta.get("completado"):
            print(f"✅ Meta '{nombre_meta}' alcanzada. ¡El camino está libre!")
        elif resumen_meta.get("restantes") > 0:
            print(f"➡️ Para {nombre_meta}: Faltan {resumen_meta['modulos']} módulos de estudio.")
        else:
            print(f"Meta '{nombre_meta}' no disponible.")

    print("-" * 60)


# --------------------------------------------------------------------------

def mostrar_mapa_y_calcular_ruta(progreso_estudiante: dict):
    """
    Permite al usuario ver el estado de todos los temas y calcular la ruta
    (prerrequisitos pendientes) para cualquier tema deseado.
    """
    temas_dominados = set(progreso_estudiante.keys())

    print("\n\n--- MAPA COMPLETO DE COMPETENCIAS MAHA ---")

    # Mostrar el estado de todos los temas del currículum
    print("\nESTADO DE TEMAS:")
    temas_por_materia = {}
    for id_tema in CONTENIDO_MAESTRO.keys():
        materia = obtener_materia_de_id(id_tema)
        if materia not in temas_por_materia:
            temas_por_materia[materia] = []

        estado = "✅ DOMINADO" if id_tema in temas_dominados else "❌ PENDIENTE"
        nombre = NOMBRES_DE_TEMAS.get(id_tema, id_tema)

        temas_por_materia[materia].append(f"  {id_tema.ljust(15)}: {nombre} ({estado})")

    # Imprimir por materia
    for materia, lista_temas in sorted(temas_por_materia.items()):
        print(f"\n[ {materia.upper()} ]")
        for linea in lista_temas:
            print(linea)

    print("\n" + "=" * 60)
    print("CÁLCULO DE RUTA:")
    print("Ahora puedes calcular cuántos módulos faltan para llegar a una meta específica.")
    print("Ingresa el ID del tema de destino (ej: CALCULO INTEGRAL) o 'A' para abortar.")

    while True:
        meta_id = input("ID del Tema Destino: ").upper().strip()

        if meta_id == 'A':
            print("Regresando al menú principal...")
            break

        if meta_id not in CONTENIDO_MAESTRO:
            print(f"❌ Error: ID '{meta_id}' no encontrado en el currículum. Intenta de nuevo.")
            continue

        resumen_meta = calcular_avance_a_meta(progreso_estudiante, meta_id)

        if resumen_meta.get("completado"):
            print(f"✅ ¡Ya dominas '{NOMBRES_DE_TEMAS[meta_id]}'! Meta alcanzada.")
        elif resumen_meta.get("restantes") > 0:
            print("\n--- RESUMEN DE RUTA ---")
            print(f"Tema Destino: **{NOMBRES_DE_TEMAS[meta_id]}**")
            print(f"Módulos Pendientes: **{resumen_meta['modulos']}** (Mínimo de pasos necesarios).")
            print("Estudia los temas desbloqueados para avanzar en esta ruta.")
            print("-" * 30)

        # Volver a preguntar por otra meta
        print("\n¿Quieres calcular otra ruta? (Ingresa otro ID o 'A' para salir)")

# ==========================================================================
# --- FUNCIÓN DE EJECUCIÓN PRINCIPAL (MODIFICADA) ---
# ==========================================================================

# ARCHIVO: main.py

def ejecutar_simulacion_maha():
    mostrar_bienvenida_maha()

    # --- 1. GESTIÓN DE PERFILES Y LOGIN ---
    datos_perfil_actual = gestionar_inicio_sesion()

    # Verificación de seguridad
    if datos_perfil_actual is None:
        print("Error fatal: No se pudo cargar o crear un perfil. Saliendo.")
        return

    nombre_estudiante = datos_perfil_actual["nombre"]
    carrera_usuario = datos_perfil_actual["carrera"]

    # Se usa la variable global MODO_ADMIN definida en el módulo
    global MODO_ADMIN

    print("\n" + "=" * 60)
    print(f"Comenzando sesión de aprendizaje para {nombre_estudiante}.")
    print("=" * 60)
    time.sleep(1)

    # --- 2. BUCLE PRINCIPAL DE APRENDIZAJE ADAPTATIVO (DAG) ---
    while True:
        # Muestra el resumen de progreso al inicio de CADA ciclo del bucle
        resumen_actual = obtener_resumen_progreso(datos_perfil_actual["progreso"])
        mostrar_resumen_progreso(nombre_estudiante, resumen_actual)

        mostrar_avance_a_metas(datos_perfil_actual["progreso"])

        # A. Generar temas disponibles (Los que cumplen prerrequisitos)
        temas_disponibles_ids = generar_temas_disponibles(datos_perfil_actual["progreso"])

        if not temas_disponibles_ids:
            # Lógica de finalización/bloqueo
            total_temas_curriculum = len(CONTENIDO_MAESTRO.keys())
            progreso_actual = len(datos_perfil_actual["progreso"])

            if progreso_actual >= total_temas_curriculum:
                print("\n¡Felicidades! Has DOMINADO TODO EL CURRÍCULUM MAHA.")
            else:
                print("\n--- ¡ALTO! ---")
                print("No hay temas disponibles. Necesitas terminar los temas pendientes para desbloquear más.")
            break

        # B. MENÚ DE FILTRADO POR MATERIA (UX)
        temas_a_mostrar = temas_disponibles_ids
        materias_disponibles = sorted(list(set(
            obtener_materia_de_id(id) for id in temas_disponibles_ids
        )))

        filtro_materia = None

        while filtro_materia is None:
            print("\n--- MENÚ DE FILTRADO ---")
            print("[0] Mostrar todos los temas disponibles")

            opciones_filtro = {"0": None}

            # Muestra las materias disponibles como opción de filtro
            for i, materia in enumerate(materias_disponibles):
                opcion_num = str(i + 1)
                opciones_filtro[opcion_num] = materia
                print(f"[{opcion_num}] Mostrar solo {materia}")

            opcion_str = input("Elige una opción de filtro ('S' para salir): ").lower().strip()

            if opcion_str == 's':
                print(f"\n¡Hasta pronto, {nombre_estudiante}! Tu progreso ha sido guardado.")
                return

            if opcion_str in opciones_filtro:
                filtro_materia = opciones_filtro[opcion_str]
                break
            else:
                print("Opción no válida. Intenta con el número de la lista.")

        # C. Aplicar el filtro seleccionado
        if filtro_materia:
            temas_a_mostrar = [
                id_tema for id_tema in temas_disponibles_ids
                if obtener_materia_de_id(id_tema) == filtro_materia
            ]
            print(f"\n✅ Mostrando temas desbloqueados de: {filtro_materia}")

        if not temas_a_mostrar and filtro_materia:
            print(f"ADVERTENCIA: No hay temas de {filtro_materia} disponibles en este momento.")
            continue  # Vuelve al menú de filtro

        # D & E. Mostrar y Seleccionar el tema
        seleccion_id = None
        while seleccion_id is None:

            # --- D. Mostrar el menú de temas para cursar (AHORA DENTRO DEL BUCLE) ---
            opciones_disponibles = {}
            print("\n--- SELECCIÓN DE TEMA ---")
            for i, id_tema in enumerate(temas_a_mostrar):
                nombre = NOMBRES_DE_TEMAS.get(id_tema, id_tema)
                materia = obtener_materia_de_id(id_tema)
                opciones_disponibles[str(i + 1)] = id_tema
                print(f"[{i + 1}] {nombre} ({materia})")

            # La opción [P] visible
            print("\n[P] Planificar avance (Ver ruta a cualquier tema)")
            # --- FIN D. La lista se imprime aquí CADA VEZ que el bucle se ejecuta ---

            # E. Selección del tema (Continúa el bucle de entrada)
            opcion_str = input(
                "\nSelecciona el NÚMERO del tema a cursar, [P] para planificar o [S] para salir: ").lower().strip()

            if opcion_str == 's':
                print(f"\n¡Hasta pronto, {nombre_estudiante}! Tu progreso ha sido guardado.")
                return

            if opcion_str == 'p':
                # Al ejecutar 'continue', el código regresa al inicio del WHILE
                # y ejecuta la impresión de la lista de temas nuevamente.
                mostrar_mapa_y_calcular_ruta(datos_perfil_actual["progreso"])
                continue

            if opcion_str in opciones_disponibles:
                seleccion_id = opciones_disponibles[opcion_str]
            else:
                print("Selección no válida. Intenta con el número de la lista o 'P'.")

        id_tema_actual = seleccion_id

        # F. Ejecutar Módulo (construir_tema, diagnóstico, reforzamiento...)
        tema_actual = construir_tema(id_tema_actual)

        if not tema_actual:
            continue

        print("\n" + "=" * 60)
        print(f"INICIANDO MÓDULO: {NOMBRES_DE_TEMAS[id_tema_actual].upper()}")
        print("=" * 60)

        time.sleep(1)

        calificacion = 0.0
        opcion_curso = None  # Valor por defecto para temas sin diagnóstico

        # --- LÓGICA DE DIAGNÓSTICO VS REFUERZO (UX) ---
        if tema_actual.requiere_diagnostico:
            print("\nEste tema tiene un diagnóstico rápido disponible.")

            while opcion_curso not in ['d', 'r']:
                opcion_curso = input(
                    "¿Deseas tomar el [D]iagnóstico o ir directo al [R]eforzamiento? (D/R): ").lower().strip()

                if opcion_curso == 'd':
                    print("✅ Iniciando Diagnóstico...")
                    calificacion = tema_actual.realizar_diagnostico_rapido()
                elif opcion_curso == 'r':
                    calificacion = UMBRAL_APROBACION - 0.01
                    print("➡️ Saltando diagnóstico. Preparando Reforzamiento...")
                else:
                    print("Opción no válida. Por favor, ingresa 'D' o 'R'.")

        # G. Lógica de Reforzamiento (basada en la calificación o la elección 'R')
        if calificacion >= UMBRAL_APROBACION:
            # Caso 1: Aprobó el diagnóstico
            print(f"\n¡Excelente, {nombre_estudiante}! Tema '{tema_actual.nombre_tema}' DOMINADO.")
            tema_actual.actualizar_estado("dominado_por_diagnostico")

        else:
            # Caso 2: Reprobó o eligió ir directo al reforzamiento
            if tema_actual.requiere_diagnostico and opcion_curso == 'd':
                print(f"\nTu calificación ({calificacion:.2f}) requiere reforzamiento.")

            # 🔥🔥🔥 LÓGICA NUEVA: MODO ADMIN (Consola) - SELECCIÓN DE LECCIÓN 🔥🔥🔥
            leccion_elegida_idx = -1  # Por defecto: todas las lecciones

            if MODO_ADMIN:
                lecciones = tema_actual.contenido_reforzamiento
                if lecciones:
                    print("\n--- MODO ADMIN: SELECCIÓN DE LECCIÓN ---")
                    for i, leccion in enumerate(lecciones):
                        titulo = leccion.get('subtema_titulo', f"Lección {i + 1}")
                        print(f"[{i + 1}] {titulo}")
                    print("[0] Ejecutar todas las lecciones / Cancelar")

                    while True:
                        try:
                            opcion_idx = int(input("Selecciona el número de lección: "))
                            if 0 <= opcion_idx <= len(lecciones):
                                leccion_elegida_idx = opcion_idx - 1  # Convertir a índice base 0
                                break
                            else:
                                print("Opción no válida. Intenta de nuevo.")
                        except ValueError:
                            print("Entrada inválida. Ingresa un número.")

            # Ejecutar Reforzamiento
            if leccion_elegida_idx != -1:
                # Caso Admin: Ejecutar solo la lección seleccionada (Índice 0 o superior)
                print(f"¡Iniciando Lección {leccion_elegida_idx + 1} en Modo Admin!")
                time.sleep(1)
                tema_actual.ejecutar_reforzamiento(carrera_usuario, leccion_idx=leccion_elegida_idx)

            else:
                # Caso Normal o Admin que eligió "0" (Ejecutar todas)
                print("¡Iniciando Curso de Reforzamiento Completo!")
                time.sleep(1)
                # La función recibe -1 y ejecuta todas las lecciones
                tema_actual.ejecutar_reforzamiento(carrera_usuario, leccion_idx=-1)

        # H. Guardar Progreso (Persistencia)
        if tema_actual.estado.startswith("dominado") or tema_actual.estado.startswith("completado"):
            datos_perfil_actual["progreso"][id_tema_actual] = tema_actual.estado
            guardar_perfil(nombre_estudiante, datos_perfil_actual)
            print("\n>>> ¡PROGRESO GUARDADO! Los nuevos temas se han desbloqueado. <<<")
            time.sleep(1)

        input("\n...presiona Enter para ver el menú de temas disponibles...")

    # 3. Fin de la sesión
    print("\n" + "=" * 60)
    print(f"¡SESIÓN FINALIZADA, {nombre_estudiante}!")
    print("Gracias por usar MAHA.")
    print("=" * 60)


# ==========================================================================
# --- PUNTO DE ENTRADA ---
# ==========================================================================

if __name__ == "__main__":
    ejecutar_simulacion_maha()