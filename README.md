# 🎬 Movie Recommender System

An end-to-end Machine Learning web application that builds a personalization engine to recommend relevant movies using content-based filtering techniques.

## 📌 Project Overview
This project processes text metadata from the **TMDB 5000 Movies** dataset to compute contextual similarities between films. It features an interactive, user-friendly **Flask web interface** where users can select a movie and instantly receive top related recommendations backed by rigorous NLP operations.

---

## 🛠️ Tools & Technologies Used

### 🔹 Programming & Frameworks
* **Python** — Core programming language for processing logic.
* **Flask** — Lightweight web framework used for building and serving the application.
* **Jupyter Notebook** — Environment for exploratory data analysis (EDA), text pre-processing, and experimentation.

### 🔹 Machine Learning & NLP
* **TF‑IDF Vectorization** — Used for text feature extraction to convert movie tags and summaries into numerical vectors.
* **Cosine Similarity** — Mathematical metric utilized to calculate proximity scores between vector spaces.
* **Pickle** — Serializes components (`movie.pkl`, `movie_dict.pkl`) to smoothly deliver pre-computed models to the Flask instance.

### 🔹 Data & Datasets
* **TMDB 5000 Movies Dataset** (`tmdb_5000_movies.csv`)
* **TMDB 5000 Credits Dataset** (`tmdb_5000_credits.csv`)

### 🔹 Frontend & UI
* **HTML5** — Document structural templates (`index.html`, `recommend.html`).
* **CSS3 / Bootstrap** — Responsive styling, responsive grids, and layout architecture.

### 🔹 Devops & Environment
* **Git & GitHub** — Version control management.
* **Virtual Environment (`venv`)** — Standard package and dependency isolation.
* **Requirements.txt** — Explicit framework version locking for pipeline reproducibility.

---

## 📂 Project Structure

```text
Recommender-System/
├── dataset/                # Raw TMDB csv files
├── notebooks/              # Jupyter Notebooks for EDA and processing
│   └── recommendation_engine.ipynb
├── models/                 # Saved similarity artifacts (movie_dict.pkl)
├── templates/              # HTML frontend layout views
│   ├── index.html
│   └── recommend.html
├── static/                 # Styled CSS stylesheets, scripts, and media
├── app.py                  # Core Flask server execution engine
├── requirements.txt        # System module dependencies
└── README.md               # Project documentation
```

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com
cd Recommender-System
```

### 2. Create and Activate a Virtual Environment
```bash
python -8 -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Boot Up the Server
```bash
python app.py
```
Open `http://127.0.0` in your browser to test it out!
