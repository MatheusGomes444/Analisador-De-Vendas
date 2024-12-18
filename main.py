import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
st.set_page_config(layout="wide")
df_reviews = pd.read_csv("Datasets/customer reviews.csv")
df_top100_books = pd.read_csv("Datasets/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# Definindo a seleção de páginas
page = st.sidebar.selectbox("Escolha uma página", ["Top100📗", "Review Books"])

if page == "Top100📗":
    max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
    df_books = df_top100_books[df_top100_books["book price"] <= max_price]
    df_books
    fig = px.bar(df_books["year of publication"].value_counts())
    fig2 = px.histogram(df_books["book price"])

    col1, col2 = st.columns(2)
    col1.plotly_chart(fig)
    col2.plotly_chart(fig2)
  

elif page == "Review Books":
    st.title("")
    # Conteúdo específico para a Página 2
    books = df_top100_books["book title"].unique()
    book = st.sidebar.selectbox("Books", books)

    df_book = df_top100_books[df_top100_books["book title"] == book]
    df_reviews_f = df_reviews[df_reviews["book name"] == book]

    book_title = df_book["book title"].iloc[0]
    book_genre = df_book["genre"].iloc[0]
    book_price = f"${df_book['book price'].iloc[0]}"
    book_rating = df_book['rating'].iloc[0]
    book_year = df_book['year of publication'].iloc[0]

    st.title(book_title)
    st.subheader(book_genre)
    col1, col2, col3 = st.columns(3)
    col1.metric("Price", book_price)
    col2.metric("Rating", book_rating)
    col3.metric("Year of Publications", book_year)


    st.divider()

    for row in df_reviews_f.values:
        message = st.chat_message(f"{row[4]}")
        message.write(f"**{row[2]}**")
        message.write(row[5])


