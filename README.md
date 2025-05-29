# research_assistant_ai_agent
Here is a descriptive `README.md` file for your AI Research Assistant project, incorporating the details from your files and our conversation.

-----

# AI Research Assistant Agent

[](https://github.com/Yuvraajb/research_assistant_ai_agent)

This project is an AI-powered Research Assistant designed to help users conduct research on various topics. It utilizes LangChain, Google Gemini, and a suite of tools (like DuckDuckGo Search and Wikipedia) to gather, summarize, and present information, complete with sources. It features a Python (Flask) backend and an interactive React frontend, ready for deployment on Vercel.

## Features

  * **AI-Powered Research:** Leverages Google Gemini via LangChain to understand queries and orchestrate research.
  * **Web Search:** Integrates DuckDuckGo Search to find up-to-date information online.
  * **Wikipedia Integration:** Uses Wikipedia for in-depth-yet-concise information retrieval.
  * **Structured Output:** Provides research results in a clear JSON format, including a summary, sources, and tools used.
  * **API Backend:** Built with Flask, making it easy to interact with via a web interface or other clients.
  * **Interactive Frontend:** A React-based user interface for easy interaction (under development).
  * **Vercel Ready:** Configured for seamless deployment on the Vercel platform.

## Technologies Used

  * **Backend:**
      * Python 3.9+
      * LangChain
      * Google Generative AI (Gemini)
      * Flask
      * Pydantic
      * DuckDuckGo Search
      * Wikipedia
  * **Frontend:**
      * React.js
      * HTML5 & CSS3
      * JavaScript (ES6+)
  * **Deployment:**
      * Vercel

## Project Structure

```
research_assistant_ai_agent/
├── api/
│   └── index.py         # Flask Backend (Vercel Serverless Function)
├── frontend/
│   ├── public/          # React public assets
│   ├── src/             # React source code (App.js, etc.)
│   ├── package.json     # Frontend dependencies
│   └── ...
├── tools.py             # LangChain tool definitions
├── requirements.txt     # Python backend dependencies
├── .env                 # Environment variables (API Keys)
├── vercel.json          # Vercel deployment configuration
└── README.md            # This file
```

## Setup & Installation

**Prerequisites:**

  * Python 3.9+
  * Node.js & npm
  * Git
  * Vercel Account (for deployment)
  * Google AI API Key

**Steps:**

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Yuvraajb/research_assistant_ai_agent.git
    cd research_assistant_ai_agent
    ```

2.  **Setup Backend:**

      * Create a Python virtual environment:
        ```bash
        python3 -m venv venv
        source venv/bin/activate  # On macOS/Linux
        # or
        # venv\Scripts\activate   # On Windows
        ```
      * Install Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```
      * Create a `.env` file in the root directory and add your Google API key:
        ```
        GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
        ```

3.  **Setup Frontend:**

      * Navigate to the frontend directory:
        ```bash
        cd frontend
        ```
      * Install Node.js dependencies:
        ```bash
        npm install
        ```
      * Return to the root directory:
        ```bash
        cd ..
        ```

## Running Locally

You need to run both the backend and frontend servers simultaneously in separate terminals.

1.  **Run Backend (Terminal 1):**

      * Make sure you are in the root directory and your virtual environment is active.
      * Start the Flask server:
        ```bash
        python -m flask --app api.index run
        ```
      * The backend will be available at `http://127.0.0.1:5000`.

2.  **Run Frontend (Terminal 2):**

      * Navigate to the `frontend` directory.
      * Start the React development server:
        ```bash
        npm start
        ```
      * Your browser should open automatically to `http://localhost:3000`.

## Usage

1.  Open `http://localhost:3000` in your browser.
2.  Type your research query into the input field.
3.  Click the "Search" or "Research" button.
4.  The results, including the topic, summary, sources, and tools used, will be displayed on the page.

## Deployment to Vercel

1.  **Push to GitHub:** Ensure your project is pushed to your GitHub repository.
2.  **Import to Vercel:** Connect your GitHub account to Vercel and import the repository.
3.  **Configure Environment Variables:** In your Vercel project settings, add your `GOOGLE_API_KEY` as an environment variable.
4.  **Deploy:** Vercel should automatically detect the `vercel.json` file and deploy your project. It will build the Python backend and the React frontend and handle the routing.
5.  Access your live application via the URL provided by Vercel.

-----
