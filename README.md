# The Shrine - Retrieval-Augmented Q&A Prototype (Flask)

**Short summary**
This repository is a small, focused prototype that combines a Flask web app, a local embedding + FAISS retrieval layer, and a generative model (Google Gemini) to answer user questions from a small local document set. It is intentionally a prototype - suitable for demos and learning. Production hardening is listed in the **Production notes** section.

---

## Tech stack (quick)

- Python 3.9+ (recommended)
- Flask - web server and templates
- sentence-transformers (`all-MiniLM-L6-v2`) - embeddings
- FAISS (`faiss-cpu`) - vector index / nearest-neighbor retrieval
- Google Generative AI client (`google-generativeai`) - model generation
- numpy - arrays and .npy storage
- python-dotenv - local env vars

---

## Repo layout (important files)

- `app.py` - Flask application and all HTTP routes (`/`, `/sell`, `/ask`, etc.).
- `the_shrine.py` - `Shrine` class: OOP business logic (inventory, persistence, actions).
- `ask_shrine.py` - orchestration: retrieve context → assemble prompt → call Gemini.
- `retrieve.py` - FAISS index loader and `search_context(query)` function.
- `create_embeddings.py` - create embeddings from `data/*.txt` and write `shrine_embeddings.npy` + `shrine_map.json`.
- `templates/` - `index.html`, `about.html` and Jinja2 templates.
- `static/` - CSS, JS, and media assets.
- `data/` - text documents used for retrieval (e.g., `lore_asan.txt`, `caretaker_rules.txt`, ...).
- `.env` (not committed) - store `GOOGLE_API_KEY` here.

---

## Prerequisites

1. Python 3.9 or newer installed.
2. Virtual environment recommended.
3. Internet access for model downloads and the Google Generative AI API (if using the `ask` flow).
4. A valid Google Generative AI API key for `ask_shrine.py` (put in `.env` as `GOOGLE_API_KEY`).

---

## How to run locally (step-by-step)

Open a terminal in the project root and follow these commands exactly.

### 1) Create and activate a virtual environment

```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3) Prepare environment variables

Create a .env file in the project root with the following line:
`GOOGLE_API_KEY=your_real_google_generative_api_key_here`
Do not commit `.env` to source control.

### 4) Create embeddings (one-time step after you add `data/\*.txt`)

```bash
python create_embeddings.py
```

- This reads the files listed in `create_embeddings.py` (the `data` folder).
- It writes `shrine_embeddings.npy` and `shrine_map.json`.
- If no documents exist, the script warns and exits.

### 5) (Optional) Test retrieval locally

```bash
python retrieve.py
```

- This runs a simple interactive loop. Type a question to see which document is retrieved.

### 6) Run the Flask app

```bash
python app.py
```

- By default it runs in debug mode on `http://127.0.0.1:5000`.
- Open the URL in your browser and try the chat box ("Ask the Spirits"). The `/ask` endpoint runs retrieval + Gemini generation.

```mermaid
flowchart LR
  Browser["Browser (index.html)"]
  Browser -->|POST /ask (JSON)| Flask["Flask app (app.py)"]
  Flask -->|call| Ask["ask_shrine.py"]
  Ask -->|call| Retrieve["retrieve.py (FAISS index)"]
  Retrieve -->|returns context| Ask
  Ask -->|call| Gemini["Google Generative AI (Gemini)"]
  Gemini -->|answer| Ask
  Ask -->|returns JSON| Flask
  Flask -->|response| Browser
  subgraph Storage
    embeddings["shrine_embeddings.npy"]
    map["shrine_map.json"]
    data_files["data/*.txt"]
  end
  Retrieve --> embeddings
  Retrieve --> map
  Retrieve --> data_files
```
