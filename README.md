# Accord-HMS 🏥

**Accord-HMS** is a simple Hospital Appointment & Management System built with Django. It is an academic project focused on hospital information, patient accounts, doctor discovery and appointment management.

## 🚀 Project Overview

Accord-HMS provides a single web interface where visitors can explore hospital departments and doctors, while registered patients can create an account, book appointments, manage their profile and track their appointments.

The project intentionally uses a straightforward Django structure so that the code is easy to understand, maintain and demonstrate as a student project.

## ✨ Main Features

- 🏠 Hospital landing page
- 👨‍⚕️ Doctors listing and individual doctor profiles
- 🏥 Departments listing and department details
- 📅 Appointment booking
- ⏰ Future date and time validation
- 🚫 Prevention of duplicate active appointments for the same doctor and time
- 🔐 User registration and login
- 👤 Patient profile
- 📊 Patient dashboard with appointment statistics
- ❌ Appointment cancellation
- 🖼️ Gallery with admin-managed entries and image URL support
- 📞 Contact form with database storage
- ⚙️ Django admin panel for hospital data management
- 📱 Responsive Bootstrap interface
- 🎨 Custom CSS styling

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Database:** SQLite for development
- **Version Control:** Git & GitHub

## 📁 Project Structure

```text
Accord-HMS/
├── accounts/          # Registration, login, logout and dashboard routing
├── config/            # Django project configuration
├── hospital/          # Main hospital application, models, forms and views
├── static/css/        # Custom stylesheet
├── templates/         # HTML templates
├── manage.py           # Django management script
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

Do not copy the `.venv` folder from another computer. Create a fresh environment on each system.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the address shown by Django, normally:

```text
http://127.0.0.1:8000/
```

## ⚙️ Adding Hospital Data

Departments and doctors are managed through the Django admin panel.

Open:

```text
http://127.0.0.1:8000/admin/
```

Recommended demo departments:

- Cardiology
- Neurology
- Orthopedics
- Pediatrics
- General Medicine
- Dermatology

After creating departments, add doctors and assign each doctor to a department. Keep **Available** enabled for doctors who should appear on the public booking pages.

### Gallery

Gallery entries can also be added from the admin panel. The current model supports an image URL, so pictures can be added later without changing the project structure.

## 🔑 Application Flow

```text
Visitor
  ↓
Home → Doctors / Departments / Gallery / Contact
  ↓
Create Account / Login
  ↓
Patient Dashboard
  ↓
Book Appointment
  ↓
My Appointments → Track / Cancel
  ↓
Profile → Update Patient Information
```

## 🧪 Testing

Basic Django tests are included in `hospital/tests.py`.

Run them with:

```bash
python manage.py test
```

The tests cover important parts of the project such as page loading, doctor listing, login redirection, appointment validation and appointment creation.

## 🔄 Development Workflow

The project is maintained using Git and GitHub so it can be continued from different systems.

Before starting work on another computer:

```bash
git pull origin main
```

After making changes:

```bash
git add .
git commit -m "Describe your changes"
git push origin main
```

If you move the project using a pendrive, copy the project files but create a fresh `.venv` and install the dependencies using `requirements.txt`.

## 📌 Project Status

The main Accord-HMS workflow is complete for the academic project:

- Authentication is working.
- Navigation and main pages are connected.
- Doctors and departments have public detail pages.
- Patients can book, view and cancel appointments.
- Patient profiles and dashboard are available.
- Appointment validation is implemented.
- Contact messages are stored in the database.
- Gallery entries can be managed through admin.
- Hospital data can be managed through Django admin.
- Basic automated tests are included.

The gallery can remain empty until final presentation data and images are added.

## 👨‍💻 Author

**Aditya Tiwari**

B.Tech Bioinformatics Student | Django & Web Development Learner

---

> Accord-HMS is developed as an academic and practical project to learn and demonstrate Django-based web application development.
