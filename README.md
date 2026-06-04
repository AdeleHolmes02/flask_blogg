# Studio Notes – Flask Blog Application

## Project Overview

Studio Notes is a personal blogging application developed as part of the PRO1002 Backend Essentials course. The application is built using Python, Flask, SQLite, HTML, CSS, and Jinja templates.

The purpose of the project was to demonstrate backend development skills by creating a complete web application with database integration, CRUD functionality, routing, template rendering, testing, and version control through Git and GitHub.

The application allows users to create, read, update, and delete blog posts, add comments, organise posts using tags, and browse posts by category.

---

## Features

### Blog Posts

* View all blog posts on the homepage
* View individual blog posts
* Create new blog posts
* Edit existing blog posts
* Delete blog posts

### Comments

* Add comments to blog posts
* View comments connected to individual posts

### Tags

* Add tags to blog posts
* Display tags on each post
* Filter posts by tag

### Database

* SQLite database storage
* Relational database design
* Foreign key relationships
* SQL JOIN queries

### Testing

* Automated database tests
* Automated route tests using Flask's test client

---

## Technologies Used

### Backend

* Python 3
* Flask
* SQLite

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Development Tools

* Visual Studio Code
* Git
* GitHub
* SQLite3
* unittest

---

## Project Structure

```text
flask_blogg/
│
├── app.py
├── database.py
├── schema.sql
├── seed.sql
├── blog.db
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   ├── layout.html
│   ├── index.html
│   ├── post.html
│   ├── new_post.html
│   ├── edit_post.html
│   └── tag.html
│
└── tests/
    ├── test_database.py
    └── test_routes.py
```

---

## Database Design

The application uses a relational SQLite database.

### Tables

#### posts

Stores blog posts.

Fields:

* id
* title
* body
* created_at
* updated_at

#### comments

Stores comments connected to blog posts.

Fields:

* id
* post_id
* title
* body
* created_at

#### tags

Stores unique tags.

Fields:

* id
* name

#### post_tags

Many-to-many relationship table between posts and tags.

Fields:

* post_id
* tag_id

---

## Installation

### Clone the repository

```bash
git clone https://github.com/AdeleHolmes02/flask_blogg.git
cd flask_blogg
```

### Create virtual environment

```bash
python3 -m venv .venv
```

### Activate virtual environment

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install flask
```

---

## Database Setup

Create the database:

```bash
sqlite3 blog.db < schema.sql
```

Insert sample data:

```bash
sqlite3 blog.db < seed.sql
```

---

## Running the Application

Start the Flask development server:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## Running Tests

Database tests:

```bash
python -m unittest tests/test_database.py
```

Route tests:

```bash
python -m unittest tests/test_routes.py
```

Run all tests:

```bash
python -m unittest discover
```

---

## Security Considerations

The application uses parameterised SQL queries when interacting with the database. This helps reduce the risk of SQL injection attacks.

Basic input validation has also been implemented for creating and editing blog posts.

The application does not currently include authentication or user management, as these features were outside the scope of the project.

---

## Challenges and Learning Outcomes

During development, several challenges were encountered:

* Understanding Flask routing and template rendering
* Designing a relational SQLite database
* Implementing CRUD functionality
* Working with foreign key relationships
* Creating many-to-many relationships using tags
* Debugging Flask errors and route issues
* Using Git and GitHub for version control
* Writing automated tests

Through these challenges, I gained practical experience with backend development workflows and improved my understanding of Python, databases, debugging, testing, and web application architecture.

---

## Future Improvements

Potential future enhancements include:

* User authentication and login system
* User-specific blog posts
* Search functionality
* Pagination
* Improved form validation
* Responsive mobile design
* Rich text editor support
* Comment editing and deletion

---

## AI Usage Statement

Artificial Intelligence tools were used during development as a learning aid for:

* Understanding concepts
* Debugging errors
* Explaining Flask and SQLite functionality
* Receiving feedback on code structure

All code was reviewed, tested, and integrated manually by the developer.

---

## Author

Adele Holmes

PRO1002 – Backend Essentials

Oslo Nye Fagskole
