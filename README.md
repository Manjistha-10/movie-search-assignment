# Movie Semantic Search Assignment

This repository contains my solution for the **Semantic Search on Movie Plots** assignment.  
It uses [SentenceTransformers](https://www.sbert.net) (`all-MiniLM-L6-v2`) to build embeddings of movie plots and performs semantic search using cosine similarity.

---

## Project Overview
- Implemented a semantic search engine for movie plots.
- The core function is `search_movies(query, top_n)` which returns the top matching movies.
- Verified correctness with unit tests (`tests/test_movie_search.py`).
- Demonstrated step-by-step solution in `movie_search_solution.ipynb`.

---

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Manjistha-10/movie-search-assignment.git
   cd movie-search-assignment
   ```

2. (Optional but recommended) Create a virtual environment:
    ```bash
    python -m venv venv
    # Activate
    venv\Scripts\activate   # Windows
    source venv/bin/activate # macOS/Linux
    ```

3. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the notebook (optional demo / explanation):
    ```bash
    jupyter notebook movie_search_solution.ipynb
    ```

---

## Testing

Run unit tests to verify functionality:
    ```bash
    python -m unittest tests/test_movie_search.py -v
    ```

Expected: all 4 tests should pass.

---

## Example Usage in Python
```python
from movie_search import search_movies
results = search_movies("spy thriller in Paris", top_n=3)
print(results)
```