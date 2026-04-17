# Flask HR ERP (Employee Management)

A simple Flask web app for basic employee registration and admin management (add, list, search, view profile, update, delete) backed by a MySQL database.

## Features

- Admin login (demo credentials)
- Add employee
- List employees
- Search employees by name prefix
- View employee profile
- Update employee details
- Delete employee

## Tech stack

- Python + Flask
- MySQL
- `pymysql`
- Jinja templates (`templates/`) + static assets (`static/`)

## Prerequisites

- Python 3.x
- MySQL server running locally

## Database setup

This app connects to MySQL with:

- Host: `localhost`
- User: `root`
- Password: empty
- Database: `hr_erp_db`

Create the database and table:

```sql
CREATE DATABASE IF NOT EXISTS hr_erp_db;
USE hr_erp_db;

CREATE TABLE IF NOT EXISTS registration (
  empid INT PRIMARY KEY,
  empname VARCHAR(100) NOT NULL,
  emailid VARCHAR(100),
  mobile VARCHAR(20),
  designation VARCHAR(100),
  salary DECIMAL(10,2)
);
```

## Install & run

1) Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies:

```bash
pip install -r requirements.txt
```

3) Start the app:

```bash
python3 main.py
```

Flask will run in debug mode. Open the app in your browser at `http://127.0.0.1:5000/`.

## Admin login (demo)

- Username: `admin`
- Password: `super`

## Project structure

- `main.py`: Flask app + routes + MySQL queries
- `templates/`: HTML templates
- `static/`: CSS/JS/images

## Notes / caveats

- This is a learning/demo project: credentials and configuration are currently hardcoded in `main.py`.
- For production, move secrets/config to environment variables, and use parameterized queries everywhere.

