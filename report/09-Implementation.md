# 9. Project Implementation and Features

## 9.1 Authentication

Django's built-in authentication system handles user creation, password hashing, login, sessions and logout. Passwords are not stored as plain text by Django.

## 9.2 Patient Management

A registered patient has a Django `User` and a related `Profile`. The dashboard retrieves appointments belonging to the logged-in patient.

## 9.3 Doctor Management

Doctors contain department, qualification, experience, email, phone and availability fields. The normal doctor directory shows available doctors.

The demonstration seed command creates six doctors:

- Aarav Sharma – Cardiology
- Meera Kapoor – Neurology
- Rohan Verma – Orthopedics
- Ananya Singh – Pediatrics
- Kunal Gupta – General Medicine
- Nisha Patel – Dermatology

These are demonstration records, not real medical professionals.

## 9.4 Department Management

The demo data contains six departments:

1. Cardiology
2. Neurology
3. Orthopedics
4. Pediatrics
5. General Medicine
6. Dermatology

Departments can also be managed through Django Admin.

## 9.5 Appointment Management

```text
Login
  ↓
Select Doctor
  ↓
Select Date
  ↓
Select Time
  ↓
Optional Reason
  ↓
Validate
  ↓
Check Active Slot
  ↓
Save as Pending
  ↓
My Appointments
```

A booking is rejected if the doctor is unavailable, the date is in the past, today's time has already passed, or a Pending/Confirmed appointment already exists for that doctor/date/time.

## 9.6 Demo Data

The command below creates demonstration data:

```bash
python manage.py seed_demo
```

It creates departments, six doctors, seven demo patients, gallery entries and an example appointment. The command is written so repeated execution does not unnecessarily create duplicate demonstration records.

The command prints a demo patient password after completion. This is only for local demonstration and should not be used as a production credential.

## 9.7 UI and Branding

The final interface uses Bootstrap 5 with custom CSS and hospital/doctor imagery. The project includes the Accord-HMS logo and a custom browser favicon. The interface was refined to remain professional, responsive and easy to explain.

## 9.8 GitHub Workflow

The project is maintained in the `adityatiwari-git/Accord-HMS` GitHub repository. A typical workflow is:

```bash
git pull origin main
git add .
git commit -m "Describe changes"
git push origin main
```

The `.venv` directory and local database should remain excluded according to `.gitignore` where applicable.