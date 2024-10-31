import streamlit as st

def freemium_page():
    st.title("¡Desbloquea tu Potencial en Criptomonedas y Blockchain!")
    st.subheader("Empieza con las Herramientas Básicas y Prepárate para el Éxito Financiero y Profesional 🚀")

    st.write("""
    Este es el primer paso en tu camino hacia la libertad financiera. Aprovecha el contenido exclusivo que te ayudará a entender y dominar el mundo de las criptomonedas.
    """)

    st.markdown("### 🌟 **Acceso Freemium**: Herramientas y Contenidos Exclusivos")
    
    # Link al eBook
    st.markdown("""
    ### 📘 ¡Descarga tu eBook Gratuito!
    Aprende los fundamentos de Blockchain y criptomonedas con nuestro eBook exclusivo.  
    <a href="https://drive.google.com/file/d/1L-PKO5xWZy5Nk1Fv3B721nz60sIzxB0k/view?usp=sharing" style='color: red; font-weight: bold;'>
    **Descargar 'Introducción a Blockchain y Criptomonedas'**
    </a>
    """, unsafe_allow_html=True)

    st.subheader("⚙️ Tus Herramientas de Inversión")
    st.write("Aquí puedes acceder a las herramientas básicas freemium que te ayudarán a comenzar en el fascinante mundo de la inversión digital.")

   # Enlace para ir a la Calculadora de Inversiones
    st.markdown(
        """
        <a href="https://cryptonomicant-calculator-investment.streamlit.app/" style="font-size: 18px; color: red; text-decoration: underline;">
            Ir a la Calculadora de Inversiones
        </a>
        """,
        unsafe_allow_html=True
    )

    # Call to action para que el usuario se mantenga enganchado
    st.markdown("""
    ### ¿Listo para llevar tu conocimiento al siguiente nivel?
    Completa los cursos básicos y explora el mundo de las inversiones más avanzadas con nuestras herramientas premium.
    """)

    # Opción para cambiar de usuario
    if st.button("Cambiar Usuario"):
        # Limpiar la sesión actual
        for key in list(st.session_state.keys()):
            del st.session_state[key]  # Elimina la sesión actual
        st.success("Has cerrado sesión correctamente. Por favor, inicia sesión de nuevo.")

if __name__ == "__main__":
    freemium_page()
