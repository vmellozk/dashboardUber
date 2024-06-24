#Bibliotecas
import streamlit as st
import pandas as pd
import numpy as np

#Título da página
st.title("Uber pickups in NYC!")

#Define o tipo de column para date/time e a url com o arquivo csv...
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#Usado para não ter que carregar novamente todo o dataframe
@st.cache_data
#Função que baixa alguns dados, coloca-os em um dataframe do Pandas e
#converte a coluna de data de texto para datetime. A função aceita um
#único parâmetro (nrows), que especifica o número de linhas que você
# deseja carregar no dataframe
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Texto para loading do dataframe
data_load_state = st.text("Loading data...")
data = load_data(10000)
data_load_state.text(f"Done! (using st.cache_data)")

#Adicionando um subtítulo e chamando o dataframe
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

#Adicionando um subtítulo e fazendo o histograma do horário de pico
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#Adicionando um subtítulo e mostrando o mapa de onde é mais pedido no horario de pico
hour_to_filter = st.slider('hour', 0, 23, 17) #--> min, max, default
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f"Map of all pickups at {hour_to_filter}:00h")
st.map(filtered_data)