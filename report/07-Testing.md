# 7. Testing

## 7.1 Testing Strategy

Testing was performed using Django's automated test framework and manual browser testing. The aim was to check both normal workflows and invalid input cases.

## 7.2 Automated Tests

The project contains tests for:

- Home page loading.
- Doctors page loading.
- Successful login and dashboard redirection.
- Rejection of past appointment dates.
- Successful future appointment booking.
- Prevention of duplicate appointment slots.
- Appointment cancellation.
- Expected access behaviour for public and protected pages.

The final test run completed successfully with **6 tests passing and `OK`**.

Run the tests with:

```bash
python manage.py test
```

The Django system check was also run successfully:

```bash
python manage.py check
```

## 7.3 Manual Testing

| Test Case | Expected Result | Result |
|---|---|---|
| Home page | Page loads | Pass |
| Registration | New account created | Pass |
| Correct login | Dashboard opens | Pass |
| Wrong login | Error message | Pass |
| Doctors page | Available doctors displayed | Pass |
| Department page | Department details displayed | Pass |
| Doctor profile | Doctor information displayed | Pass |
| Future appointment | Appointment saved | Pass |
| Past appointment date | Validation error | Pass |
| Unavailable doctor | Booking prevented | Pass |
| Duplicate doctor/time | Booking prevented | Pass |
| Appointment history | Patient appointments displayed | Pass |
| Appointment cancellation | Status changes to Cancelled | Pass |
| Profile update | Profile saved | Pass |
| Contact form | Message saved | Pass |
| Django Admin | Admin opens | Pass |
| Demo seed command | Demo data created | Pass |

## 7.4 Test Evidence

Before final submission, capture screenshots of:

- `python manage.py check`
- `python manage.py test`
- `python manage.py seed_demo`
- Main patient workflow
- Django Admin

These screenshots should be inserted into the final Word/PDF report.