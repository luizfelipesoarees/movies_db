import streamlit as st
import pandas as pd\

st.set_page_config(layout="wide")

df_top100movies = pd.read_csv("datasets/TOP 100 IMDB MOVIES.csv")

movies = df_top100movies["title"].unique()
movie = st.sidebar.selectbox("Movies", movies)

df_movie = df_top100movies[df_top100movies["title"] == movie]

movie_title = df_movie["title"].iloc[0]
movie_genre = df_movie["genre"].iloc[0]
movie_description = df_movie["description"].iloc[0]
movie_rank = df_movie["rank"].iloc[0]
movie_rating = df_movie["rating"].iloc[0]
movie_year = df_movie["year"].iloc[0]

st.title(movie_title)
st.header(movie_genre)
st.subheader(movie_description)

st.divider()

col1, col2, col3 =st.columns(3)
col1.metric("Rank", movie_rank)
col2.metric("Rating", movie_rating)
col3.metric("Year", movie_year)


