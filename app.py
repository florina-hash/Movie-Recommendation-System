import streamlit as st
import pickle
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Cine-Match AI", page_icon="🎬", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #050509;
        color: #e0fbfc;
    }

    h1 {
        color: #00f3ff;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 800;
        letter-spacing: 2px;
        text-shadow: 2px 2px 10px rgba(0, 243, 255, 0.5);
    }

    /* Fixing that weird green box (st.success) */
    .stAlert {
        background-color: #0a0a12 !important;
        color: #00f3ff !important;
        border: 1px solid #00f3ff !important;
        border-radius: 5px !important;
    }
    .stAlert p {
        color: #00f3ff !important;
        font-weight: bold;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: transparent;
        color: #00f3ff;
        font-weight: bold;
        border: 2px solid #00f3ff;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #00f3ff;
        color: #050509;
        box-shadow: 0 0 20px #00f3ff;
    }

    /* Movie Cards */
    .movie-card {
        background-color: #0a0a12;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #333;
        margin-bottom: 12px;
        transition: 0.3s;
    }
    .movie-card:hover {
        border: 1px solid #ff0055;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1>CINE-MATCH AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff0055;'>MACHINE LEARNING MOVIE INTELLIGENCE</p>", unsafe_allow_html=True)
st.write("---")

#  Load Data
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

selected_movie_name = st.selectbox(
    'SELECT A MOVIE YOU LIKE:',
    movies['title'].values)

st.write("") 

if st.button('GENERATE MATCHES'):
    with st.spinner('Scanning database...'):
        recommendations = recommend(selected_movie_name)
        st.info(f"ANALYSIS COMPLETE: Recommendations for {selected_movie_name}")
        
        for i in recommendations:
            st.markdown(f"""
                <div class="movie-card">
                    <span style="color: #e0fbfc; font-size: 18px;">✨ {i}</span>
                </div>
            """, unsafe_allow_html=True)
