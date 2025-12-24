import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Setup my data source
data_folder = "data"
files = ["lore_asan.txt", "caretaker_rules.txt",
         "tech_stack.txt", "author_bio.txt"]

# Load The pre-trained model
# This downloads a small model the first time someone runs it.
print("Loading the model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

documents = []
doc_names = []

# Read the text files
print("Reading files...")
for filename in files:
    file_path = os.path.join(data_folder, filename)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            documents.append(content)
            doc_names.append(filename)
            print(f" - Loaded: {filename}")
    except FileNotFoundError:
        print(
            f" WARNING: Could not find {filename}. Make sure it is in the 'data' folder!")

# Turn text into numbers (Embeddings)
if documents:
    print("Converting text to numbers...")
    embeddings = model.encode(documents)

    # Save the results
    # It saves the numbers to a .npy file (fast math format)
    np.save("shrine_embeddings.npy", embeddings)

    # It saves the actual text to a .json file so the user can look it up later
    with open("shrine_map.json", "w") as f:
        json.dump({"documents": documents, "names": doc_names}, f)

    print("✅ Success! 'shrine_embeddings.npy' and 'shrine_map.json' created.")
else:
    print("❌ No documents found. Please check your data folder.")
