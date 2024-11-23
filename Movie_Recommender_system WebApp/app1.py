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

# Apply custom CSS for background and styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #FFFFFF;
        }
        .title {
            font-family: 'Arial Black', sans-serif;
            color: #FF6347;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-family: 'Verdana', sans-serif;
            color: #FFD700;
        }
        .movie {
            font-family: 'Georgia', serif;
            background: #1C1C1C;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            box-shadow: 2px 2px 5px #000000;
        }
        .movie:hover {
            background: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app interface
st.markdown('<h1 class="title">🎥 Movie Recommender System 🎬</h1>', unsafe_allow_html=True)

# Dropdown menu for movie selection
movie_name = st.selectbox(
    "Select or Type a Movie Title:",
    movies['title'].values
)

# Button for recommendations
if st.button('Recommend'):
    recommendations = recommend(movie_name)
    st.markdown('<h2 class="subheader">Recommended Movies:</h2>', unsafe_allow_html=True)
    for movie in recommendations:
        st.markdown(f'<div class="movie">{movie}</div>', unsafe_allow_html=True)
