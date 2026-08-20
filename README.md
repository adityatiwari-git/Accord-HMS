# Accord-HMS 🏥

**Accord-HMS (Hospital Appointment & Management System)** is a Django-based academic project developed to manage basic hospital information, patient accounts, doctors, departments and appointments through a simple web interface.

The project is intentionally built with a **simple and understandable Django structure** so that the code, database flow and application workflow can be explained clearly during a project demonstration or viva.

---

## 📌 Project Overview

Accord-HMS provides three main areas of functionality:

- **Visitors** can explore the hospital, doctors, departments and gallery, and submit enquiries through the contact form.
- **Registered patients** can create an account, log in, manage their profile, book appointments and view or cancel their appointments.
- **Hospital administrators** can manage hospital records through Django's built-in admin panel.

The project focuses on practical Django fundamentals rather than unnecessary complexity.

---

## ✨ Features

### 👤 Patient Features

- User registration and login
- Secure logout
- Patient profile management
- Personal dashboard
- Appointment booking
- Appointment history
- Appointment cancellation
- Appointment date and time validation
- Prevention of duplicate active appointments for the same doctor and time

### 🏥 Hospital Features

- Doctors listing
- Individual doctor profiles
- Hospital departments listing
- Individual department details
- Gallery section
- Contact/enquiry form
- Django admin panel for hospital data management
- Demo data generation command

### 🎨 UI & Design

- Responsive Bootstrap 5 interface
- Custom CSS styling
- Professional hospital-themed colour palette
- Accord-HMS custom logo
- Custom browser favicon
- Responsive navigation
- Hospital and doctor-focused visual design
- Separate dashboard and profile experience for logged-in patients

---

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Django |
| Frontend | HTML, CSS, Bootstrap 5, JavaScript |
| Database | SQLite (development) |
| Version Control | Git & GitHub |
| Code Editor | Visual Studio Code |

---

## 📁 Project Structure

```text
Accord-HMS/
├── accounts/                  # Registration, authentication, dashboard and profile
├── config/                    # Django project configuration and settings
├── hospital/                  # Hospital models, forms, views, tests and commands
├── static/
│   ├── css/                   # Custom stylesheets
│   └── images/                # Logo, favicon and visual assets
├── templates/                 # HTML templates
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

> Create a fresh `.venv` on each computer. Do not copy a Windows virtual environment to Ubuntu/Linux or vice versa.

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

Open the website at:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 🏥 Hospital Data

Hospital records can be managed through the Django admin panel.

### Recommended Departments

For a demonstration, the following departments can be added:

- Cardiology
- Neurology
- Orthopedics
- Pediatrics
- General Medicine
- Dermatology
- General Surgery

Doctors can then be created and assigned to their respective departments. Doctors marked as **Available** can be selected for appointments.

---

## 🌱 Demo Data

Accord-HMS includes a simple Django management command for generating demonstration data.

Run:

```bash
python manage.py seed_demo
```

The command can create sample:

- Departments
- Doctors
- Seven demo patients
- Appointment data
- Gallery entries

The command is designed to avoid unnecessary duplicate demo records when it is run again. The demo patient password is displayed by the command after it completes.

---

## 🔄 Application Workflow

```text
                         ACCORD-HMS
                              │
                ┌─────────────┴─────────────┐
                │                           │
             Visitor                     Patient
                │                           │
       ┌────────┼────────┐            Create Account
       │        │        │                  │
    Doctors Departments Gallery           Login
       │        │        │                  │
       └────────┴────────┘              Dashboard
                                            │
                                     Book Appointment
                                            │
                                    My Appointments
                                      │           │
                                    View        Cancel
                                            │
                                         Profile
```

---

## 🔐 Main Modules

### 1. Accounts

Responsible for patient account functionality:

- Registration
- Login
- Logout
- Dashboard
- Patient profile

### 2. Hospital

Responsible for the main hospital functionality:

- Doctors
- Departments
- Appointments
- Gallery
- Contact messages
- Forms and validation
- Demo data generation

### 3. Admin

Accord-HMS uses Django's built-in admin interface to manage hospital records without creating an unnecessarily complex custom administration system.

---

## 🧪 Testing

The project contains automated Django tests for important application behaviour, including authentication, protected pages, hospital pages, appointment creation and appointment-related validation/actions.

Run the test suite with:

```bash
python manage.py test
```

Also run the Django system check:

```bash
python manage.py check
```

Both commands should complete successfully before submitting or demonstrating the project.

---

## 🔄 GitHub Development Workflow

The project is maintained on GitHub so the source code can be accessed from different computers.

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

When moving the project to another computer using a pendrive, copy the project source code but create a **new virtual environment** and install dependencies using `requirements.txt`.

---

## 📋 Project Status

The main academic workflow of Accord-HMS has been completed and tested:

- ✅ User registration
- ✅ Login and logout
- ✅ Patient dashboard
- ✅ Patient profile
- ✅ Doctors listing and profiles
- ✅ Departments and department details
- ✅ Appointment booking
- ✅ Appointment validation
- ✅ Duplicate appointment prevention
- ✅ Appointment cancellation
- ✅ Gallery
- ✅ Contact form
- ✅ Django admin management
- ✅ Demo data command
- ✅ Automated tests
- ✅ Responsive Bootstrap UI
- ✅ Accord-HMS logo
- ✅ Browser favicon
- ✅ GitHub repository documentation

**Current stage: Ready for final screenshots, project report, presentation and academic submission.**

---

## 🚀 Future Scope

The current implementation is intentionally kept simple for academic use. Possible future improvements include:

- Email or SMS appointment notifications
- Doctor-side dashboard
- Online appointment reminders
- Prescription management
- Patient medical history
- Role-based access for doctors and hospital staff
- PostgreSQL for production deployment
- Online hosting and deployment

---

## 👨‍💻 Author

**Aditya Tiwari**  
B.Tech Bioinformatics Student | Django & Web Development Learner

---

## 📄 Academic Note

Accord-HMS is developed as an academic and practical project to learn and demonstrate the development of a Django-based hospital appointment and management system using Python, HTML, CSS, Bootstrap and JavaScript.

The project is suitable for academic demonstration and can be extended with additional hospital-management features in the future.
