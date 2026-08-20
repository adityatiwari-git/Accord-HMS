from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .forms import AppointmentForm
from .models import Appointment, Department, Doctor


class HospitalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.department = Department.objects.create(
            name="Cardiology",
            description="Heart care department.",
        )
        self.doctor = Doctor.objects.create(
            name="Dr. Test Doctor",
            department=self.department,
            qualification="MBBS, MD",
            experience=5,
            available=True,
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_doctors_page_loads(self):
        response = self.client.get(reverse("doctors"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dr. Test Doctor")

    def test_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("login"),
            {"username": "testuser", "password": "testpass123"},
        )
        self.assertRedirects(response, reverse("dashboard"))

    def test_appointment_form_rejects_past_date(self):
        form = AppointmentForm(
            data={
                "doctor": self.doctor.id,
                "appointment_date": timezone.localdate() - timedelta(days=1),
                "appointment_time": "10:00",
                "reason": "Check-up",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("appointment_date", form.errors)

    def test_logged_in_user_can_book_future_appointment(self):
        self.client.login(username="testuser", password="testpass123")
        future_date = timezone.localdate() + timedelta(days=2)

        response = self.client.post(
            reverse("book_appointment"),
            {
                "doctor": self.doctor.id,
                "appointment_date": future_date,
                "appointment_time": "10:00",
                "reason": "Routine check-up",
            },
        )

        self.assertRedirects(response, reverse("appointments"))
        self.assertEqual(Appointment.objects.count(), 1)

    def test_duplicate_appointment_is_not_allowed(self):
        future_date = timezone.localdate() + timedelta(days=2)
        Appointment.objects.create(
            patient=self.user,
            doctor=self.doctor,
            appointment_date=future_date,
            appointment_time="10:00",
            reason="First appointment",
            status="Confirmed",
        )

        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("book_appointment"),
            {
                "doctor": self.doctor.id,
                "appointment_date": future_date,
                "appointment_time": "10:00",
                "reason": "Second appointment",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertContains(response, "already has an appointment")

    def test_user_can_cancel_appointment(self):
        appointment = Appointment.objects.create(
            patient=self.user,
            doctor=self.doctor,
            appointment_date=timezone.localdate() + timedelta(days=2),
            appointment_time="11:00",
            reason="Routine check-up",
            status="Pending",
        )

        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("cancel_appointment", args=[appointment.id])
        )

        appointment.refresh_from_db()
        self.assertRedirects(response, reverse("appointments"))
        self.assertEqual(appointment.status, "Cancelled")

    def test_contact_and_profile_pages_require_expected_access(self):
        self.assertEqual(self.client.get(reverse("contact")).status_code, 200)
        self.assertEqual(self.client.get(reverse("profile")).status_code, 302)
