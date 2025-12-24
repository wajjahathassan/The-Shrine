import os
import glob
import json
import numpy as np
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Not using 'sentence_transformers' because it is a heavy library,
# and I need to upload my code to PythonAnywhere for a live demo.#
##### from sentence_transformers import SentenceTransformer #####
# Not using 'sentence_transformers' because it is a heavy library,
# and I need to upload my code to PythonAnywhere for a live demo.#

# --- SETUP --- #
load_dotenv()
my_key = os.getenv("GOOGLE_API_KEY")

if not my_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env file!")
    exit()

# 1. Connecting to Google #
client = genai.Client(api_key=my_key)

# --- SETTINGS --- #
# Using a specific model optimized for retrieval (searching) #
MODEL_NAME = "text-embedding-004"


def make_the_embeddings():
    print("🧹 Clearing old memory...")
    all_text_chunks = []
    all_filenames = []

    # 2. Reads the Files #
    text_files = glob.glob("data/*.txt")

    for filename in text_files:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            # Skipping empty files #
            if content:
                all_text_chunks.append(content)
                # Saving just the generic name (e.g., "lore_asan.txt")
                all_filenames.append(os.path.basename(filename))
                print(f"📖 Read: {filename}")

    if not all_text_chunks:
        print("❌ No text found! Are your .txt files in the 'data/' folder?")
        return

    print(f"🧠 Sending {len(all_text_chunks)} memories to the Cloud...")

    # 3. GENERATING EMBEDDINGS #
    # Instead of model.encode(), I'm asking Google to do it. #

    response = client.models.embed_content(
        model=MODEL_NAME,
        contents=all_text_chunks,
        config=types.EmbedContentConfig(
            # Tells Google: "These are facts to be searched later" #
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    # Google sends back a list of embedding objects. #
    # I need to extract the 'values' from each one. #
    embeddings = np.array([e.values for e in response.embeddings])

    # 4. Saves the Data (Using NumPy) #
    np.save("shrine_embeddings.npy", embeddings)

    # I also need to save the map so I know which text belongs to which file #
    with open("shrine_map.json", "w") as f:
        json.dump({"documents": all_text_chunks, "names": all_filenames}, f)

    print("✅ Success! The Shrine's new Cloud Memory is saved.")


if __name__ == "__main__":
    make_the_embeddings()
