# 5. Backend Design

## 5.1 Project Structure

```text
Accord-HMS/
├── accounts/                  # registration, authentication, dashboard
├── config/                    # Django configuration
├── hospital/                  # main hospital application
├── static/                    # CSS and images
├── templates/                 # HTML templates
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 5.2 Accounts Module

The `accounts` application handles patient registration, login, logout and dashboard functionality. Django's built-in `User` model is used for authentication.

The dashboard calculates total, pending and confirmed appointments for the logged-in user and displays recent appointment records.

## 5.3 Hospital Module

The `hospital` application contains departments, doctors, profiles, appointments, gallery records, contact messages, forms, tests and the demo-data management command.

## 5.4 Models

### Department

Stores department name and description.

### Doctor

Stores name, department, qualification, experience, email, phone and availability.

### Profile

Uses a one-to-one relationship with Django's `User` and stores full name, phone and address.

### Appointment

Stores patient, doctor, appointment date/time, reason, status and creation time. Status choices are Pending, Confirmed, Completed and Cancelled.

### Gallery

Stores title, description, image URL and creation time.

### ContactMessage

Stores visitor name, email, subject, message and creation time.

## 5.5 Views

Important function-based views include:

- `home()`
- `about()`
- `departments()`
- `department_detail()`
- `doctors()`
- `doctor_detail()`
- `gallery()`
- `contact()`
- `book_appointment()`
- `appointments()`
- `cancel_appointment()`
- `profile()`
- `register()`
- `login_view()`
- `dashboard()`
- `logout_view()`

The views use standard Django helpers such as `render`, `redirect`, `get_object_or_404` and `login_required`.

## 5.6 Forms and Validation

`AppointmentForm` validates doctor availability, prevents past dates and prevents past times when today's date is selected.

The appointment view additionally checks whether a Pending or Confirmed appointment already exists for the same doctor, date and time.

`ProfileForm` handles patient profile details and `ContactForm` handles visitor enquiries.

## 5.7 URLs and Templates

URL patterns connect browser requests to views. Templates present data to the user. A common base template is used for shared navigation and page styling.

## 5.8 Django Admin

Django's built-in admin interface is used for record management. This keeps the project small and avoids writing a separate complex administration dashboard for the academic version.