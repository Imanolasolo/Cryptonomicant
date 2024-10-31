import streamlit as st

def premium_page():
    st.title("Bienvenido a la Página Premium")
    st.write("Acceso a contenido avanzado y herramientas exclusivas.")
    st.write("- Cursos avanzados de criptomonedas")
    st.write("- Herramientas de análisis técnico y gráficos en tiempo real")

    # Proceso específico para el rol premium
    st.subheader("Herramientas Disponibles")
    st.write("Accede a las herramientas premium para mejorar tus análisis de criptomonedas.")

    # Opción para cambiar de usuario
    if st.button("Cambiar Usuario"):
        # Limpiar la sesión actual
        for key in list(st.session_state.keys()):
            del st.session_state[key]  # Elimina la sesión actual
        st.success("Has cerrado sesión correctamente. Por favor, inicia sesión de nuevo.")
        st.experimental_rerun()  # Recargar para redirigir a la página de inicio de sesión

if __name__ == "__main__":
    premium_page()
