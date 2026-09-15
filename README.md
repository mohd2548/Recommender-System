# 🎬 Movie Recommender System

An end-to-end Machine Learning web application that builds a personalization engine to recommend relevant movies based on content metadata analysis.

## 📌 Project Overview
This project processes text metadata (genres, keywords, cast, crew, and overviews) from the popular **TMDB 5000 Movies & Credits** datasets. By combining advanced Text Preprocessing (Stemming) and Text Vectorization techniques, the model computes similarity distances between movies. A user-friendly **Flask web interface** allows users to pick a movie and instantly receive 5 highly related recommendations along with rich metadata profiles.

---

## 🛠️ Tools & Technologies Used

### 🔹 Core Programming & Libraries
* **Python** — Core development language.
* **Pandas & NumPy** — Used heavily for data manipulation, handling missing/duplicate rows, merging dataframes, and feature aggregation.
* **Jupyter Notebook** — Interactive development environment for exploratory data analysis (EDA).

### 🔹 Machine Learning & Natural Language Processing (NLP)
* **`ast.literal_eval`** — Used to safely parse and extract dictionary objects nested inside stringified JSON data structural columns (`genres`, `keywords`, `cast`, `crew`).
* **NLTK (`PorterStemmer`)** — Used to stem words (e.g., converting "dancing", "danced" to "danc") to prevent redundant feature creation.
* **Scikit-Learn (`CountVectorizer`)** — Used to convert text tags into numerical vector arrays using a Bag of Words approach with `max_features=5000` and English stop-words filtering.
* **Scikit-Learn (`cosine_similarity`)** — Used to calculate the angular distance between vectors to establish close relational similarities.

### 🔹 Data Serialization & UI Backend
* **Pickle** — Serializes operational assets to be loaded by the application efficiently:
  * `movie_dict.pkl` — Main index dataframe mapped to a dictionary format.
  * `similarity.pkl` — Pre-calculated mathematical similarity matrix.
  * `movie_details.pkl` — Extracted rich features (`vote_average`, `runtime`, `tagline`, `overview`, `genres`) for rendering a beautiful frontend response.
* **Flask** — Powers the web application server logic.

---

## 📂 Project Structure

```text
Recommender-System/
├── dataset/                # Raw TMDB csv dataset files
├── notebooks/              # Jupyter Notebook containing data pipeline steps
│   └── recommendation_engine.ipynb
├── models/                 # Saved pickle artifacts (.pkl files)
├── templates/              # HTML layout view files (index.html, recommend.html)
├── static/                 # CSS stylesheets, interactive scripts, images
├── app.py                  # Core Flask application script
├── requirements.txt        # System module dependencies 
└── README.md               # Project documentation
```

---

## ⚙️ Data Pipeline Summary (As Coded)
1. **Data Integration:** Merged the TMDB Movies and Credits dataframes matching on the `title` column.
2. **Feature Filtering:** Retained core structural components: `movie_id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
3. **Data Cleaning:** Handled structural null fields via `.dropna()` and validated duplicates.
4. **Tokenization Transformation:** Applied space-removal techniques across fields so names like *"Sam Worthington"* combine into unique structural tokens like *"SamWorthington"* (preventing model vector confusion with other distinct people named "Sam").
5. **Tag Concatenation:** Compressed text metadata fields into a unified `'tags'` paragraph element.
6. **Vector Alignment:** Stemmed the unified strings using NLTK and processed them through `CountVectorizer` to generate an array matrix shape of `(4806, 5000)`.

---

