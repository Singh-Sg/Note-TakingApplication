# Note-Taking Application

## Project Overview

This project is a basic yet efficient back-end for a note-taking application. The application allows users to create, read, update, and delete (CRUD) notes. Additionally, it integrates LangChain with ChatGPT to summarize notes as a bonus feature.

## Features

- **CRUD Operations:** Create, read, update, and delete notes.
- **Database Integration:** Uses SQLite for storing notes.
- **LangChain Integration:** Integrates with ChatGPT for summarizing notes.
- **Bonus Features:** Potential for additional LangChain functionalities, such as adding an Agent or Chain to search the internet before adding notes.

## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- OpenAI API Key
- LangChain

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/yourusername/note_taking_app.git
cd note_taking_app
```

## Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables
``` bash
OPENAI_API_KEY=your-openai-api-key
```

## Start the Application
``` bash
uvicorn app.main:app --reload
```
 