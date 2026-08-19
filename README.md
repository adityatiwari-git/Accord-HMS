# Accord-HMS 🏥

**Accord-HMS** is a modern Hospital Appointment & Management System built as a Django web application. The project is designed to provide a clean and simple interface for managing hospital-related information and appointment workflows.

## 🚀 Project Overview

Accord-HMS is being developed as a practical full-stack web development project using Django. It focuses on creating a user-friendly hospital management experience while keeping the codebase simple, organized, and easy to understand.

## ✨ Features

- 🏠 Hospital landing/home page
- 👨‍⚕️ Doctors section
- 🏥 Hospital departments
- 📅 Appointment booking workflow
- 🔐 User registration and login
- 👤 User profile and dashboard
- 🖼️ Hospital gallery
- 📞 Contact section
- ⚙️ Django administration for managing project data
- 📱 Responsive interface using Bootstrap
- 🎨 Custom styling with CSS

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite (development)
- **Version Control:** Git & GitHub

## 📁 Project Structure

```text
Accord-HMS/
├── accounts/          # User authentication and account-related functionality
├── config/            # Django project configuration
├── hospital/          # Main hospital application
├── static/            # CSS and other static assets
├── templates/         # HTML templates
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
├── .gitignore         # Ignored files and folders
└── README.md          # Project documentation
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/adityatiwari-git/Accord-HMS.git
cd Accord-HMS
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Ubuntu/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the local server shown in the terminal, usually:

```text
http://127.0.0.1:8000/
```

## 🔑 Admin Panel

To create an administrator account:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

## 🔄 Development Workflow

The project is maintained using Git and GitHub so development can continue across different systems.

```bash
git pull origin main
```

After making changes:

```bash
git add .
git commit -m "Describe your changes"
git push origin main
```

When moving the project to another operating system, create a new virtual environment and install the dependencies from `requirements.txt` instead of copying the existing `.venv` folder.

## 📌 Current Status

The core project structure, authentication pages, dashboard, profile functionality, navigation, gallery, and other initial hospital-management components are under development. More hospital-specific features and UI improvements will be added as the project progresses.

## 🎯 Future Improvements

- Complete doctor management
- Complete department management
- Appointment management and status tracking
- Improved patient dashboard
- Doctor profiles
- Admin-side management features
- Gallery image management
- Better validation and user feedback
- UI and accessibility improvements

## 👨‍💻 Author

**Aditya Tiwari**

B.Tech Bioinformatics Student | Django & Web Development Learner

---

> Accord-HMS is developed as an academic and practical project to learn and demonstrate Django-based web application development.