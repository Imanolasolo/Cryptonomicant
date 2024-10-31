import streamlit as st

def pro_page():
    st.title("Bienvenido a la Página Pro")
    st.write("Acceso total a todos los cursos y herramientas.")
    st.write("- Cursos especializados para traders expertos")
    st.write("- Herramientas de trading de alta frecuencia")
    st.write("- Soporte personalizado y análisis en vivo")

    # Proceso específico para el rol pro
    st.subheader("Herramientas Disponibles")
    st.write("Accede a todas las herramientas y soporte premium.")

    # Opción para cambiar de usuario
    if st.button("Cambiar Usuario"):
        # Limpiar la sesión actual
        for key in list(st.session_state.keys()):
            del st.session_state[key]  # Elimina la sesión actual
        st.success("Has cerrado sesión correctamente. Por favor, inicia sesión de nuevo.")
        st.experimental_rerun()  # Recargar para redirigir a la página de inicio de sesión

if __name__ == "__main__":
    pro_page()
