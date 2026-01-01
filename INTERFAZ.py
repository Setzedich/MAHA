# ARCHIVO: INTERFAZ.py (Modificado para Cursos de Reforzamiento)

from __future__ import annotations

import io
import sys
import html  # <-- Importado para mostrar código/ejemplos de forma segura
# --- Integración visual de la red neuronal ---
import os
import pickle
import matplotlib
import random
import time

matplotlib.use("QtAgg")  # para PySide6

import networkx as nx

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.patheffects as path_effects
from matplotlib.figure import Figure
from TEMA import Tema
from contextlib import redirect_stdout
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from PySide6.QtCore import Qt, QSize, Signal, Slot, QTimer, QEasingCurve, QPropertyAnimation
from PySide6.QtGui import QAction, QPixmap, QMovie
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QListWidget, QListWidgetItem, QStackedWidget, QFrame, QLineEdit, QComboBox,
    QMessageBox, QScrollArea, QGraphicsOpacityEffect, QSpacerItem, QSizePolicy, QSplitter,
    QFileDialog, QStyle, QDialog, QSlider, QCheckBox, QRadioButton, QButtonGroup
)

# --- Integración con los módulos del proyecto ---
from CONTENIDO import (
    RUTAS_POR_MATERIA,
    NOMBRES_DE_TEMAS,
    BANCO_PREGUNTAS_MAESTRO,
    CONTENIDO_MAESTRO
)
from PERFILES import (
    obtener_lista_perfiles,
    cargar_perfil,
    guardar_perfil,
    crear_perfil_nuevo
)
from UTILIDADES import validar_respuesta, limpiar_texto
import main as core  # mostrar_bienvenida_maha, obtener_resumen_progreso, etc.
# (MODIFICADO) Asegurarnos de tener las funciones de main que necesitamos
from main import generar_temas_disponibles, construir_tema, UMBRAL_APROBACION, obtener_resumen_progreso

from GRAFO_LOGICA import (
    crear_grafo_mundos,
    crear_grafo_simple,        # <--- AGREGADO
    obtener_mapeo_nombre_id,
    obtener_mapeo_id_nombre    # <--- AGREGADO
)

try:
    from modelo_nn import sugerir_siguiente_tema, MODEL_PATH
except ImportError:
    print("Advertencia: No se pudo importar 'modelo_nn'. Las sugerencias de IA estarán desactivadas.")
    MODEL_PATH = "modelo_nn.pkl"  # Path de respaldo


    # Función de respaldo si la IA no existe
    def sugerir_siguiente_tema(usuario_progreso, lista_temas, porcentaje_global):
        print("Usando sugerencia de respaldo (primer tema)")
        if not lista_temas:
            return None, 0.0, 0.0
        return lista_temas[0], 0.5, 0.0

# ---------------------------- Estilos de UI ----------------------------

PRIMARY = "#0ea5e9"  # azul elegante
PRIMARY_DARK = "#0284c7"
BG = "#0b1020"  # fondo oscuro
FG = "#e5e7eb"  # texto claro
MUTED = "#a1a1aa"  # gris
CARD_BG = "#0f172a"
CARD_BORDER = "#1f2937"


def app_stylesheet() -> str:
    return f"""
    QWidget {{
        background-color: {BG};
        color: {FG};
        font-family: 'Inter', 'Segoe UI', system-ui, -apple-system;
        font-size: 14px;
    }}

    /* --------- Botones --------- */
    QPushButton {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 {PRIMARY}, stop:1 {PRIMARY_DARK});
        border: none;
        border-radius: 10px;
        padding: 10px 18px;
        font-weight: 600;
        color: white;
        letter-spacing: 0.4px;
        transition: all 180ms ease;
    }}
    QPushButton:hover {{
        background: #38bdf8;
    }}
    QPushButton:disabled {{
        background: #334155;
        color: #94a3b8;
    }}

    /* --------- Sidebar --------- */
    QFrame#Sidebar {{
        background-color: rgba(15, 23, 42, 0.6);
        border-radius: 18px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        backdrop-filter: blur(10px);
    }}

    /* --------- Chat container --------- */
    QFrame#ChatContainer {{
        background-color: #0a1120;
        border-radius: 20px;
        border: 1px solid #1e293b;
        box-shadow: 0 0 16px rgba(14,165,233,0.05);
    }}

    QLabel#Title {{
        font-size: 18px;
        font-weight: 700;
        color: #f1f5f9;
    }}

    QLabel#Small {{
        font-size: 13px;
        font-weight: 500;
        color: #94a3b8;
        margin-top: 8px;
    }}

    QListWidget {{
        background-color: rgba(15,23,42,0.5);
        border: 1px solid #1e293b;
        border-radius: 10px;
        color: #e2e8f0;
        padding: 6px;
    }}
    QListWidget::item:hover {{
        background-color: #1e293b;
        border-radius: 8px;
    }}

    /* --------- Burbujas --------- */
    QLabel#BubbleBot {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
            stop:0 #1e40af, stop:1 #2563eb);
        color: #f8fafc;
        border-radius: 16px;
        padding: 14px 20px;
        font-size: 15px;
        line-height: 1.4em;
        margin: 8px auto;
        max-width: 720px;
        min-width: 300px;
        box-shadow: 0 0 12px rgba(30,64,175,0.2);
    }}
    QLabel#BubbleUser {{
        background: #1e293b;
        color: #f1f5f9;
        border-radius: 14px;
        padding: 10px 14px;
        font-size: 15px;
        line-height: 1.3em;
        margin: 6px auto;
        max-width: 70%;
        box-shadow: 0 0 6px rgba(14,165,233,0.1);
    }}

    QScrollArea {{
        background: transparent;
        border: none;
    }}

    QMenuBar {{
        background-color: #0b1020;
        color: #f8fafc;
        font-weight: 600;
    }}
    QMenuBar::item:selected {{
        background-color: #1e293b;
    }}
                /* --------- Selección activa en Materias y Temas --------- */
    QListWidget::item:selected {{
        background-color: #1e40af;
        border-radius: 8px;
        color: white;
        font-weight: 600;
        border: 1px solid #38bdf8;
    }}

    QListWidget::item:focus {{
        outline: none;
    }}
    """


# ---------------------------- Helpers ----------------------------

def _capture_welcome_lines() -> List[str]:
    """Obtiene el texto multilinea de main.mostrar_bienvenida_maha() y lo divide de forma agradable."""
    if hasattr(core, "mostrar_bienvenida_maha"):
        buf = io.StringIO()
        with redirect_stdout(buf):
            try:
                core.mostrar_bienvenida_maha()
            except Exception:
                pass
        txt = buf.getvalue().strip()
        if not txt:
            txt = (
                "BIENVENIDO A MAHA\n"
                "Tu asistente de aprendizaje para ingeniería.\n"
                "Explora materias, contesta diagnósticos y mide tu progreso."
            )
    else:
        txt = (
            "BIENVENIDO A MAHA\n"
            "Tu asistente de aprendizaje para ingeniería.\n"
            "Explora materias, contesta diagnósticos y mide tu progreso."
        )
    # limpieza básica y split por saltos
    lines = [l.strip() for l in txt.replace("\r", "").split("\n") if l.strip()]
    return lines


def _fade_in(widget: QWidget, msec: int = 280):
    eff = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(eff)
    anim = QPropertyAnimation(eff, b"opacity", widget)
    anim.setDuration(msec)
    anim.setStartValue(0.0)
    anim.setEndValue(1.0)
    anim.setEasingCurve(QEasingCurve.OutCubic)
    anim.start(QPropertyAnimation.DeleteWhenStopped)


def _typewriter_effect(label: QLabel, text: str, speed: int = 35):
    """Escribe el texto letra por letra con efecto de máquina de escribir."""
    label.setText("")  # empieza vacío
    label.full_text = text
    label.current_index = 0

    timer = QTimer(label)
    timer.setInterval(speed)

    def update_text():
        if label.current_index < len(label.full_text):
            label.setText(label.full_text[: label.current_index + 1])
            label.current_index += 1
        else:
            timer.stop()

    timer.timeout.connect(update_text)
    timer.start()


def ensure_dict(d: Optional[dict]) -> dict:
    return d if isinstance(d, dict) else {}


@dataclass
class Usuario:
    nombre: str
    carrera: str
    progreso: Dict[str, str]  # id_tema -> estado


# ----------------------------- Componentes -----------------------------
# ==============================================================
# WIDGET MATPLOTLIB + VENTANA DE RED NEURONAL
# ==============================================================

# ==============================================================
# WIDGET MATPLOTLIB + VENTANA DE RED NEURONAL (CORREGIDO)
# ==============================================================

# ARCHIVO: INTERFAZ.py

