import requests
import streamlit as st
from dados import DADOS_CIDADES

try:
    API_KEY = st.secrets["OPENWEATHER_KEY"]
except FileNotFoundError:
    st.error("Arquivo não encontrado.")
    st.stop()

def buscar_clima(cidade, pais, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},{DADOS_CIDADES[cidade]["pais_codigo"]}&appid={api_key}&units=metric&lang=pt_br"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            clima_info = {
                "cidade": data["name"],
                "descricao":data["weather"][0]["description"],
                "clima_icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png",
                "country_icon": f"https://flagcdn.com/w160/{data['sys']['country'].lower()}.png",
                "temp": data["main"]["temp"],
                "sensacao": data["main"]["feels_like"],
                "umidade": data["main"]["humidity"],
                "min": data["main"]["temp_min"],
                "max": data["main"]["temp_max"]
            }
            return clima_info
        else:
            return None
    except requests.exceptions.RequestException:
        return None

lista_cidades = list(DADOS_CIDADES.keys())

with st.sidebar:
    st.title("Consulta de Clima 🌦️")
    cidade_selecionada = st.selectbox("Selecione a cidade: ", lista_cidades)
    st.text(DADOS_CIDADES[cidade_selecionada]["descricao"])
    st.image(DADOS_CIDADES[cidade_selecionada]["imagem"])

clima = buscar_clima(cidade_selecionada, DADOS_CIDADES[cidade_selecionada]["pais_codigo"], API_KEY)

st.title(f"{cidade_selecionada}")
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