import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_top100movies = pd.read_csv("datasets/TOP 100 IMDB MOVIES.csv")

st.title("Top 100 IMDB movies")
st.caption("Esta é uma aplicação demonstrando os conceitos iniciais estudados em Python - por Luiz Felipe Soares")

rating_high = df_top100movies["rating"].max()
rating_low = df_top100movies["rating"].min()

max_rating = st.sidebar.slider("Rating Range", rating_low, rating_high, rating_high)
df_movies = df_top100movies[df_top100movies["rating"] <= max_rating]
df_movies

fig = px.bar(df_movies["year"].value_counts())
fig2 = px.histogram(df_movies["rating"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)