# 10. Results and Discussion

## 10.1 Functional Result

The completed application demonstrates the main workflow of a small hospital appointment system. Visitors can explore hospital information, while authenticated patients can manage their account and appointments.

The project demonstrates how Django ORM connects database records to application views and templates. Relationships between users, profiles, doctors, departments and appointments are handled through Django models.

## 10.2 Testing Result

The final verification showed that the Django system check completed successfully and the automated test suite completed with **6 tests passing and `OK`**. Manual browser testing also covered the major user workflows.

## 10.3 Limitations

The current academic version has the following limitations:

- SQLite is used for development.
- No online payment system.
- No SMS/email notifications.
- No dedicated doctor dashboard.
- No electronic medical record module.
- No prescription management.
- No production-grade security/deployment configuration.
- Vercel deployment was not used for the final project because the current Django setup needs additional server-side deployment configuration.

## 10.4 Overall Outcome

The project reached the intended academic MVP stage and is suitable for demonstration, report preparation and Techpile training submission. The implementation is intentionally simple so its database flow and Django logic can be explained clearly during a viva.