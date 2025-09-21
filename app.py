import streamlit as st
from lessons.lesson_basics import lesson as basics_lesson
# Aquí importarías tus otras lecciones a medida que las crees
# from lessons.hash_evidence import lesson as hash_lesson

# --- Configuración de la Página ---
st.set_page_config(layout="wide", page_title="Simulador Pythonless")

# --- Funciones para dibujar la interfaz ---

def render_code_view(code, active_line):
    lines = code.split('\\n')
    formatted_code = ""
    for i, line in enumerate(lines, 1):
        # Añade un marcador y un color sutil a la línea activa
        if i == active_line:
            formatted_code += f"{i:02d} > {line.strip()}\\n"
        else:
            formatted_code += f"{i:02d}   {line.strip()}\\n"
    st.code(formatted_code, language="python")

def render_state_view(state):
    if not state: # Si no hay 'state' en el paso, no mostrar nada
        return

    globals_state = state.get("globals", {})
    io_state = state.get("io", {})
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Variables")
        st.json(globals_state) if globals_state else st.write("—")
    with col2:
        st.subheader("Pila de llamadas")
        st.write("—") # Simplificado por ahora
    with col3:
        st.subheader("IO / Logs")
        st.json(io_state) if io_state else st.write("—")

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

# --- Lógica Principal de la Aplicación ---

st.title("Simulador Pythonless")
st.markdown("Una herramienta para entender la lógica de Python, aplicada al Derecho y Blockchain, **sin ejecutar código real**.")

# Diccionario para seleccionar las lecciones
lessons = {
    "Sintaxis Básica y Variables": basics_lesson,
    # "Acta de Evidencia (Hash)": hash_lesson, # Descomenta esto cuando crees el archivo
}

selected_lesson_title = st.selectbox("Selecciona una lección:", list(lessons.keys()))
lesson = lessons[selected_lesson_title]

# Usamos st.session_state para recordar el paso en el que estamos
session_key = f'step_{selected_lesson_title}'
if session_key not in st.session_state:
    st.session_state[session_key] = 0

step_idx = st.session_state[session_key]
current_step_data = lesson["steps"][step_idx]
total_steps = len(lesson["steps"])

st.markdown("---")

# Controles de navegación (botones y contador de pasos)
nav_cols = st.columns([1, 1, 8])
if nav_cols[0].button("⬅️ Anterior"):
    st.session_state[session_key] = max(0, step_idx - 1)
    st.rerun()

if nav_cols[1].button("Siguiente ➡️"):
    st.session_state[session_key] = min(total_steps - 1, step_idx + 1)
    st.rerun()

nav_cols[2].write(f"**Paso {step_idx + 1} de {total_steps}**")

# Dibujamos todos los componentes en la pantalla
render_code_view(lesson["code"], current_step_data["highlight"]["line"])
st.markdown("---")
render_explain_cards(current_step_data)
st.markdown("---")
render_state_view(current_step_data.get("state"))
