import json
import numpy as np
import faiss
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

    # Sets-up FAISS (The Librarian) ONE time
    # It creates an index based on how long the vectors are (dimension)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)   # We can say that it adds our books to the library

    print("✅ The Shrine is ready.")

except FileNotFoundError:
    print("Error: Embeddings not found. Did you run create_embeddings.py?")
    model = None
    index = None


# --- THE NEWER FAST SEARCH FUNCTION ---
def search_context(query):
    if model is None or index is None:
        return "System Error", "The Shrine's memory is damaged."

    # Translate the Question
    # Just does the quick math!
    # It wraps the Question in a list [query] because the model expects a list
    query_vector = model.encode([query])

    # Searching!
    # k=1 means "Give me the Top 1 best match"
    k = 1
    distances, indices = index.search(query_vector, k)

    # The 'indices' result tells us which document number matched best
    best_doc_index = indices[0][0]
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
