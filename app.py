import streamlit as st

# --- Importar TODAS las Lecciones Creadas ---
# (Asegúrate de que todos los archivos .py de lecciones existen en la carpeta 'lessons')
from lessons.lesson_basics import lesson as lesson_01
from lessons.lesson_data_types import lesson as lesson_02
from lessons.lesson_03_lists_tuples import lesson as lesson_03
from lessons.lesson_04_dicts_sets import lesson as lesson_04
from lessons.lesson_05_conditionals import lesson as lesson_05
from lessons.lesson_06_loops import lesson as lesson_06
from lessons.lesson_07_functions import lesson as lesson_07
from lessons.lesson_08_modules import lesson as lesson_08
from lessons.lesson_09_exceptions import lesson as lesson_09
from lessons.lesson_10_oop_intro import lesson as lesson_10
from lessons.lesson_11_oop_inheritance import lesson as lesson_11
from lessons.lesson_12_list_comprehensions import lesson as lesson_12
from lessons.lesson_13_regex import lesson as lesson_13
from lessons.lesson_14_lambdas import lesson as lesson_14
from lessons.lesson_15_environments import lesson as lesson_15
from lessons.lesson_16_pip import lesson as lesson_16
from lessons.lesson_17_testing import lesson as lesson_17
from lessons.lesson_18_static_typing import lesson as lesson_18

# --- Configuración de la Página ---
st.set_page_config(layout="wide", page_title="Simulador Pythonless")

# --- Funciones para "Renderizar" Componentes ---

def render_code_view(code, active_line):
    lines = code.split('\n')
    formatted_code = ""
    for i, line in enumerate(lines, 1):
        if i == active_line:
            formatted_code += f"{i:02d} > {line.strip()}\n"
        else:
            formatted_code += f"{i:02d}   {line.strip()}\n"
    st.code(formatted_code, language="python")

# --- FUNCIÓN CORREGIDA ---
def render_state_view(state):
    # Si el paso no tiene estado, no dibujamos nada.
    if not state:
        return

    globals_state = state.get("globals", {})
    io_state = state.get("io", {})
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Variables")
        if globals_state:
            st.json(globals_state) # Llama a st.json() directamente, sin print()
        else:
            st.write("—")
    with col2:
        st.subheader("Pila de llamadas")
        st.write("—") # Simplificado por ahora
    with col3:
        st.subheader("IO / Logs")
        if io_state:
            st.json(io_state) # Llama a st.json() directamente, sin print()
        else:
            st.write("—")

def render_explain_cards(step):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info(f"**Qué hace:** {step['what']}")
    with col2:
        st.success(f"**Por qué importa:** {step['why']}")
    with col3:
        st.warning(f"**Aplicación en Datos:** {step['appData']}")
    with col4:
        st.error(f"**Aplicación en Derecho:** {step['appLaw']}")

# --- Aplicación Principal ---

st.title("Simulador Pythonless")
st.markdown("Una herramienta para entender la lógica de Python, aplicada al Derecho y Blockchain, **sin ejecutar código real**.")

# Diccionario con TODAS las lecciones
lessons = {
    "1: Sintaxis y Variables": lesson_01,
    "2: Tipos de Datos": lesson_02,
    "3: Listas y Tuplas": lesson_03,
    "4: Diccionarios y Conjuntos": lesson_04,
    "5: Condicionales (If/Else)": lesson_05,
    "6: Bucles (For/While)": lesson_06,
    "7: Funciones": lesson_07,
    "8: Módulos": lesson_08,
    "9: Manejo de Excepciones": lesson_09,
    "10: Clases y Objetos (OOP)": lesson_10,
    "11: Herencia (OOP)": lesson_11,
    "12: List Comprehensions": lesson_12,
    "13: Expresiones Regulares (RegEx)": lesson_13,
    "14: Lambdas": lesson_14,
    "15: Entornos Virtuales": lesson_15,
    "16: Gestores de Paquetes (Pip)": lesson_16,
    "17: Testing (Pruebas Unitarias)": lesson_17,
    "18: Tipado Estático (Pydantic)": lesson_18,
}

# Selector para elegir la lección
selected_lesson_title = st.selectbox("Selecciona una lección para comenzar:", list(lessons.keys()))
lesson = lessons[selected_lesson_title]

# Usamos el estado de la sesión para recordar el paso actual de CADA lección
session_key = f'step_{selected_lesson_title}'
if session_key not in st.session_state:
    st.session_state[session_key] = 0

step_idx = st.session_state[session_key]
if step_idx >= len(lesson["steps"]):
    st.session_state[session_key] = 0
    step_idx = 0

current_step_data = lesson["steps"][step_idx]
total_steps = len(lesson["steps"])

st.markdown("---")
st.header(lesson["title"])
st.caption(lesson["description"])

# Controles de navegación y contador
nav_cols = st.columns([1, 1, 8])
if nav_cols[0].button("⬅️ Anterior"):
    st.session_state[session_key] = max(0, step_idx - 1)
    st.rerun()

if nav_cols[1].button("Siguiente ➡️"):
    st.session_state[session_key] = min(total_steps - 1, step_idx + 1)
    st.rerun()

nav_cols[2].write(f"**Paso {step_idx + 1} de {total_steps}**")

# Renderizado de los componentes visuales
render_code_view(lesson["code"], current_step_data["highlight"]["line"])
st.markdown("---")
render_explain_cards(current_step_data)
st.markdown("---")
render_state_view(current_step_data.get("state"))
