import streamlit as st
import pickle
import pandas as pd
import requests

# def fetch_poster(id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(id))
#     data = response.json()
#     return 'https://image.tmdb.org/t/p/w500' + data['poster_path']

sim = pickle.load(open('sim.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = sim[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:6]
    recommended_movie = []  
    recommended_poster = []
    
    for i in movie_list:
        # movie_id = movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        # recommended_poster.append(fetch_poster(movie_id))
    return recommended_movie#, recommended_poster

movie_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_list)


st.title('Movie Recommendation System')
movie_selected = st.selectbox('Enter the movie',
                      movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(movie_selected)
    for i in recommendations:
        st.write(i)
    # names,posters = recommend(movie_selected)
    # col1, col2, col3 , col4, col5 = st.beta_columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1]) 
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
    