# The Digital Shrine (RAG Portfolio Project)

## Project Overview

This project is a web application that acts as a digital shrine. I built it to demonstrate my full-stack development skills. It uses an AI "Caretaker" that answers questions based on specific text files I provided.

The main goal was to build a Retrieval-Augmented Generation (RAG) system from scratch. I wanted to show that I can connect a Python backend to a modern Large Language Model (LLM) and make it work with custom data.

## Why I Built This

I am currently looking to build my future in South Korea. I wanted to create a project that mixes high-tech engineering with the traditional feeling of a historic shrine.

Most tutorials just show how to use a pre-made tool. I wanted to understand how the search actually works, so I built the retrieval system myself using FAISS and Python.

## Tech Stack

I used the following tools to build this application:

- **Language:** Python 3.10+
- **Web Framework:** Flask (for the backend server)
- **Database:** FAISS (Facebook AI Similarity Search) for vector storage
- **AI Model:** Google Gemini 1.5 Flash (via API)
- **Frontend:** HTML5, CSS3, and JavaScript (Vanilla)

## Key Features

### 1. Retrieval-Augmented Generation (RAG)

The core of this project is the RAG pipeline.

- **Ingestion:** I wrote a script (`create_embeddings.py`) that reads text files and converts them into vector embeddings using `SentenceTransformer`.
- **Retrieval:** When a user asks a question, the system uses FAISS to find the most similar text chunk in the database.
- **Generation:** The retrieved text is combined with the user's question and sent to Google Gemini 1.5 Flash to generate an accurate answer.

### 2. Contextual Chat Memory

The application supports multi-turn conversations.

- **Problem:** Standard API calls are stateless, meaning the AI forgets the previous question immediately.
- **Solution:** I implemented a global list in Flask that stores the conversation history. This history is passed to the AI with every new request, allowing it to understand pronouns like "he" or "it" based on previous context.

### 3. Asynchronous Typing Effect

To match the "mystical" theme, answers do not appear instantly.

- **Implementation:** I used a recursive JavaScript function to render the text one character at a time.
- **Challenge:** I had to ensure that appending the "Source" citation did not interrupt the typing animation. I solved this by creating separate DOM elements for the answer and the source.

## How to Run

### Prerequisites

- Python 3.10 or higher
- A Google Gemini API Key

### Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/yourusername/shrine-rag.git](https://github.com/yourusername/shrine-rag.git)
   cd shrine-rag
   ```

2. **Create and activate a virtual environment:**
   python -m venv .venv

# Windows:

.venv\Scripts\activate

# Mac/Linux:

source .venv/bin/activate

3. **Install dependencies:**
   pip install -r requirements.txt

### Setup

1. Create a .env file in the root directory.

2. Add your Google API key:
   GOOGLE_API_KEY=your_api_key_here

### Usage

1. **Build the Vector Database:** Run the ingestion script to read the text files in data/ and generate the FAISS index.
   python create_embeddings.py

2. **Start the Caretaker:** Launch the Flask web server.
   python app.py

3. **Visit the Shrine:** Open your browser and go to http://127.0.0.1:5000.
