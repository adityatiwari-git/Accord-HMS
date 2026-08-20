# 4. System Design Approach

## 4.1 Application Architecture

Accord-HMS follows the basic Django Model-View-Template pattern.

```text
Browser
  ↓
URL Pattern
  ↓
Django View
  ↓
Model / Form
  ↓
SQLite Database
  ↓
Django View
  ↓
HTML Template + CSS + Bootstrap
  ↓
Browser
```

This separation keeps database operations, request handling and page presentation understandable.

## 4.2 Top-Down Design

```text
Accord-HMS
├── Accounts
│   ├── Register
│   ├── Login
│   ├── Dashboard
│   └── Logout
└── Hospital
    ├── Departments
    ├── Doctors
    ├── Profiles
    ├── Appointments
    ├── Gallery
    └── Contact
```

## 4.3 Bottom-Up Design

The project was also developed by building smaller pieces such as models and forms and then connecting them to views, URLs and templates. This allowed individual parts to be checked before combining them into the complete workflow.

## 4.4 Database Design

Django ORM is used instead of writing raw SQL for normal application operations. Main relationships are:

- One department → many doctors.
- One user → one profile.
- One user → many appointments.
- One doctor → many appointments.

## 4.5 User Interface Design

The UI uses Bootstrap 5 for responsive layout and custom CSS for Accord-HMS branding. The design includes a hospital-oriented colour palette, responsive navigation, doctor profile cards, department cards, dashboard cards, forms, gallery sections, a custom logo and browser favicon.

## 4.6 Page Design

The public pages are designed for information discovery, while authenticated pages focus on patient actions. The dashboard provides quick appointment information and links to the patient's main actions.

## 4.7 Design Principle

The main design principle was **simple, readable and explainable code**. The project avoids unnecessary frameworks and complicated patterns so that the complete flow can be understood by a second-year B.Tech student during demonstration or viva.