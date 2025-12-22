import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


def debug_system():
    # TEST 1: Check the raw file
    print("--- TEST 1: Checking author_bio.txt ---")
    try:
        with open("data/author_bio.txt", "r", encoding="utf-8") as f:
            print(f"File Content:\n{f.read().strip()}")
    except Exception as e:
        print(f"Error reading file: {e}")

    # TEST 2: Check the Search Math
    print("\n--- TEST 2: Checking Search Scores ---")

    # Load data
    embeddings = np.load("shrine_embeddings.npy")
    with open("shrine_map.json", "r") as f:
        data_map = json.load(f)
        names = data_map["names"]

    # Setup Search
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Run Query
    query = "Who created this shrine?"
    print(f"Query: '{query}'")

    query_vector = model.encode([query])

    # Get Top 3 matches
    D, I = index.search(query_vector, 3)  # D = Distances, I = Indices

    print("\nTop 3 Matches (Lower distance is better):")
    for i in range(3):
        idx = I[0][i]
        score = D[0][i]
        name = names[idx]
        print(f"Rank {i+1}: {name} (Score: {score:.4f})")


if __name__ == "__main__":
    debug_system()
