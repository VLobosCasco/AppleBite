
# Nuevo environment
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  habilitaar powershell
# .\AppleBite\Scripts\Activate.ps1   para activar el environment   
# pip install libreria

import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="AppleBite", layout="wide")
st.title("📱 AppleBite ")
st.subheader("Catálogo de Productos Sellados")  # opción simple

# Obtener cotización dólar blue con margen
url = 'https://mercados.ambito.com/dolar/informal/variacion'
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(url, headers=headers)
data = res.json()
dolar = float(data['venta'].replace(',', '.')) + 10
fecha = data['fecha']

st.markdown(f"Actualizacion: {fecha} ", unsafe_allow_html=True)
st.markdown(f"Cotización del dólar: **${dolar:,.2f} ARS**", unsafe_allow_html=True)

# Datos
data = {
    "Producto": ["iPhone 13 - 128GB", "iPhone 14 - 128GB", "iPhone 15 - 128GB", "iPhone 16 - 128GB", "iPhone 16E - 128GB", "iPhone 16 Pro - 256GB",
                 "iPad 10", "iPad 11", "iPad Air 13 M2",
                 "Apple Watch SE 2 (40mm)", "Apple Watch SE 2 (44mm)", "Apple Watch S9 (41mm)", "Apple Watch S10 (42mm)",
                 "Adaptador original 20W"],
    "Categoría": ["Celulares"] * 6 + ["Tablets"] * 3 + ["Reloj"] * 4 + ["Accesorios"],
    "USD": [560, 670, 750, 850, 685, 1100, 600, 500, 890, 310, 330, 450, 460, 45]
}
df = pd.DataFrame(data)
df["ARS"] = df["USD"] * dolar

# Sidebar de categorías
categoria = st.sidebar.selectbox("Seleccioná una categoría", df["Categoría"].unique())
filtro = df[df["Categoría"] == categoria][["Producto", "USD", "ARS"]].copy()

# Centrado CSS
st.markdown("""
<style>
thead tr th, tbody tr td {
    text-align: center !important;
    vertical-align: middle !important;
}
</style>
""", unsafe_allow_html=True)

filtro["USD"] = filtro["USD"].apply(lambda x: f"US$ {x:,.2f}")
filtro["ARS"] = filtro["ARS"].apply(lambda x: f"${x:,.2f}")

st.dataframe(filtro, use_container_width=True, hide_index=True)






