# 2. System Analysis

## 2.1 Existing System

A basic manual appointment process may involve maintaining patient details, checking doctor availability, recording appointments and handling cancellations through registers, calls or separate files. Such a process can be slow and makes searching and updating records harder.

## 2.2 Proposed System

Accord-HMS centralizes basic hospital information in one Django application. Patient accounts, doctors, departments and appointments are represented as database records. Patients use a browser interface while administrators can manage records through Django Admin.

## 2.3 Advantages

- Centralized record management.
- Faster access to appointment information.
- Patient authentication.
- Appointment date/time validation.
- Duplicate active-slot prevention.
- Easier administration.
- Responsive interface.
- Simple code structure suitable for academic explanation.
- GitHub-based source control.

## 2.4 SDLC Approach

The project followed a simple development life cycle:

1. **Requirement Gathering** – identify pages, users and functions.
2. **Analysis and Design** – plan models, relationships, page flow and interface.
3. **Development** – implement models, views, forms, URLs and templates.
4. **Testing** – run Django tests and manual browser checks.
5. **Documentation** – prepare README and project report.

## 2.5 Application Workflow

```text
Visitor
  ├── Home
  ├── About
  ├── Departments → Department Details → Available Doctors
  ├── Doctors → Doctor Profile
  ├── Gallery
  └── Contact

Patient
  ├── Register
  └── Login → Dashboard
                 ├── Profile
                 ├── Book Appointment
                 └── My Appointments → View / Cancel

Administrator
  └── Django Admin
        ├── Departments
        ├── Doctors
        ├── Profiles
        ├── Appointments
        ├── Gallery
        └── Contact Messages
```

## 2.6 ER Relationship Summary

```text
User 1 ───── 1 Profile
User 1 ───── N Appointment N ───── 1 Doctor N ───── 1 Department

Gallery and ContactMessage are independent content/enquiry records.
```

## 2.7 Appointment Data Flow

```text
Patient Login
     ↓
Appointment Form
     ↓
Django Form Validation
     ↓
Doctor Availability Check
     ↓
Date/Time Validation
     ↓
Existing Pending/Confirmed Slot Check
     ↓
Save Appointment
     ↓
My Appointments
```

## 2.8 Security and Access

Protected patient pages use Django's `login_required` decorator. Authentication uses Django's built-in user system. Patient appointment queries are filtered using the logged-in user so a patient sees their own appointment records.