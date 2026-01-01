# ARCHIVO: PERFILES.py

import json
import os
import unicodedata  # Para limpiar nombres de archivos

# El nombre de la carpeta donde se guardarán los perfiles
DIRECTORIO_PERFILES = "perfiles"


# ==========================================================================
# --- FUNCIONES INTERNAS (Helpers) ---
# ==========================================================================

def _asegurar_directorio_perfiles():
    """
    Verifica si la carpeta 'perfiles/' existe. Si no, la crea.
    """
    if not os.path.exists(DIRECTORIO_PERFILES):
        os.makedirs(DIRECTORIO_PERFILES)


def _limpiar_nombre_archivo(nombre: str) -> str:
    """
    Convierte un nombre de usuario (ej: "José Ángel") en un nombre
    de archivo seguro (ej: "jose_angel.json").
    """
    # Normaliza para quitar acentos
    texto = unicodedata.normalize('NFD', nombre).encode('ascii', 'ignore').decode('utf-8')
    # Quita espacios y lo hace minúscula
    texto = texto.lower().strip().replace(" ", "_")
    # Quita cualquier otro caracter no seguro
    texto = "".join(c for c in texto if c.isalnum() or c == "_")
    return f"{texto}.json"


def _obtener_ruta_perfil(nombre_usuario: str) -> str:
    """
    Devuelve la ruta completa del archivo para un usuario.
    Ej: 'perfiles/mauricio_lopez.json'
    """
    nombre_archivo = _limpiar_nombre_archivo(nombre_usuario)
    return os.path.join(DIRECTORIO_PERFILES, nombre_archivo)


# ==========================================================================
# --- FUNCIONES PÚBLICAS (Las que usará main.py) ---
# ==========================================================================

def obtener_lista_perfiles() -> list[str]:
    """
    Escanea la carpeta 'perfiles/' y devuelve una lista con los
    nombres de los estudiantes ya registrados.
    """
    _asegurar_directorio_perfiles()
    archivos = os.listdir(DIRECTORIO_PERFILES)

    perfiles = []
    for archivo in archivos:
        if archivo.endswith(".json"):
            # Carga el archivo solo para leer el nombre guardado
            ruta_completa = os.path.join(DIRECTORIO_PERFILES, archivo)
            try:
                with open(ruta_completa, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    perfiles.append(datos.get("nombre", "Error de Perfil"))
            except Exception:
                continue  # Ignora archivos corruptos

    return perfiles


def cargar_perfil(nombre_usuario: str) -> dict | None:
    """
    Carga el perfil .json de un estudiante.
    Si el archivo no existe o está dañado, devuelve None.
    """
    _asegurar_directorio_perfiles()
    ruta_perfil = _obtener_ruta_perfil(nombre_usuario)

    if not os.path.exists(ruta_perfil):
        return None

    try:
        with open(ruta_perfil, 'r', encoding='utf-8') as f:
            datos_perfil = json.load(f)
        return datos_perfil
    except json.JSONDecodeError:
        print(f"Error: El archivo de perfil '{ruta_perfil}' está dañado.")
        return None


def guardar_perfil(nombre_usuario: str, datos_perfil: dict) -> bool:
    """
    Guarda (o sobrescribe) los datos de un estudiante en su archivo .json.
    """
    _asegurar_directorio_perfiles()
    ruta_perfil = _obtener_ruta_perfil(nombre_usuario)

    try:
        with open(ruta_perfil, 'w', encoding='utf-8') as f:
            json.dump(datos_perfil, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error fatal al guardar el perfil '{ruta_perfil}': {e}")
        return False


def crear_perfil_nuevo(nombre_usuario: str, carrera_usuario: str) -> dict:
    """
    Crea la estructura de datos para un estudiante nuevo y la guarda.
    """
    print(f"Creando perfil nuevo para {nombre_usuario}...")

    datos_nuevos = {
        "nombre": nombre_usuario,
        "carrera": carrera_usuario,
        "progreso": {}  # El progreso empieza vacío
    }

    # Lo guardamos inmediatamente
    guardar_perfil(nombre_usuario, datos_nuevos)

    return datos_nuevos