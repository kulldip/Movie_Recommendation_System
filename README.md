# Movie Recommendation System

A content-based Movie Recommendation System built to understand how movie recommendation systems work from the ground up.

The project uses the **TMDB 5000 Movie Dataset** and recommends movies based on similarities in their content using **TF-IDF and Cosine Similarity**.

## Live Demo

https://movie-recommendation-system-x5kd.onrender.com/

## Objective

The main goal of this project was to understand the complete workflow of a content-based recommendation system:

```text
Raw Movie Data
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Tag Creation
      ↓
TF-IDF Vectorization
      ↓
Cosine Similarity
      ↓
Top 5 Recommendations
      ↓
Streamlit Deployment
```

## Dataset

The project uses the **TMDB 5000 Movie Dataset**:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

Movie information used includes:

* Genres
* Keywords
* Cast
* Director
* Movie Overview

These features are combined into a single `tags` column to represent each movie.

## How It Works

### 1. Data Preprocessing

The movie and credits datasets are merged and relevant information is extracted from the structured metadata.

Missing movie overviews are also handled during preprocessing.

### 2. Feature Engineering

The following information is combined:

```text
Overview + Genres + Keywords + Cast + Director
```

This creates a text-based representation of each movie.

### 3. TF-IDF

TF-IDF is used to convert the movie tags into numerical vectors.

```python
TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)
```

### 4. Cosine Similarity

Cosine Similarity is used to calculate how similar movies are to each other.

For a selected movie, the system finds the movies with the highest similarity scores and returns the top five recommendations.

## TMDB API

The **TMDB API** is used to fetch movie posters dynamically using the movie ID.

The API key is stored as an environment variable rather than directly in the source code.

## Technologies Used

| Technology   | Purpose                         |
| ------------ | -------------------------------- |
| Python       | Core programming                |
| Pandas       | Data preprocessing              |
| NumPy        | Numerical operations            |
| Scikit-learn | TF-IDF and Cosine Similarity    |
| NLTK         | Text preprocessing and stemming |
| Streamlit    | Web application                 |
| Requests     | API requests                    |
| TMDB API     | Movie posters                   |
| Git/GitHub   | Version control                 |
| Git LFS      | Large file management           |
| Render       | Deployment                      |

## Project Structure

```text
Movie_Recommendation_System/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kulldip/Movie_Recommendation_System.git
cd Movie_Recommendation_System
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your TMDB API key as an environment variable:

```powershell
$env:TMDB_API_KEY="YOUR_TMDB_API_KEY"
```

Run the application:

```bash
streamlit run app.py
```

## Limitations

* Recommendations depend on the quality of the available movie metadata.
* TF-IDF focuses mainly on word-level similarity and does not fully understand semantic meaning.
* The system does not use user ratings or watch history.
* The quality of recommendations depends on how the `tags` feature is constructed.
* The similarity matrix can become large as the number of movies increases.

## Future Improvements

* Experiment with SBERT for semantic similarity.
* Build a hybrid TF-IDF + SBERT recommendation system.
* Add ratings and popularity to the recommendation score.
* Implement collaborative filtering.
* Evaluate recommendations using Precision@K and Recall@K.
* Improve the user interface with additional movie information.

## What I Learned

This project helped me understand the fundamentals of a content-based recommendation system, including:

* Data preprocessing
* Feature engineering
* Text preprocessing
* TF-IDF vectorization
* Cosine similarity
* API integration
* Streamlit development
* Git and Git LFS
* Machine learning application deployment

## Author

**Kuldip Mhase**

GitHub: [https://github.com/kulldip](https://github.com/kulldip)

## Live Application

[https://movie-recommendation-system-x5kd.onrender.com/](https://movie-recommendation-system-x5kd.onrender.com/)
