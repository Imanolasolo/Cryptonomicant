import streamlit as st
import sqlite3
import base64
import freemium
import premium
import pro
import webbrowser

# Configuración de la página
st.set_page_config(
    page_title="Cryptonomicant",
    page_icon=":coin:",
    layout="wide",
)

# Function to encode image as base64 to set as background
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Encode the background image
img_base64 = get_base64_of_bin_file('background1.jpg')

# Set the background image using the encoded base64 string
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
        background-size: cover;
        background-blend-mode: color-burn;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Inicializar la base de datos
def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS usuarios (username TEXT, password TEXT, role TEXT, first_login INTEGER)')
    conn.commit()
    conn.close()

init_db()

# Función para verificar credenciales
def check_credentials(username, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT role, first_login FROM usuarios WHERE username = ? AND password = ?', (username, password))
    result = c.fetchone()
    conn.close()
    return result if result else None

# Función para actualizar el campo 'first_login' en la base de datos
def update_first_login(username):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('UPDATE usuarios SET first_login = 0 WHERE username = ?', (username,))
    conn.commit()
    conn.close()

# Función para generar el enlace de WhatsApp
def send_whatsapp_message(name, phone):
    message = f"Hola, soy {name}, y me gustaría registrarme en Cryptonomicant."
    whatsapp_url = f"https://api.whatsapp.com/send?phone=593993513082&text={message.replace(' ', '%20')}"
    webbrowser.open(whatsapp_url)

# Función para mostrar mensajes
def show_message(message, message_type='success'):
    if message_type == 'success':
        st.success(message)
    else:
        st.error(message)

# Función principal
def main():
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = None
    if "first_login" not in st.session_state:
        st.session_state["first_login"] = None

    if st.session_state["user_role"]:
        role = st.session_state["user_role"]
        first_login = st.session_state["first_login"]

        # Mostrar el formulario de entrevista solo si es la primera vez que inicia sesión
        if first_login and role != "admin":  # No mostrar para administradores
            with st.expander("¿Primera vez en Cryptonomicant? Regístrate para una entrevista personalizada"):
                st.write("Por favor, completa el siguiente formulario y contactaremos contigo para agendar una entrevista.")
                name = st.text_input("Nombre Completo")
                phone = st.text_input("Número de Teléfono")

                if st.button("Enviar Solicitud de Entrevista"):
                    if name and phone:
                        send_whatsapp_message(name, phone)
                        show_message("Solicitud enviada correctamente a través de WhatsApp.")
                        update_first_login(st.session_state["username"])
                        st.session_state["first_login"] = 0
                    else:
                        show_message("Por favor, completa todos los campos.", message_type='error')

        # Cargar la página correspondiente según el rol
        if role == "admin":
            import admin
            admin.main()
        elif role == "freemium":
            freemium.freemium_page()
        elif role == "premium":
            premium.premium_page()
        elif role == "pro":
            pro.pro_page()

        return

    # Pantalla de inicio de sesión
    st.title(":red[Cryptonomicant:] La Revolución de la Inversión en Cripto")
    st.subheader("Descubre, Invierte y Domina el Mundo Digital de las Criptomonedas")

    # Crear formulario de inicio de sesión
    with st.form(key='login_form'):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type='password')
        submit_button = st.form_submit_button("Iniciar Sesión")

    if submit_button:
        credentials = check_credentials(username, password)
        if credentials:
            role, first_login = credentials
            st.session_state["user_role"] = role
            st.session_state["username"] = username
            st.session_state["first_login"] = first_login
            show_message(f"Inicio de sesión exitoso como {role}.")
            st.rerun()
        else:
            show_message("Usuario o contraseña incorrectos.", message_type='error')

    # Agregar opción para registrarse
    with st.expander("¿No tienes una cuenta? Regístrate para solicitar acceso."):
        name = st.text_input("Nombre Completo (Registro)")
        phone = st.text_input("Número de Teléfono (Registro)")

        if st.button("Enviar Solicitud de Registro"):
            if name and phone:
                send_whatsapp_message(name, phone)
                show_message("Solicitud de registro enviada correctamente a través de WhatsApp.")
            else:
                show_message("Por favor, completa todos los campos.", message_type='error')

if __name__ == "__main__":
    main()
