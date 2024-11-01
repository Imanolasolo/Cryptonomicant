# investment_manager.py
import streamlit as st
from utils.data_manager import add_project_data, get_all_projects, delete_project_data
import pandas as pd
import matplotlib.pyplot as plt
import base64

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

def main():
    st.title("Gestión de Proyectos de Inversión")

    # Selector de procesos
    menu_options = ["Agregar Proyecto", "Ver Proyectos", "Gestionar Proyectos", "Generar Gráficos", "Descargar Reporte"]
    choice = st.selectbox("Selecciona un proceso", menu_options)

    if choice == "Agregar Proyecto":
        add_project()
    elif choice == "Ver Proyectos":
        view_projects()
    elif choice == "Gestionar Proyectos":
        manage_projects()
    elif choice == "Generar Gráficos":
        generate_graphs()
    elif choice == "Descargar Reporte":
        download_report()

def add_project():
    st.subheader("Agregar Nuevo Proyecto")
    
    name = st.text_input("Nombre del Proyecto")
    investment_amount = st.number_input("Monto de Inversión", min_value=0.0, step=100.0)
    estimated_return = st.number_input("Retorno Estimado (%)", min_value=0.0, step=0.1)
    duration_months = st.number_input("Duración (Meses)", min_value=1, step=1)
    
    if st.button("Agregar Proyecto"):
        if name and investment_amount and estimated_return and duration_months:
            add_project_data(name, investment_amount, estimated_return, duration_months)
            st.success(f"Proyecto '{name}' agregado con éxito.")
        else:
            st.error("Por favor, completa todos los campos.")

def view_projects():
    st.subheader("Ver Todos los Proyectos")
    projects = get_all_projects()
    
    if projects:
        for project in projects:
            st.write(f"**Nombre:** {project['name']}")
            st.write(f"**Monto Inversión:** {project['investment_amount']}")
            st.write(f"**Retorno Estimado:** {project['estimated_return']}%")
            st.write(f"**Duración:** {project['duration_months']} meses")
            st.markdown("---")
    else:
        st.write("No hay proyectos registrados.")

def manage_projects():
    st.subheader("Gestionar Proyectos")
    
    projects = get_all_projects()
    
    if projects:
        project_names = [project['name'] for project in projects]
        selected_project = st.selectbox("Selecciona un Proyecto", project_names)
        
        if st.button("Eliminar Proyecto"):
            delete_project_data(selected_project)
            st.success(f"Proyecto '{selected_project}' eliminado con éxito.")
            st.experimental_rerun()
    else:
        st.write("No hay proyectos para gestionar.")

def generate_graphs():
    st.subheader("Gráficos de Proyectos")

    projects = get_all_projects()
    if projects:
        names = [project['name'] for project in projects]
        investments = [project['investment_amount'] for project in projects]

        fig, ax = plt.subplots()
        ax.bar(names, investments)
        ax.set_xlabel("Proyectos")
        ax.set_ylabel("Inversión")
        ax.set_title("Inversión por Proyecto")

        st.pyplot(fig)
    else:
        st.write("No hay proyectos para mostrar.")

def download_report():
    st.subheader("Descargar Reporte de Proyectos")
    
    projects = get_all_projects()
    
    if projects:
        df = pd.DataFrame(projects)
        st.write(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Descargar Reporte CSV",
            data=csv,
            file_name="reporte_proyectos.csv",
            mime="text/csv",
        )
    else:
        st.write("No hay proyectos para generar un reporte.")

if __name__ == "__main__":
    main()
