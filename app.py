import requests
import streamlit as st
from dados import DADOS_CIDADES

api_key = "d5bd4956fa21383aaa7f6ccd99698533"
units = "metric"
lista_cidades = list(DADOS_CIDADES.keys())

with st.sidebar:
    st.title("Consulta de Clima")
    cidade = st.selectbox("Selecione a cidade: ", lista_cidades)
    st.text(DADOS_CIDADES[cidade]["descricao"])
    st.image(DADOS_CIDADES[cidade]["imagem"])

url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},{DADOS_CIDADES[cidade]["pais_codigo"]}&appid={api_key}&units={units}&lang=pt_br"
data = requests.get(url).json()

weather_icon = f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
country_icon = f"https://flagcdn.com/w160/{data['sys']['country'].lower()}.png"

clima = data['weather'][0]['main']
clima_descricao = data['weather'][0]['description'].upper()
clima_temp = data['main']['temp']
clima_sensacao = data['main']['feels_like']
clima_umidade = data['main']['humidity']
clima_min = data['main']['temp_min']
clima_max = data['main']['temp_max']

st.title(f"{cidade}")
with st.container(border=True): 

    col1, col2 = st.columns([1,2])

    with col1: 
        st.image(weather_icon, width=150)
        st.metric(label="Temperatura: ", value=f"{clima_temp:.0f} ºC")
        st.image(country_icon)

    with col2: 
        st.header("Descrição: ")
        st.subheader(clima_descricao)
        st.divider()

        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.metric(label="Sensação: ", value=f"{clima_sensacao:.0f} ºC")
            st.metric(label="Mínima: ", value=f"{clima_min:.0f} ºC")
            
        with sub_col2:
            st.metric(label="Umidade: ", value=f"{clima_umidade:.0f}")
            st.metric(label="Máxima: ", value=f"{clima_max:.0f} ºC")