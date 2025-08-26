"""
Semantic Search Engine for Movie Plots using SentenceTransformers.
Implements search_movies(query, top_n) to return the most relevant movies.
"""

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")  

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute embeddings for all movie plots
embeddings = model.encode(df['plot'].tolist(), convert_to_tensor=False)

def search_movies(query: str, top_n: int = 5) -> pd.DataFrame:
    """
    Search for the most relevant movies given a natural language query.

    Args:
        query (str): Natural language search query.
        top_n (int): Number of top results to return.

    Returns:
        pd.DataFrame: DataFrame with columns ['title', 'plot', 'similarity'].
    """
    # Encode the query into an embedding
    query_embedding = model.encode([query], convert_to_tensor=False)

    # Compute cosine similarity between query and movie embeddings
    similarities = cosine_similarity(query_embedding, embeddings)[0]

    # Attach similarity scores to the DataFrame
    results = df.copy()
    results['similarity'] = similarities

    # Sort by similarity (highest first) and return top_n results
    results = results.sort_values(by='similarity', ascending=False).head(top_n)

    return results[['title', 'plot', 'similarity']].reset_index(drop=True)


# Optional: Demo when run directly
if __name__ == "__main__":
    query = "spy thriller in Paris"
    results = search_movies(query, top_n=3)
    print(f"\nSearch results for: '{query}'\n")
    print(results)
