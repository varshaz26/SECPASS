SECPASS - Secure Password Manager
Overview
SECPASS is a secure and user-friendly web application designed to help users manage their passwords safely and efficiently. With the increasing number of online accounts users maintain, SECPASS addresses the problem of password management by providing a centralized, encrypted repository for storing, generating, and managing complex passwords.

Developed using the Django framework, SECPASS leverages the Model-View-Controller (MVC) architectural pattern, providing modularity, maintainability, and scalability. The system uses SQLite for data storage and integrates encryption techniques to ensure password security.

Features
User Registration and Authentication: Secure signup and login functionality to protect user accounts.

Password Storage: Safely store usernames, passwords, application names, categories, and descriptions.

Password Generation: Generate strong, random passwords to enhance security.

Password Management: Edit, update, or delete stored passwords.

Search Functionality: Quickly find passwords by username, application name, or category.

Session Management: Secure logout feature to protect data privacy.

Responsive UI: User-friendly and accessible interface developed with HTML, CSS, Bootstrap, and JavaScript.

Technologies Used
Frontend: HTML, CSS, Bootstrap, JavaScript

Backend: Python, Django

Database: SQLite

Encryption: Custom encryption and decryption methods implemented for password security.

Installation and Setup
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/secpass.git
cd secpass
Create a Virtual Environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Apply Migrations

bash
Copy code
python manage.py migrate
Run the Development Server

bash
Copy code
python manage.py runserver
Access the Application
Open your web browser and navigate to http://127.0.0.1:8000

Usage
Register a new user account.

Log in with your credentials.

Add new passwords by specifying username, application name, category, and description.

Use the password generator for secure password creation.

Manage your stored passwords by updating or deleting them.

Use the search feature to quickly find your stored credentials.

Log out securely when finished.

Testing
Unit tests cover critical features such as user authentication, password creation, editing, deletion, and search functionalities. Run tests using:

bash
Copy code
python manage.py test
