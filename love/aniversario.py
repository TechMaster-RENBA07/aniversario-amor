import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import time
import random

# --- CONFIGURACIÓN GLOBAL ---
st.set_page_config(
    page_title="Aniversario",
    page_icon="💖",
    layout="wide"
)

# ==============================================================================
# === 🔐 SISTEMA DE LOGIN DE AMOR ===
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
            with st.form("login_form"):
                password = st.text_input("Introduce la Clave Secreta:", type="password", help="Pista: Nuestra fecha especial (03/11/2024) o 'te amo'")
                submit_login = st.form_submit_button("💘 Solicitar Acceso")
            
            if submit_login:
                if password == "03/11/2024" or password.lower() == "te amo":
                    st.success("✅ ¡Identidad Confirmada! Bienvenida mi amor...")
                    time.sleep(1)
                    st.session_state.ingreso_exitoso = True
                    st.session_state.mostrar_confeti = True
                    st.rerun() 
                else:
                    errores = ["Contraseña incorrecta, dame un beso y prueba de nuevo.", "Error 404: Amor no encontrado.", "Pista: 03/11/2024"]
                    st.error(random.choice(errores))
    st.stop()

# ==============================================================================
# === 🎉 CONTENIDO PRINCIPAL ===
# ==============================================================================

# 1. LLUVIA ABUNDANTE DE PICADILLOS (Generado con Python para evitar errores externos)
if st.session_state.mostrar_confeti:
    confetti_html = ""
    colors = ['#FF69B4', '#FFD700', '#00BFFF', '#32CD32', '#FF4500', '#9400D3']
    for _ in range(150): # 150 papelitos
        left = random.randint(0, 100)
        delay = random.uniform(0, 3)
        duration = random.uniform(3, 5)
        color = random.choice(colors)
        confetti_html += f'<div class="confetti" style="left: {left}%; animation-delay: {delay}s; animation-duration: {duration}s; background-color: {color};"></div>'

    st.markdown(f"""
    <style>
        @keyframes fall {{ 0% {{ top: -10vh; opacity: 1; transform: rotate(0deg); }} 100% {{ top: 110vh; opacity: 0; transform: rotate(720deg); }} }}
        .confetti {{ position: fixed; width: 15px; height: 15px; z-index: 99999; pointer-events: none; animation: fall linear forwards; }}
    </style>
    {confetti_html}
    """, unsafe_allow_html=True)
    st.session_state.mostrar_confeti = False

# 2. MARCO DE CINTAS DE AMOR (CSS PURO - SIN IMÁGENES QUE SE ROMPAN)
st.markdown("""
<style>
    @keyframes moveStripes { 0% { background-position: 0 0; } 100% { background-position: 50px 50px; } }
    .moving-border {
        position: fixed; z-index: 9999; pointer-events: none;
        /* ESTO CREA LAS CINTAS ROSAS Y ROJAS SIN IMÁGENES */
        background: repeating-linear-gradient(45deg, #ffb6c1, #ffb6c1 10px, #ff69b4 10px, #ff69b4 20px);
        opacity: 0.7;
        animation: moveStripes 2s linear infinite;
    }
    .border-top { top: 0; left: 0; width: 100%; height: 20px; }
    .border-bottom { bottom: 0; left: 0; width: 100%; height: 20px; }
    .border-left { top: 0; left: 0; width: 20px; height: 100%; }
    .border-right { top: 0; right: 0; width: 20px; height: 100%; }
    .main .block-container { padding: 50px; }
</style>
<div class="moving-border border-top"></div>
<div class="moving-border border-bottom"></div>
<div class="moving-border border-left"></div>
<div class="moving-border border-right"></div>
""", unsafe_allow_html=True)

# --- DATOS Y LÓGICA ---
FECHA_INICIO = date(2024, 11, 3) 
hoy = date.today()
dias_juntos = (hoy - FECHA_INICIO).days if hoy >= FECHA_INICIO else 0
anos_juntos = hoy.year - FECHA_INICIO.year
if hoy.month < FECHA_INICIO.month or (hoy.month == FECHA_INICIO.month and hoy.day < FECHA_INICIO.day):
    anos_juntos -= 1

# --- INTERFAZ ---
st.title("💖 ¡Feliz Aniversario Mi Vida! 💖")
st.markdown(f"### Han pasado {anos_juntos} años desde que dijimos 'sí'.")

st.header("✨ Nuestro Viaje Juntos ✨")
st.metric(label="Días Inolvidables", value=f"{dias_juntos} días", delta="¡Y contando!")
st.write("---")

st.header("📸 Recuerdos que Amo")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("love/foto1.jpg", caption="Salidita para distraerse jsjs")
    if st.button("Ver Anécdota #1"): st.success("¡Ese fue una de nuestras aventuras hermosas!")
with col2:
    st.image("love/foto2.jpg", caption="Bechitos")
    if st.button("Ver Anécdota #2"): st.info("Sintiendo tu amor que me lleva a perder la mente.")
with col3:
    st.image("love/foto3.jpg", caption="En el cine")
    if st.button("Ver Anécdota #3"): st.warning("Estuvo bonito y espero tener más anécdotas contigo.")

st.write("---")

st.header("🎁 ¡El Botón Sorpresa! 🎁")
st.write("Mi amor, tengo un pequeño video para ti.")
VIDEO_ID = "RIHROUXdVpY"
TIEMPO_VIDEO_MS = 173000

# Sección oculta para scroll
st.markdown('<div id="promesa_section"></div>', unsafe_allow_html=True)

if st.button("¡Presiona para ver! 🌹", key="surprise_button"):
    st.balloons()
    st.success("¡Aquí está tu sorpresa! Cada segundo cuenta.")
    
    # VIDEO CON AUTOSCROLL
    components.html(f"""
        <iframe width="100%" height="500" src="https://www.youtube.com/embed/{VIDEO_ID}?autoplay=1" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
        <script>setTimeout(function() {{ document.getElementById('promesa_section').scrollIntoView({{behavior: 'smooth'}}); }}, {TIEMPO_VIDEO_MS});</script>
    """, height=520)
    st.info("Espero que te guste. ¡Te amo mucho!")

st.write("---")

st.header("💌 Una Promesa y Un Deseo")
st.write("Deja tu recuerdo favorito de este año:")

with st.form(key='promesa_form'):
    recuerdo = st.text_area("Escribe aquí:", height=150)
    submit_button = st.form_submit_button('¡Guardar Nuestro Recuerdo!')

if submit_button and recuerdo:
    st.balloons()
    st.success("¡Recuerdo Guardado!")
    st.markdown(f"> **{recuerdo}**")
    st.markdown("---")
    st.markdown("<div style='text-align: center; font-size: 30px; color: #ff69b4;'>**Gracias por ser mi mejor aventura. Te Amo.**</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; font-size: 100px;'>❤️</div>", unsafe_allow_html=True)

