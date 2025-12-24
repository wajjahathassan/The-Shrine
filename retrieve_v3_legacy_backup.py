import json
import numpy as np

from sentence_transformers import SentenceTransformer

# --- GLOBAL SETUP (Runs only once!) ---
# --- FASTER VERSION ---
print("⏳ The Shrine is awakening (Loading AI Models)...")

try:
    # Loads the Brain ONE time
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Loads our data (The Book) ONE time
    embeddings = np.load("shrine_embeddings.npy")
    with open("shrine_map.json", "r") as f:
        data_map = json.load(f)
        documents = data_map["documents"]
        doc_names = data_map["names"]

    print("✅ The Shrine is ready (using NumPy for search).")

except FileNotFoundError:
    print("Error: Embeddings not found. Did you run create_embeddings.py?")
    model = None
    embeddings = None


# --- THE NEWER FAST SEARCH FUNCTION ---
def search_context(query):
    if model is None or embeddings is None:
        return "System Error", "The Shrine's memory is damaged."

    # Translate the Question
    # Just does the quick math!
    # It wraps the Question in a list [query] because the model expects a list
    query_vector = model.encode([query])

    # Calculate Similarity (The Dot Product)
    # Multiplying the query vector by ALL document vectors at once!
    # This creates a list of scores, one for each document.
    # Note: Using .T (Transpose) to line up the numbers for multiplication.
    scores = np.dot(embeddings, query_vector.T)

    # Finds the Winner (The best matched document)
    # np.argmax tells us the *index* of the highest score
    best_doc_index = np.argmax(scores)

    best_doc_text = documents[best_doc_index]
    best_doc_name = doc_names[best_doc_index]

    return best_doc_name, best_doc_text


if __name__ == "__main__":
    while True:
        # Testing it out right here in the terminal
        user_query = input("Ask a question about the Shrine: ")
        if user_query == "quit":
            break
        source, answer = search_context(user_query)

        print("\n--- RETRIEVED CONTEXT ---")
        print(f"Source: {source}")
        print(f"Content: {answer}")
        print("-------------------------")
