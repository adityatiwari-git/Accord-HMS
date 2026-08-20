# Accord-HMS 🏥

**Accord-HMS (Hospital Appointment & Management System)** is a Django-based academic project for managing basic hospital information, patient accounts, doctors, departments and appointments through a simple web interface.

The project is designed with a clean and understandable structure so that the code and workflow can be easily explained during a project demonstration or viva.

---

## 📌 Project Overview

Accord-HMS provides two main experiences:

- **Visitors** can explore the hospital, doctors, departments and gallery, and send enquiries through the contact form.
- **Registered patients** can create an account, log in, manage their profile, book appointments and view or cancel their appointments.
- **Hospital administrators** can manage hospital data through the Django admin panel.

The project focuses on the practical implementation of Django fundamentals rather than unnecessary complexity.

---

## ✨ Features

### Patient Features

- User registration and login
- Secure logout
- Patient profile management
- Personal dashboard
- Appointment booking
- Appointment history
- Appointment cancellation
- Appointment date/time validation
- Prevention of duplicate active appointments for the same doctor and time

### Hospital Features

- Doctors listing
- Individual doctor profiles
- Hospital departments listing
- Individual department details
- Gallery section
- Contact/enquiry form
- Django admin panel for managing hospital information
- Demo data generation command

### UI & Design

- Responsive Bootstrap 5 interface
- Custom CSS styling
- Hospital-themed colour palette
- Accord-HMS logo in the navigation and footer
- Custom favicon/browser tab icon
- Responsive navigation for smaller screens

---

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5, JavaScript |
| Database | SQLite (development) |
| Version Control | Git, GitHub |
| Development | Visual Studio Code |

---

## 📁 Project Structure

```text
Accord-HMS/
├── accounts/                  # Authentication, dashboard and profile-related views
├── config/                    # Django project configuration and settings
├── hospital/                  # Hospital models, forms, views, tests and management commands
├── static/
│   ├── css/                   # Custom stylesheet
│   └── images/                # Accord-HMS logo and favicon assets
├── templates/                 # HTML templates for the website
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files excluded from Git
└── README.md                  # Project documentation
```

---

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

> Create a fresh `.venv` on each computer. Do not copy the virtual environment from another operating system.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

### 6. Check the project

```bash
python manage.py check
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🏥 Adding Hospital Data

Hospital data can be managed through the Django admin panel:

```text
http://127.0.0.1:8000/admin/
```

### Recommended Departments

For a demonstration, the following departments can be added:

- Cardiology
- Neurology
- Orthopedics
- Pediatrics
- General Medicine
- Dermatology
- General Surgery

Doctors can then be created and assigned to their respective departments. Enable **Available** for doctors who should appear as available for appointments.

---

## 🌱 Demo Data

Accord-HMS includes a simple Django management command for creating demonstration data.

Run:

```bash
python manage.py seed_demo
```

The command creates sample hospital data such as:

- Departments
- Doctors
- Seven demo patients
- A sample appointment
- Gallery entries

The command is designed to avoid unnecessary duplicate demo records when it is run again. The demo patient password is displayed by the command after it completes.

---

## 🔄 Application Workflow

```text
                    ACCORD-HMS
                        │
          ┌─────────────┴─────────────┐
          │                           │
       Visitor                    Patient
          │                           │
    ┌─────┼─────┐             Create Account
    │     │     │                    │
 Doctors Departments Gallery      Login
    │     │     │                    │
    └─────┴─────┘               Dashboard
          │                           │
       Contact                  Book Appointment
                                      │
                              My Appointments
                                 │         │
                              View       Cancel
                                      │
                                   Profile
```

---

## 🔐 Main Modules

### 1. Accounts

Handles patient authentication and account-related functionality:

- Registration
- Login
- Logout
- Dashboard
- Patient profile

### 2. Hospital

Handles the main hospital functionality:

- Doctors
- Departments
- Appointments
- Gallery
- Contact messages
- Hospital-related forms and validation

### 3. Admin

Django's built-in admin interface is used to manage hospital records without creating a separate complex administration system.

---

## 🧪 Testing

The project contains automated Django tests for important application behaviour.

Run:

```bash
python manage.py test
```

Before submission, the project should also be checked with:

```bash
python manage.py check
```

The tests cover areas such as page access, authentication, doctor and hospital pages, appointment creation, appointment validation and appointment-related actions.

---

## 🔄 GitHub Development Workflow

The project is maintained on GitHub so it can be accessed from different computers.

### Before starting work

```bash
git pull origin main
```

### After making changes

```bash
git add .
git commit -m "Describe your changes"
git push origin main
```

When moving the project to another computer using a pendrive, copy the source code but create a new virtual environment and install the dependencies from `requirements.txt`.

---

## 📋 Project Status

The main academic workflow of Accord-HMS is implemented:

- ✅ Authentication
- ✅ Registration and login
- ✅ Patient dashboard
- ✅ Patient profile
- ✅ Doctors and doctor profiles
- ✅ Departments and department details
- ✅ Appointment booking
- ✅ Appointment validation
- ✅ Appointment cancellation
- ✅ Gallery
- ✅ Contact form
- ✅ Django admin management
- ✅ Demo data command
- ✅ Automated tests
- ✅ Responsive Bootstrap UI
- ✅ Accord-HMS logo and favicon

The project is ready for final documentation, screenshots, presentation and academic submission.

---

## 🚀 Future Scope

The current project is intentionally kept simple for academic use. Possible future improvements include:

- Email or SMS appointment notifications
- Doctor-side dashboard
- Online appointment reminders
- Prescription management
- Patient medical history
- Role-based access for doctors and hospital staff
- PostgreSQL deployment for production use
- Online hosting and deployment

---

## 👨‍💻 Author

**Aditya Tiwari**  
B.Tech Bioinformatics Student | Django & Web Development Learner

---

## 📄 Academic Note

Accord-HMS is developed as an academic and practical project to learn and demonstrate the development of a Django-based hospital management and appointment system using Python, HTML, CSS, Bootstrap and JavaScript.
