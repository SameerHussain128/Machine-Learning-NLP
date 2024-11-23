import streamlit as st
import pickle

# Load pickled data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found! Please try a different title."]
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# Streamlit app interface
st.title("Movie Recommender System")

# Dropdown menu for movie selection
movie_name = st.selectbox(
    "Select or Type a Movie Title:",
    movies['title'].values
)

# Button for recommendations
if st.button('Recommend'):
    recommendations = recommend(movie_name)
    st.subheader("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)