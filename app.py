
# Nuevo environment
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  habilitaar powershell
# .\AppleBite\Scripts\Activate.ps1   para activar el environment   
# pip install libreria

import requests
import pandas as pd
import streamlit as st


url = 'https://mercados.ambito.com/dolar/informal/variacion'
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(url, headers=headers)
data = res.json()

dolar_venta = float(data['venta'].replace(',', '.'))

celulares = {'Modelo': ['iPhone 15'],
             'Precio USD': [770]}
df = pd.DataFrame(celulares)
df['Precio ARS'] = df['Precio USD'] * dolar_venta

st.title("Precios de celulares")
st.write(f"Dólar venta informal: {dolar_venta} ARS")
st.dataframe(df)


