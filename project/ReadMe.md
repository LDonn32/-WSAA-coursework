# WSAA Coursework Project: Student Management System

This repository contains my final project for the WSAA (Web Services and APIs) coursework. The project demonstrates the creation and consumption of RESTful APIs using Flask, with a SQLite database backend and a simple web interface for performing CRUD (Create, Read, Update, Delete) operations on student data.

## Description

The Student Management System is a web application that allows users to manage student records. It consists of:
- A Flask REST API server that handles HTTP requests for student data
- A SQLite database to store student information
- A static HTML/CSS/JavaScript frontend that interacts with the API via AJAX calls

The application supports full CRUD operations: adding new students, viewing all students, editing existing student details, and deleting students.

## Key Features

- **RESTful API**: Endpoints for managing student data
- **Database Integration**: SQLite database with student table
- **Web Interface**: Simple, responsive UI for student management
- **CRUD Operations**: Create, Read, Update, and Delete students
- **Error Handling**: Proper HTTP status codes and error messages
- 

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite (note: MYSQL no longer supported on Free accounts for PythonAnywhere)
- **Frontend**: HTML, CSS, JavaScript 
- **HTTP Client**: Fetch API for AJAX requests
- **Deployment**: PythonAnywhere

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip 

### Local Setup

1. **Clone the repository** (if not already done):
   ```
   git clone <gh repo clone LDonn32/WSAA-coursework>
   cd project
   ```


2. **Set up the database**:
   - Update `dbconfig.py` to point to your local database path (I have currently set it for PythonAnywhere deployment)
   - Run the database creation script:
     ```
     python createscema.py
     ```

4. **Run the application**:
   ```
   python server.py
   ```

5. **Access the application**:
   - Open your browser and go to `http://localhost:5000`

### Database Configuration

The database path is configured in `dbconfig.py`. For local development, you might need to modify the `BASE_DIR` variable to point to your local project directory.

## Usage

### Web Interface

- **View Students**: The main web page displays a table of all students
- **Add Student**: Fill out the form and click "Add Student"
- **Edit Student**: Click the "Edit" button next to a student, modify details, and submit
- **Delete Student**: Click the "Delete" button next to a student to remove them

### API Usage

The application provides a REST API that can be consumed by other applications or tools.

#### Endpoints

- `GET /api/students` - Retrieve all students
- `GET /api/students/<id>` - Retrieve a specific student by ID
- `POST /api/students` - Create a new student
- `PUT /api/students/<id>` - Update an existing student
- `DELETE /api/students/<id>` - Delete a student

#### Example API Requests

**Get all students:**
```bash
curl http://localhost:5000/api/students
```

**Create a new student:**
```bash
curl -X POST http://localhost:5000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Joe Bloggs","address":"321 Rattlin Road","email":"123@example.ie","course":"Web Services and Application"}'
```

## Database Schema

The application uses a single SQLite table:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    course TEXT NOT NULL
);
```

## Project Structure

```
project/
│
├── server.py              # Main Flask application
├── studentDAO.py          # Data Access Object for student operations
├── dbconfig.py            # Database configuration
├── createscema.py         # Database schema creation script
├── requirements.txt       # Python dependencies
├── ReadMe.md              # This file
├── webpath.txt            # Deployment URL
│
│
└── static/
    ├── index.html         # Main web page html file
    └── styles.css         # CSS styles
```

## Deployment

The application is deployed on PythonAnywhere at: https://ldonn32.pythonanywhere.com/

For deployment on PythonAnywhere or similar platforms:
1. Upload the project files
2. Install dependencies in the virtual environment
3. Update `dbconfig.py` with the correct paths
4. Run `createscema.py` to create the database
5. Configure the web app to run `server.py`

## A quick look at the API JSON file

https://ldonn32.pythonanywhere.com/api/students


## References 

The main structure and inspiration of this project's code was rehashed from the example project of Lecturer Andrew Beatty at [GitHub](https://github.com/andrewbeattycourseware/deploytopythonanywhere)

Further documentation was used for the following:



- server.py – Built with guidance from [Flask Quickstart examples](https://flask.palletsprojects.com/en/stable/quickstart/) and [Flask Quickstart Error handling](https://flask.palletsprojects.com/en/stable/quickstart/#redirects-and-errors). This follows RESTful route conventions (GET, POST, PUT, DELETE) and [MDN Documentation](https://developer.mozilla.org/en-US/docs/Glossary/REST) was used for guidance here.

- studentDAO.py – Built with guidance from [sqlite3.html](https://docs.python.org/3/library/sqlite3.html). This follows SQLite usage from Python docs for persistent local storage.

- createschema.py – Schema creation pattern drawn directly from [sqlite3 documentation examples](https://sqlite.org/schematab.html).

- index.html/ styles.css - Followed W3schools for [HTML](https://www.w3schools.com/tags/default.asp) and [CSS](https://www.w3schools.com/cssref/index.php) documentation for base markup and structure. 

I also refered to [dev.to](https://dev.to/erasmuskotoka/html-css-best-practices-writing-clean-maintainable-and-responsive-code-1d5o) and [w3.org](https://www.w3.org/TR/2025/REC-WCAG21-20250506/)for accessibility best practices. I went with a Color contrast for visible focus indicators, clear sans‑serif fonts for readability and a dyslexic friendly font.

- Deployment config – I used [PythonAnywhere’s official tutorial](https://help.pythonanywhere.com/pages/) for Flask/SQLite mapping and WSGI setup.


Github built in copilot was used at the later stages of project development to assist with trouble shooting errors with code and debugging. 


## Contact

For any questions or queries relating to this project, feel free to message me on GitHub or at my student email G00472977@atu.ie