import streamlit as st
import pickle
import pandas as pd
import requests
st.title('FlickFlow - Personalized Cinema Recommender')

df = pickle.load(open('df_pycharm.pkl','rb'))
df = pd.DataFrame(df)

similarity = pickle.load(open('similarity_pycharm.pkl','rb'))
def recommend(movie_name):
    index = df[df['title'] == movie_name].index[0]

    dis = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)[1:11]
    movies_list = []
    poster_list = []
    for i in dis:
        movie_id = df.iloc[i[0]].movie_id
        movies_list.append(df.iloc[i[0]].title)
        poster_list.append(fetch_poster(movie_id))
    return movies_list,poster_list

def fetch_poster(movie_id):
    url = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=d82f61badfce4bd7305645adbb97ab70&language=en-US".format(movie_id))
    data = url.json()
    poster_path = "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    return poster_path

option = st.selectbox('Select Movie', df['title'].values)

if st.button("Recommend"):
    title, poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(title[0])
        st.image(poster[0])
    with col2:
        st.text(title[1])
        st.image(poster[1])
    with col3:
        st.text(title[2])
        st.image(poster[2])
    with col4:
        st.text(title[3])
        st.image(poster[3])
    with col5:
        st.text(title[4])
        st.image(poster[4])

    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(title[5])
        st.image(poster[5])
    with col7:
        st.text(title[6])
        st.image(poster[6])
    with col8:
        st.text(title[7])
        st.image(poster[7])
    with col9:
        st.text(title[8])
        st.image(poster[8])
    with col10:
        st.text(title[9])
        st.image(poster[9])