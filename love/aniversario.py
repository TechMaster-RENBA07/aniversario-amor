import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import time
import random

# --- CONFIGURACIÓN GLOBAL ---
st.set_page_config(
    page_title="Aniversario",
    page_icon="💘",
    layout="wide"
)

# ==============================================================================
# === 🔐 SISTEMA DE LOGIN DE AMOR (CON FORMULARIO PARA QUE FUNCIONE ENTER) ===
# ==============================================================================
if 'ingreso_exitoso' not in st.session_state:
    st.session_state.ingreso_exitoso = False
if 'mostrar_confeti' not in st.session_state:
    st.session_state.mostrar_confeti = False

if not st.session_state.ingreso_exitoso:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>🔐 Acceso Restringido</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Departamento de Seguridad del Corazón</h3>", unsafe_allow_html=True)
        st.write("---")
        
        usuario = st.radio("Primero, identifícate:", 
                           ["Una desconocida", "La chica más linda del mundo", "El amor de tu vida"], 
                           index=0)
        
        if usuario == "Una desconocida":
            st.warning("⛔ Lo siento, este sitio es privado. Solo para mi novia.")
        else:
            # --- CAMBIO IMPORTANTE: USAMOS UN FORMULARIO PARA QUE EL ENTER FUNCIONE ---
            with st.form("login_form"):
                password = st.text_input("Introduce la Clave Secreta:", type="password", help="Pista: Nuestra fecha especial (03/11/2024) o 'te amo'")
                
                # El botón de envío del formulario
                submit_login = st.form_submit_button("💘 Solicitar Acceso")
            
            if submit_login:
                # VALIDACIÓN
                if password == "03/11/2024" or password.lower() == "te amo":
                    st.success("✅ ¡Identidad Confirmada! Bienvenida mi amor...")
                    time.sleep(1)
                    st.session_state.ingreso_exitoso = True
                    st.session_state.mostrar_confeti = True # Activamos el confeti
                    st.rerun() 
                else:
                    errores = [
                        "Ups, contraseña incorrecta. ¿Me das un beso y pruebas otra vez?",
                        "Error 404: Amor no encontrado. Intenta con nuestra fecha.",
                        "Mmm... casi, pero no. Pista: 03/11/2024",
                        "Acceso denegado. Pero te ves muy guapa hoy."
                    ]
                    st.error(random.choice(errores))
    st.stop()

# ==============================================================================
# === 🎉 CONTENIDO PRINCIPAL ===
# ==============================================================================

# 1. LLUVIA DE PICADILLOS (CONFETI) - VERSIÓN CSS PURO (SIN GIFS EXTERNOS)
# ------------------------------------------------------------------------
if st.session_state.mostrar_confeti:
    # Este CSS crea "confeti" usando emojis y animaciones CSS
    st.markdown("""
    <style>
        @keyframes fall {
            0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
        }
        
        .confetti-piece {
            position: fixed;
            top: -10vh;
            font-size: 2rem;
            z-index: 999999;
            pointer-events: none;
            animation: fall 4s linear forwards;
        }
    </style>
    
    <div class="confetti-piece" style="left: 5%; animation-delay: 0s;">🎉</div>
    <div class="confetti-piece" style="left: 15%; animation-delay: 0.5s;">🎊</div>
    <div class="confetti-piece" style="left: 25%; animation-delay: 1.2s;">✨</div>
    <div class="confetti-piece" style="left: 35%; animation-delay: 0.2s;">❤️</div>
    <div class="confetti-piece" style="left: 45%; animation-delay: 0.8s;">🎉</div>
    <div class="confetti-piece" style="left: 55%; animation-delay: 1.5s;">🎊</div>
    <div class="confetti-piece" style="left: 65%; animation-delay: 0.3s;">✨</div>
    <div class="confetti-piece" style="left: 75%; animation-delay: 1.0s;">❤️</div>
    <div class="confetti-piece" style="left: 85%; animation-delay: 0.6s;">🎉</div>
    <div class="confetti-piece" style="left: 95%; animation-delay: 1.8s;">🎊</div>
    
    <div class="confetti-piece" style="left: 10%; animation-delay: 2.0s;">❤️</div>
    <div class="confetti-piece" style="left: 20%; animation-delay: 2.5s;">✨</div>
    <div class="confetti-piece" style="left: 30%; animation-delay: 1.7s;">🎉</div>
    <div class="confetti-piece" style="left: 40%; animation-delay: 2.2s;">🎊</div>
    <div class="confetti-piece" style="left: 50%; animation-delay: 1.9s;">❤️</div>
    <div class="confetti-piece" style="left: 60%; animation-delay: 2.8s;">✨</div>
    <div class="confetti-piece" style="left: 70%; animation-delay: 2.1s;">🎉</div>
    <div class="confetti-piece" style="left: 80%; animation-delay: 1.4s;">🎊</div>
    <div class="confetti-piece" style="left: 90%; animation-delay: 2.6s;">❤️</div>
    
    """, unsafe_allow_html=True)
    
    # Desactivamos la variable para que si recarga la página no salga de nuevo
    st.session_state.mostrar_confeti = False


