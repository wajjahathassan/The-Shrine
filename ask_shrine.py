import os
import google.generativeai as genai
from dotenv import load_dotenv

# imports the search tool I just built!
from retrieve import search_context

# Setup
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Using the same model as my original app
model = genai.GenerativeModel("gemini-2.5-flash")


def ask_the_shrine(user_question, history):
    # Retrieve (The Librarian)
    # Asks the retrieval script to find the best matching text
    source_name, context_text = search_context(user_question)

    # Formats History
    # Joins the list into a single string so the AI can read it
    history_text = "\n".join(history)

    # Augment (The Sandwich)
    # Creates the prompt that forces the AI to use my data
    prompt = f"""You are the wise Caretaker of a digital shrine.
    Use the following pieces of context to answer the question at the end.
    
    If the answer is not in the context, say "The spirits are silent on this matter."
    Do not try to make up an answer
    
    Context:
    {context_text}
    
    Conversation History:
    {history_text}
    
    Question:
    {user_question}
    """

    # Generate (The Oracle)
    response = model.generate_content(prompt)

    return response.text, source_name


if __name__ == "__main__":
    # Test Loop
    print("--- Ask the Shrine (Type 'quit' to exit) ---")
    while True:
        q = input("\nYou: ")
        if q.lower() == "quit":
            break

        answer, source = ask_the_shrine(q)
        print(f"Shrine: {answer}")
        print(f"(Source: {source})")
