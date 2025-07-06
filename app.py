import streamlit as st
import pandas as pd
from collections import defaultdict

# Cargar base de datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("peliculas_nolan_con_imagenes.csv")

df = cargar_datos()

# Configuración inicial
st.set_page_config(page_title="Test Nolan", page_icon="🎬")
st.title("Test de Personalidad: ¿Qué película de Nolan eres tú?")

# Estado inicial
if "inicio" not in st.session_state:
    st.session_state.inicio = True
if "pregunta" not in st.session_state:
    st.session_state.pregunta = 1
    st.session_state.puntajes = defaultdict(int)

# Frases por película
frases = {
    "Inception": "Eres creativo, complejo y vives entre ideas profundas.",
    "Interstellar": "Eres curioso, sentimental y amas lo desconocido.",
    "Memento": "Valoras la verdad, incluso si duele. Tu mente nunca descansa.",
    "The Prestige": "Eres perfeccionista, apasionado y algo misterioso.",
    "Tenet": "Te encanta el caos ordenado. Piensas en 4 dimensiones.",
    "Dunkirk": "Eres realista, valiente y directo. El silencio también te dice mucho.",
    "The Dark Knight": "Tienes un fuerte sentido de justicia, aunque luchas con tu oscuridad.",
    "Oppenheimer": "Eres reflexivo, profundo y te cuestionas el impacto de tus decisiones."
}

# Pantalla de bienvenida
if st.session_state.inicio:
    nombre = st.text_input("¿Cómo te llamas?")
    conoce = st.radio("¿Conoces a Christopher Nolan?", ["Sí", "No"])
    if st.button("Comenzar"):
        st.session_state.inicio = False
    st.markdown("Christopher Nolan es un director conocido por películas complejas y con mensaje profundo. Este test te dirá cuál te representa más.")
    st.stop()

# Preguntas
preguntas = {
    1: {"texto": "¿Qué tema te interesa más?", "opciones": {
        "Sueños": ["Inception"],
        "Espacio y tiempo": ["Interstellar", "Tenet"],
        "Memoria": ["Memento"],
        "Ciencia": ["Oppenheimer"],
        "Magia": ["The Prestige"],
        "Guerra": ["Dunkirk"],
        "Caos": ["The Dark Knight"]}},
    2: {"texto": "¿Qué emoción prefieres?", "opciones": {
        "Confusión": ["Memento", "Tenet"],
        "Asombro": ["Interstellar", "Inception"],
        "Tensión": ["Dunkirk", "The Dark Knight"],
        "Reflexión": ["Oppenheimer"]}},
    3: {"texto": "¿Qué tipo de protagonista prefieres?", "opciones": {
        "Con traumas": ["Inception", "Memento"],
        "Exploradores": ["Interstellar"],
        "Héroes": ["The Dark Knight"],
        "Obsesivos": ["The Prestige", "Tenet"]}},
    4: {"texto": "¿Conoces a estos actores?", "opciones": {
        "DiCaprio": ["Inception"],
        "Murphy": ["Oppenheimer", "Dunkirk"],
        "Bale": ["The Prestige", "The Dark Knight"]}, "multiple": True},
    5: {"texto": "¿Qué estilo visual prefieres?", "opciones": {
        "Bélico": ["Dunkirk"],
        "Espacial": ["Interstellar"],
        "Teatral": ["The Prestige"],
        "Urbano": ["Inception"]}}
}

# Mostrar pregunta actual
p = st.session_state.pregunta
if p <= len(preguntas):
    q = preguntas[p]
    st.markdown(f"### Pregunta {p}: {q['texto']}")
    if q.get("multiple"):
        seleccion = st.multiselect("Selecciona todas:", list(q["opciones"].keys()))
    else:
        seleccion = st.radio("Selecciona una:", list(q["opciones"].keys()))

    if st.button("Siguiente"):
        if seleccion:
            if isinstance(seleccion, list):
                for s in seleccion:
                    for peli in q["opciones"][s]:
                        st.session_state.puntajes[peli] += 1
            else:
                for peli in q["opciones"][seleccion]:
                    st.session_state.puntajes[peli] += 1
            st.session_state.pregunta += 1
            st.experimental_rerun()
        else:
            st.warning("Selecciona una opción para continuar.")

# Mostrar resultado
if p > len(preguntas):
    st.success("¡Test completado!")
    resultado = max(st.session_state.puntajes, key=st.session_state.puntajes.get)
    peli = df[df["Título"] == resultado].iloc[0]

    st.image(peli["Imagen"], use_container_width=True)
    st.markdown(f"## {peli['Título']} ({peli['Año']})")
    st.write(f"**Género:** {peli['Género']}")
    st.write(f"**Sinopsis:** {peli['Sinopsis']}")
    st.markdown(f"[Ver trailer]({peli['Enlace']})")
    st.info(frases.get(peli['Título'], ""))

    if st.button("Reiniciar"):
        st.session_state.pregunta = 1
        st.session_state.puntajes = defaultdict(int)
        st.session_state.inicio = True
        st.experimental_rerun()