class InteractiveMatplotlibWidget(QWidget):
    """
    Widget de Matplotlib interactivo - SIN BORDES NI MÁRGENES
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.fig = Figure(figsize=(10, 8), dpi=100, facecolor='none')

        # 🔥🔥🔥 CAMBIO CLAVE: ELIMINAR MÁRGENES BLANCOS 🔥🔥🔥
        self.fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
        # ----------------------------------------------------

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.canvas.setStyleSheet("background: transparent; border: none;")
        self.canvas.setMouseTracking(True)
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()

        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)

        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('none')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        for spine in self.ax.spines.values():
            spine.set_visible(False)

        self._is_panning = False
        self._pan_start_x = None
        self._pan_start_y = None
        self._zoom_factor = 1.15
        self._current_scale = 1.0
        self.initial_xlim = None
        self.initial_ylim = None

        self.canvas.mpl_connect('button_press_event', self.on_press)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.canvas.mpl_connect('key_press_event', self.on_key_press)

    def on_press(self, event):
        if event.button == 1 and event.inaxes == self.ax:
            self._is_panning = True
            self._pan_start_x = event.xdata
            self._pan_start_y = event.ydata
            self.canvas.setCursor(Qt.ClosedHandCursor)

    def on_release(self, event):
        if event.button == 1:
            self._is_panning = False
            self._pan_start_x = None
            self._pan_start_y = None
            self.canvas.setCursor(Qt.ArrowCursor)

    def on_motion(self, event):
        if not self._is_panning or event.xdata is None or event.inaxes != self.ax:
            return
        dx = event.xdata - self._pan_start_x
        dy = event.ydata - self._pan_start_y
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        self.ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
        self.ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
        self.canvas.draw_idle()

    def on_scroll(self, event):
        if event.inaxes != self.ax: return
        x_center, y_center = event.xdata, event.ydata
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()

        if event.button == 'up':
            scale_factor = 1 / self._zoom_factor
            self._current_scale *= self._zoom_factor
        elif event.button == 'down':
            scale_factor = self._zoom_factor
            self._current_scale /= self._zoom_factor
        else:
            return

        # Límites de zoom amplios
        if self._current_scale < 0.01 or self._current_scale > 100:
            return

        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
        rel_x = (x_center - cur_xlim[0]) / (cur_xlim[1] - cur_xlim[0])
        rel_y = (y_center - cur_ylim[0]) / (cur_ylim[1] - cur_ylim[0])

        self.ax.set_xlim(x_center - new_width * rel_x, x_center + new_width * (1 - rel_x))
        self.ax.set_ylim(y_center - new_height * rel_y, y_center + new_height * (1 - rel_y))
        self.canvas.draw_idle()

    def on_key_press(self, event):
        cur_xlim = self.ax.get_xlim()
        cur_ylim = self.ax.get_ylim()
        step_x = (cur_xlim[1] - cur_xlim[0]) * 0.08
        step_y = (cur_ylim[1] - cur_ylim[0]) * 0.08

        if event.key == 'right':
            self.ax.set_xlim(cur_xlim[0] + step_x, cur_xlim[1] + step_x)
        elif event.key == 'left':
            self.ax.set_xlim(cur_xlim[0] - step_x, cur_xlim[1] - step_x)
        elif event.key == 'up':
            self.ax.set_ylim(cur_ylim[0] + step_y, cur_ylim[1] + step_y)
        elif event.key == 'down':
            self.ax.set_ylim(cur_ylim[0] - step_y, cur_ylim[1] - step_y)
        elif event.key in ['r', 'R']:
            self.reset_view()
        elif event.key in ['=', '+']:
            self._zoom_at_center(1 / self._zoom_factor)
        elif event.key in ['-', '_']:
            self._zoom_at_center(self._zoom_factor)
        self.canvas.draw_idle()

    def _zoom_at_center(self, scale_factor):
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        center_x = (xlim[0] + xlim[1]) / 2
        center_y = (ylim[0] + ylim[1]) / 2
        new_width = (xlim[1] - xlim[0]) * scale_factor
        new_height = (ylim[1] - ylim[0]) * scale_factor
        self.ax.set_xlim(center_x - new_width / 2, center_x + new_width / 2)
        self.ax.set_ylim(center_y - new_height / 2, center_y + new_height / 2)

    def set_initial_bounds(self, x_min, x_max, y_min, y_max):
        """Configura límites iniciales sin padding extra."""
        self.initial_xlim = (x_min, x_max)
        self.initial_ylim = (y_min, y_max)
        self.reset_view()

    def reset_view(self):
        if self.initial_xlim and self.initial_ylim:
            self.ax.set_xlim(self.initial_xlim)
            self.ax.set_ylim(self.initial_ylim)
            self._current_scale = 1.0
            self.canvas.draw_idle()

    def reset_interaction_state(self):
        self._is_panning = False
        self._pan_start_x = None
        self._pan_start_y = None
        self.canvas.setCursor(Qt.ArrowCursor)


class NodoInfoDialog(QDialog):
    """Muestra una tabla de información detallada para un nodo del grafo."""

    def __init__(self, datos_nodo: dict, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Información: {datos_nodo['Nombre del Tema']}")
        self.setFixedSize(550, 450)

        # Estilo de la tarjeta del diálogo
        self.setStyleSheet(f"""
            QDialog {{ background-color: {BG}; color: {FG}; border: 1px solid {CARD_BORDER}; border-radius: 10px; }}
            QLabel {{ background: transparent; color: {FG}; padding: 4px 0; }}
            .Titulo {{ font-size: 18px; font-weight: bold; color: {PRIMARY}; }}
            .Etiqueta {{ font-weight: bold; color: {MUTED}; }}
            .Valor {{ font-weight: normal; color: {FG}; }}
            .Alerta {{ color: #FCD34D; font-weight: bold; }}
            .Exito {{ color: #22C55E; font-weight: bold; }}
            .Fallo {{ color: #EF4444; font-weight: bold; }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        # Título
        lbl_titulo = QLabel(datos_nodo['Nombre del Tema'])
        lbl_titulo.setObjectName("Titulo")
        layout.addWidget(lbl_titulo)
        layout.addSpacing(10)

        # --- TABLA PRINCIPAL (Datos Generales) ---

        data_layout = QVBoxLayout()

        def add_data_row(key, value):
            h_layout = QHBoxLayout()
            h_layout.setSpacing(10)
            lbl_key = QLabel(key)
            lbl_key.setObjectName("Etiqueta")
            lbl_key.setFixedWidth(180)
            lbl_value = QLabel(value)
            lbl_value.setObjectName("Valor")
            h_layout.addWidget(lbl_key)
            h_layout.addWidget(lbl_value)
            h_layout.addStretch()
            data_layout.addLayout(h_layout)

        add_data_row("ID del Tema:", datos_nodo['ID del Tema'])
        add_data_row("Carrera:", datos_nodo['Carrera de Usuario'])
        add_data_row("Estado:", datos_nodo['Estado Actual'])
        add_data_row("Prerrequisitos:", datos_nodo['Prerrequisitos Cumplidos'])

        layout.addLayout(data_layout)
        layout.addSpacing(20)

        # --- Detalle de Prerrequisitos ---
        lbl_detalle = QLabel("Detalle de Prerrequisitos:")
        lbl_detalle.setObjectName("Etiqueta")
        layout.addWidget(lbl_detalle)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumHeight(150)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(5, 5, 5, 5)
        scroll_content.setStyleSheet(f"background-color: {CARD_BG}; border-radius: 8px;")

        for nombre, estado in datos_nodo['Detalle de Prerrequisitos']:
            h_layout = QHBoxLayout()

            # Formatear el estado con color
            if "Cumplido" in estado:
                color_class = "Exito"
            elif "Pendiente" in estado:
                color_class = "Fallo"
            else:
                color_class = "Valor"

            lbl_prereq_nombre = QLabel(nombre)
            lbl_prereq_nombre.setStyleSheet(f"color: {FG};")
            lbl_prereq_estado = QLabel(estado)
            lbl_prereq_estado.setObjectName(color_class)

            h_layout.addWidget(lbl_prereq_nombre)
            h_layout.addStretch()
            h_layout.addWidget(lbl_prereq_estado)
            scroll_layout.addLayout(h_layout)

        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)
        layout.addStretch()

        # Botón de cierre
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.setStyleSheet(f"background-color: {PRIMARY}; color: white; border-radius: 8px; padding: 8px;")
        btn_cerrar.clicked.connect(self.accept)
        layout.addWidget(btn_cerrar)


class VentanaRedNeuronal(QDialog):
    def __init__(self, modelo, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualización de la Red Neuronal MAHA")
        self.resize(900, 600)

        self.widget = InteractiveMatplotlibWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

        self.modelo = modelo
        self._dibujar_red()

    def _dibujar_red(self):
        # ✅ CORREGIDO: Usar self.widget.ax en lugar de crear nuevo eje
        ax = self.widget.ax
        ax.clear()

        coefs = self.modelo.coefs_

        G = nx.DiGraph()
        pos = {}
        layer_x = 0

        # Construcción de nodos y conexiones
        for i, capa in enumerate(coefs):
            num_inputs = capa.shape[0]
            num_outputs = capa.shape[1]

            # Nodos izquierda
            for n in range(num_inputs):
                nodo = f"L{i}_N{n}"
                if nodo not in G:
                    G.add_node(nodo)
                    pos[nodo] = (layer_x, -n)

            # Nodos derecha
            for n in range(num_outputs):
                nodo = f"L{i + 1}_N{n}"
                if nodo not in G:
                    G.add_node(nodo)
                    pos[nodo] = (layer_x + 1, -n)

            # Conexiones
            for a in range(num_inputs):
                for b in range(num_outputs):
                    w = capa[a, b]
                    G.add_edge(f"L{i}_N{a}", f"L{i + 1}_N{b}", weight=w)

            layer_x += 2

        edges = G.edges()
        weights = [abs(G[u][v]['weight']) * 3 for u, v in edges]

        nx.draw(
            G, pos,
            ax=ax,
            with_labels=False,
            node_size=550,
            node_color="#38bdf8",
            width=weights,
            arrows=False
        )

        ax.set_title("Red Neuronal MAHA (capas y pesos)")
        ax.axis("off")
        self.widget.canvas.draw()


class VentanaRedNeuronal(QDialog):
    def __init__(self, modelo, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Visualización de la Red Neuronal MAHA")
        self.resize(900, 600)

        self.widget = InteractiveMatplotlibWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.widget)

        self.modelo = modelo
        self._dibujar_red()

    def _dibujar_red(self):
        ax = self.widget.fig.add_subplot(111)
        ax.clear()

        coefs = self.modelo.coefs_

        G = nx.DiGraph()
        pos = {}
        layer_x = 0

        # Construcción de nodos y conexiones
        for i, capa in enumerate(coefs):
            num_inputs = capa.shape[0]
            num_outputs = capa.shape[1]

            # Nodos izquierda
            for n in range(num_inputs):
                nodo = f"L{i}_N{n}"
                if nodo not in G:
                    G.add_node(nodo)
                    pos[nodo] = (layer_x, -n)

            # Nodos derecha
            for n in range(num_outputs):
                nodo = f"L{i + 1}_N{n}"
                if nodo not in G:
                    G.add_node(nodo)
                    pos[nodo] = (layer_x + 1, -n)

            # Conexiones
            for a in range(num_inputs):
                for b in range(num_outputs):
                    w = capa[a, b]
                    G.add_edge(f"L{i}_N{a}", f"L{i + 1}_N{b}", weight=w)

            layer_x += 2

        edges = G.edges()
        weights = [abs(G[u][v]['weight']) * 3 for u, v in edges]

        nx.draw(
            G, pos,
            ax=ax,
            with_labels=False,
            node_size=550,
            node_color="#38bdf8",
            width=weights,
            arrows=False
        )

        ax.set_title("Red Neuronal MAHA (capas y pesos)")
        ax.axis("off")
        self.widget.canvas.draw()


def mostrar_red_neuronal_en_GUI(parent=None):
    """Abre un QDialog dentro de MAHA con la red neuronal dibujada."""
    if not os.path.exists(MODEL_PATH):
        QMessageBox.information(parent, "Red neuronal",
                                "Aún no hay modelo entrenado.\n\n"
                                "Responde algunos temas para que MAHA pueda aprender de ti.")
        return

    try:
        with open(MODEL_PATH, "rb") as f:
            paquete = pickle.load(f)
        modelo = paquete["modelo"]
    except Exception as e:
        QMessageBox.critical(parent, "Error IA",
                             f"No se pudo cargar el modelo de IA.\n\nDetalles: {e}")
        return

    dlg = VentanaRedNeuronal(modelo, parent)
    dlg.exec()


from PySide6.QtCore import QSettings


# Nuevo componente de diálogo para filtrar materias
# ARCHIVO: INTERFAZ.py (Agregar esta clase antes de GrafoView)

class FiltroGrafoDialog(QDialog):
    """Muestra una lista de materias para que el usuario filtre los nodos del grafo."""

    def __init__(self, materias_disponibles: List[str], materias_seleccionadas: List[str], parent=None):
        super().__init__(parent)
        self.setWindowTitle("Filtrar Materias del Mapa")
        self.resize(400, 500)
        # Usamos estilos inline para asegurar consistencia
        self.setStyleSheet(f"""
            QDialog {{ background-color: {BG}; color: {FG}; border: 1px solid {CARD_BORDER}; border-radius: 10px; }}
            QCheckBox {{ color: {FG}; padding: 5px; }}
            QCheckBox::indicator {{ width: 16px; height: 16px; border: 1px solid #64748b; border-radius: 4px; background-color: #1e293b; }}
            QCheckBox::indicator:checked {{ background-color: #38bdf8; border-color: #38bdf8; }}
            QPushButton {{ background-color: {PRIMARY}; color: white; border-radius: 8px; padding: 8px; }}
            QPushButton:hover {{ background-color: {PRIMARY_DARK}; }}
        """)

        layout = QVBoxLayout(self)
        self.checkboxes = []
        self._materias_seleccionadas = set(materias_seleccionadas)

        # Contenedor de Scroll para los checkboxes
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_content.setStyleSheet("background: transparent;")
        scroll_layout.setAlignment(Qt.AlignTop)

        # Crear Checkboxes para cada materia
        for materia in sorted(materias_disponibles):
            cb = QCheckBox(materia.title())
            cb.setProperty("materia_id", materia)
            cb.setChecked(materia in self._materias_seleccionadas)
            self.checkboxes.append(cb)
            scroll_layout.addWidget(cb)

        scroll_layout.addStretch()  # Empuja los checkboxes hacia arriba
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)

        # Botones de Acción
        btn_layout = QHBoxLayout()
        btn_aceptar = QPushButton("Aplicar Filtro")
        btn_aceptar.clicked.connect(self.accept)

        btn_cancelar = QPushButton("Cancelar")
        # Estilo específico para cancelar
        btn_cancelar.setStyleSheet(f"background-color: {MUTED}; color: white; border-radius: 8px; padding: 8px;")
        btn_cancelar.clicked.connect(self.reject)

        btn_layout.addWidget(btn_cancelar)
        btn_layout.addWidget(btn_aceptar)
        layout.addLayout(btn_layout)

    def get_selected_materias(self) -> List[str]:
        """Devuelve los IDs de las materias seleccionadas."""
        if self.result() == QDialog.Accepted:
            return [cb.property("materia_id") for cb in self.checkboxes if cb.isChecked()]
        return []


class GrafoView(QWidget):
    """Esta es la nueva 'pantalla' del mapa de competencias con interacción."""

    regresar = Signal()

    def __init__(self, usuario: Usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Variable de estado para el filtro
        self.materias_activas: List[str] = list(RUTAS_POR_MATERIA.keys())
        self.pos_nodos: Dict[str, Tuple[float, float]] = {}

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # --- Fila superior ---
        top_bar = QHBoxLayout()
        self.titulo = QLabel(f"Universo de Aprendizaje: {self.usuario.nombre}")
        self.titulo.setStyleSheet("font-size: 22px; font-weight: 900; color: #fcd34d; text-shadow: 1px 1px 2px #000;")

        btn_style = """
            QPushButton { background: #3b82f6; color: white; font-weight: bold; border-radius: 10px; padding: 8px 15px; border: 2px solid #1d4ed8; }
            QPushButton:hover { background: #60a5fa; border-color: #93c5fd; }
        """

        btn_filtro = QPushButton("⚙️ Filtrar Sistemas")
        btn_filtro.clicked.connect(self._mostrar_dialogo_filtro)
        btn_filtro.setStyleSheet(btn_style.replace("#3b82f6", "#f59e0b").replace("#1d4ed8", "#d97706"))

        btn_centrar = QPushButton("🔄 Centrar Vista")
        btn_centrar.clicked.connect(self._centrar_vista)
        btn_centrar.setStyleSheet(btn_style)

        btn_regresar = QPushButton("❌ Salir")
        btn_regresar.clicked.connect(self.regresar.emit)
        btn_regresar.setStyleSheet(btn_style.replace("#3b82f6", "#ef4444").replace("#1d4ed8", "#b91c1c"))

        top_bar.addWidget(self.titulo)
        top_bar.addStretch()
        top_bar.addWidget(btn_filtro)
        top_bar.addSpacing(10)
        top_bar.addWidget(btn_centrar)
        top_bar.addSpacing(10)
        top_bar.addWidget(btn_regresar)

        # --- Widget del Grafo ---
        self.widget_grafo = InteractiveMatplotlibWidget(self)
        self.widget_grafo.fig.patch.set_alpha(0.0)
        self.widget_grafo.setStyleSheet("background: transparent;")
        self.widget_grafo.canvas.mpl_connect('button_press_event', self._on_canvas_click)

        layout.addLayout(top_bar)
        layout.addWidget(self.widget_grafo, 1)

        QTimer.singleShot(50, self._dibujar_grafo_competencias)

    def _obtener_datos_del_nodo(self, tema_id: str) -> dict:
        progreso = self.usuario.progreso
        datos_tema = CONTENIDO_MAESTRO.get(tema_id, {})
        nombre_completo = NOMBRES_DE_TEMAS.get(tema_id, tema_id)
        prerequisitos_ids = datos_tema.get("prerequisitos", [])

        def is_completed(p_id):
            if p_id not in progreso: return False
            estado_str = progreso[p_id]
            return "dominado" in estado_str or "completado" in estado_str

        estado_base = "Bloqueado 🔒"
        if tema_id in progreso:
            if is_completed(tema_id):
                estado_base = "Dominado ✅"
            else:
                estado_base = "Pendiente ⚠️"
        else:
            if all(is_completed(pid) for pid in prerequisitos_ids): estado_base = "Disponible ➡️"

        prereq_info = []
        cumplidos = 0
        for pid in prerequisitos_ids:
            pnom = NOMBRES_DE_TEMAS.get(pid, pid)
            if is_completed(pid):
                prereq_info.append((pnom, "✅ Listo"));
                cumplidos += 1
            else:
                prereq_info.append((pnom, "❌ Falta"))

        if not prerequisitos_ids: prereq_info.append(("Ninguno", "N/A"))

        c = self.usuario.carrera
        carrera_disp = f"Ingeniería {'en ' if c == 'sistemas' else ''}{c.title()}"

        return {
            "Nombre del Tema": nombre_completo, "ID del Tema": tema_id, "Estado Actual": estado_base,
            "Carrera de Usuario": carrera_disp, "Prerrequisitos Cumplidos": f"{cumplidos}/{len(prerequisitos_ids)}",
            "Detalle de Prerrequisitos": prereq_info
        }

    @Slot()
    def _centrar_vista(self):
        if hasattr(self.widget_grafo, 'reset_view'):
            self.widget_grafo.reset_view()

    @Slot()
    def _mostrar_dialogo_filtro(self):
        all_mats = list(RUTAS_POR_MATERIA.keys())
        dlg = FiltroGrafoDialog(all_mats, self.materias_activas, self)
        if dlg.exec() == QDialog.Accepted:
            sel = dlg.get_selected_materias()
            if set(sel) != set(self.materias_activas):
                self.materias_activas = sel
                self._dibujar_grafo_competencias()

    def _dibujar_grafo_competencias(self):
        import matplotlib.patheffects as path_effects
        try:
            if not hasattr(self.widget_grafo, 'ax') or self.widget_grafo.ax is None:
                self.widget_grafo.ax = self.widget_grafo.fig.add_subplot(111)

            ax = self.widget_grafo.ax
            ax.clear()
            ax.set_xticks([]);
            ax.set_yticks([]);
            ax.set_frame_on(False)
            ax.patch.set_alpha(0.0)

            G = nx.DiGraph()
            import math

            # Mapeos
            mapa_id_nombre = obtener_mapeo_id_nombre()
            mapa_nombre_id = obtener_mapeo_nombre_id()

            # 1. Agrupar por Sistemas (Mundos)
            mundos = {}
            for materia in self.materias_activas:
                temas = RUTAS_POR_MATERIA.get(materia.upper(), [])
                nodos_mundo = []
                for tid in temas:
                    if tid in mapa_id_nombre:
                        nombre = mapa_id_nombre[tid]
                        nodos_mundo.append(nombre)
                        G.add_node(nombre, tipo="planeta")

                if nodos_mundo:
                    mundos[materia] = nodos_mundo
                    G.add_node(materia, tipo="sol")

            # 2. Crear Conexiones
            G_reqs = crear_grafo_simple()

            edges_pertenencia = []
            for materia, temas in mundos.items():
                for tema in temas:
                    edges_pertenencia.append((materia, tema))

            edges_requisito = []
            for u, v in G_reqs.edges():
                if u in G.nodes() and v in G.nodes():
                    edges_requisito.append((u, v))

            if not G.nodes():
                ax.text(0.5, 0.5, "Selecciona un Sistema.", transform=ax.transAxes, ha='center', color='white')
                self.widget_grafo.canvas.draw();
                return

            # 3. POSICIONAMIENTO
            pos = {}
            num_mundos = len(mundos)
            radio_universo = 45 if num_mundos > 1 else 0
            lista_mundos = sorted(mundos.keys())

            for i, nombre_materia in enumerate(lista_mundos):
                lista_nodos = mundos[nombre_materia]

                ang_mundo = (2 * math.pi * i) / max(1, num_mundos)
                cx = radio_universo * math.cos(ang_mundo)
                cy = radio_universo * math.sin(ang_mundo)
                pos[nombre_materia] = (cx, cy)

                num_nodos = len(lista_nodos)
                radio_orbita = 12  # 🔥 CAMBIO: Definimos la variable aquí

                angulo_inicio = math.pi / 2

                for j, nodo in enumerate(lista_nodos):
                    ang_nodo = angulo_inicio - (2 * math.pi * j) / max(1, num_nodos)
                    nx_pos = cx + radio_orbita * math.cos(ang_nodo)
                    # 🔥 CAMBIO: Usamos radio_orbita en ambos ejes
                    ny_pos = cy + radio_orbita * math.sin(ang_nodo)
                    pos[nodo] = (nx_pos, ny_pos)

            self.pos_nodos = pos

            # 4. DIBUJAR ARISTAS
            nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges_pertenencia,
                                   edge_color='#475569', width=1, style='dotted', alpha=0.4, arrows=False)

            req_int = []
            req_ext = []
            nodo_a_materia = {}
            for m, ts in mundos.items():
                for t in ts: nodo_a_materia[t] = m

            for u, v in edges_requisito:
                if nodo_a_materia.get(u) == nodo_a_materia.get(v):
                    req_int.append((u, v))
                else:
                    req_ext.append((u, v))

            nx.draw_networkx_edges(G, pos, ax=ax, edgelist=req_int,
                                   edge_color='#94a3b8', width=2, arrowsize=15,
                                   connectionstyle="arc3,rad=0.15", alpha=0.8)

            nx.draw_networkx_edges(G, pos, ax=ax, edgelist=req_ext,
                                   edge_color='#64748b', width=1, arrowsize=10,
                                   style='dashed', connectionstyle="arc3,rad=0.3", alpha=0.15)

            # 5. DIBUJAR NODOS
            nodos_sol = [n for n, d in G.nodes(data=True) if d.get("tipo") == "sol"]

            for sol in nodos_sol:
                x, y = pos[sol]
                ax.text(x, y, sol.title(), fontsize=14, fontweight='bold', color='#fcd34d',
                        ha='center', va='center',
                        bbox=dict(facecolor='#1e293b', edgecolor='#f59e0b', boxstyle='circle,pad=0.8', linewidth=2),
                        zorder=5)

            nodos_planeta = [n for n, d in G.nodes(data=True) if d.get("tipo") == "planeta"]
            colores = []
            bordes = []
            etiquetas = {}

            progreso = self.usuario.progreso
            temas_disp = set(generar_temas_disponibles(progreso))
            temas_dom = set(progreso.keys())

            for nodo in nodos_planeta:
                tid = mapa_nombre_id.get(nodo)
                lbl = nodo

                if tid in temas_dom:
                    if "pendiente" in progreso.get(tid, ""):
                        colores.append('#fbbf24');
                        bordes.append('#b45309');
                        lbl = f"!\n{nodo}"
                    else:
                        colores.append('#4ade80');
                        bordes.append('#15803d');
                        lbl = f"⭐\n{nodo}"
                elif tid in temas_disp:
                    colores.append('#60a5fa');
                    bordes.append('#1e40af');
                    lbl = f"▶️\n{nodo}"
                else:
                    colores.append('#9ca3af');
                    bordes.append('#4b5563');
                    lbl = f"🔒\n{nodo}"
                etiquetas[nodo] = lbl

            nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=nodos_planeta, node_color=colores,
                                   node_size=2800, node_shape='o', edgecolors=bordes, linewidths=3.5)

            textos = nx.draw_networkx_labels(G, pos, labels=etiquetas, font_size=8, font_weight='bold',
                                             font_color='white', font_family="Segoe UI Emoji", ax=ax)
            for t in textos.values():
                t.set_path_effects([path_effects.withStroke(linewidth=3, foreground='black')])
                t.set_zorder(10)

            x_vals = [p[0] for p in pos.values()]
            y_vals = [p[1] for p in pos.values()]
            if x_vals:
                margin = 15
                self.widget_grafo.set_initial_bounds(min(x_vals) - margin, max(x_vals) + margin, min(y_vals) - margin,
                                                     max(y_vals) + margin)

            self.widget_grafo.canvas.draw()

        except Exception as e:
            print(f"Error dibujando: {e}")
            import traceback;
            traceback.print_exc()

    def _on_canvas_click(self, event):
        if event.inaxes != self.widget_grafo.ax or event.button != 1: return
        if not self.pos_nodos: return

        cx, cy = event.x, event.y
        HIT_RADIUS = 30

        hit_node = None
        min_dist = float('inf')
        trans = self.widget_grafo.ax.transData

        for name, (nx, ny) in self.pos_nodos.items():
            # Solo detectar clics en temas
            if name in obtener_mapeo_nombre_id():
                px, py = trans.transform((nx, ny))
                dist = ((cx - px) ** 2 + (cy - py) ** 2) ** 0.5
                if dist < HIT_RADIUS and dist < min_dist:
                    min_dist = dist
                    hit_node = name

        if hit_node:
            mid = obtener_mapeo_nombre_id().get(hit_node)
            if mid:
                datos = self._obtener_datos_del_nodo(mid)
                NodoInfoDialog(datos, self).exec()
                if hasattr(self.widget_grafo, 'reset_interaction_state'):
                    self.widget_grafo.reset_interaction_state()


class Bubble(QFrame):
    def __init__(self, text: str, is_user: bool, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.NoFrame)

        # 🔹 FORZAR que el bubble se redibuje
        self.setAttribute(Qt.WA_StyledBackground, True)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 2, 0, 2)
        layout.setSpacing(0)

        label = QLabel(text)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        label.setAlignment(Qt.AlignLeft if not is_user else Qt.AlignRight)
        label.setObjectName("BubbleUser" if is_user else "BubbleBot")

        # 🔹 MEJOR CONTROL de tamaño
        label.setMaximumWidth(550)
        label.setMinimumWidth(200)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        if is_user:
            layout.addStretch(1)
            layout.addWidget(label, 0, Qt.AlignRight)
        else:
            layout.addWidget(label, 0, Qt.AlignLeft)
            layout.addStretch(1)

        # 🔹 FORZAR actualización del bubble
        self.update()
        self.repaint()


class WelcomeView(QWidget):
    startRegister = Signal()
    startLogin = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # --- 1. CONFIGURACIÓN DEL FONDO ---
        self.setStyleSheet("""
            WelcomeView {
                
                    stop:0 #0b1120, stop:0.4 #0d172a, stop:1 #1e293b);
            }
           
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)

        # --- 2. TARJETA CENTRAL ---
        self.card = QFrame()
        self.card.setObjectName("Card")
        self.card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(20)
        card_layout.setAlignment(Qt.AlignCenter)

        # Títulos
        title = QLabel("Bienvenido a <span style='color:#38bdf8'>MAHA</span>")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "font-size: 36px; font-weight: 900; color: white; text-shadow: 0px 0px 10px rgba(14,165,233,0.5);")

        subtitle = QLabel("Tu asistente de aprendizaje para Ingeniería")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 16px; color: #94a3b8; font-weight: 500; letter-spacing: 0.5px;")

        # --- 3. ÁREA DE TEXTO ---
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # -------------------------------------------------------------

        self.scroll_area.setStyleSheet("background: transparent; border: none;")

        self.text_container = QWidget()
        self.text_container.setStyleSheet("background: transparent;")
        text_layout = QVBoxLayout(self.text_container)
        text_layout.setContentsMargins(0, 0, 0, 0)
        text_layout.setAlignment(Qt.AlignCenter)

        self.lbl_message = QLabel("")
        self.lbl_message.setWordWrap(True)
        self.lbl_message.setAlignment(Qt.AlignCenter)
        self.lbl_message.setTextFormat(Qt.RichText)
        self.lbl_message.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        self.lbl_message.setStyleSheet("""
            QLabel {
                font-size: 18px;
                line-height: 1.6em;
                color: #f1f5f9;
                background: qlineargradient(stop:0 #1e40af, stop:1 #2563eb);
                border-radius: 20px;
                padding: 30px;
                border: 1px solid rgba(255,255,255,0.1);
            }
        """)

        self.lbl_message.setMaximumWidth(900)
        self.lbl_message.setMinimumWidth(300)

        text_layout.addWidget(self.lbl_message)
        self.scroll_area.setWidget(self.text_container)

        # --- 4. BOTONES (CORREGIDOS) ---
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(20)
        buttons_layout.setAlignment(Qt.AlignCenter)

        btn_reg = QPushButton("Registrarme")
        btn_login = QPushButton("Iniciar sesión")

        # Definimos las propiedades comunes (sin cerrar la llave } todavía)
        props_comunes = """
            font-size: 16px; 
            font-weight: bold; 
            border-radius: 12px; 
            padding: 12px 30px; 
            min-width: 180px;
            color: white;
        """

        # 🔥 APLICAMOS EL ESTILO COMPLETO A CADA UNO POR SEPARADO 🔥
        # Botón Registro (AZUL)
        btn_reg.setStyleSheet(f"""
            QPushButton {{
                {props_comunes}
                background-color: #0ea5e9;
            }}
            QPushButton:hover {{ background-color: #0284c7; }}
        """)

        # Botón Login (VERDE CLARO)
        btn_login.setStyleSheet(f"""
            QPushButton {{
                {props_comunes}
                background-color: #2ecc71; 
            }}
            QPushButton:hover {{ background-color: #27ae60; }}
        """)

        btn_reg.setCursor(Qt.PointingHandCursor)
        btn_login.setCursor(Qt.PointingHandCursor)

        btn_reg.clicked.connect(self.startRegister.emit)
        btn_login.clicked.connect(self.startLogin.emit)

        buttons_layout.addWidget(btn_reg)
        buttons_layout.addWidget(btn_login)

        # --- 5. ENSAMBLAJE ---
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(15)
        card_layout.addWidget(self.scroll_area, 1)


        card_layout.addLayout(buttons_layout)

        main_layout.addWidget(self.card, 10)

        # --- 6. IMAGEN ---
        from PySide6.QtGui import QPixmap
        self.img_footer = QLabel()
        self.img_footer.setAlignment(Qt.AlignCenter)
        self.img_footer.setStyleSheet("background: transparent; margin-top: -5px;")
        self.img_footer.setFixedHeight(90)

        self.pix_guacamaya = QPixmap("guacamaya.png")
        if not self.pix_guacamaya.isNull():
            self.img_footer.setPixmap(self.pix_guacamaya.scaledToHeight(80, Qt.SmoothTransformation))

        main_layout.addWidget(self.img_footer, 0)

        self._init_typewriter()

    def _init_typewriter(self):
        self._lines = _capture_welcome_lines()
        self._line_index = 0
        self._full_html_accumulated = ""
        self._current_paragraph_html = ""
        self._char_index = 0

        self._line_timer = QTimer(self)
        self._line_timer.setInterval(800)
        self._line_timer.timeout.connect(self._prepare_next_line)
        self._line_timer.start()

        self._char_timer = QTimer(self)
        self._char_timer.setInterval(15)
        self._char_timer.timeout.connect(self._type_next_char)

    def _prepare_next_line(self):
        if self._line_index >= len(self._lines):
            self._line_timer.stop()
            return

        raw_line = self._lines[self._line_index].strip()

        for kw in ["MAHA", "Ingeniería", "progreso", "diagnóstico", "materias"]:
            raw_line = raw_line.replace(kw, f"<b>{kw}</b>")

        prefix = "<br><br>" if self._full_html_accumulated else ""
        self._current_paragraph_html = prefix + raw_line
        self._char_index = 0

        self._line_timer.stop()
        self._char_timer.start()
        self._line_index += 1

    def _type_next_char(self):
        if self._char_index >= len(self._current_paragraph_html):
            self._char_timer.stop()
            self._full_html_accumulated += self._current_paragraph_html
            self._line_timer.start()
            return

        if self._current_paragraph_html[self._char_index] == '<':
            end_tag = self._current_paragraph_html.find('>', self._char_index)
            if end_tag != -1:
                self._char_index = end_tag + 1
            else:
                self._char_index += 1
        elif self._current_paragraph_html[self._char_index] == '&':
            end_entity = self._current_paragraph_html.find(';', self._char_index)
            if end_entity != -1:
                self._char_index = end_entity + 1
            else:
                self._char_index += 1
        else:
            self._char_index += 1

        current_visible = self._full_html_accumulated + self._current_paragraph_html[:self._char_index]
        self.lbl_message.setText(current_visible)

        QTimer.singleShot(10, lambda: self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        ))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'pix_guacamaya') and not self.pix_guacamaya.isNull():
            self.img_footer.setPixmap(
                self.pix_guacamaya.scaledToHeight(80, Qt.SmoothTransformation)
            )


import time  # 🔥 AGREGAR ESTE IMPORT
import os


class PhotoEditorWidget(QWidget):
    """Adaptación del PhotoEditor original para ser usado como un QWidget interno."""
    photo_accepted = Signal(str)
    canceled = Signal()

    def __init__(self, photo_path: str, parent=None):
        super().__init__(parent)
        self.original_photo_path = photo_path
        self.zoom_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.base_size = 300

        # Copiar estilos del PhotoEditor original aquí (usar los estilos de tu archivo)
        self.setStyleSheet(f"""
            PhotoEditorWidget {{ background: #0b1120; }}
            QLabel {{ color: #e2e8f0; background: transparent; }}
            QPushButton {{ background-color: #0ea5e9; color: white; border: none; border-radius: 8px; padding: 10px 16px; font-weight: 600; font-size: 14px; }}
            QPushButton:hover {{ background-color: #38bdf8; }}
            QPushButton#CancelButton {{ background-color: #334155; color: #e2e8f0; }}
            QPushButton#CancelButton:hover {{ background-color: #475569; }}
            QSlider::groove:horizontal {{ background: #334155; height: 6px; border-radius: 3px; }}
            QSlider::handle:horizontal {{ background: #0ea5e9; width: 16px; height: 16px; border-radius: 8px; margin: -5px 0; }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Título
        title = QLabel("Ajusta tu foto de perfil")
        title.setStyleSheet("font-size: 20px; font-weight: 700; color: #f8fafc;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Instrucciones
        instructions = QLabel("Mueve y haz zoom para ajustar la foto dentro del círculo")
        instructions.setStyleSheet("color: #94a3b8; font-size: 14px;")
        instructions.setAlignment(Qt.AlignCenter)
        layout.addWidget(instructions)

        # Área de preview
        preview_container = QWidget()
        preview_layout = QVBoxLayout(preview_container)
        preview_layout.setAlignment(Qt.AlignCenter)

        self.preview_frame = QFrame()
        self.preview_frame.setFixedSize(self.base_size, self.base_size)
        self.preview_frame.setStyleSheet(f"""
            QFrame {{
                background: qradialgradient(cx:0.5, cy:0.5, radius:0.8,
                    stop:0 #38bdf8, stop:1 #0ea5e9);
                border-radius: {self.base_size // 2}px;
            }}
        """)

        frame_layout = QVBoxLayout(self.preview_frame)
        frame_layout.setContentsMargins(10, 10, 10, 10)
        frame_layout.setAlignment(Qt.AlignCenter)

        self.preview_label = QLabel()
        self.preview_label.setFixedSize(self.base_size - 20, self.base_size - 20)
        self.preview_label.setStyleSheet(f"""
            QLabel {{
                background-color: #1e293b;
                border-radius: {(self.base_size - 20) // 2}px;
            }}
        """)
        self.preview_label.setAlignment(Qt.AlignCenter)

        frame_layout.addWidget(self.preview_label)
        preview_layout.addWidget(self.preview_frame)
        layout.addWidget(preview_container)

        # Controles de zoom
        zoom_layout = QHBoxLayout()
        zoom_layout.addWidget(QLabel("🔍 Zoom:"))

        self.zoom_slider = QSlider(Qt.Horizontal)
        self.zoom_slider.setRange(50, 200)
        self.zoom_slider.setValue(100)
        self.zoom_slider.valueChanged.connect(self._on_zoom_changed)
        zoom_layout.addWidget(self.zoom_slider)

        self.zoom_label = QLabel("100%")
        self.zoom_label.setStyleSheet("color: #38bdf8; font-weight: 600; min-width: 50px;")
        zoom_layout.addWidget(self.zoom_label)

        layout.addLayout(zoom_layout)

        # Instrucciones de arrastre
        drag_info = QLabel("💡 Arrastra la imagen para ajustar la posición")
        drag_info.setStyleSheet("color: #64748b; font-size: 13px; font-style: italic;")
        drag_info.setAlignment(Qt.AlignCenter)
        layout.addWidget(drag_info)

        # Botones
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)

        btn_cancel = QPushButton("Cancelar")
        btn_cancel.setObjectName("CancelButton")
        btn_cancel.clicked.connect(self.canceled.emit)  # Emitir signal

        btn_accept = QPushButton("✅ Usar esta foto")
        btn_accept.clicked.connect(self._accept_photo)

        button_layout.addWidget(btn_cancel)
        button_layout.addWidget(btn_accept)
        layout.addLayout(button_layout)

        # Cargar imagen original
        self.original_pixmap = QPixmap(photo_path)
        self._update_preview()

        # Configurar arrastre
        self.preview_label.setMouseTracking(True)
        self.preview_label.mousePressEvent = self._on_mouse_press
        self.preview_label.mouseMoveEvent = self._on_mouse_move
        self.preview_label.mouseReleaseEvent = self._on_mouse_release

        self.is_dragging = False
        self.last_mouse_pos = None

    # Implementar los métodos de interacción del PhotoEditor (copiar la lógica del original)
    def _on_zoom_changed(self, value):
        self.zoom_factor = value / 100.0
        self.zoom_label.setText(f"{value}%")
        self._update_preview()

    def _on_mouse_press(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.last_mouse_pos = event.position().toPoint()

    def _on_mouse_move(self, event):
        if self.is_dragging and self.last_mouse_pos:
            current_pos = event.position().toPoint()
            delta_x = current_pos.x() - self.last_mouse_pos.x()
            delta_y = current_pos.y() - self.last_mouse_pos.y()

            self.offset_x += delta_x
            self.offset_y += delta_y

            self.last_mouse_pos = current_pos
            self._update_preview()

    def _on_mouse_release(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            self.last_mouse_pos = None

    def _update_preview(self):
        if self.original_pixmap.isNull():
            return

        size = self.base_size - 20
        circular_pixmap = QPixmap(size, size)
        circular_pixmap.fill(Qt.transparent)

        painter = QPainter(circular_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)

        scaled_size = int(size * self.zoom_factor)
        scaled_pixmap = self.original_pixmap.scaled(
            scaled_size, scaled_size,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        x_pos = (size - scaled_pixmap.width()) // 2 + self.offset_x
        y_pos = (size - scaled_pixmap.height()) // 2 + self.offset_y

        painter.drawPixmap(x_pos, y_pos, scaled_pixmap)
        painter.end()

        self.preview_label.setPixmap(circular_pixmap)

    def _accept_photo(self):
        """Guarda la foto ajustada y emite la señal."""
        try:
            temp_dir = os.path.join(os.path.expanduser("~"), ".maha_temp")
            os.makedirs(temp_dir, exist_ok=True)
            temp_path = os.path.join(temp_dir, f"profile_edit_{int(time.time())}.png")

            size = 300
            final_pixmap = QPixmap(size, size)
            final_pixmap.fill(Qt.transparent)

            painter = QPainter(final_pixmap)
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)

            scaled_size = int(size * self.zoom_factor)
            scaled_pixmap = self.original_pixmap.scaled(
                scaled_size, scaled_size,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )

            scale_ratio = size / (self.base_size - 20)
            final_offset_x = int(self.offset_x * scale_ratio)
            final_offset_y = int(self.offset_y * scale_ratio)

            x_pos = (size - scaled_pixmap.width()) // 2 + final_offset_x
            y_pos = (size - scaled_pixmap.height()) // 2 + final_offset_y

            painter.drawPixmap(x_pos, y_pos, scaled_pixmap)
            painter.end()

            final_pixmap.save(temp_path, "PNG")
            self.photo_accepted.emit(temp_path)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo guardar la foto: {str(e)}")


# ARCHIVO: INTERFAZ.py (Reemplazar la clase AuthInline completa)

class AuthInline(QWidget):
    """Panel de registro/inicio de sesión dentro de la misma ventana (sin diálogos)."""
    accepted = Signal(Usuario)
    canceled = Signal()

    # ------------------- MÉTODOS AUXILIARES (INTACTOS) -------------------

    def _create_separator(self):
        """Crea un separador horizontal sutil."""
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)
        sep.setStyleSheet("background-color: #334155; max-height: 1px; border: none;")
        sep.setMaximumWidth(600)
        return sep

    @Slot()
    def _seleccionar_foto(self):
        """Abre diálogo para foto y muestra el editor estilo WhatsApp"""
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar foto",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if ruta:
            self._procesar_foto_seleccionada(ruta)

    def _procesar_foto_seleccionada(self, ruta):
        """Procesa la foto seleccionada mostrando el editor en el mismo panel."""
        try:
            if not os.path.exists(ruta):
                QMessageBox.warning(self, "Error", "El archivo no existe.")
                return

            if hasattr(self, 'editor_view'):
                self.stacked_views.removeWidget(self.editor_view)
                self.editor_view.deleteLater()

            self.editor_view = PhotoEditorWidget(ruta, self)
            self.editor_view.photo_accepted.connect(self._on_photo_edited)
            self.editor_view.canceled.connect(self._back_to_form)

            self.stacked_views.addWidget(self.editor_view)
            self.stacked_views.setCurrentWidget(self.editor_view)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo cargar la imagen: {str(e)}")

    def _back_to_form(self):
        """Regresa a la vista del formulario."""
        self.stacked_views.setCurrentWidget(self.form_view)

    def _on_photo_edited(self, edited_photo_path):
        """Callback cuando se acepta la foto editada"""
        try:
            if not os.path.exists(edited_photo_path):
                QMessageBox.warning(self, "Error", "La foto editada no se pudo guardar.")
                return

            self.foto_path = edited_photo_path

            pixmap = QPixmap(edited_photo_path)
            if pixmap.isNull():
                QMessageBox.warning(self, "Error", "No se pudo cargar la foto editada.")
                return

            size = 110
            circular = QPixmap(size, size)
            circular.fill(Qt.transparent)

            painter = QPainter(circular)
            painter.setRenderHint(QPainter.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, size, size)
            painter.setClipPath(path)

            scaled_pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            x_offset = (scaled_pixmap.width() - size) // 2
            y_offset = (scaled_pixmap.height() - size) // 2
            painter.drawPixmap(0, 0, scaled_pixmap, x_offset, y_offset, size, size)
            painter.end()

            self.lbl_foto.setPixmap(circular)
            self.lbl_foto.setStyleSheet("border: 2px solid #38bdf8; border-radius: 55px; background-color: #1e293b;")
            self.btn_foto_texto.setText("Cambiar foto")

            self._back_to_form()

        except Exception as e:
            QMessageBox.warning(self, "Error", f"No se pudo mostrar la foto: {str(e)}")

    def _seleccionar_perfil(self, nombre):
        self.nombre_seleccionado = nombre
        for n, w in getattr(self, "_cards", {}).items():
            w.setProperty("selected", n == nombre)
            w.style().unpolish(w)
            w.style().polish(w)
        self.btn_ok.setEnabled(True)
        self.btn_ok.setStyleSheet("""
            QPushButton {
                background-color: #10b981; 
                color: white;
                border-radius: 8px;
                padding: 12px 30px;
                font-weight: 600;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #059669;
            }
        """)
        self.btn_ok.setCursor(Qt.PointingHandCursor)

    def _recalcular_layout(self):
        self.adjustSize()
        self.updateGeometry()
        if self.parent():
            self.parent().adjustSize()

    # ------------------- INIT y BUILD FORM -------------------

    def __init__(self, modo: str = "registro", parent=None):
        super().__init__(parent)
        self._modo = modo
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.foto_path = None  # Inicializar variable

        self.setStyleSheet("""
            AuthInline {
               
                    stop:0 #0b1120, stop:0.4 #0d172a, stop:1 #1e293b);
            }
            QLabel { color: #e2e8f0; font-size: 15px; background: transparent; }
            QLineEdit, QComboBox {
                background-color: #1e293b; 
                border: 1px solid #475569; 
                border-radius: 10px;
                padding: 12px;
                color: white;
                font-size: 15px;
                min-width: 300px;
                margin-bottom: 5px;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #38bdf8;
                background-color: #1e293b;
            }
            QComboBox::drop-down { border: none; }
            QComboBox::down-arrow { 
                image: none; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 6px solid #94a3b8; margin-right: 12px; 
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        self.stacked_views = QStackedWidget()
        layout.addWidget(self.stacked_views)

        self.form_view = self._build_form_view(modo)
        self.stacked_views.addWidget(self.form_view)
        self.stacked_views.setCurrentWidget(self.form_view)

        QTimer.singleShot(0, self._recalcular_layout)

    def _build_form_view(self, modo: str) -> QWidget:
        """Contiene la lógica original con la adición del Modo Admin."""

        form_widget = QWidget()
        form_widget.setStyleSheet("background: transparent;")

        # --- TARJETA CONTENEDORA ---
        card = QFrame()
        card.setObjectName("AuthCard")
        card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 🔥 AJUSTE DE ESPACIO: Aumentar altura mínima para que quepa el nuevo botón
        if modo == "registro":
            card.setMinimumHeight(650)

        card.setStyleSheet("""
            QFrame#AuthCard {
                background-color: rgba(30, 41, 59, 0.7); 
                border: 1px solid #334155;
                border-radius: 20px;
            }
        """)

        cv = QVBoxLayout(card)
        cv.setContentsMargins(40, 40, 40, 40)
        cv.setSpacing(25)  # Espacio general
        cv.setAlignment(Qt.AlignCenter)

        # --- ENCABEZADO (INTACTO) ---
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)
        header_layout.setAlignment(Qt.AlignCenter)

        lbl_icon = QLabel("📝" if modo == "registro" else "🚀")
        lbl_icon.setStyleSheet("font-size: 48px; margin-bottom: 15px; background: transparent; border: none;")
        lbl_icon.setAlignment(Qt.AlignCenter)

        title = QLabel("Crear Perfil" if modo == "registro" else "Bienvenido de nuevo")
        title.setStyleSheet("font-size: 20px; font-weight: 800; color: #f8fafc; background: transparent; border: none;")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel(
            "Configura tu experiencia MAHA" if modo == "registro" else "Selecciona tu perfil para continuar")
        subtitle.setStyleSheet("font-size: 16px; color: #94a3b8; background: transparent; border: none;")
        subtitle.setAlignment(Qt.AlignCenter)

        header_layout.addWidget(lbl_icon)
        header_layout.addWidget(title)
        header_layout.addWidget(subtitle)
        cv.addLayout(header_layout)

        sep = self._create_separator()
        sep.setFixedWidth(400)
        cv.addWidget(sep, 0, Qt.AlignCenter)

        cv.addSpacing(10)

        # --- CONTENIDO DINÁMICO ---
        content_container = QWidget()
        content_container.setStyleSheet("background: transparent;")
        content_container.setFixedWidth(600)
        content_layout = QVBoxLayout(content_container)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(15)

        if modo == "registro":
            # 1. Foto (INTACTO)
            foto_layout = QHBoxLayout()
            foto_layout.setAlignment(Qt.AlignCenter)

            self.lbl_foto = QLabel()
            self.lbl_foto.setFixedSize(110, 110)
            self.lbl_foto.setAlignment(Qt.AlignCenter)
            self.lbl_foto.setText("👤")
            self.lbl_foto.setStyleSheet("""
                background-color: #1e293b; 
                border: 2px dashed #475569;
                border-radius: 55px;
                color: #64748b;
                font-size: 40px;
            """)
            self.lbl_foto.setCursor(Qt.ArrowCursor)
            self.lbl_foto.mousePressEvent = lambda event: None

            btn_upload_container = QVBoxLayout()
            btn_upload_container.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

            self.btn_foto_texto = QPushButton("Agregar foto (Opcional)")
            self.btn_foto_texto.setCursor(Qt.PointingHandCursor)
            self.btn_foto_texto.setStyleSheet("""
                QPushButton {
                    background-color: #38bdf8;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 8px 15px;
                    font-weight: 600;
                    font-size: 14px;
                    min-width: 160px;
                    max-width: 200px;
                    text-align: center;
                }
                QPushButton:hover { 
                    background-color: #0ea5e9; 
                }
            """)
            self.btn_foto_texto.clicked.connect(self._seleccionar_foto)

            btn_upload_container.addWidget(self.btn_foto_texto)

            foto_layout.addWidget(self.lbl_foto)
            foto_layout.addSpacing(20)
            foto_layout.addLayout(btn_upload_container)

            content_layout.addLayout(foto_layout)
            content_layout.addSpacing(10)

            # 2. Inputs (INTACTO)
            self.nombre = QLineEdit()
            self.nombre.setPlaceholderText("Tu nombre completo")

            self.carrera = QComboBox()
            self.carrera.addItems([
                "Ingeniería en Cibernética y Sistemas Computacionales",
                "Ingeniería Mecánica",
                "Ingeniería Eléctrica",
                "Ingeniería Civil",
                "Ingeniería Mecatrónica",
                "Ingeniería Aeronáutica",
                "Ingeniería Química"
            ])

            lbl_nom = QLabel("Nombre")
            lbl_nom.setStyleSheet(
                "color: #cbd5e1; font-weight: 600; margin-bottom: 4px; background: transparent; border: none;")
            lbl_car = QLabel("Carrera")
            lbl_car.setStyleSheet(
                "color: #cbd5e1; font-weight: 600; margin-bottom: 4px; background: transparent; border: none;")

            content_layout.addWidget(lbl_nom)
            content_layout.addWidget(self.nombre)
            content_layout.addWidget(lbl_car)
            content_layout.addWidget(self.carrera)

            self.lbl_advertencia = QLabel("⚠️ Ingresa tu nombre para continuar")
            self.lbl_advertencia.setStyleSheet(
                "color: #ef4444; font-size: 13px; background: transparent; border: none; margin-top: 5px;")
            self.lbl_advertencia.hide()
            content_layout.addWidget(self.lbl_advertencia)

            self.foto_path = None

            # 🔥🔥🔥 AGREGADO SOLO ESTO: TOGGLE MODO ADMIN 🔥🔥🔥
            content_layout.addSpacing(15)  # Espacio extra para que no se vea amontonado

            self.admin_toggle = QCheckBox("Activar MODO ADMINISTRADOR")
            self.admin_toggle.setStyleSheet("""
                QCheckBox { color: #f8fafc; font-weight: 600; spacing: 10px; }
                QCheckBox::indicator { width: 18px; height: 18px; border: 1px solid #64748b; border-radius: 4px; background-color: #1e293b; }
                QCheckBox::indicator:checked { background-color: #38bdf8; border-color: #38bdf8; }
            """)

            content_layout.addWidget(self.admin_toggle)

            # -----------------------------------------------------

        else:  # MODO INICIO (LOGIN) - INTACTO
            perfiles = obtener_lista_perfiles()

            if not perfiles:
                empty_state = QLabel("No se encontraron perfiles.\nRegresa para crear uno nuevo.")
                empty_state.setAlignment(Qt.AlignCenter)
                empty_state.setStyleSheet(
                    "color: #64748b; font-size: 16px; padding: 30px; background: transparent; border: none;")
                content_layout.addWidget(empty_state)
            else:
                scroll = QScrollArea()
                scroll.setWidgetResizable(True)
                scroll.setMinimumHeight(300)
                scroll.setStyleSheet("""
                    QScrollArea { border: none; background: transparent; }
                    QScrollBar:vertical { background: #0f172a; width: 8px; border-radius: 4px; margin: 0px; }
                    QScrollBar::handle:vertical { background: #334155; border-radius: 4px; }
                    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }
                """)

                container = QWidget()
                container.setStyleSheet("background: transparent;")
                self.grid = QVBoxLayout(container)
                self.grid.setSpacing(12)
                self.grid.setContentsMargins(5, 0, 10, 0)

                self._cards = {}

                for nombre in perfiles:
                    datos = cargar_perfil(nombre)

                    btn_card = QFrame()
                    btn_card.setObjectName("CardPerfil")
                    btn_card.setCursor(Qt.PointingHandCursor)
                    btn_card.setProperty("selected", False)

                    btn_card.setStyleSheet("""
                        QFrame#CardPerfil {
                            background-color: #1e293b; 
                            border: 1px solid #475569;
                            border-radius: 14px;
                        }
                        QFrame#CardPerfil:hover {
                            border: 1px solid #94a3b8;
                            background-color: #253346;
                        }
                        QFrame#CardPerfil[selected="true"] {
                            background-color: #172554;
                            border: 1px solid #38bdf8;
                        }
                    """)

                    h_layout = QHBoxLayout(btn_card)
                    h_layout.setContentsMargins(15, 15, 15, 15)
                    h_layout.setSpacing(20)

                    lbl_avatar = QLabel("👤")
                    lbl_avatar.setFixedSize(48, 48)
                    lbl_avatar.setAlignment(Qt.AlignCenter)
                    lbl_avatar.setStyleSheet("background: #334155; border-radius: 24px; font-size: 24px; border: none;")

                    foto = datos.get("foto")
                    if foto:
                        pix = QPixmap(foto).scaled(48, 48, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
                        from PySide6.QtGui import QPainter, QPainterPath
                        circ = QPixmap(48, 48)
                        circ.fill(Qt.transparent)
                        p = QPainter(circ)
                        p.setRenderHint(QPainter.Antialiasing)
                        path = QPainterPath()
                        path.addEllipse(0, 0, 48, 48)
                        p.setClipPath(path)
                        p.drawPixmap(0, 0, pix)
                        p.end()
                        lbl_avatar.setPixmap(circ)
                        lbl_avatar.setText("")

                    v_text = QVBoxLayout()
                    v_text.setSpacing(4)
                    v_text.setContentsMargins(0, 2, 0, 2)
                    lbl_n = QLabel(nombre)
                    lbl_n.setStyleSheet(
                        "font-weight: bold; color: white; font-size: 16px; background: transparent; border: none;")

                    carrera_raw = datos.get("carrera", "").title()
                    if "Cibernética" in carrera_raw: carrera_raw = "Ing. Sistemas"

                    lbl_c = QLabel(carrera_raw)
                    lbl_c.setStyleSheet("color: #94a3b8; font-size: 13px; background: transparent; border: none;")

                    v_text.addWidget(lbl_n)
                    v_text.addWidget(lbl_c)

                    h_layout.addWidget(lbl_avatar)
                    h_layout.addLayout(v_text)
                    h_layout.addStretch()

                    self._cards[nombre] = btn_card
                    btn_card.mousePressEvent = lambda e, n=nombre: self._seleccionar_perfil(n)

                    self.grid.addWidget(btn_card)

                self.grid.addStretch()
                scroll.setWidget(container)
                content_layout.addWidget(scroll)

        # 🔥 CORRECCIÓN CLAVE: Usar addWidget (content_container es un QWidget)
        cv.addWidget(content_container, 0, Qt.AlignCenter)

        # Agregamos un pequeño stretch para dar aire abajo
        cv.addStretch(1)
        cv.addSpacing(20)

        # --- BOTONES DE ACCIÓN (INTACTO) ---
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(20)
        actions_layout.setAlignment(Qt.AlignCenter)

        self.btn_cancel = QPushButton("Cancelar")
        self.btn_cancel.setCursor(Qt.PointingHandCursor)
        self.btn_cancel.setMinimumHeight(50)
        self.btn_cancel.setMinimumWidth(150)

        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #94a3b8;
                border: 1px solid #475569;
                border-radius: 12px;
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #1e293b;
                color: white;
                border: 1px solid #64748b;
            }
        """)

        self.btn_ok = QPushButton("Crear Perfil" if modo == "registro" else "Continuar")
        self.btn_ok.setCursor(Qt.PointingHandCursor)
        self.btn_ok.setMinimumHeight(50)
        self.btn_ok.setMinimumWidth(200)

        bg_color = "#0ea5e9" if modo == "registro" else "#334155"
        text_color = "white" if modo == "registro" else "#94a3b8"

        self.btn_ok.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                color: {text_color};
                border-radius: 12px;
                font-size: 15px;
                font-weight: 600;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {'#0284c7' if modo == 'registro' else '#334155'};
            }}
        """)

        if modo == "inicio":
            self.btn_ok.setEnabled(False)

        actions_layout.addWidget(self.btn_cancel)
        actions_layout.addWidget(self.btn_ok)

        cv.addLayout(actions_layout)

        main_form_layout = QVBoxLayout(form_widget)
        # 🔥 Ajuste de política para respetar el alto mínimo de 650px en registro
        card.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        main_form_layout.addWidget(card, 0, Qt.AlignCenter)

        self.btn_cancel.clicked.connect(self.canceled.emit)
        self.btn_ok.clicked.connect(self._ok)

        return form_widget

    # ------------------- LÓGICA GUARDAR (MODIFICADA PARA ADMIN) -------------------
    @Slot()
    def _ok(self):
        if self._modo == "registro":
            nombre = (self.nombre.text() or "").strip()
            if not nombre:
                self.lbl_advertencia.show()
                self.nombre.setFocus()
                return

            MAPA_CARRERAS = {
                "Ingeniería en Cibernética y Sistemas Computacionales": "sistemas",
                "Ingeniería Mecánica": "mecanica",
                "Ingeniería Eléctrica": "electrica",
                "Ingeniería Civil": "civil",
                "Ingeniería Mecatrónica": "mecatronica",
                "Ingeniería Aeronáutica": "aeronautica",
                "Ingeniería Química": "quimica"
            }
            carrera_display = self.carrera.currentText()
            carrera_key = MAPA_CARRERAS.get(carrera_display, "sistemas")

            # 🔥 1. DETECTAR MODO ADMIN
            is_admin_mode = self.admin_toggle.isChecked()

            try:
                datos = crear_perfil_nuevo(nombre, carrera_key) or {}

                # 🔥 2. SOBREESCRIBIR PROGRESO SI ES ADMIN
                if is_admin_mode:
                    temas_curriculum = core.CONTENIDO_MAESTRO.keys()
                    datos["progreso"] = {
                        id_t: "dominado_por_admin" for id_t in temas_curriculum
                    }
                    print(f"🔐 Perfil '{nombre}' creado en MODO ADMIN por toggle.")

                if getattr(self, "foto_path", None):
                    datos["foto"] = self.foto_path

                guardar_perfil(nombre, datos)

            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
                return

            u = Usuario(
                nombre=datos.get("nombre", nombre),
                carrera=datos.get("carrera", carrera_key),
                progreso=ensure_dict(datos.get("progreso"))
            )
            self.accepted.emit(u)

        else:  # Login (INTACTO)
            nombre = getattr(self, "nombre_seleccionado", None)
            if not nombre: return

            datos = cargar_perfil(nombre)
            if not datos: return

            u = Usuario(
                nombre=datos.get("nombre", nombre),
                carrera=datos.get("carrera", "sistemas"),
                progreso=ensure_dict(datos.get("progreso"))
            )
            self.accepted.emit(u)


# ARCHIVO: INTERFAZ.py

# ARCHIVO: INTERFAZ.py

class DiagnosticoView(QWidget):
    terminado = Signal(dict)

    def __init__(self, usuario: Usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self._idx = 0
        self._preguntas = []
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 🔥 ESTILOS
        self.setStyleSheet("""
            DiagnosticoView {
                color: #334155;
                background: transparent;
            }
            QLabel {
                color: #e2e8f0;
            }
            QRadioButton {
                color: #e2e8f0;
                font-size: 18px;
                padding: 8px;
            }
            QRadioButton::indicator {
                width: 24px;
                height: 24px;
                border-radius: 10px;
                border: 2px solid #94a3b8;
            }
            QRadioButton::indicator:checked {
                background-color: #0ea5e9;
                border-color: #0ea5e9;
            }
        """)

        # Diccionario para llevar el conteo de aciertos por materia
        self._puntajes_por_materia = {
            "MATEMATICAS": 0,
            "FISICA": 0,
            "QUIMICA": 0,
            "PROGRAMACION": 0
        }

        self._materia_de_pregunta_actual = []

        # --- UI Layout ---
        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 40, 50, 40)
        layout.setSpacing(20)

        # Tarjeta contenedora
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #0f172a;
                border-radius: 20px;
                border: 1px solid #334155;
            }
        """)
        cv = QVBoxLayout(card)
        cv.setContentsMargins(40, 40, 40, 40)
        cv.setSpacing(20)

        # Título y Progreso
        self.lbl_titulo = QLabel("Diagnóstico de Competencias")
        self.lbl_titulo.setStyleSheet("font-size: 36px; font-weight: bold; color: #38bdf8; border: none;")
        self.lbl_titulo.setAlignment(Qt.AlignCenter)
        cv.addWidget(self.lbl_titulo)

        self.progreso_lbl = QLabel("Generando examen personalizado...")
        self.progreso_lbl.setStyleSheet("color: #94a3b8; font-size: 14px; font-weight: 600; border: none;")
        self.progreso_lbl.setAlignment(Qt.AlignCenter)
        cv.addWidget(self.progreso_lbl)

        # Área de Pregunta
        self.lbl_pregunta = QLabel("")
        self.lbl_pregunta.setWordWrap(True)
        self.lbl_pregunta.setStyleSheet(
            "font-size: 20px; color: white; margin-top: 15px; font-weight: 500; border: none;")
        self.lbl_pregunta.setAlignment(Qt.AlignLeft)
        cv.addWidget(self.lbl_pregunta)

        # Área de Opciones (Radio Buttons)
        self.opciones_widget = QWidget()
        self.opciones_widget.setStyleSheet("background: transparent; border: none;")
        self.opciones_layout = QVBoxLayout(self.opciones_widget)
        self.opciones_layout.setSpacing(12)
        cv.addWidget(self.opciones_widget)

        self.btn_group = QButtonGroup(self)

        # Feedback y Botón
        self.feedback_lbl = QLabel("")
        self.feedback_lbl.setAlignment(Qt.AlignCenter)
        self.feedback_lbl.setStyleSheet("font-size: 20px; font-weight: bold; border: none;")
        cv.addWidget(self.feedback_lbl)

        self.btn_siguiente = QPushButton("Confirmar Respuesta")
        self.btn_siguiente.setCursor(Qt.PointingHandCursor)
        self.btn_siguiente.setMinimumHeight(50)
        self.btn_siguiente.setStyleSheet("""
            QPushButton {
                background-color: #0ea5e9;
                color: white;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                border: none;
            }
            QPushButton:hover { background-color: #0284c7; }
            QPushButton:disabled { background-color: #334155; color: #94a3b8; }
        """)
        self.btn_siguiente.clicked.connect(self._evaluar)
        cv.addWidget(self.btn_siguiente)

        layout.addWidget(card)

        # Iniciar carga
        QTimer.singleShot(50, self._generar_examen_balanceado)

    # 🔥 SOPORTE PARA ENTER
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.btn_siguiente.isEnabled():
                self.btn_siguiente.click()
        else:
            # Permitir seleccionar opciones con números 1-4
            if event.text() in ['1', '2', '3', '4']:
                idx = int(event.text()) - 1
                buttons = self.btn_group.buttons()
                if 0 <= idx < len(buttons):
                    buttons[idx].setChecked(True)
            super().keyPressEvent(event)

    def _generar_examen_balanceado(self):
        try:
            nuevas_preguntas = []
            materia_map = []

            materias_obj = core.RUTAS_POR_MATERIA

            for nombre_materia, lista_ids_temas in materias_obj.items():
                banco_filtrado = []
                set_ids_materia = set(lista_ids_temas)

                if hasattr(core, "BANCO_PREGUNTAS_MAESTRO"):
                    for p in core.BANCO_PREGUNTAS_MAESTRO:
                        if p.get("tema_id") in set_ids_materia:
                            banco_filtrado.append(p)

                if len(banco_filtrado) >= 3:
                    seleccion = random.sample(banco_filtrado, 3)
                else:
                    seleccion = banco_filtrado

                for preg in seleccion:
                    nuevas_preguntas.append(preg)
                    materia_map.append(nombre_materia)

            combinado = list(zip(nuevas_preguntas, materia_map))
            random.shuffle(combinado)

            if combinado:
                self._preguntas, self._materia_de_pregunta_actual = zip(*combinado)
                self.progreso_lbl.setText(f"Pregunta 1 de {len(self._preguntas)}")
                self._mostrar_pregunta()
            else:
                self.lbl_pregunta.setText("Error: No se encontraron preguntas en el banco.")
                self.btn_siguiente.setEnabled(False)

        except Exception as e:
            print(f"Error generando examen: {e}")
            self.lbl_pregunta.setText("Ocurrió un error al generar el examen.")

    def _mostrar_pregunta(self):
        if self._idx < len(self._preguntas):
            datos = self._preguntas[self._idx]
            txt = datos.get("pregunta") or datos.get("enunciado", "Pregunta sin texto")
            self.lbl_pregunta.setText(f"<b>{self._idx + 1}.</b> {txt}")
            self.lbl_pregunta.setAlignment(Qt.AlignLeft)

            while self.opciones_layout.count():
                item = self.opciones_layout.takeAt(0)
                if item.widget(): item.widget().deleteLater()

            opciones = datos.get("opciones", []).copy()
            if not opciones: opciones = ["Verdadero", "Falso"]
            random.shuffle(opciones)

            buttons = self.btn_group.buttons()
            for b in buttons: self.btn_group.removeButton(b)

            for i, opt_text in enumerate(opciones):
                rb = QRadioButton(str(opt_text))
                self.opciones_layout.addWidget(rb)
                self.btn_group.addButton(rb)

            if self.btn_group.checkedButton():
                self.btn_group.setExclusive(False)
                self.btn_group.checkedButton().setChecked(False)
                self.btn_group.setExclusive(True)

            self.setFocus()
            self.progreso_lbl.setText(f"Avance: {self._idx + 1} / {len(self._preguntas)}")
            self.feedback_lbl.setText("")
            self.btn_siguiente.setText("Confirmar Respuesta")
            self.btn_siguiente.setEnabled(True)
            self.opciones_widget.setEnabled(True)
        else:
            self._finalizar()

    def _evaluar(self):
        seleccionado = self.btn_group.checkedButton()
        if not seleccionado:
            self.feedback_lbl.setText("<span style='color:#FCD34D'>⚠️ Selecciona una opción.</span>")
            return

        self.opciones_widget.setEnabled(False)
        self.btn_siguiente.setEnabled(False)

        respuesta_usuario = seleccionado.text()
        datos = self._preguntas[self._idx]
        correcta = datos.get("respuesta") or datos.get("respuesta_correcta")

        es_correcta = validar_respuesta(respuesta_usuario, correcta)

        if es_correcta:
            self.feedback_lbl.setText("<span style='color:#22C55E'>✅ ¡Correcto!</span>")
            materia_actual = self._materia_de_pregunta_actual[self._idx]
            if materia_actual in self._puntajes_por_materia:
                self._puntajes_por_materia[materia_actual] += 1
        else:
            self.feedback_lbl.setText(f"<span style='color:#EF4444'>❌ Incorrecto. La respuesta era: {correcta}</span>")

        QTimer.singleShot(1500, self._siguiente_paso)

    def _siguiente_paso(self):
        self._idx += 1
        self._mostrar_pregunta()

    def _finalizar(self):
        self.lbl_pregunta.setAlignment(Qt.AlignCenter)
        self.lbl_pregunta.setText("📊 <b>Diagnóstico Finalizado</b><br>Analizando tus fortalezas y debilidades...")
        self.opciones_widget.hide()
        self.btn_siguiente.hide()
        self.progreso_lbl.hide()

        # Ordenar materias por puntaje
        materias_ordenadas_tuplas = sorted(
            self._puntajes_por_materia.items(),
            key=lambda x: (x[1], x[0])
        )

        lista_ordenada = [m[0] for m in materias_ordenadas_tuplas]

        # 🔥 CORRECCIÓN: Centrar celdas de la tabla (text-align: center)
        reporte = "<br><table style='width:100%; font-size:20px; margin-left:auto; margin-right:auto;'>"
        for mat, pts in materias_ordenadas_tuplas:
            if pts == 0:
                nivel = "<b style='color:#EF4444'>CRÍTICO (0/3)</b>"
            elif pts == 1:
                nivel = "<b style='color:#F97316'>ALTA PRIORIDAD (1/3)</b>"
            elif pts == 2:
                nivel = "<b style='color:#FCD34D'>MEDIA (2/3)</b>"
            else:
                nivel = "<b style='color:#22C55E'>DOMINADO (3/3)</b>"

            # Ambos td con text-align: center
            reporte += f"<tr><td style='padding:5px; text-align:center;'>{mat.title()}</td><td style='padding:5px; text-align:center;'>{nivel}</td></tr>"
        reporte += "</table>"

        self.lbl_pregunta.setText(
            f"<div style='font-size: 26px; margin-bottom: 15px;'><b>Resultados por Área:</b></div>"
            f"{reporte}"
            f"<br><br><div style='font-size: 18px; color:#94a3b8;'><i>Hemos reordenado tu Dashboard según tus necesidades.</i></div>"
        )

        datos_perfil = {
            "nombre": self.usuario.nombre,
            "carrera": self.usuario.carrera,
            "progreso": self.usuario.progreso,
            "orden_materias": lista_ordenada,
            "puntajes_diagnostico": self._puntajes_por_materia
        }

        datos_perfil["progreso"]["INTRO-DIAG"] = "dominado_por_diagnostico"

        guardar_perfil(self.usuario.nombre, datos_perfil)
        self.usuario.progreso = datos_perfil["progreso"]

        QTimer.singleShot(5000, lambda: self.terminado.emit(self.usuario.progreso))


# ARCHIVO: INTERFAZ.py

class ChatView(QWidget):
    tema_completado = Signal()
    repass_confirmed = Signal(str)
    repass_cancelled = Signal()

    def __init__(self, usuario: Usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.tema_id = None
        self._lecciones = []
        self._idx_leccion = 0
        self._estado_leccion = "idle"
        self._modo_manual = False
        self._similares_pendientes = []
        self._datos_ejercicio_actual = {}
        self._similares_cargados_para_idx = -1
        self.current_repass_tema_id: Optional[str] = None
        self.current_options_widget = None

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.messages_widget = QWidget()
        self.messages_layout = QVBoxLayout(self.messages_widget)
        self.messages_layout.setContentsMargins(10, 20, 10, 20)
        self.messages_layout.setSpacing(15)
        self.messages_layout.setAlignment(Qt.AlignTop)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.messages_widget)
        self.scroll_area.setStyleSheet("""
            QScrollArea { background: transparent; border: none; }
            QScrollBar:vertical { background: #1e293b; width: 8px; border-radius: 4px; }
            QScrollBar::handle:vertical { background: #475569; border-radius: 4px; min-height: 20px; }
        """)

        self.repass_buttons_widget = self._build_repass_prompt_ui()
        self.repass_buttons_widget.hide()

        self.input_widget = QWidget()
        input_layout = QHBoxLayout(self.input_widget)
        self.input = QLineEdit()
        self.input.setPlaceholderText("Escribe tu respuesta aquí...")
        self.send_btn = QPushButton("Enviar")

        self.input.returnPressed.connect(self._enviar)
        self.send_btn.clicked.connect(self._enviar)
        input_layout.addWidget(self.input)
        input_layout.addWidget(self.send_btn)

        layout.addWidget(self.scroll_area, 1)
        layout.addWidget(self.repass_buttons_widget)
        layout.addWidget(self.input_widget)
        self.input_widget.hide()

    def _add_message(self, text, is_user):
        lbl = QLabel(text)
        lbl.setWordWrap(True)
        lbl.setTextFormat(Qt.RichText)

        wrapper = QWidget()
        wl = QHBoxLayout(wrapper)
        wl.setContentsMargins(0, 0, 0, 0)

        if is_user:
            lbl.setStyleSheet("""
                background: #1e293b; color: white; padding: 12px 16px; 
                border-radius: 12px; border: 1px solid #334155;
            """)
            lbl.setMaximumWidth(600)
            lbl.setAlignment(Qt.AlignLeft)
            wl.addStretch()
            wl.addWidget(lbl)
        else:
            lbl.setStyleSheet("""
                background: #1e40af; color: white; padding: 20px; 
                border-radius: 15px; font-size: 15px;
            """)
            lbl.setAlignment(Qt.AlignLeft)
            wl.addWidget(lbl)

        self.messages_layout.addWidget(wrapper)
        self._force_update()

    def _add_media(self, file_path: str, is_user: bool = False):
        if not os.path.exists(file_path): return
        container = QLabel();
        container.setAlignment(Qt.AlignCenter)
        container.setStyleSheet(
            f"QLabel {{ background: {'#1e40af' if not is_user else '#1e293b'}; padding: 15px; border-radius: 15px; margin: 5px; }}")

        if file_path.lower().endswith(".gif"):
            movie = QMovie(file_path);
            movie.setScaledSize(QSize(500, 350))
            container.setMovie(movie);
            movie.start()
        else:
            pixmap = QPixmap(file_path);
            pixmap = pixmap.scaledToWidth(500, Qt.SmoothTransformation)
            container.setPixmap(pixmap)

        wrapper = QWidget();
        wl = QHBoxLayout(wrapper);
        wl.setContentsMargins(0, 0, 0, 0)
        if is_user:
            wl.addStretch(); wl.addWidget(container)
        else:
            wl.addStretch(); wl.addWidget(container); wl.addStretch()
        self.messages_layout.addWidget(wrapper);
        self._force_update()

    def _obtener_materia_padre(self, tema_id_buscado: str) -> str:
        for materia, lista_temas in core.RUTAS_POR_MATERIA.items():
            if tema_id_buscado in lista_temas:
                if materia == "MATEMATICAS": return "Matemáticas"
                if materia == "FISICA": return "Física"
                if materia == "QUIMICA": return "Química"
                if materia == "PROGRAMACION": return "Programación"
                return materia.title()
        return "General"

    # 🔥 FUNCIÓN DE FELICITACIÓN AGREGADA
    def mostrar_felicitacion_tema(self, tema_id: str):
        self._clear_chat()
        self._hide_input()
        nombre_tema = NOMBRES_DE_TEMAS.get(tema_id, tema_id)

        html_msg = f"""
        <div style='text-align:center; margin-top:20px;'>
            <div style='font-size:60px;'>🎉</div>
            <div style='font-size:28px; font-weight:800; color:#22c55e; margin:15px 0;'>¡Felicidades!</div>
            <div style='font-size:18px; color:#e2e8f0; line-height:1.6;'>
                Has completado exitosamente el módulo:<br>
                <b style='color:#38bdf8; font-size:20px;'>{nombre_tema}</b>
            </div>
            <hr style='border: 1px solid #334155; margin: 25px 0;'>
            <div style='font-size:16px; color:#94a3b8;'>
                Tu progreso ha sido guardado.<br>
                Ahora puedes seleccionar el siguiente tema en el menú de la izquierda.
            </div>
            <div style='font-size:30px; margin-top:20px;'>🚀</div>
        </div>
        """
        self._add_message(html_msg, is_user=False)

    def mostrar_bienvenida_materia(self, materia_id: str):
        self._clear_chat();
        self._hide_input();
        self.repass_buttons_widget.hide()
        descripciones = {
            "MATEMATICAS": "El lenguaje del universo. Dominarás desde números básicos hasta cálculo avanzado.",
            "FISICA": "Leyes de la realidad. Movimiento, fuerzas, energía y electricidad.",
            "QUIMICA": "La ciencia de la materia. Átomos, enlaces y reacciones.",
            "PROGRAMACION": "Pensamiento lógico para crear soluciones tecnológicas."
        }
        nombre_materia = materia_id.title()
        if materia_id == "MATEMATICAS":
            nombre_materia = "Matemáticas"
        elif materia_id == "FISICA":
            nombre_materia = "Física"
        elif materia_id == "QUIMICA":
            nombre_materia = "Química"
        elif materia_id == "PROGRAMACION":
            nombre_materia = "Programación"

        desc = descripciones.get(materia_id, "Explora los temas fundamentales.")
        header = f"""
        <div style='margin-bottom:15px;'>
            <div style='color:#38bdf8; font-size:14px; font-weight:bold; margin-bottom:5px;'>PLAN DE ESTUDIOS</div>
            <div style='color:#ffffff; font-size:32px; font-weight:800; margin-bottom:10px;'>{nombre_materia}</div>
            <div style='color:#cbd5e1; font-size:16px; line-height:1.5; font-style:italic;'>"{desc}"</div>
        </div>
        <hr style='border: 1px solid #334155; margin: 20px 0;'>
        <div style='font-size:18px; color:#e2e8f0; margin-bottom:15px;'><b>📚 Temario del Curso:</b></div>
        <div style='margin-left:10px;'>
        """
        temas = core.RUTAS_POR_MATERIA.get(materia_id, [])
        lista_temas_html = ""
        for i, tid in enumerate(temas):
            nombre_tema = NOMBRES_DE_TEMAS.get(tid, tid)
            lista_temas_html += f"<div style='margin-bottom:10px; font-size:15px; color:#e2e8f0;'><span style='color:#38bdf8; font-weight:bold; margin-right:10px;'>{i + 1}.</span> {nombre_tema}</div>"
        footer = "<br><div style='color:#94a3b8; font-size:14px;'><i>Selecciona un tema del menú izquierdo para comenzar.</i></div>"
        self._add_message(header + lista_temas_html + footer, is_user=False)

    def show_prerequisites(self, tema_id: str):
        self._clear_chat();
        self._hide_input()
        nombre_tema = NOMBRES_DE_TEMAS.get(tema_id, tema_id)
        materia_actual = self._obtener_materia_padre(tema_id)

        desc_breve = "conceptos fundamentales."
        if hasattr(core, "CONTENIDO_MAESTRO"):
            datos = core.CONTENIDO_MAESTRO.get(tema_id, {})
            refuerzo = datos.get("refuerzo", [])
            if refuerzo:
                raw = refuerzo[0].get("definicion", "")
                if raw: desc_breve = raw[:150] + "..." if len(raw) > 150 else raw

        header = f"""
        <div style='margin-bottom:15px;'>
            <div style='color:#38bdf8; font-size:14px; font-weight:bold; margin-bottom:4px;'>{materia_actual.upper()} • {tema_id}</div>
            <div style='color:#ffffff; font-size:28px; font-weight:800; margin-bottom:10px;'>{nombre_tema}</div>
            <div style='color:#cbd5e1; font-size:16px; line-height:1.5; font-style:italic;'>"{desc_breve}"</div>
        </div>
        <hr style='border: 1px solid #334155; margin: 20px 0;'>
        """
        lock = """
        <div style='display:flex; align-items:center; margin-bottom:15px;'>
            <span style='font-size:26px;'>🔒</span>
            <span style='color:#ef4444; font-size:20px; font-weight:bold; margin-left:10px;'>Contenido Bloqueado</span>
        </div>
        <div style='color:#e2e8f0; font-size:16px; margin-bottom:15px;'>Para desbloquear, necesitas dominar:</div>
        """
        prereqs = core.CONTENIDO_MAESTRO.get(tema_id, {}).get("prerequisitos", [])
        lst = "<div style='margin-left: 10px;'>"
        for pid in prereqs:
            p_nom = NOMBRES_DE_TEMAS.get(pid, pid)
            p_mat = self._obtener_materia_padre(pid)
            loc = "En esta materia" if p_mat == materia_actual else f"Ir a: <b>{p_mat}</b>"
            col_loc = "#94a3b8" if p_mat == materia_actual else "#38bdf8"
            comp = pid in self.usuario.progreso
            icon, col = ("✅", "#22c55e") if comp else ("❌", "#f87171")
            lst += f"<div style='margin-bottom:15px;'><div style='font-size:18px; font-weight:bold; color:{col};'>{icon} {p_nom}</div><div style='font-size:14px; color:{col_loc}; margin-left:30px;'>📍 {loc}</div></div>"
        lst += "</div>"
        self._add_message(header + lock + lst, False)

    def _build_repass_prompt_ui(self):
        w = QWidget();
        l = QHBoxLayout(w);
        l.setAlignment(Qt.AlignCenter)
        b1 = QPushButton("✅ SÍ");
        b1.clicked.connect(lambda: self._handle_button_click("SÍ"))
        b2 = QPushButton("❌ NO");
        b2.clicked.connect(lambda: self._handle_button_click("NO"))
        b1.setStyleSheet("background:#10B981;color:white;border-radius:8px;padding:10px 20px; font-weight:bold;")
        b2.setStyleSheet("background:#EF4444;color:white;border-radius:8px;padding:10px 20px; font-weight:bold;")
        l.addWidget(b1);
        l.addSpacing(30);
        l.addWidget(b2);
        return w

    def _handle_button_click(self, dec):
        self.repass_buttons_widget.hide()
        if dec == "SÍ" and self.current_repass_tema_id:
            self._add_message("👍 ¡Repaso aceptado!", False);
            self.repass_confirmed.emit(self.current_repass_tema_id)
        else:
            self._add_message("❌ Repaso cancelado.", False);
            self.repass_cancelled.emit()

    def show_repass_prompt(self, tid):
        self.current_repass_tema_id = tid; self._hide_input(); self.repass_buttons_widget.show()

    def _show_options_input(self, opts):
        self.input_widget.hide();
        self.repass_buttons_widget.hide()
        if self.current_options_widget: self.current_options_widget.deleteLater(); self.current_options_widget = None
        options_container = QWidget();
        layout = QVBoxLayout(options_container)
        layout.setContentsMargins(0, 10, 20, 10);
        layout.setSpacing(8);
        layout.setAlignment(Qt.AlignRight)
        for o in opts:
            b = QPushButton(str(o));
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(
                "text-align:left; padding:12px 20px; background:#1e293b; color:white; border:1px solid #334155; border-radius:12px; font-size:15px; min-width: 200px;")
            b.clicked.connect(lambda c, t=o: self._procesar_respuesta_desde_boton(str(t)))
            layout.addWidget(b)
        self.messages_layout.addWidget(options_container);
        self.current_options_widget = options_container
        self._force_update()

    def _procesar_respuesta_desde_boton(self, txt):
        if self.current_options_widget: self.current_options_widget.deleteLater(); self.current_options_widget = None
        self.input.setText(txt);
        self._enviar()

    def _clear_chat(self):
        while self.messages_layout.count():
            it = self.messages_layout.takeAt(0)
            if it.widget(): it.widget().deleteLater()

    def _show_input(self):
        self.input_widget.show();
        if self.current_options_widget: self.current_options_widget.deleteLater(); self.current_options_widget = None
        self.input.setFocus()

    def _hide_input(self):
        self.input_widget.hide()
        if self.current_options_widget: self.current_options_widget.deleteLater(); self.current_options_widget = None

    def _force_update(self):
        self.messages_widget.adjustSize()
        QTimer.singleShot(10, lambda: self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()))

    def presentar_menu_lecciones(self, tema_id):
        self._clear_chat();
        self._hide_input();
        self._modo_manual = True;
        self.tema_id = tema_id
        obj = core.construir_tema(tema_id)
        self._lecciones = obj.contenido_reforzamiento if obj else []
        if not self._lecciones: self._add_message("No hay lecciones disponibles.", False); return
        nombre_tema = NOMBRES_DE_TEMAS.get(tema_id, tema_id)
        header = f"<div style='font-size:22px; color:#38bdf8; margin-bottom:5px;'><b>📂 {nombre_tema}</b></div><div style='color:#94a3b8; font-size:14px;'>Modo Exploración Admin</div>"
        self._add_message(header, False)
        for i, l in enumerate(self._lecciones):
            b = QPushButton(f"Lección {i + 1}: {l.get('subtema_titulo')}")
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(
                "text-align:left;padding:15px;background:#1e293b;color:white;border-radius:10px;margin-bottom:8px;border:1px solid #334155;font-size:15px;")
            b.clicked.connect(lambda c, x=i: self._iniciar_leccion_manual(x))
            self.messages_layout.addWidget(b)
        self._force_update()

    def _iniciar_leccion_manual(self, idx):
        self._clear_chat();
        self._idx_leccion = idx;
        self._similares_cargados_para_idx = -1
        self._mostrar_siguiente_leccion()

    def load_tema(self, tid):
        self._clear_chat();
        self._hide_input();
        self._modo_manual = False;
        self.tema_id = tid
        obj = core.construir_tema(tid)
        self._lecciones = obj.contenido_reforzamiento if obj else []
        self._idx_leccion = 0;
        self._similares_cargados_para_idx = -1
        nombre = NOMBRES_DE_TEMAS.get(tid, tid)
        self._add_message(f"<div style='font-size:20px; color:#fcfcfc;'>📘 <b>Iniciando Módulo: {nombre}</b></div>",
                          False)
        QTimer.singleShot(500, self._mostrar_siguiente_leccion)

    def _mostrar_siguiente_leccion(self):
        self._hide_input()
        if self._idx_leccion >= len(self._lecciones):
            self._finalizar_reforzamiento()
            return
        l = self._lecciones[self._idx_leccion]
        html_content = f"<h2 style='color:#c084fc; margin-bottom:10px;'>{l.get('subtema_titulo')}</h2><div style='font-size:16px; line-height:1.6; margin-bottom:15px;'><b>Definición:</b><br>{l.get('definicion')}</div>"
        self._add_message(html_content, False)
        diagrama = l.get('diagrama')
        if diagrama and os.path.exists(diagrama): self._add_media(diagrama, is_user=False)
        if l.get('ejemplo_resuelto'):
            ejemplo_html = f"<div style='margin-top:15px; padding-left:12px; border-left: 4px solid #fbbf24;'><b style='color:#fbbf24; font-size:17px;'>★ Ejemplo Resuelto:</b><br><div style='font-size:15px; margin-top:5px; color:#e2e8f0; line-height:1.5;'>{l.get('ejemplo_resuelto').replace(chr(10), '<br>')}</div></div>"
            self._add_message(ejemplo_html, False)
        if self._similares_cargados_para_idx != self._idx_leccion:
            import random
            base = l.get('ejercicio', {})
            sims = base.get('similares', []).copy()
            random.shuffle(sims)
            self._similares_pendientes = sims
            self._datos_ejercicio_actual = {"enunciado": base.get('enunciado'),
                                            "respuesta": base.get('respuesta_correcta'),
                                            "opciones": base.get('opciones', []), "es_recuperacion": False}
            self._similares_cargados_para_idx = self._idx_leccion
        self._presentar_ejercicio()

    def _presentar_ejercicio(self):
        self._hide_input()
        dat = self._datos_ejercicio_actual
        color_titulo = "#f59e0b" if dat.get("es_recuperacion") else "#ef4444"
        titulo = "🔄 Intentemos otro ejercicio:" if dat.get("es_recuperacion") else "⚡ Demuestre lo aprendido, futuro ingeniero:"
        html_ej = f"<div style='font-size:18px; font-weight:bold; color:{color_titulo}; margin-bottom:8px;'>{titulo}</div><div style='font-size:16px; line-height:1.5; color:#e2e8f0;'>{dat.get('enunciado')}</div>"
        self._add_message(html_ej, False)
        opts = dat.get('opciones', [])
        if opts and len(opts) > 1:
            QTimer.singleShot(500, lambda: self._show_options_input(opts))
        else:
            QTimer.singleShot(500, self._show_input)

    def _mostrar_aplicacion_y_avanzar(self):
        if self._idx_leccion >= len(self._lecciones): return
        l = self._lecciones[self._idx_leccion]
        c = self.usuario.carrera
        apps = l.get('aplicaciones', {})
        app = apps.get(c) or apps.get('sistemas')
        if app:
            prefijo = "Ingeniería en" if c == "sistemas" else "Ingeniería"
            titulo_carrera = f"{prefijo} {c.title()}"
            html_app = f"<div style='font-size:16px; margin-top:5px;'>💡 <b>Aplicación en {titulo_carrera}:</b><br><br><b>Uso:</b> {app.get('uso')}<br><br><span style='color:#fcfcfc;'><b>Consecuencia de un error:</b> {app.get('consecuencia_de_error')}</span></div>"
            self._add_message(html_app, False)
        if self._modo_manual:
            self._add_message("✅ Lección finalizada.", False)
            QTimer.singleShot(2000, lambda: self.presentar_menu_lecciones(self.tema_id))
        else:
            self._idx_leccion += 1
            QTimer.singleShot(2500, self._mostrar_siguiente_leccion)

    @Slot()
    def _enviar(self):
        txt = self.input.text().strip();
        if not txt: return
        self._add_message(txt, True);
        self.input.clear();
        self._hide_input()
        corr = self._datos_ejercicio_actual.get('respuesta', '')
        if validar_respuesta(txt, corr):
            self._add_message("<b>✅ ¡Correcto!</b>", False)
            QTimer.singleShot(1000, self._mostrar_aplicacion_y_avanzar)
        else:
            self._add_message(f"❌ <b>Incorrecto.</b><br>La respuesta era: <b>{corr}</b>", False)
            if self._similares_pendientes:
                new_ej = self._similares_pendientes.pop(0)
                self._datos_ejercicio_actual = {"enunciado": new_ej.get('pregunta'),
                                                "respuesta": new_ej.get('respuesta_correcta'),
                                                "opciones": new_ej.get('opciones', []), "es_recuperacion": True}
                QTimer.singleShot(1500, self._presentar_ejercicio)
            else:
                self._add_message("Avancemos por ahora...", False)
                QTimer.singleShot(2000, self._mostrar_aplicacion_y_avanzar)

    def _finalizar_reforzamiento(self):
        if self._modo_manual: return
        # Se quita el mensaje directo y la limpieza para evitar conflicto con el refresco del dashboard
        self.usuario.progreso[self.tema_id] = "completado_por_reforzamiento"
        guardar_perfil(self.usuario.nombre, {"nombre": self.usuario.nombre, "carrera": self.usuario.carrera,
                                             "progreso": self.usuario.progreso})
        self.tema_completado.emit()


# ARCHIVO: INTERFAZ.py

class Dashboard(QWidget):
    # Señales
    ver_mapa_signal = Signal()
    solicitar_lecciones = Signal(object, str)
    salir_signal = Signal()

    def __init__(self, usuario: Usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.mapa_materias = {}

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Left Panel
        left_panel = QFrame()
        left_panel.setStyleSheet("QFrame { background: #0f172a; border-radius: 12px; border: 1px solid #1e293b; }")
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(15, 15, 15, 15);
        left_layout.setSpacing(15)

        MAPA_DISPLAY = {"sistemas": "Ing. Sistemas", "mecanica": "Ing. Mecánica", "electrica": "Ing. Eléctrica",
                        "civil": "Ing. Civil", "mecatronica": "Ing. Mecatrónica", "aeronautica": "Ing. Aeronáutica",
                        "quimica": "Ing. Química"}
        carrera_display = MAPA_DISPLAY.get(usuario.carrera, usuario.carrera.title())

        user_info = QLabel(f"👤 <b>{usuario.nombre}</b>\n🎓 {carrera_display}")
        user_info.setStyleSheet("color: white; font-size: 14px; line-height: 1.4em;");
        user_info.setTextFormat(Qt.RichText)
        left_layout.addWidget(user_info)

        self.btn_red = QPushButton("🤖 Visualizar IA de entrenamiento (No disponible)")
        self.btn_red.clicked.connect(lambda: mostrar_red_neuronal_en_GUI(self))
        left_layout.addWidget(self.btn_red)

        self.btn_grafo = QPushButton("🗺️ Ver Mapa de progreso")
        self.btn_grafo.clicked.connect(self.ver_mapa_signal.emit)
        left_layout.addWidget(self.btn_grafo)

        left_layout.addWidget(QLabel("📚 <b>Materias</b>"))
        self.materias_list = QListWidget()
        self.materias_list.setStyleSheet(
            "background: #1e293b; border: 1px solid #334155; border-radius: 8px; color: white; QListWidget::item:selected { background: #3b82f6; }")
        left_layout.addWidget(self.materias_list)

        left_layout.addWidget(QLabel("🧠 <b>Temas</b>"))
        self.temas_list = QListWidget()
        self.temas_list.setStyleSheet(
            "background: #1e293b; border: 1px solid #334155; border-radius: 8px; color: white; QListWidget::item:selected { background: #3b82f6; }")
        left_layout.addWidget(self.temas_list)
        left_layout.addStretch()

        self.btn_salir = QPushButton("💾 Guardar y Salir")
        self.btn_salir.clicked.connect(self._guardar_y_salir)
        left_layout.addWidget(self.btn_salir)

        # Right Panel
        right_panel = QFrame()
        right_panel.setStyleSheet("QFrame { background: #0f172a; border-radius: 12px; border: 1px solid #1e293b; }")
        right_layout = QVBoxLayout(right_panel);
        right_layout.setContentsMargins(0, 0, 0, 0)

        self.tema_actual_label = QLabel("Selecciona un tema")
        self.tema_actual_label.setStyleSheet(
            "background: #1e293b; color: #60a5fa; font-size: 16px; font-weight: bold; padding: 15px; border-bottom: 1px solid #334155;")
        right_layout.addWidget(self.tema_actual_label)

        self.chat_view = ChatView(usuario)
        self.chat_view.repass_confirmed.connect(self._start_repass_confirmed)
        self.chat_view.repass_cancelled.connect(self._repass_cancelled)
        self.chat_view.tema_completado.connect(self._on_tema_completado_dashboard)  # Conexión clave
        right_layout.addWidget(self.chat_view, 1)

        layout.addWidget(left_panel, 1);
        layout.addWidget(right_panel, 2)

        self.materias_list.currentTextChanged.connect(self._on_materia_selected)
        self.temas_list.itemClicked.connect(self._on_tema_selected_item)

        self._cargar_datos_iniciales()

    @Slot()
    def _guardar_y_salir(self):
        datos = cargar_perfil(self.usuario.nombre)
        if datos:
            datos["progreso"] = self.usuario.progreso
            guardar_perfil(self.usuario.nombre, datos)
        self.salir_signal.emit()

    @Slot()
    def _on_tema_completado_dashboard(self):
        # 1. Refrescar la lista de temas (pone checks verdes)
        self.refrescar_listas_temas()

        # 2. 🔥 ACTUALIZAR EL COLOR DE LA MATERIA (Si completó todo)
        self._actualizar_estilo_materias()

        # 3. Mostrar felicitación
        if self.chat_view.tema_id:
            QTimer.singleShot(100, lambda: self.chat_view.mostrar_felicitacion_tema(self.chat_view.tema_id))

    def _actualizar_estilo_materias(self):
        """Recalcula el color de las materias en tiempo real."""
        datos_perfil = cargar_perfil(self.usuario.nombre)
        if not datos_perfil: return

        puntajes = datos_perfil.get("puntajes_diagnostico", {})
        orden = datos_perfil.get("orden_materias", [])

        # Si no hay orden, usamos el default para no romper
        if not orden: orden = sorted(list(RUTAS_POR_MATERIA.keys()))

        # Recorrer la lista visual y actualizar
        for i in range(self.materias_list.count()):
            item = self.materias_list.item(i)
            materia_id = item.data(Qt.UserRole)

            # Verificar si completó todos los temas de esa materia
            temas_ids = RUTAS_POR_MATERIA.get(materia_id, [])
            completados = [t for t in temas_ids if t in self.usuario.progreso]
            es_dominada = len(completados) == len(temas_ids) and len(temas_ids) > 0

            nombre_display = item.text().split(" ", 1)[-1]  # Mantener nombre base

            if es_dominada:
                item.setText(f"🏆 {nombre_display}")
                item.setForeground(QColor("#fbbf24"))  # Dorado
            elif orden and puntajes:
                score = puntajes.get(materia_id)
                if score == 0:
                    item.setText(f"🔴 {nombre_display}"); item.setForeground(QColor("#ef4444"))
                elif score == 1:
                    item.setText(f"🟠 {nombre_display}"); item.setForeground(QColor("#f97316"))
                elif score == 2:
                    item.setText(f"🟡 {nombre_display}"); item.setForeground(QColor("#fcd34d"))
                else:
                    item.setText(f"🟢 {nombre_display}"); item.setForeground(QColor("#22c55e"))

    def _cargar_datos_iniciales(self):
        self.materias_list.clear()
        datos = cargar_perfil(self.usuario.nombre)
        orden = datos.get("orden_materias", []) if datos else []
        lista_final = orden if orden else sorted(list(RUTAS_POR_MATERIA.keys()))

        for mid in lista_final:
            nom = mid.title()
            if mid == "MATEMATICAS":
                nom = "Matemáticas"
            elif mid == "FISICA":
                nom = "Física"
            elif mid == "QUIMICA":
                nom = "Química"
            elif mid == "PROGRAMACION":
                nom = "Programación"

            item = QListWidgetItem(nom)
            item.setData(Qt.UserRole, mid)
            self.materias_list.addItem(item)

        # Aplicar colores iniciales
        self._actualizar_estilo_materias()
        self.materias_list.clearSelection()
        self.materias_list.setCurrentItem(None)

    def _on_materia_selected(self, _):
        current = self.materias_list.currentItem()
        if not current: return
        mid = current.data(Qt.UserRole)

        self.temas_list.clear()
        t_ids = RUTAS_POR_MATERIA.get(mid, [])
        disp = set(generar_temas_disponibles(self.usuario.progreso))
        dom = set(self.usuario.progreso.keys())

        for tid in t_ids:
            tnom = NOMBRES_DE_TEMAS.get(tid, tid.title())
            it = QListWidgetItem()
            it.setData(Qt.UserRole, tid)
            if tid in dom:
                it.setText(f"✅ {tnom}"); it.setForeground(Qt.gray)
            elif tid in disp:
                it.setText(f"➡️ {tnom}"); it.setForeground(Qt.white)
            else:
                it.setText(f"🔒 {tnom}"); it.setForeground(Qt.darkGray); it.setFlags(it.flags() & ~Qt.ItemIsEnabled)
            self.temas_list.addItem(it)

        self.chat_view.mostrar_bienvenida_materia(mid)

    def _on_tema_selected_item(self, item):
        tid = item.data(Qt.UserRole)
        if not tid: return
        nom = NOMBRES_DE_TEMAS.get(tid, tid)

        if tid in self.usuario.progreso:
            # Si es admin o ya lo hizo
            if self.usuario.progreso[tid] == "dominado_por_admin":
                self.tema_actual_label.setText(f"📂 Exploración Admin: {nom}")
                self.chat_view.presentar_menu_lecciones(tid)
            else:
                # --- MODIFICACIÓN AQUÍ ---
                self.chat_view._clear_chat()
                mensaje = (
                    f"<div style='font-size:18px;'>🎉 <b>¡Tema Completado!</b></div><br>"
                    f"Ya has realizado el curso de <b>{nom}</b> anteriormente.<br><br>"
                    "¿Te gustaría volver a cursarlo para reforzar tus conocimientos?"
                )
                self.chat_view._add_message(mensaje, False)
                self.chat_view.show_repass_prompt(tid)
                self.tema_actual_label.setText(f"✅ Repaso: {nom}")
            return

        if not (item.flags() & Qt.ItemIsEnabled):
            self.chat_view.show_prerequisites(tid)
            return

        self.tema_actual_label.setText(f"📍 Módulo: {nom}")
        self.chat_view.load_tema(tid)
        self._force_update()

    @Slot()
    def _repass_cancelled(self):
        self.tema_actual_label.setText("Selecciona un tema")
        self.chat_view._clear_chat()
        self.chat_view._add_message("📚 Selecciona otro tema.", False)

    @Slot(str)
    def _start_repass_confirmed(self, tid):
        self.tema_actual_label.setText(f"📍 Repaso: {tid}")
        self.chat_view.load_tema(tid)
        self._force_update()

    @Slot()
    def refrescar_listas_temas(self):
        curr = self.materias_list.currentItem()
        if curr: self._on_materia_selected(None)
        self._force_update()

    def _force_update(self):
        self.update();
        self.repaint();
        self.chat_view.update();
        QApplication.processEvents()

class LessonMenuView(QWidget):
    """
    Muestra la lista de lecciones (subtemas) de un Tema y permite seleccionar.
    """
    # Emite el ID del tema y el índice de la lección (0-based)
    leccion_seleccionada = Signal(str, int)
    regresar_a_dashboard = Signal()

    def __init__(self, usuario: Usuario, tema_id: str, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.tema_id = tema_id
        self.tema_obj: Optional[Tema] = None

        # Cargar el objeto Tema para obtener las lecciones
        if hasattr(core, "construir_tema"):
            self.tema_obj = core.construir_tema(tema_id)

        nombre_tema = NOMBRES_DE_TEMAS.get(tema_id, tema_id.title())

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(20)

        # Título
        titulo = QLabel(f"📚 Lecciones de: <b>{nombre_tema}</b>")
        titulo.setTextFormat(Qt.RichText)
        titulo.setStyleSheet("font-size:24px; font-weight:700; color:#38bdf8;")
        layout.addWidget(titulo)

        # Lista de lecciones
        self.lecciones_list = QListWidget()
        self.lecciones_list.setStyleSheet("""
            QListWidget { background: #1e293b; border: 1px solid #334155; border-radius: 10px; color: white; padding: 5px; }
            QListWidget::item { padding: 10px; }
            QListWidget::item:hover { background-color: #334155; border-radius: 8px; }
            QListWidget::item:selected { background-color: #1e40af; border-radius: 8px; color: white; font-weight: 600; }
        """)
        self.lecciones_list.setMinimumHeight(400)
        self.lecciones_list.itemClicked.connect(self._on_leccion_selected)

        layout.addWidget(self.lecciones_list, 1)

        # Botón de regreso
        btn_regresar = QPushButton("⬅️ Regresar al Dashboard")
        btn_regresar.setStyleSheet(ESTILOS["btn_explorar"].replace("14px", "12px"))
        btn_regresar.clicked.connect(self.regresar_a_dashboard.emit)
        layout.addWidget(btn_regresar)

        self._cargar_lecciones()

    def _cargar_lecciones(self):
        """Llena la lista con los subtemas."""
        self.lecciones_list.clear()

        if not self.tema_obj or not self.tema_obj.contenido_reforzamiento:
            item = QListWidgetItem("❌ No hay lecciones de reforzamiento definidas para este tema.")
            item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
            self.lecciones_list.addItem(item)
            return

        for i, leccion in enumerate(self.tema_obj.contenido_reforzamiento):
            subtema = leccion.get('subtema_titulo', f"Lección {i+1} (Sin Título)")
            item = QListWidgetItem(f"Lección {i+1}: {subtema}")
            item.setData(Qt.UserRole, i) # Guardar el índice
            self.lecciones_list.addItem(item)

    def _on_leccion_selected(self, item: QListWidgetItem):
        """Emite la señal para iniciar la lección."""
        leccion_index = item.data(Qt.UserRole)
        if leccion_index is not None:
            self.leccion_seleccionada.emit(self.tema_id, leccion_index)

# 🔥🔥🔥 NUEVA VISTA: EJECUCIÓN MANUAL DE LECCIÓN 🔥🔥🔥
class LessonView(QWidget):
    """
    Ejecuta el flujo de una sola lección del ChatView.
    """
    leccion_terminada = Signal(str) # Emite el tema_id para volver al LessonMenuView

    def __init__(self, usuario: Usuario, tema_id: str, leccion_idx: int, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.tema_id = tema_id
        self.leccion_idx = leccion_idx

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # Usamos una versión del ChatView para mostrar el contenido
        self.chat_view = ChatView(usuario)
        layout.addWidget(self.chat_view)

        self.tema_obj = None
        QTimer.singleShot(100, self._iniciar_leccion)

    def _iniciar_leccion(self):
        """Carga y muestra la lección seleccionada."""
        self.chat_view._clear_chat()

        if hasattr(core, "construir_tema"):
            self.tema_obj = core.construir_tema(self.tema_id)

        if not self.tema_obj:
            self.chat_view._add_message("❌ Error: No se pudo cargar el tema.", is_user=False)
            QTimer.singleShot(2000, lambda: self.leccion_terminada.emit(self.tema_id))
            return

        try:
            leccion = self.tema_obj.contenido_reforzamiento[self.leccion_idx]

            self._mostrar_contenido(leccion)

        except IndexError:
            self.chat_view._add_message(f"❌ Error: El índice de lección {self.leccion_idx + 1} no existe.", is_user=False)
            QTimer.singleShot(2000, lambda: self.leccion_terminada.emit(self.tema_id))

    def _mostrar_contenido(self, leccion: dict):
        """Muestra el contenido de la lección seleccionada (similar a ChatView.load_tema)."""

        # 1. Presentar Definición y Ejemplo
        titulo = f"<h2>📘 Lección {self.leccion_idx + 1}: {leccion.get('subtema_titulo', 'Sin Título')}</h2>"
        self.chat_view._add_message(titulo, is_user=False)

        definicion_html = f"<b>Definición:</b><br>{html.escape(leccion.get('definicion', '...'))}"
        self.chat_view._add_message(definicion_html, is_user=False)

        ejemplo_resuelto_text = leccion.get('ejemplo_resuelto', '...')
        ejemplo_contenido_html = html.escape(ejemplo_resuelto_text).replace('\n', '<br>')

        ejemplo_html = f"""
            <p style="margin: 0 0 5px 0; padding: 0; font-weight: bold;">--- 🧠 Ejemplo Resuelto ---</p>
            <div style="padding: 0; margin: 0; line-height: 1.4; word-wrap: break-word;">
            {ejemplo_contenido_html}
            </div>
            """
        self.chat_view._add_message(ejemplo_html, is_user=False)

        # 2. Presentar el ejercicio
        ejercicio_base = leccion.get('ejercicio', {})
        self.chat_view._datos_ejercicio_actual = {
            "enunciado": ejercicio_base.get('enunciado', ''),
            "respuesta_correcta": ejercicio_base.get('respuesta_correcta', ''),
            "opciones": ejercicio_base.get('opciones', []),
            "es_recuperacion": False
        }

        self.chat_view._similares_pendientes = [] # Desactivar similares en modo manual

        self.chat_view._presentar_ejercicio_actual() # Inicia el ciclo de pregunta/respuesta

        # 3. Al terminar el ejercicio, el ChatView llama a _mostrar_aplicacion_y_avanzar.
        #    Debemos reemplazar ese comportamiento para que emita la señal.
        self.chat_view._mostrar_aplicacion_y_avanzar = self._override_aplicacion_y_avanzar
        self.chat_view.tema_completado.connect(lambda: self.leccion_terminada.emit(self.tema_id))

    def _override_aplicacion_y_avanzar(self):
        """Sobreescribe la función original de ChatView para emitir la señal."""
        # Mostrar la aplicación de carrera
        leccion = self.tema_obj.contenido_reforzamiento[self.leccion_idx]
        carrera_usuario = self.usuario.carrera

        app_html = "<h3>¿Por qué es importante esto para tu carrera?</h3>"

        aplicaciones = leccion.get('aplicaciones', {})
        if carrera_usuario in aplicaciones:
            app = aplicaciones[carrera_usuario]
            app_html += (
                f"💡 <b>En Ing. {carrera_usuario.title()}:</b><br>"
                f"<b>Uso:</b> {html.escape(app.get('uso', '...'))}<br><br>"
                f"<b>Consecuencia de un error:</b> {html.escape(app.get('consecuencia_de_error', '...'))}"
            )
        else:
            app_generica = aplicaciones.get('sistemas', {})
            app_html += (
                f"💡 <b>Aplicación (Ej. Ing. Sistemas):</b><br>"
                f"<b>Uso:</b> {html.escape(app_generica.get('uso', '...'))}<br><br>"
                f"<b>Consecuencia de un error:</b> {html.escape(app_generica.get('consecuencia_de_error', '...'))}"
            )

        self.chat_view._add_message(app_html, is_user=False)
        self.chat_view._add_message("✅ <b>Lección Finalizada.</b> Regresando al menú de lecciones...", is_user=False)

        # Emitir la señal de finalización
        QTimer.singleShot(3000, lambda: self.leccion_terminada.emit(self.tema_id))


def _resumen_local(progreso: dict) -> dict:
    """Función de respaldo en caso de que core.obtener_resumen_progreso falle."""
    dominados = len(progreso)
    total = len(NOMBRES_DE_TEMAS) if NOMBRES_DE_TEMAS else 1
    porc = (dominados / total) * 100 if total > 0 else 0
    return {"porcentaje": porc, "temas_dominados": dominados, "total_temas": total}


# ------------------------------- MainWindow ------------------------------
# (PreguntaDiagnosticoView, BienvenidaDashboardView)
# (Estas clases son idénticas a las que subiste, omitidas por brevedad)

class PreguntaDiagnosticoView(QWidget):
    """Pantalla intermedia que pregunta si el usuario quiere hacer el diagnóstico inicial."""
    diagnostico_si = Signal(Usuario)
    diagnostico_no = Signal(Usuario)

    def __init__(self, usuario: Usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        layout = QVBoxLayout(self)
        layout.setContentsMargins(60, 60, 60, 60)
        layout.setSpacing(20)
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #1e293b;
                border-radius: 20px;
                border: 1px solid #334155;
                padding: 30px;
            }
        """)
        cv = QVBoxLayout(card)
        cv.setContentsMargins(40, 40, 40, 40)
        cv.setSpacing(18)
        title = QLabel("Examen Diagnóstico Inicial")
        title.setStyleSheet("font-size:30px; font-weight:800; color:#38bdf8;")
        title.setAlignment(Qt.AlignCenter)
        cv.addWidget(title)
        subtitle = QLabel(
            f"¡Hola {usuario.nombre}! 👋<br><br>"
            "¿Te gustaría realizar un <b>examen diagnóstico</b> para medir tus conocimientos iniciales?"
            "<br><br>Este examen te ayudará a personalizar tu ruta de aprendizaje en MAHA"
        )
        subtitle.setTextFormat(Qt.RichText)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("color:#e2e8f0; font-size:18px; line-height:1.6em;")
        cv.addWidget(subtitle)
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(30)
        btn_layout.setAlignment(Qt.AlignCenter)
        btn_si = QPushButton("Realizar Diagnóstico")
        btn_no = QPushButton("Ir directo al Dashboard")
        btn_si.setStyleSheet("""
            QPushButton {
                background-color: #0ea5e9;
                color: white;
                border-radius: 12px;
                padding: 10px 18px;
                font-weight: 600;
                font-size: 15px;
            }
            QPushButton:hover { background-color: #38bdf8; }
        """)
        btn_no.setStyleSheet("""
            QPushButton {
                background-color: #334155;
                color: #e2e8f0;
                border-radius: 12px;
                padding: 10px 18px;
                font-weight: 600;
                font-size: 15px;
            }
            QPushButton:hover { background-color: #475569; }
        """)
        btn_si.clicked.connect(lambda: self.diagnostico_si.emit(self.usuario))
        btn_no.clicked.connect(lambda: self.diagnostico_no.emit(self.usuario))
        btn_layout.addWidget(btn_si)
        btn_layout.addWidget(btn_no)
        cv.addLayout(btn_layout)

        layout.addWidget(card, 0, Qt.AlignCenter)
        self.setStyleSheet("background-color: #0b1020;")


from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal, QSize, QTimer
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QColor

from PERFILES import cargar_perfil  # Asumimos esta importación
from UTILIDADES import limpiar_texto  # Asumimos esta importación
from dataclasses import dataclass
from typing import Dict, Optional


# Definición de la clase Usuario de tu propio código para un mejor tipado
@dataclass
class Usuario:
    nombre: str
    carrera: str
    progreso: Dict[str, str]


# --- Estilos CSS Centralizados ---
ESTILOS = {
    "contenedor_principal": "background-color:#0b1020;",
    "tarjeta": """
        QFrame {
            background-color: #111827;
            border-radius: 22px;
            border: 1px solid #1e293b;
            padding: 40px 60px;
        }
    """,
    "foto_base": "font-size:48px; background:#1e293b; border-radius:60px; color: #94a3b8;",
    "nombre": "font-size:24px; font-weight:800; color:#f8fafc; margin-top:10px;",
    "carrera": "font-size:16px; color:#93c5fd; margin-bottom:12px;",
    "mensaje": "color:#e2e8f0; font-size:16px; line-height:1.6em; padding: 8px 20px;",
    "btn_empezar": """
        QPushButton {
            background-color: #0ea5e9; color: white; border-radius: 14px; 
            padding: 12px 26px; font-size:15px; font-weight:600;
        }
        QPushButton:hover { background-color: #38bdf8; }
    """,
    "btn_explorar": """
        QPushButton {
            background-color: #334155; color: #e2e8f0; border-radius: 14px; 
            padding: 12px 26px; font-size:15px; font-weight:600;
        }
        QPushButton:hover { background-color: #475569; }
    """
}

# --- Mapeo de Carreras ---
MAPA_DISPLAY_CARRERAS = {
    "sistemas": "Ingeniería en Cibernética y Sistemas Computacionales",
    "mecanica": "Ingeniería Mecánica",
    "electrica": "Ingeniería Eléctrica",
    "civil": "Ingeniería Civil",
    "mecatronica": "Ingeniería Mecatrónica",
    "aeronautica": "Ingeniería Aeronáutica",
    "quimica": "Ingeniería Química"
}




class BienvenidaDashboardView(QWidget):

    empezar = Signal(object)
    explorar = Signal(object)

    FOTO_SIZE = 120

    def __init__(self, usuario: Usuario, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setAttribute(Qt.WA_StyledBackground, True)

        # --- ESTILOS ---
        self.setStyleSheet("""
            BienvenidaDashboardView {
                background-color: #0b1020; 
            }
            QLabel {
                color: #334155;
                background: transparent;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)

        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.setContentsMargins(20, 20, 20, 20)
        central_layout.setAlignment(Qt.AlignCenter)

        # --- TARJETA ---
        self.card = QFrame()
        self.card.setObjectName("MainCard")
        self.card.setFixedWidth(650)
        self.card.setStyleSheet("""
            QFrame#MainCard {
                background-color: #111827; 
                border: 1px solid #374151;
                border-radius: 24px;
            }
        """)

        card_layout = QVBoxLayout(self.card)
        card_layout.setContentsMargins(50, 60, 50, 60)
        card_layout.setSpacing(25)
        card_layout.setAlignment(Qt.AlignCenter)

        # 1. FOTO
        self.lbl_foto = QLabel("👤")
        self.lbl_foto.setFixedSize(self.FOTO_SIZE, self.FOTO_SIZE)
        self.lbl_foto.setAlignment(Qt.AlignCenter)
        self.lbl_foto.setStyleSheet(f"""
            background-color: #1f2937;
            border-radius: {self.FOTO_SIZE // 2}px;
            border: 2px solid #38bdf8;
            color: #94a3b8;
            font-size: 48px;
        """)

        h_foto = QHBoxLayout()
        h_foto.addStretch()
        h_foto.addWidget(self.lbl_foto)
        h_foto.addStretch()
        card_layout.addLayout(h_foto)

        # 2. NOMBRE Y CARRERA
        lbl_nombre = QLabel(self.usuario.nombre)
        lbl_nombre.setAlignment(Qt.AlignCenter)
        lbl_nombre.setStyleSheet("font-size: 32px; font-weight: 800; color: #f8fafc; margin-top: 10px;")
        card_layout.addWidget(lbl_nombre)

        nombre_carrera = self.usuario.carrera.title()
        if self.usuario.carrera == "sistemas": nombre_carrera = "Ing. Cibernética y Sistemas Computacionales"

        lbl_carrera = QLabel(nombre_carrera)
        lbl_carrera.setAlignment(Qt.AlignCenter)
        lbl_carrera.setStyleSheet("font-size: 18px; color: #38bdf8; font-weight: 600; letter-spacing: 0.5px;")
        card_layout.addWidget(lbl_carrera)

        # 3. MENSAJES
        es_admin = any(s == "dominado_por_admin" for s in self.usuario.progreso.values())

        if es_admin:
            titulo_msg = "🔓 ACCESO TOTAL MAESTRO"
            cuerpo_msg = (
                "Modo Administrador activo. Tienes el control absoluto del mapa curricular.<br>"
                "Explora Matemáticas, Física, Química y Programación libremente."
            )
            icono_msg = "⚡"
        else:
            titulo_msg = "🚀 TU TRAYECTORIA PERSONALIZADA ESTÁ LISTA"
            cuerpo_msg = (
                "Hemos optimizado tu ruta de aprendizaje.<br>"
                "Domina las ciencias exactas y la programación fundamentales para tu ingeniería."
            )
            icono_msg = "🎓"

        mensaje_html = (
            f"<p style='font-size: 40px; margin:0; padding:0;'>{icono_msg}</p>"
            f"<p style='font-size: 20px; font-weight: bold; color: #e2e8f0; margin-bottom: 5px;'>{titulo_msg}</p>"
            f"<p style='font-size: 15px; color: #94a3b8; line-height: 1.5;'>{cuerpo_msg}</p>"
        )

        lbl_msg = QLabel(mensaje_html)
        lbl_msg.setAlignment(Qt.AlignCenter)
        lbl_msg.setWordWrap(True)
        card_layout.addWidget(lbl_msg)

        card_layout.addSpacing(15)

        # 4. BOTÓN
        btn_empezar = QPushButton("Comenzar Aventura")
        btn_empezar.setCursor(Qt.PointingHandCursor)
        btn_empezar.setFixedSize(240, 60)
        btn_empezar.setStyleSheet("""
            QPushButton {
                background-color: #0ea5e9;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 18px;
                font-weight: 700;
            }
            QPushButton:hover {
                background-color: #0284c7;
                margin-top: 2px;
            }
            QPushButton:pressed {
                background-color: #0369a1;
            }
        """)
        btn_empezar.clicked.connect(lambda: self.empezar.emit(self.usuario))

        h_btn = QHBoxLayout()
        h_btn.addStretch()
        h_btn.addWidget(btn_empezar)
        h_btn.addStretch()
        card_layout.addLayout(h_btn)

        central_layout.addWidget(self.card)
        layout.addWidget(central_widget)

        QTimer.singleShot(50, self._cargar_foto)

    def _cargar_foto(self):
        """Carga la foto de perfil si existe."""
        try:
            datos = cargar_perfil(self.usuario.nombre)
            path = datos.get("foto") if datos else None

            if path and os.path.exists(path):
                pix = QPixmap(path)
                if not pix.isNull():
                    size = self.FOTO_SIZE
                    # 🔥 CORRECCIÓN AQUÍ: Usamos 'circ' consistentemente
                    circ = QPixmap(size, size)
                    circ.fill(Qt.transparent)

                    p = QPainter(circ)
                    p.setRenderHint(QPainter.Antialiasing, True)
                    p.setRenderHint(QPainter.SmoothPixmapTransform, True)

                    path_draw = QPainterPath()
                    path_draw.addEllipse(0, 0, size, size)
                    p.setClipPath(path_draw)

                    p.drawPixmap(0, 0, pix.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
                    p.end()

                    self.lbl_foto.setPixmap(circ)  # Ahora usamos 'circ'
                    self.lbl_foto.setText("")
                    self.lbl_foto.setStyleSheet(f"background: transparent; border: none;")
        except Exception as e:
            print(f"Error cargando foto: {e}")


# ARCHIVO: INTERFAZ.py

# ARCHIVO: INTERFAZ.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MAHA · Interfaz")
        self.setMinimumSize(QSize(1280, 720))
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.viewWelcome = WelcomeView()
        self.viewAuth = AuthInline("registro")

        self.viewDashboard = None
        self.viewPreguntaDiag = None
        self.diag_view = None
        self.viewBienvenidaDash = None
        self.viewGrafo = None

        self.viewWelcome.startRegister.connect(lambda: self._swap_auth("registro"))
        self.viewWelcome.startLogin.connect(lambda: self._swap_auth("inicio"))
        self.stack.addWidget(self.viewWelcome)
        self.stack.addWidget(self.viewAuth)

        self.viewAuth.accepted.connect(self._on_user_ready)
        self.viewAuth.canceled.connect(self._back_to_welcome)
        self._make_menu()

    def _make_menu(self):
        b = self.menuBar();
        b.setStyleSheet("background:#0b1020;color:white;")
        m = b.addMenu("Archivo")
        m.addAction("Inicio", self._back_to_welcome)
        m.addAction("Salir", self.close)

    def _fade_to(self, w):
        self.stack.setCurrentWidget(w)
        e = QGraphicsOpacityEffect(w);
        w.setGraphicsEffect(e)
        a = QPropertyAnimation(e, b"opacity", self);
        a.setDuration(280);
        a.setStartValue(0);
        a.setEndValue(1)
        a.setEasingCurve(QEasingCurve.OutCubic);
        a.start(QPropertyAnimation.DeleteWhenStopped)

    def _show_with_fade(self, w):
        if self.stack.indexOf(w) == -1: self.stack.addWidget(w)
        self.stack.setCurrentWidget(w)
        e = QGraphicsOpacityEffect(w);
        w.setGraphicsEffect(e);
        e.setOpacity(0)
        a = QPropertyAnimation(e, b"opacity", self);
        a.setDuration(280);
        a.setStartValue(0);
        a.setEndValue(1)
        a.setEasingCurve(QEasingCurve.OutCubic);
        a.start(QPropertyAnimation.DeleteWhenStopped)

    def _swap_auth(self, m):
        if self.stack.indexOf(self.viewAuth) != -1: self.stack.removeWidget(self.viewAuth); self.viewAuth.deleteLater()
        self.viewAuth = AuthInline(m)
        self.viewAuth.accepted.connect(self._on_user_ready)
        self.viewAuth.canceled.connect(self._back_to_welcome)
        self.stack.insertWidget(1, self.viewAuth)
        self._show_with_fade(self.viewAuth)
        QTimer.singleShot(0, self.viewAuth._recalcular_layout)

    @Slot()
    def _back_to_welcome(self):
        for v in [self.viewDashboard, self.viewPreguntaDiag, self.diag_view, self.viewBienvenidaDash, self.viewGrafo]:
            if v and self.stack.indexOf(v) != -1: self.stack.removeWidget(v); v.deleteLater()
        self.viewDashboard = None;
        self.viewPreguntaDiag = None
        self._fade_to(self.viewWelcome)

    @Slot(Usuario)
    def _on_user_ready(self, usuario: Usuario):
        # 1. Admin
        if any(s == "dominado_por_admin" for s in usuario.progreso.values()):
            self._mostrar_bienvenida_dashboard(usuario);
            return

        # 2. Verificar archivo real para ver si ya tiene configuración
        datos_reales = cargar_perfil(usuario.nombre)

        # Si tiene 'orden_materias', ya pasó por el diagnóstico (o lo saltó)
        ya_configurado = datos_reales and "orden_materias" in datos_reales

        if ya_configurado:
            print("📂 Configuración encontrada. Yendo al Dashboard.")
            self._mostrar_bienvenida_dashboard(usuario)
        else:
            print("🆕 Sin configuración. Ofreciendo diagnóstico.")
            self.viewPreguntaDiag = PreguntaDiagnosticoView(usuario)
            self.stack.addWidget(self.viewPreguntaDiag)
            self._fade_to(self.viewPreguntaDiag)
            self.viewPreguntaDiag.diagnostico_si.connect(self._mostrar_diagnostico)
            self.viewPreguntaDiag.diagnostico_no.connect(self._saltar_diagnostico)

    @Slot(Usuario)
    def _saltar_diagnostico(self, usuario):
        # Guardar configuración por defecto para que no vuelva a preguntar
        defs = sorted(list(core.RUTAS_POR_MATERIA.keys()))
        d = {"nombre": usuario.nombre, "carrera": usuario.carrera, "progreso": usuario.progreso,
             "orden_materias": defs, "puntajes_diagnostico": {}}
        guardar_perfil(usuario.nombre, d)
        self._mostrar_bienvenida_dashboard(usuario)

    @Slot(Usuario)
    def _mostrar_bienvenida_dashboard(self, usuario):
        self.viewBienvenidaDash = BienvenidaDashboardView(usuario)
        self.stack.addWidget(self.viewBienvenidaDash)
        self._fade_to(self.viewBienvenidaDash)
        self.viewBienvenidaDash.empezar.connect(lambda u: self._continuar_dashboard(u, False))

    @Slot(Usuario)
    def _mostrar_diagnostico(self, usuario):
        self.diag_view = DiagnosticoView(usuario)
        self.stack.addWidget(self.diag_view)
        self._fade_to(self.diag_view)
        self.diag_view.terminado.connect(lambda prog: (
            setattr(self.diag_view.usuario, 'progreso', prog),
            self._mostrar_bienvenida_dashboard(self.diag_view.usuario)
        ))

    @Slot(Usuario, bool)
    @Slot(Usuario, bool)
    def _continuar_dashboard(self, usuario: Usuario, auto: bool):
        """
        Muestra el Dashboard, conecta señales y presenta la bienvenida
        con los resultados del diagnóstico en el chat.
        """
        # 1. CONFIGURACIÓN TÉCNICA
        if self.viewDashboard is None:
            self.viewDashboard = Dashboard(usuario)

            # Conexiones de señales vitales
            self.viewDashboard.salir_signal.connect(self._back_to_welcome)
            self.viewDashboard.ver_mapa_signal.connect(self._mostrar_mapa)
            self.viewDashboard.solicitar_lecciones.connect(
                self.viewDashboard.chat_view.presentar_menu_lecciones
            )

            self.stack.addWidget(self.viewDashboard)

        self._fade_to(self.viewDashboard)
        self.viewDashboard._force_update()
        self.viewDashboard.refrescar_listas_temas()

        # 2. PREPARAR MENSAJE DE BIENVENIDA (Combina saludo + resultados)
        self.viewDashboard.chat_view._clear_chat()
        self.viewDashboard.chat_view._hide_input()

        # A) Saludo e Instrucciones
        texto_bienvenida = (
            f"<div style='font-size:24px; margin-bottom:10px;'>👋 <b>¡Bienvenido al Panel, {usuario.nombre}!</b></div>"
            "<div style='font-size:16px; line-height:1.6; margin-bottom:15px;'>"
            "Este es tu centro de comando para el aprendizaje de ingeniería."
            "</div>"
        )
        texto_navegacion = (
            "<div style='font-size:16px; line-height:1.6; margin-bottom:15px; color:#cbd5e1;'>"
            "👈 <b>A tu izquierda</b> encontrarás el menú completo de <b>Materias y Temas</b>. "
            "Desde ahí podrás seleccionar cualquier módulo para ver sus lecciones, ejercicios y aplicaciones prácticas."
            "</div>"
            "<hr style='margin:15px 0; border:1px solid #334155;'>"
        )

        # B) Cargar datos para la Tabla de Resultados
        datos = cargar_perfil(usuario.nombre)
        puntajes = datos.get("puntajes_diagnostico", {})
        orden = datos.get("orden_materias", [])

        # C) Construir el cierre del mensaje
        if orden and puntajes:
            # Si hizo diagnóstico, mostramos la tabla
            tabla_html = "<div style='font-size:18px; margin-bottom:10px;'><b>📉 Tus Resultados del Diagnóstico:</b></div>"
            tabla_html += "<table style='width:100%; font-size:16px; border-collapse: collapse;'>"

            for mat in orden:
                pts = puntajes.get(mat, 3)
                if pts == 0:
                    estado, icono = "<span style='color:#EF4444'><b>CRÍTICO (0/3)</b></span>", "🔴"
                elif pts == 1:
                    estado, icono = "<span style='color:#F97316'><b>ALTA PRIORIDAD (1/3)</b></span>", "🟠"
                elif pts == 2:
                    estado, icono = "<span style='color:#FCD34D'><b>MEDIA (2/3)</b></span>", "🟡"
                else:
                    estado, icono = "<span style='color:#22C55E'><b>DOMINADO (3/3)</b></span>", "🟢"

                nombre_m = mat.title()
                if mat == "MATEMATICAS":
                    nombre_m = "Matemáticas"
                elif mat == "FISICA":
                    nombre_m = "Física"
                elif mat == "QUIMICA":
                    nombre_m = "Química"
                elif mat == "PROGRAMACION":
                    nombre_m = "Programación"

                tabla_html += f"<tr><td style='padding:6px;'>{icono} {nombre_m}</td><td style='padding:6px; text-align:right;'>{estado}</td></tr>"

            tabla_html += "</table>"

            texto_cierre = (
                f"{tabla_html}"
                "<div style='font-size:16px; margin-top:20px; color:#e2e8f0;'>"
                "Hemos reordenado la lista de materias según tu desempeño.<br>"
                "<b>Te recomendamos comenzar por la primera materia marcada en Rojo (🔴).</b>"
                "</div>"
            )
        else:
            # Si no hay diagnóstico (Admin o saltado)
            texto_cierre = (
                "<div style='font-size:16px; margin-top:10px;'>"
                "Tu ruta de aprendizaje está libre y desbloqueada.<br>"
                "¡Selecciona cualquier tema para comenzar!"
                "</div>"
            )

        # 3. MOSTRAR MENSAJE FINAL
        mensaje_final = texto_bienvenida + texto_navegacion + texto_cierre
        self.viewDashboard.chat_view._add_message(mensaje_final, is_user=False)

    @Slot()
    def _mostrar_mapa(self):
        if not self.viewDashboard: return
        if self.viewGrafo: self.stack.removeWidget(self.viewGrafo); self.viewGrafo.deleteLater()
        self.viewGrafo = GrafoView(self.viewDashboard.usuario)
        self.viewGrafo.regresar.connect(self._regresar_a_dashboard)
        self.stack.addWidget(self.viewGrafo)
        self._fade_to(self.viewGrafo)

    @Slot()
    def _regresar_a_dashboard(self):
        if self.viewDashboard:
            self._fade_to(self.viewDashboard)
            self.viewDashboard.refrescar_listas_temas()


# ------------------------------- run -------------------------------------

def run():
    app = QApplication.instance() or QApplication(sys.argv)
    app.setStyleSheet(app_stylesheet())
    win = MainWindow()
    win.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(run())