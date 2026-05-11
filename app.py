import streamlit as st
import pickle
import pandas as pd

# Page Configuration
st.set_page_config(page_title="NEO-RECOM v1.0", page_icon="📡", layout="centered")

st.markdown("""
    <style>
    /* Main app background */
    .stApp {
        background-color: #050509; /* Very deep, dark blue-black */
        color: #e0fbfc; /* Light cyan text */
    }

    /* Titles and headers */
    h1 {
        color: #00f3ff; /* Electric Cyan */
        text-align: center;
        text-transform: uppercase;
        font-family: 'Courier New', monospace;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #00f3ff, 0 0 20px #00f3ff;
    }
    .subheader {
        color: #ff0055; /* Neo Pink/Magenta accent */
        text-align: center;
        font-family: 'Courier New', monospace;
        letter-spacing: 1px;
    }

    /* The Main Button */
    .stButton>button {
        width: 100%;
        border-radius: 2px; /* Less rounded, more blocky */
        height: 3em;
        background-color: #050509;
        color: #00f3ff;
        font-weight: bold;
        text-transform: uppercase;
        border: 2px solid #00f3ff; /* Electric border */
        font-family: 'Courier New', monospace;
        box-shadow: 0 0 10px #00f3ff;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00f3ff;
        color: #050509;
        box-shadow: 0 0 20px #00f3ff, 0 0 30px #ff0055;
    }

    /* Recommendation Cards */
    .movie-card {
        background-color: #0a0a12; /* Slightly lighter dark blue */
        padding: 15px;
        border-radius: 0px; /* Sharp corners */
        border: 1px solid #00f3ff; /* Thin cyan border */
        margin-bottom: 15px;
        box-shadow: inset 0 0 10px rgba(0, 243, 255, 0.2);
    }
    .movie-card:hover {
        border: 1px solid #ff0055; /* Hover turns border magenta */
        box-shadow: inset 0 0 15px rgba(255, 0, 85, 0.3), 0 0 10px rgba(0, 243, 255, 0.3);
    }

    /* Success Message styling */
    .stAlert {
        background-color: #0a0a12;
        border: 1px solid #ff0055; /* Magenta border */
        color: #ff0055;
        border-radius: 0px;
    }
    
    /* Text Input/Selectbox labels */
    label {
        color: #00f3ff !important;
        font-family: 'Courier New', monospace !important;
    }
    </style>
    """, unsafe_allow_html=True)

#  App Title & Subheader
st.markdown("<h1>> NEO-RECOM v1.0</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>> AI-Driven Movie Analysis Interface</p>", unsafe_allow_html=True)
st.write("---")

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

#  UI Layout
selected_movie_name = st.selectbox(
    '> INPUT_TARGET_FILM',
    movies['title'].values)

st.write("") # Static Spacer

if st.button('RUN_SIMILARITY_MATRIX'):
    with st.spinner('> ACCESSING NEURAL NETWORK...'):
        recommendations = recommend(selected_movie_name)
        st.success(f"> MATCHES FOUND FOR: {selected_movie_name.upper()}")
        
        for i in recommendations:
            st.markdown(f"""
                <div class="movie-card">
                    <span style="color: #e0fbfc; font-size: 18px; font-weight: bold; font-family: 'Courier New', monospace;">[🎥] {i}</span>
                </div>
            """, unsafe_allow_html=True)
