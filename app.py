from flask import Flask, render_template,request
import pickle
import requests
import os 
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor


load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
print("TMDB API KEY LOADED:", bool(TMDB_API_KEY))
poster_cache = {}

url ="https://api.themoviedb.org/3/movie/58"
params ={
    "api_key":TMDB_API_KEY
}

response = requests.get(url,params=params)
print("TMDB status:",response.status_code)
data = response.json()

print("Movie:",data.get("title"))
print("Poster:",data.get("poster_path"))

app = Flask(__name__)

movies = pickle.load(open('movie.pkl','rb'))
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_details = pickle.load(open('movie_details.pkl','rb'))

print("Recommendation data loaded:",movies.shape)
print("Similarity matrix shape:", similarity.shape)
print("Movie details loaded:", movies_details.shape)

@app.route('/')
def home():

    movie_list = movies[
        ['movie_id', 'title']
    ].head(20).to_dict('records')

    for movie in movie_list:

        url = f"https://api.themoviedb.org/3/movie/{movie['movie_id']}"

        response = requests.get(
            url,
            params={"api_key": TMDB_API_KEY}
        )

        movie['poster_url'] = None

        if response.status_code == 200:

            data = response.json()

            poster_path = data.get('poster_path')

            if poster_path:
                movie['poster_url'] = (
                    f"https://image.tmdb.org/t/p/w500{poster_path}"
                )

    return render_template(
        'index.html',
        movies=movie_list
    )
    
    
def get_recommendations(movie_id):
    
    movie_index = movies[movies['movie_id'] == movie_id].index[0]
    
    recommendations = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    
    recommended_movies=[]
    
    for i in recommendations:
        recommended_movies.append(
            movies.iloc[i[0]][['movie_id', 'title']].to_dict()
        )
    return recommended_movies


@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):

    movie = movies_details[
        movies_details['movie_id'] == movie_id
    ].iloc[0]

    genres = eval(movie['genres'])
    genres_names = [genre['name'] for genre in genres]

    recommendations = get_recommendations(movie_id)

    # Main movie poster
    poster_url = poster_cache.get(movie_id)

    if poster_url is None:

        url = f"https://api.themoviedb.org/3/movie/{movie_id}"

        response = requests.get(
            url,
            params={"api_key": TMDB_API_KEY}
        )

        if response.status_code == 200:

            data = response.json()

            poster_path = data.get('poster_path')

            if poster_path:

                poster_url = (
                    f"https://image.tmdb.org/t/p/w500{poster_path}"
                )

                poster_cache[movie_id] = poster_url


    # Function to fetch recommendation poster
    def fetch_poster(rec):

        movie_id = rec['movie_id']

        # Check cache first
        rec['poster_url'] = poster_cache.get(movie_id)

        # If poster is not cached, call TMDB
        if rec['poster_url'] is None:

            rec_url = (
                f"https://api.themoviedb.org/3/movie/"
                f"{movie_id}"
            )

            rec_response = requests.get(
                rec_url,
                params={"api_key": TMDB_API_KEY}
            )

            if rec_response.status_code == 200:

                rec_data = rec_response.json()

                rec_poster_path = rec_data.get('poster_path')

                if rec_poster_path:

                    rec['poster_url'] = (
                        f"https://image.tmdb.org/t/p/w500"
                        f"{rec_poster_path}"
                    )

                    # Save poster URL in cache
                    poster_cache[movie_id] = rec['poster_url']

        return rec


    # Fetch 5 recommendation posters in parallel
    with ThreadPoolExecutor(max_workers=5) as executor:

        recommendations = list(
            executor.map(fetch_poster, recommendations)
        )


    return render_template(
        'movie.html',
        movie=movie,
        genres=genres_names,
        recommendations=recommendations,
        poster_url=poster_url
    )
    
    
@app.route('/search')
def search():

    query = request.args.get('query', '').strip()

    results = movies[
        movies['title'].str.contains(
            query,
            case=False,
            na=False
        )
    ][['movie_id', 'title']].drop_duplicates(
        subset=['movie_id']
    ).head(20).to_dict('records')

    # Fetch posters for ssearch results
    for movie in results:

        url = f"https://api.themoviedb.org/3/movie/{movie['movie_id']}"

        response = requests.get(
            url,
            params={"api_key": TMDB_API_KEY}
        )

        movie['poster_url'] = None

        if response.status_code == 200:

            data = response.json()

            poster_path = data.get('poster_path')

            if poster_path:
                movie['poster_url'] = (
                    f"https://image.tmdb.org/t/p/w500{poster_path}"
                )


    return render_template(
        'search.html',
        results=results,
        query=query
    )


if __name__ == '__main__':
    app.run(debug=True)