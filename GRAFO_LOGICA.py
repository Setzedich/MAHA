# ARCHIVO: GRAFO_LOGICA.py

import networkx as nx
from CONTENIDO import NOMBRES_DE_TEMAS, CONTENIDO_MAESTRO, RUTAS_POR_MATERIA

def crear_grafo_mundos():
    """
    Crea un grafo jerárquico para visualización:
    - Las Materias son nodos centrales ('Mundos').
    - Los Temas son nodos satélite ('Niveles').
    """
    G = nx.DiGraph()

    # 1. Crear Nodos de Mundos (Materias) y conectarlos con sus Niveles
    for materia, lista_temas_ids in RUTAS_POR_MATERIA.items():
        # Nodo Mundo
        nombre_mundo = materia  # Ej: "MATEMATICAS"
        G.add_node(nombre_mundo, tipo="mundo")

        for id_tema in lista_temas_ids:
            # Nodo Nivel
            nombre_nivel = NOMBRES_DE_TEMAS.get(id_tema, id_tema)
            if nombre_nivel:
                G.add_node(nombre_nivel, tipo="nivel", id_tema=id_tema)
                # Conexión Mundo -> Nivel (para agrupar visualmente)
                G.add_edge(nombre_mundo, nombre_nivel, tipo="pertenencia")

    # 2. Crear Conexiones de Prerrequisitos (Nivel -> Nivel)
    for id_destino, datos in CONTENIDO_MAESTRO.items():
        nombre_destino = NOMBRES_DE_TEMAS.get(id_destino)
        if not nombre_destino: continue

        prerequisitos = datos.get('prerequisitos', [])
        for id_origen in prerequisitos:
            nombre_origen = NOMBRES_DE_TEMAS.get(id_origen)
            if nombre_origen:
                G.add_edge(nombre_origen, nombre_destino, tipo="requisito")

    return G

# 🔥 FUNCIÓN RESTAURADA (FALTABA ESTA)
def crear_grafo_simple():
    """
    Crea un grafo simple solo con temas y relaciones de prerrequisitos.
    Se usa para calcular la lógica de conexiones entre niveles.
    """
    G = nx.DiGraph()

    for id_tema, nombre_legible in NOMBRES_DE_TEMAS.items():
        G.add_node(nombre_legible)

    for id_destino, datos in CONTENIDO_MAESTRO.items():
        nombre_destino = NOMBRES_DE_TEMAS.get(id_destino)
        if not nombre_destino: continue

        prerequisitos = datos.get('prerequisitos', [])
        for id_origen in prerequisitos:
            nombre_origen = NOMBRES_DE_TEMAS.get(id_origen)
            if nombre_origen:
                G.add_edge(nombre_origen, nombre_destino)
    return G

def obtener_mapeo_nombre_id():
    """Diccionario para traducir 'Nombre Bonito' -> 'ID_TEMA'."""
    return {nombre: id_tema for id_tema, nombre in NOMBRES_DE_TEMAS.items()}

def obtener_mapeo_id_nombre():
    """Diccionario para traducir 'ID_TEMA' -> 'Nombre Bonito'."""
    return NOMBRES_DE_TEMAS.copy()