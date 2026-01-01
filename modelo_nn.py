# ============================================================
# MODELO DE RED NEURONAL MAHA + VISUALIZACIÓN
# ============================================================
# Aprende del desempeño del usuario en cada tema, permite
# predecir dificultad futura y sugerir el siguiente tema.
# Además, incluye visualización gráfica de la arquitectura.
# ============================================================

import os
import pickle
import pandas as pd
import numpy as np

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
import networkx as nx

# Archivo donde guardamos la red neuronal entrenada
MODEL_PATH = "modelo_maha.pkl"
DATASET_PATH = "dataset_maha.csv"

# Estructura básica esperada para entrenamiento
COLUMNAS = ["tema_id", "score", "porcentaje_global", "num_intentos"]


# ------------------------------------------------------------
# Cargar o inicializar dataset
# ------------------------------------------------------------
def _load_dataset():
    if os.path.exists(DATASET_PATH):
        try:
            return pd.read_csv(DATASET_PATH)
        except:
            pass

    df = pd.DataFrame(columns=COLUMNAS)
    df.to_csv(DATASET_PATH, index=False)
    return df


# ------------------------------------------------------------
# Guardar dataset
# ------------------------------------------------------------
def _save_dataset(df: pd.DataFrame):
    df.to_csv(DATASET_PATH, index=False)


# ------------------------------------------------------------
# Cargar o crear modelo
# ------------------------------------------------------------
def _load_model():
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, "rb") as f:
                return pickle.load(f)
        except:
            pass

    # Modelo inicial
    modelo = MLPRegressor(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        learning_rate_init=0.001,
        max_iter=400,
        random_state=42
    )
    return modelo


# ------------------------------------------------------------
# Guardar modelo
# ------------------------------------------------------------
def _save_model(modelo):
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(modelo, f)


# ------------------------------------------------------------
# Registrar datos y entrenar
# ------------------------------------------------------------
def registrar_resultado_tema(usuario_nombre: str, tema_id: str,
                             score: float,
                             porcentaje_global: float,
                             num_intentos: int = 1):

    df = _load_dataset()

    nuevo = {
        "tema_id": int(abs(hash(tema_id)) % 10000),
        "score": float(score),
        "porcentaje_global": float(porcentaje_global),
        "num_intentos": int(num_intentos)
    }

    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    _save_dataset(df)

    if len(df) < 5:
        return

    # Entrenamiento
    X = df[["tema_id", "porcentaje_global", "num_intentos"]].values
    y = df["score"].values

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    modelo = _load_model()
    modelo.fit(X_scaled, y)

    paquete = {"modelo": modelo, "scaler": scaler}
    _save_model(paquete)


# ------------------------------------------------------------
# PREDICCIÓN
# ------------------------------------------------------------
def predecir_score_esperado(tema_id: str, porcentaje_global: float) -> float:
    if not os.path.exists(MODEL_PATH):
        return 0.8

    try:
        with open(MODEL_PATH, "rb") as f:
            paquete = pickle.load(f)
        modelo = paquete["modelo"]
        scaler = paquete["scaler"]
    except:
        return 0.8

    entrada = np.array([[int(abs(hash(tema_id)) % 10000),
                         porcentaje_global,
                         1]])
    entrada_scaled = scaler.transform(entrada)

    pred = modelo.predict(entrada_scaled)[0]
    return float(max(0.0, min(1.0, pred)))


# ------------------------------------------------------------
# SUGERENCIA DE TEMA
# ------------------------------------------------------------
def sugerir_siguiente_tema(usuario_progreso: dict, lista_temas: list,
                           porcentaje_global: float):

    candidatos = []
    for tema in lista_temas:
        pred = predecir_score_esperado(tema, porcentaje_global)
        distancia = abs(pred - 0.65)
        candidatos.append((tema, pred, distancia))

    candidatos.sort(key=lambda x: x[2])
    return candidatos[0]


# ============================================================
# VISUALIZACIÓN DE LA RED NEURONAL
# ============================================================
def visualizar_red_neuronal():
    """
    Muestra un diagrama de la red neuronal entrenada:
    - Capas
    - Neuronas
    - Conexiones
    - Pesos coloreados
    """
    if not os.path.exists(MODEL_PATH):
        print("El modelo aún no está entrenado. Entrena con al menos 5 registros.")
        return

    with open(MODEL_PATH, "rb") as f:
        paquete = pickle.load(f)
    modelo = paquete["modelo"]

    # Obtenemos pesos
    coefs = modelo.coefs_

    G = nx.DiGraph()
    pos = {}
    layer_x = 0

    # Construcción de nodos capa por capa
    for i, capa in enumerate(coefs):
        num_inputs = capa.shape[0]
        num_outputs = capa.shape[1]

        # Capa izquierda (entradas)
        for n in range(num_inputs):
            G.add_node(f"L{i}_N{n}")
            pos[f"L{i}_N{n}"] = (layer_x, -n)

        # Capa derecha (salidas)
        for n in range(num_outputs):
            G.add_node(f"L{i+1}_N{n}")
            pos[f"L{i+1}_N{n}"] = (layer_x + 1, -n)

        # Crear conexiones con pesos
        for a in range(num_inputs):
            for b in range(num_outputs):
                weight = capa[a, b]
                G.add_edge(f"L{i}_N{a}", f"L{i+1}_N{b}", weight=weight)

        layer_x += 2

    # Dibujado
    plt.figure(figsize=(12, 6))
    edges = G.edges()
    weights = [G[u][v]['weight'] for u, v in edges]

    nx.draw(G, pos,
            with_labels=False,
            node_size=600,
            node_color="skyblue",
            arrows=False,
            width=[abs(w)*2 for w in weights])

    sm = plt.cm.ScalarMappable(cmap="coolwarm")
    sm.set_array(weights)
    plt.colorbar(sm, label="Peso")

    plt.title("Visualización de la Red Neuronal MAHA")
    plt.show()
