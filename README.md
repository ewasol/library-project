# Library Management API

## Overview

This project is a RESTful API for managing a library's book inventory. Implemented using Flask and SQLAlchemy, the API allows library staff to track and update book availability, including checking in and checking out books. The database used is PostgreSQL, and the project can be easily run and managed using Docker and Docker Compose.

## Features

- **Add a New Book**: Add new books to the library's inventory.
- **Delete a Book**: Remove a book from the inventory.
- **Get All Books**: Retrieve a list of all books in the inventory.
- **Update Book Availability**: Update the availability status of a book (checked out or available).

## Technologies

- **Flask**: Web framework for building the API.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database management system.
- **Marshmallow**: Object serialization/deserialization and validation.
- **Docker**: Containerization platform for running the application.
- **Docker Compose**: Tool for defining and running multi-container Docker applications.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Docker Compose**: Ensure Docker Compose is installed.

### Setup

1. **Clone the Repository**

   ```
   git clone https://github.com/ewasol/library-project.git
   cd library-project
   ```
   
2. **Create a .env File**

   ```
   cp .env.example .env
   ```
   
Example .env file content:
 ```
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_DB=...
DB_HOST=...
SQLALCHEMY_DATABASE_URI=...
SECRET_KEY=...
 ```

3. **Build and Run the Containers**

 ```
docker-compose up --build
 ```

4. **Initialize the Database**

Run the following command to create the necessary database tables:

 ```
docker-compose exec web flask db upgrade
 ```

## API Endpoints

1. **Add a New Book**
* Endpoint: /books
* Method: POST
* Request Body:
```
{
  "serial_number": "111111",
  "title": "Title1",
  "author": "Author1"
}
```

2. **Get All Books**
* Endpoint: /books
* Method: GET

3. **Delete a Book**
* Endpoint: /books/<serial_number>
* Method: DELETE

4. **Update Book Availability**
* Endpoint: /books/<serial_number>
* Method: PUT
* Request Body:

```
{
  "serial_number": "111111",
  "title": "Title1",
  "author": "Author1",
  "is_checked_out": false
}
```
or
```
{
  "serial_number": "333333",
  "title": "Title3",
  "author": "Author3",
  "is_checked_out": true,
  "checked_out_by": "555555"
}
```