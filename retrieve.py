import json
import os
import numpy as np
from google import genai
from google.genai import types
from dotenv import load_dotenv

# --- SETUP ---
load_dotenv()
my_key = os.getenv("GOOGLE_API_KEY")

if not my_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env file!")
    model = None
else:
    client = genai.Client(api_key=my_key)

# --- LOAD DATA ---
print("⏳ The Shrine is awakening (Loading Cloud Memory)...")
try:
   # Loads our data (The Book) ONE time
    embeddings = np.load("shrine_embeddings.npy")

    with open("shrine_map.json", "r") as f:
        data_map = json.load(f)
        documents = data_map["documents"]
        doc_names = data_map["names"]

    print("✅ The Shrine is ready (using NumPy for search).")

except FileNotFoundError:
    print("Error: Embeddings not found. Did you run create_embeddings.py?")
    embeddings = None


# --- THE NEWER FAST SEARCH FUNCTION ---
def search_context(query):
    if embeddings is None:
        return "System Error", "The Shrine's memory is damaged."

    try:
        # 1. Embeds the Query (Cloud Side) ☁️
        # I ask Google to turn the question into numbers
        response = client.models.embed_content(
            model="text-embedding-004",
            contents=query,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY"  # optimized for questions
            )
        )

        # Extracts the vector from the response object
        query_vector = np.array(response.embeddings[0].values)

        # 2. Math (Dot Product)
        # Compares the question vector to all document vectors
        scores = np.dot(embeddings, query_vector)

        # 3. Finds the Winner (The best matched document)
        # np.argmax tells me the *index* of the highest score
        best_doc_index = np.argmax(scores)

        return doc_names[best_doc_index], documents[best_doc_index]

    except Exception as e:
        print(f"Search Error: {e}")
        return "Error", "I could not search the memory."


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
