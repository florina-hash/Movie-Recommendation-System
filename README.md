# Movie Recommendation System 🎬

A Content-Based Movie Recommender built with Python that suggests movies based on their plot descriptions and genres.
🚀 Features
* **Natural Language Processing:** Uses **CountVectorizer** to turn text data into mathematical vectors.
* **Smart Recommendations:** Implements **Cosine Similarity** to calculate the distance between movies.
* **Data Cleaning:** Processes messy JSON-formatted genres into clean, usable tags.

🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas, Scikit-Learn, NLTK, AST
* **Platform:** Google Colab

📊 How it Works
1. **Data Acquisition:** Uses the TMDB 5000 Movies dataset.
2. **Feature Engineering:** Combines movie overviews, genres, and keywords into a single "tags" column.
3. **Vectorization:** Converts tags into a 5,000-dimensional space.
4. **Similarity Mapping:** Measures the angle between movie vectors to find the top 5 closest matches.
