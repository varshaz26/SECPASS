# SECPASS 🔒  
### Secure Password Manager

SECPASS is a secure and user-friendly web application designed to help users manage their passwords safely and efficiently.  
It provides a centralized, encrypted repository for storing, generating, and managing complex passwords.

Developed using the **Django framework**, SECPASS leverages the MVC architectural pattern for modularity, maintainability, and scalability.  
The system uses **SQLite** for data storage and integrates **encryption techniques** to ensure password security.

---

## 📌 Features

- **User Registration and Authentication:** Secure signup and login functionality  
- **Password Storage:** Safely store usernames, passwords, application names, categories, and descriptions  
- **Password Generation:** Generate strong, random passwords  
- **Password Management:** Edit, update, or delete stored passwords  
- **Search Functionality:** Quickly find passwords by username, application name, or category  
- **Session Management:** Secure logout to protect data privacy  
- **Responsive UI:** User-friendly interface with HTML, CSS, Bootstrap, and JavaScript  

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **Backend:** Python, Django  
- **Database:** SQLite  
- **Encryption:** Custom encryption and decryption methods for password security  

---

## ▶️ Installation and Setup

Clone the repository:

# SECPASS 🔒  
### Secure Password Manager

SECPASS is a secure and user-friendly web application designed to help users manage their passwords safely and efficiently.  
It provides a centralized, encrypted repository for storing, generating, and managing complex passwords.

Developed using the **Django framework**, SECPASS leverages the MVC architectural pattern for modularity, maintainability, and scalability.  
The system uses **SQLite** for data storage and integrates **encryption techniques** to ensure password security.

---

## 📌 Features

- **User Registration and Authentication:** Secure signup and login functionality  
- **Password Storage:** Safely store usernames, passwords, application names, categories, and descriptions  
- **Password Generation:** Generate strong, random passwords  
- **Password Management:** Edit, update, or delete stored passwords  
- **Search Functionality:** Quickly find passwords by username, application name, or category  
- **Session Management:** Secure logout to protect data privacy  
- **Responsive UI:** User-friendly interface with HTML, CSS, Bootstrap, and JavaScript  

---

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **Backend:** Python, Django  
- **Database:** SQLite  
- **Encryption:** Custom encryption and decryption methods for password security  

---

## ▶️ Installation and Setup

Clone the repository:

```bash
git clone https://github.com/yourusername/secpass.git
cd secpass
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open your web browser and navigate to:

```bash
http://127.0.0.1:8000
```
---

## ▶️ Usage
1. Register a new user account
2. Log in with your credentials
3. Add new passwords by specifying username, application name, category, and description
4. Use the password generator for secure password creation
5. Manage stored passwords by updating or deleting them
6. Use the search feature to quickly find your credentials
7. Log out securely when finished

---

### 🧪 Testing

Unit tests cover critical features such as:
  User authentication
  Password creation, editing, and deletion
  Search functionalities

Run tests using:

```bash
python manage.py test
```