# 2. MARCO DE CORAZONES
# ---------------------
st.markdown("""
<style>
    @keyframes moveBackground {
        0% { background-position: 0 0; }
        100% { background-position: 50px 50px; }
    }
    .moving-border {
        position: fixed;
        z-index: 9999;
        background-image: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPSc1MCcgaGVpZ2h0PSc1MCcgdmlld0JveD0nMCAwIDUwIDUwJz48cGF0aCBkPSJNMjUgMzkuN2wtLjYtLjVDMTEuNSAyOC43IDQgMjEuNSA0IDEzLjIgNCA4LjggNy41IDUuMyAxMS45IDUuM2MyLjUgMCA0LjkgMS4yIDYuNCAzLjJDMTkuOCA2LjUgMjIuMiA1LjMgMjQuNyA1LjNjNC40IDAgNy45IDMuNSA3LjkgNy45IDAgOC4zLTcuNSAxNS41LTE5LjYgMjZsLS42LjV6IiBmaWxsPSIjZmY2OWI0IiBvcGFWNpdHk9IjAuNiIvPjwvc3ZnPg==");
        background-size: 50px 50px; 
        pointer-events: none; 
        animation: moveBackground 3s linear infinite; 
    }
    .border-top { top: 0; left: 0; width: 100%; height: 30px; }
    .border-bottom { bottom: 0; left: 0; width: 100%; height: 30px; }
    .border-left { top: 0; left: 0; width: 30px; height: 100%; }
    .border-right { top: 0; right: 0; width: 30px; height: 100%; }
    .main .block-container { padding: 50px; }
</style>
<div class="moving-border border-top"></div>
<div class="moving-border border-bottom"></div>
<div class="moving-border border-left"></div>
<div class="moving-border border-right"></div>
""", unsafe_allow_html=True)


# --- RESTO DEL CÓDIGO (LÓGICA, FOTOS, VIDEO) ---
FECHA_INICIO = date(2024, 11, 3) 

def calcular_dias():
    hoy = date.today()
    if hoy < FECHA_INICIO:
        return 0
    dias_juntos = (hoy - FECHA_INICIO).days
    return dias_juntos

st.title("💖 ¡Feliz Aniversario Mi Vida! 💖")

anos_juntos = date.today().year - FECHA_INICIO.year
if date.today().month < FECHA_INICIO.month or (date.today().month == FECHA_INICIO.month and date.today().day < FECHA_INICIO.day):
    anos_juntos -= 1

st.markdown(f"### Han pasado {anos_juntos} años desde que dijimos 'sí'.")

st.header("✨ Nuestro Viaje Juntos ✨")
dias = calcular_dias()
st.metric(label="Días Inolvidables", value=f"{dias} días", delta="¡Y contando!")

st.write("---")

st.header("📸 Recuerdos que Amo")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("foto1.jpg", caption="Salidita para distraerse jsjs") 
    if st.button("Ver Anécdota #1"):
        st.success("¡Ese fue una de nuestras aventuras hermosas de varias que tenemos!")

with col2:
    st.image("foto2.jpg", caption="Bechitos") 
    if st.button("Ver Anécdota #2"):
        st.info("Sintiendo tu amor que me lleva a perder la mente jsjs.")

with col3:
    st.image("foto3.jpg", caption="En el cine, nuestra primera vez jsjs") 
    if st.button("Ver Anécdota #3"):
        st.warning("Estuvo bonito y espero tener mas anecdotas hermosas junto a tí.")

st.write("---")

st.header("🎁 ¡El Botón Sorpresa! 🎁")
st.write("Mi amor, tengo un pequeño video para ti.")

VIDEO_ID = "RIHROUXdVpY" 
TIEMPO_VIDEO_MS = 173000 

st.markdown('<div id="promesa_section"></div>', unsafe_allow_html=True)

if st.button("¡Presiona para ver! 🌹", key="surprise_button"):
    st.balloons() 
    st.success("¡Aquí está tu sorpresa! Cada segundo cuenta.")
    
    # ROSAS FLOTANTES
    st.markdown("""
        <style>
        .rose-container {
            position: fixed; bottom: 50px; left: -150px; width: 100%; z-index: 9999; pointer-events: none;
            animation: floatRoses 18s linear infinite;
        }
        @keyframes floatRoses { 0% { transform: translateX(-150px); } 100% { transform: translateX(110vw); } }
        .rose-img { height: 120px; margin-right: 60px; display: inline-block; }
        </style>
        <div class="rose-container">
            <img src="https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif" class="rose-img">
            <img src="https://i.gifer.com/origin/c9/c97e179379856f6c019777d13038b303_w200.gif" class="rose-img">
            <img src="https://media.giphy.com/media/l4pTfx2qLSzrWnSyo/giphy.gif" class="rose-img">
        </div>
    """, unsafe_allow_html=True)

    # VIDEO
    video_html = f"""
        <iframe width="100%" height="500" 
        src="https://www.youtube.com/embed/{VIDEO_ID}?autoplay=1&mute=0" 
        frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
        <script>
            setTimeout(function() {{
                document.getElementById('promesa_section').scrollIntoView({{behavior: 'smooth'}});
            }}, {TIEMPO_VIDEO_MS});
        </script>
    """
    components.html(video_html, height=520)
    st.info("Espero que te guste 🥹. ¡Te amo mucho!")

st.write("---")

st.header("💌 Una Promesa y Un Deseo")
st.write("Mi amor, este es tu espacio. Deja tu recuerdo favorito de este año para que lo atesore por siempre.")

with st.form(key='promesa_form'):
    recuerdo = st.text_area("Escribe aquí tu recuerdo o mensaje:", height=150)
    submit_button = st.form_submit_button(label='¡Guardar Nuestro Recuerdo!')

if submit_button and recuerdo:
    st.balloons()
    st.success(f"¡Recuerdo Guardado! Gracias por este hermoso mensaje:")
    st.markdown(f"> **{recuerdo}**")
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; font-size: 30px; color: #ff69b4; animation: fadeIn 3s;'>
            **Gracias por ser mi mejor aventura. Te Amo.**
        </div>
        <div style='text-align: center; font-size: 100px;'>❤️</div>
        """, 
        unsafe_allow_html=True
    )