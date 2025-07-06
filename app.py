import streamlit as st
import pandas as pd
from collections import defaultdict

# Fondo con imagen de cielo nocturno estrellado
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://wallpapers.com/images/featured/fondos-solidos-morados-6m27kn7or229vcaa.jpg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        background-color: #0b0c10;  /* color oscuro de respaldo */
    }
    </style>
""", unsafe_allow_html=True)

# Cargar base de datos
df = pd.read_csv("peliculas_nolan_con_imagenes.csv")

# Cargar críticas desde archivo CSV
criticas_df = pd.read_csv("criticas_nolan.csv")

# Configuración de página
st.set_page_config(page_title="Test Nolan")

# Inicialización de estados
if "inicio" not in st.session_state:
    st.session_state.inicio = False
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "pregunta" not in st.session_state:
    st.session_state.pregunta = 1
if "puntajes" not in st.session_state:
    st.session_state.puntajes = defaultdict(int)
if "respuestas" not in st.session_state:
    st.session_state.respuestas = {}

# Preguntas para el Test
preguntas = {
    1: {
        "texto": "¿Qué tema central te atrae más?",
        "opciones": {
            "Sueños y subconsciente": ["Inception"],
            "Viajes espaciales y tiempo": ["Interstellar", "Tenet"],
            "Identidad y memoria": ["Memento"],
            "Ética y ciencia": ["Oppenheimer"],
            "Magia y obsesión": ["The Prestige"],
            "Guerra y supervivencia": ["Dunkirk"],
            "Crimen y caos": ["The Dark Knight"]
        }
    },
    2: {
        "texto": "¿Qué emoción disfrutas más al ver cine?",
        "opciones": {
            "Confusión estimulante": ["Memento", "Tenet"],
            "Admiración científica": ["Interstellar", "Oppenheimer"],
            "Asombro y creatividad": ["Inception", "The Prestige"],
            "Tensión y adrenalina": ["Dunkirk", "The Dark Knight"],
            "Reflexión filosófica": ["Oppenheimer", "Inception"]
        }
    },
    3: {
        "texto": "¿Te gustan los protagonistas...?",
        "opciones": {
            "Con traumas o pérdidas": ["Inception", "Memento"],
            "Científicos o exploradores": ["Interstellar", "Oppenheimer"],
            "Heroicos y éticos": ["The Dark Knight"],
            "Obsesivos y ambiguos": ["The Prestige", "Tenet"],
            "Realistas y vulnerables": ["Dunkirk"]
        }
    },
    4: {
        "texto": "¿Conoces a alguno de estos actores?",
        "opciones": {
            "Leonardo DiCaprio": ["Inception"],
            "Cillian Murphy": ["Oppenheimer", "Dunkirk", "Inception"],
            "Christian Bale": ["The Prestige", "The Dark Knight"],
            "Matthew McConaughey": ["Interstellar"],
            "Guy Pearce": ["Memento"],
            "Robert Pattinson": ["Tenet"]
        },
        "multiple": True
    },
    5: {
        "texto": "¿Qué estilo visual prefieres?",
        "opciones": {
            "Realismo bélico": ["Dunkirk"],
            "Espacios vastos y estéticos": ["Interstellar"],
            "Ilusiones y teatralidad": ["The Prestige"],
            "Ambientes urbanos distorsionados": ["Inception"],
            "Oscuridad y caos": ["The Dark Knight"],
            "Estética limpia y futurista": ["Tenet"]
        }
    },
    6: {
        "texto": "¿Qué frase te representa más?",
        "opciones": {
            "La mente puede construir mundos.": ["Inception"],
            "El tiempo es relativo.": ["Interstellar", "Tenet"],
            "No confíes ni en ti mismo.": ["Memento"],
            "El fin justifica los medios.": ["The Dark Knight", "Oppenheimer"],
            "La perfección cuesta todo.": ["The Prestige"]
        }
    },
    7: {
        "texto": "¿Qué tipo de final te gusta más?",
        "opciones": {
            "Sorprendente y abierto": ["Inception", "Tenet"],
            "Reflexivo y filosófico": ["Oppenheimer"],
            "Trágico o ambiguo": ["Memento", "The Prestige"],
            "Heroico y potente": ["The Dark Knight"],
            "Realista y sin redención": ["Dunkirk"]
        }
    },
    8: {
        "texto": "¿Te interesa la ciencia en el cine?",
        "opciones": {
            "Sí, me fascina": ["Oppenheimer", "Interstellar"],
            "Solo si es entendible": ["Inception", "Tenet"],
            "Prefiero emociones": ["The Prestige", "The Dark Knight"]
        }
    },
    9: {
        "texto": "¿Qué tipo de historia te motiva más?",
        "opciones": {
            "Una misión imposible": ["Interstellar", "Tenet"],
            "Un duelo de mentes": ["The Prestige", "The Dark Knight"],
            "Una lucha interna": ["Inception", "Memento"],
            "Una tragedia inevitable": ["Oppenheimer", "Dunkirk"]
        }
    },
    10: {
        "texto": "¿Qué tan dispuesto estás a pensar mucho durante la película?",
        "opciones": {
            "¡Me encanta!": ["Memento", "Inception", "Tenet"],
            "Me gusta, pero no todo el tiempo": ["Oppenheimer", "The Prestige"],
            "Prefiero algo más directo": ["The Dark Knight", "Dunkirk"]
        }
    }
}

# Pantalla de bienvenida
if not st.session_state.inicio:
    st.title("Test de Personalidad: ¿Qué película de Nolan eres tú?")
    st.markdown("A través de **10 preguntas**, descubre qué película del director *Christopher Nolan* representa mejor tu personalidad.")
    
    st.session_state.nombre = st.text_input("¿Cuál es tu nombre? (Obligatorio) (Presionar Enter para Continuar)")
    conoce = st.radio("¿Conoces a Christopher Nolan?", ["Sí", "No"], key="conoce_nolan")

    st.markdown("**¿Quién es Christopher Nolan?**")
    st.info("""
    Christopher Nolan es un director británico reconocido por sus películas complejas, profundas y visualmente impactantes.  
    Aborda temas como el tiempo, la memoria, los sueños y la moralidad.  
    Obras destacadas: *Inception*, *Interstellar*, *The Dark Knight*, *Oppenheimer* y más.
    """)

    if st.session_state.nombre and st.button("Iniciar test"):
        st.session_state.inicio = True
        st.rerun()

# Preguntas del test
elif st.session_state.pregunta <= 10:
    p = st.session_state.pregunta
    pregunta = preguntas[p]
    st.markdown(f"### Pregunta {p}: {pregunta['texto']}")
    opciones = list(pregunta["opciones"].keys())

    if pregunta.get("multiple", False):
        seleccion = st.multiselect("Selecciona todas las que apliquen:", opciones, key=f"sel_{p}")
    else:
        seleccion = st.radio("Selecciona una opción:", opciones, key=f"sel_{p}")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Anterior", key=f"prev_{p}"):
            if st.session_state.pregunta > 1:
                st.session_state.pregunta -= 1
                st.rerun()
    with col2:
        if st.button("Siguiente", key=f"next_{p}"):
            if seleccion:
                # Limpiar puntajes anteriores de esta pregunta
                for pelis in pregunta["opciones"].values():
                    for peli in pelis:
                        st.session_state.puntajes[peli] -= st.session_state.respuestas.get(p, []).count(peli)

                # Registrar respuesta
                if isinstance(seleccion, list):
                    st.session_state.respuestas[p] = []
                    for s in seleccion:
                        st.session_state.respuestas[p].extend(pregunta["opciones"][s])
                        for peli in pregunta["opciones"][s]:
                            st.session_state.puntajes[peli] += 1
                else:
                    st.session_state.respuestas[p] = pregunta["opciones"][seleccion]
                    for peli in pregunta["opciones"][seleccion]:
                        st.session_state.puntajes[peli] += 1

                st.session_state.pregunta += 1
                st.rerun()
            else:
                st.warning("Selecciona al menos una opción.")

# Resultado final
else:
    st.success("¡Test completado!")
    peli_final = max(st.session_state.puntajes, key=st.session_state.puntajes.get)
    pelicula = df[df["Título"] == peli_final].iloc[0]

    frases = {
        "Inception": "Eres una persona creativa, que siempre está imaginando cosas nuevas. Te gusta pensar en temas profundos y hacer preguntas que no todos se hacen. Tu forma de ver el mundo es especial, porque no te quedas con lo que se ve por fuera, sino que buscas entender lo que hay detrás. Aunque a veces parezcas estar en tu propio mundo, es ahí donde nacen tus mejores ideas.",
        "Interstellar": "Eres una persona curiosa, que siempre quiere aprender y descubrir cosas nuevas. Sientes todo con mucha intensidad, porque tu corazón está muy conectado con lo que vives. Y aunque a veces lo desconocido asusta a otros, tú lo amas, porque sabes que ahí es donde empieza lo más interesante.",
        "Memento": "Eres alguien que valora la verdad, aunque a veces duela, porque sabes que solo así se crece. Tu mente nunca se detiene, siempre está pensando, imaginando o buscando respuestas. No te conformas con lo fácil, porque sabes que lo real y profundo es lo que realmente importa.",
        "The Prestige": "Eres una persona perfeccionista, que cuida cada detalle y siempre quiere dar lo mejor. Haces todo con pasión, porque pones el corazón en lo que amas. A veces pareces misterioso, porque no todos logran entender lo que piensas o sientes, pero eso también es parte de tu encanto.",
        "Tenet": "Te gusta el caos ordenado, ese desorden que solo tú entiendes y que tiene sentido en tu mundo. Tu forma de pensar es diferente, como si vieras las cosas desde varios ángulos a la vez. Piensas en muchas capas, en muchas ideas al mismo tiempo, como si tu mente funcionara en otra dimensión.",
        "Dunkirk": "Eres una persona realista, que ve las cosas como son, sin adornos. No tienes miedo de decir lo que piensas, porque eres valiente y directo. No necesitas muchas palabras para entender; incluso el silencio te dice mucho, porque sabes leer lo que otros no dicen.",
        "The Dark Knight": "Tienes un fuerte sentido de la justicia, siempre quieres hacer lo correcto y defender lo que crees. Pero también cargas con una parte oscura, con dudas o emociones difíciles que a veces te cuesta manejar. Aun así, sigues adelante, luchando por ser mejor sin dejar de ser tú.",
        "Oppenheimer": "Eres una persona reflexiva, que piensa mucho antes de actuar. No haces las cosas por hacer, siempre buscas entender el porqué. Eres profundo, te haces preguntas que otros evitan, y te importa el impacto que tienen tus decisiones en los demás y en ti mismo."
    }

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(pelicula["Imagen"], use_container_width=True)
    with col2:
        st.markdown(f"## {pelicula['Título']} ({pelicula['Año']})")
        st.write(f"**Género:** {pelicula['Género']}")
        st.write(f"**Valoración:** {pelicula['Valoración']}")
        st.write(f"**Sinopsis:** {pelicula['Sinopsis']}")
        st.info(f"{frases.get(pelicula['Título'], '')}")
        st.markdown(f"[Ver en Youtube]({pelicula['Enlace']})")

# Mostrar críticas positivas y negativas
    st.markdown("### Opiniones del público")

    positivas = criticas_df[
        (criticas_df["Título"] == peli_final) & 
        (criticas_df["Tipo"] == "Positivas")
    ]["Comentario"].tolist()

    negativas = criticas_df[
        (criticas_df["Título"] == peli_final) & 
        (criticas_df["Tipo"] == "Negativas")
    ]["Comentario"].tolist()

    with st.expander("Críticas positivas"):
        for comentario in positivas:
            st.write(f"• {comentario}")

    with st.expander("Críticas negativas"):
        for comentario in negativas:
            st.write(f"• {comentario}")
    
    if st.button("Reiniciar test"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
