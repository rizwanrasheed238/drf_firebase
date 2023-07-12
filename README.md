# User Registration and Login API with Firebase Notification Integration

This project implements a user registration and login API using Django REST Framework. After registration, a notification is sent to the user via Firebase Cloud Messaging (FCM). The success or failure response from Firebase is stored in the database.

## Features

- User registration with username and password
- User login with authentication
- Firebase notification integration
- Storage of notification response in the database

## Installation

1. Clone the repository:


git clone <repository-url>

2.Install the required dependencies:
pip install -r requirements.txt

3.Configure Firebase:

 Create a Firebase project and obtain the necessary credentials.
 Update the Firebase configuration in the project's settings.py file.

4.Database Configuration:
  Set up your preferred database (e.g., MySQL, PostgreSQL).
  Configure the database settings in the project's settings.py file.

5.Run database migrations:

python manage.py makemigrations
python manage.py migrate

6.Start the development server:

python manage.py runserver


The API will be accessible at http://localhost:8000/.

API Endpoints
POST /register/: Register a new user. Requires username and password in the request body.

POST /api/createbin/: Create a new bin. Requires username and password in the request body.

GET /api/bin/: Retrieve bin details.


Technologies Used
Django: Web framework for building the API
Django REST Framework: Toolkit for building RESTful APIs
Firebase: Cloud-based platform for sending notifications
Database: (SQlite3)





