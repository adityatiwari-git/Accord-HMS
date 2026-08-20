# 14. Appendix – Screenshots, Front Matter and Viva Notes

## A. Cover Page

**A PROJECT REPORT**  
**on**  
**ACCORD-HMS**  
**Hospital Appointment & Management System**

Submitted towards partial fulfillment of the requirements of the **B.Tech in Bioinformatics**.

**Submitted By:** Aditya Tiwari  
**Institute:** Jacob Institute of Biotechnology and Bioengineering, SHUATS  
**Training Organization:** Techpile Technology Pvt. Ltd., Lucknow  
**Academic Session:** 2026–2027

> Add official supervisor, coordinator, registration number and training dates from the relevant documents.

## B. Completion Certificate

Attach the official Techpile completion certificate here.

## C. Preface

Summer training gives students an opportunity to apply classroom concepts to practical development work. During this training project, Accord-HMS was developed using Python and Django. The project covered requirement understanding, database design, development, validation, testing, debugging and documentation.

The application was intentionally kept simple and understandable so that its workflow can be explained during a project demonstration and viva.

## D. Acknowledgement

I sincerely thank Techpile Technology Pvt. Ltd., my trainers and supervisors for their guidance during the project. I also thank my college faculty and the Jacob Institute of Biotechnology and Bioengineering, SHUATS, for their academic support. Finally, I thank my friends and classmates who helped with testing and feedback.

**Aditya Tiwari**

## E. Declaration

I hereby declare that the project entitled **“Accord-HMS – Hospital Appointment & Management System”** is my academic project work completed as part of my training and academic requirements. The project uses Python, Django, HTML, CSS, Bootstrap and JavaScript and is maintained in my GitHub repository for academic reference.

**Aditya Tiwari**

## F. Screenshots to Add Before Final Submission

1. Home page
2. About page
3. Departments page
4. Department detail page
5. Doctors page
6. Doctor profile
7. Registration
8. Login
9. Patient dashboard
10. Patient profile
11. Appointment booking
12. Appointment validation error
13. My appointments
14. Appointment cancellation
15. Gallery
16. Contact form and success message
17. Django Admin login
18. Django Admin dashboard
19. Department records in Admin
20. Doctor records in Admin
21. Appointment records in Admin
22. `python manage.py check`
23. `python manage.py test`
24. `python manage.py seed_demo`
25. GitHub repository with report directory

## G. Viva Questions and Short Answers

### What is Accord-HMS?
A Django-based Hospital Appointment & Management System developed as an academic project.

### Why Django?
Django provides models, views, templates, forms, authentication and an admin panel in a clear structure.

### Why SQLite?
SQLite is lightweight and suitable for local academic development without requiring a separate database server.

### What is a model?
A model represents a database table and defines the fields stored in it.

### What is a view?
A view handles a web request, performs application logic and returns a response, commonly by rendering a template.

### What is a form?
A form collects and validates user input before it is processed or stored.

### How is duplicate appointment booking prevented?
The system checks whether a Pending or Confirmed appointment already exists for the selected doctor, date and time.

### Why is the dashboard protected?
It uses Django's `login_required` decorator so only authenticated users can access it.

### What are the main models?
Department, Doctor, Profile, Appointment, Gallery and ContactMessage, along with Django's built-in User model.

### What can be added in future?
Doctor dashboards, role-based access, notifications, medical history, prescriptions, production database support and secure deployment.

## H. Final Submission Checklist

- [ ] Official certificate inserted.
- [ ] Official Techpile details inserted.
- [ ] College supervisor/coordinator details inserted if required.
- [ ] Screenshots captured from the final working project.
- [ ] Screenshots inserted into Word/PDF.
- [ ] Page numbers and table of contents generated.
- [ ] Names and dates proofread.
- [ ] `python manage.py check` passes.
- [ ] `python manage.py test` passes.
- [ ] `python manage.py seed_demo` tested when fresh demo data is needed.
- [ ] `.venv/` and local database are not unnecessarily committed.
- [ ] Final source code pushed to GitHub.
- [ ] Final report material kept under `report/` in the repository.