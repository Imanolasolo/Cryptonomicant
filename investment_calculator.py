import streamlit as st
import pandas as pd
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


def investment_calculator():
    st.title("Calculadora de Inversiones")
    st.write("Calcula el retorno de tu inversión y visualiza su crecimiento.")

    # Entradas del usuario
    principal = st.number_input("Cantidad de Inversión Inicial ($)", min_value=0.0, step=100.0)
    rate_of_return = st.number_input("Tasa de Retorno (%)", min_value=0.0, step=0.1)
    years = st.number_input("Número de Años", min_value=1, step=1)

    # Calcular retorno de inversión
    if st.button("Calcular ROI"):
        if rate_of_return < 0:
            st.error("La tasa de retorno no puede ser negativa.")
        else:
            final_amount = principal * (1 + (rate_of_return / 100)) ** years
            roi = final_amount - principal
            
            st.success(f"El monto final después de {years} años será: ${final_amount:,.2f}")
            st.write(f"El retorno de la inversión (ROI) será: ${roi:,.2f}")

            # Visualización
            data = {
                "Año": list(range(1, years + 1)),
                "Valor de la Inversión": [principal * (1 + (rate_of_return / 100)) ** year for year in range(1, years + 1)]
            }
            df = pd.DataFrame(data)
            
            st.line_chart(df.set_index("Año"))

            # Opción para descargar resultados
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Descargar Resultados",
                data=csv,
                file_name='resultados_inversion.csv',
                mime='text/csv'
            )

            # Detalles Anuales
            st.write("### Desglose Anual de la Inversión:")
            st.dataframe(df)

if __name__ == "__main__":
    investment_calculator()

