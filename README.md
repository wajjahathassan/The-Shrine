# The Shrine | Full-Stack Asset Management System

> **A Python-based RPG inventory system featuring asynchronous state management and AI-driven NPC interactions.**

## 📖 Overview

The Shrine is a web application that simulates the backend mechanics of a Role-Playing Game (RPG). It serves as a technical demonstration of how **Object-Oriented Programming (OOP)** can be used to manage complex application state, user sessions, and persistent data storage in a web environment.

I built this project to bridge the gap between **interactive design** (Game Logic) and **software engineering** (Backend Architecture).

- **Live Demo:** [https://wajahat2106hassan.pythonanywhere.com)]
- **Tech Stack:** Python, Flask, SQLite, JavaScript (ES6), HTML5/CSS3.

## ⚙️ Key Features

### 1. Robust Backend Architecture (OOP)

Instead of relying on global variables, the application logic is encapsulated within a `Shrine` class. This handles:

- **Inventory Management:** Adding, removing, and validating items.
- **Economy System:** Calculating costs and updating "Spirit Energy" currency.
- **Persistence:** Loading and saving user progress to JSON/SQLite to ensure data integrity.

### 2. Asynchronous State Management (AJAX)

To create a seamless user experience, the frontend communicates with the Flask backend using the **Fetch API**.

- **Real-time Updates:** Actions like "Cleaning" or "Selling" update the UI DOM immediately without requiring a full page reload.
- **RESTful Design:** The backend exposes endpoints (e.g., `/sell`) that return JSON data rather than HTML, decoupling the data logic from the presentation layer.

### 3. AI Integration (Google Gemini)

The "Wisdom" feature integrates the **Google Gemini API**.

- The system constructs a dynamic prompt based on the game state.
- It processes the LLM's response to provide unique, context-aware dialogue for the "Caretaker" character.

## 🛠️ Installation & Setup

If you want to run this project locally, follow these steps:

**1. Clone the repository**

```bash
git clone [https://github.com/wajjahathassan/The-Shrine.git](https://github.com/wajjahathassan/The-Shrine.git)
cd The-Shrine
```

**2. Create a virtual environment**

python -m venv venv

# Windows:

venv\Scripts\activate

# Mac/Linux:

source venv/bin/activate

**3. Install dependencies**

pip install -r requirements.txt

**4. Set up Environment Variables Create a .env file in the root folder and add your API key:**

GOOGLE_API_KEY=your_actual_api_key_here

**5. Run the application**

python app.py

Visit http://127.0.0.1:5000 in your browser.

📂 Project Structure
app.py: Main Flask application and route definitions.

app_v11.py: Core business logic and Shrine class definition.

templates/: HTML files with Jinja2 templating.

static/: CSS styles, JavaScript logic, and assets.

requirements.txt: List of Python dependencies.

📬 Contact
Wajahat Hassan

LinkedIn: linkedin.com/in/wajahat-hassan-tech

Email: wajahat.hassan.2106@gmail.com
