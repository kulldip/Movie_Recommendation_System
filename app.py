import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="uv.png",
    layout="wide"
)

def fetch_poster(movie_id):
    responce = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=988d5a318cb43df6cc566424cc1b615d&language=en-US')
    data = responce.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/original/" + poster_path
    return None



st.title("Movie Recommandation System") 
similarity = pickle.load(open('similarity.pkl','rb'))
movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(list(movie_dict.items()),columns=['index','title'])


def recommend(movie):
    movie_index = int(movies[movies['title'] == movie].index[0])
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]
    r_m = []
    r_m_p = []
    for i in movie_list:
        row_index = i[0]
        movie_id = movies.iloc[row_index]['index']
        movie_title = movies.iloc[row_index]['title']
        r_m.append(movie_title)
        r_m_p.append(fetch_poster(movie_id))
    return r_m, r_m_p



option = st.selectbox(
    "Select Movie",
    (movies['title']),

)
if st.button('Recommend'):
    names, posters = recommend(option)
    cols = st.columns(5)
    for col, name, poster_url in zip(cols, names, posters):
        with col:
            if poster_url:
                st.image(
                    poster_url,
                    use_container_width=True
                )
            st.markdown(
                f"""
                <div style="
                    text-align: center;
                    margin-top: 10px;
                    min-height: 55px;
                    font-size: 18px;
                    font-weight: 600;
                    line-height: 1.25;
                ">
                    {name}
                </div>
                """,
                unsafe_allow_html=True
            )