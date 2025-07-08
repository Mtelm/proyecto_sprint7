#Importar librerias
import pandas as pd
import plotly.express as px 
import streamlit as st

#importar dataset
car_data=pd.read_csv('vehicles_us.csv')

#Encabezado de streamlit

st.header('Proyecto Sprint 7')
 #boton para generar histograma
hist_button=st.checkbox('Generar Histograma')
Scatter_button=st.checkbox('Generar Gráfico de Dispersión')
""" 
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    #crea un histograma
    fig=px.histogram(car_data, x='odometer')
    #mostrar un grafico interactivo con plotly
    st.plotly_chart(fig, use_container_width=True)
     """
# metodo opcional
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    #crea un histograma
    fig=px.histogram(car_data, x='odometer')
    #mostrar un grafico interactivo con plotly
    st.plotly_chart(fig, use_container_width=True)
if Scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    #crear un gráfico de dispersión
    fig=px.scatter(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)


