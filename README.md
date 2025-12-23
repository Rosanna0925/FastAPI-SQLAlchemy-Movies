# ** Movie Database Management System**
A lightweight, web-based movie management application built with **FastAPI** and **SQLAlchemy**. This project provides a user-friendly interface to manage a digital library of movies using full CRUD (Create, Read, Update, Delete) operations.

## Features

**-View Movie Library:** Browse a comprehensive list of all movies stored in the database on the main dashboard.
**-Add New Movies:** Integrated add.html interface that captures form data from the browser to expand your collection.
**-Update Information:** Modify details of existing movie records dynamically.
**-Delete Records:** Remove entries from the database with a single action.
**-Interactive API Docs:** Fully documented endpoints powered by Swagger UI.

## Tech Stack

<ul>
<li>
**-Framework:** [FastAPI](https://fastapi.tiangolo.com/)</li>
<li>
**-ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)</li>
<li>
**-Database:** SQLite</li>
<li>
**-Templating:** Jinja2</li>
<li>
**-Frontend:** HTML5, CSS3</li>
</ul>

## Project Structure

```text
├── main.py              # Main application logic (API, Models, and Database config)
├── README.md            # Project documentation
├── test.db              # SQLite database file (generated after first run)
├── templates/           # HTML frontend files
│   ├── index.html       # Homepage showing all movies
│   ├── add.html         # Form to add new movie entries
│   └── edit.html        # Form to update existing movies information
└── requirements.txt     # Project dependencies
```

## Getting Started
**1.Installation**
Clone the repository and navigate into the project directory:
```git clone https://github.com/Rosanna0925/fastapi-practice.git
cd movie-database-fastapi```

**2.Set Up Virtual Environment**

```python -m venv venv
source venv/bin/activate```

**3.Install Dependencies**

```pip install -r requirements.txt```

**4.Run the Application**

```uvicorn main:app --reload```

The application will be available at: http://127.0.0.1:8000

## API Documentation
FastAPI automatically generates interactive documentation for the backend logic. You can explore the API endpoints here:

**-Swagger UI:** http://127.0.0.1:8000/docs
**-ReDoc:** http://127.0.0.1:8000/redoc
