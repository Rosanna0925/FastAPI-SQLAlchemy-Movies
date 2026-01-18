# **Movie Database Management System**
A robust, web-based movie management application built with FastAPI, PostgreSQL, and Docker. This project demonstrates a professional backend workflow including database migrations and containerized environments.

## Features

* **View Movie Library:** Browse a comprehensive list of all movies stored in the database on the main dashboard.
* **Add New Movies:** Integrated add.html interface that captures form data from the browser to expand your collection.
* **Update Information:** Modify details of existing movie records dynamically.
* **Delete Records:** Remove entries from the database with a single action.
* **Database Migrations:** Version-controlled schema changes using Alembic.
* **Containerized DB:** Reliable PostgreSQL environment powered by Docker Compose.

## Tech Stack


* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)

* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)

* **Database:** PostgreSQL 15

* **Migration Tool:** Alembic

* **Templating:** Jinja2

* **Frontend:** HTML5, CSS3

## Project Structure

```text
├── alembic/              # Database migration scripts and environment
├── alembic.ini           # Alembic configuration
├── docker-compose.yml    # Docker services (PostgreSQL container setup)
├── database.py           # Database engine connection and session logic
├── models.py             # SQLAlchemy ORM models (database table schemas)
├── main.py               # Main application logic and API route handlers
├── README.md             # Project documentation
├── templates/            # HTML frontend files (Jinja2)
│   ├── index.html        # Main dashboard showing movie list
│   ├── add.html          # Interface for adding new movies
│   └── edit.html         # Interface for updating existing records
└── requirements.txt      # Project dependencies and libraries
```

## Getting Started
**1.Installation**
Clone the repository and navigate into the project directory:
```git clone https://github.com/Rosanna0925/FastAPI-SQLAlchemy-Movies.git
cd movie-database-fastapi
```

**2.Set Up Virtual Environment**

```python -m venv venv
source venv/bin/activate
```

**3.Install Dependencies**

```pip install -r requirements.txt```

**4.Start Database (Docker)**

```docker-compose up -d```

**5.Apply Database Migrations**

```alembic upgrade head```

**6.Run the Application**

```uvicorn main:app --reload```

The application will be available at: http://127.0.0.1:8000

## API Documentation
FastAPI automatically generates interactive documentation for the backend logic. You can explore the API endpoints here:

* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc
<div align="center">
  <picture>
    <img src="image/topic photo.jpg"
         width="50%">
  </picture>
</div>


# **Movie Database Management System**
A lightweight, web-based movie management application built with **FastAPI** and **SQLAlchemy**. This project provides a user-friendly interface to manage a digital library of movies using full CRUD (Create, Read, Update, Delete) operations.

## Features

* **View Movie Library:** Browse a comprehensive list of all movies stored in the database on the main dashboard.
* **Add New Movies:** Integrated add.html interface that captures form data from the browser to expand your collection.
* **Update Information:** Modify details of existing movie records dynamically.
* **Delete Records:** Remove entries from the database with a single action.
* **Interactive API Docs:** Fully documented endpoints powered by Swagger UI.

## Tech Stack


* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)

* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)

* **Database:** SQLite

* **Templating:** Jinja2

* **Frontend:** HTML5, CSS3

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
```git clone https://github.com/Rosanna0925/FastAPI-SQLAlchemy-Movies.git
cd movie-database-fastapi
```

**2.Set Up Virtual Environment**

```python -m venv venv
source venv/bin/activate
```

**3.Install Dependencies**

```pip install -r requirements.txt```

**4.Run the Application**

```uvicorn main:app --reload```

The application will be available at: http://127.0.0.1:8000

## API Documentation
FastAPI automatically generates interactive documentation for the backend logic. You can explore the API endpoints here:

* **Swagger UI:** http://127.0.0.1:8000/docs
* **ReDoc:** http://127.0.0.1:8000/redoc
