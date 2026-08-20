from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from hospital.models import Appointment, Department, Doctor, Gallery, Profile


class Command(BaseCommand):
    help = "Create simple demo data for Accord-HMS."

    def handle(self, *args, **options):
        demo_password = "Demo@1234"

        departments = {
            "Cardiology": "Diagnosis and treatment of heart and cardiovascular conditions.",
            "Neurology": "Care for disorders related to the brain and nervous system.",
            "Orthopedics": "Treatment of bones, joints, muscles and related conditions.",
            "Pediatrics": "Medical care for infants, children and adolescents.",
            "General Medicine": "Diagnosis and treatment of common illnesses and general health conditions.",
            "Dermatology": "Diagnosis and treatment of skin, hair and nail conditions.",
        }

        department_objects = {}
        for name, description in departments.items():
            department_objects[name], _ = Department.objects.get_or_create(
                name=name,
                defaults={"description": description},
            )

        doctors = [
            ("Aarav Sharma", "Cardiology", "MBBS, MD (Cardiology)", 10, "aarav@accordhms.com", "9876500001"),
            ("Meera Kapoor", "Neurology", "MBBS, MD (Neurology)", 8, "meera@accordhms.com", "9876500002"),
            ("Rohan Verma", "Orthopedics", "MBBS, MS (Orthopedics)", 9, "rohan@accordhms.com", "9876500003"),
            ("Ananya Singh", "Pediatrics", "MBBS, MD (Pediatrics)", 7, "ananya@accordhms.com", "9876500004"),
            ("Kunal Gupta", "General Medicine", "MBBS, MD (Medicine)", 12, "kunal@accordhms.com", "9876500005"),
            ("Nisha Patel", "Dermatology", "MBBS, MD (Dermatology)", 6, "nisha@accordhms.com", "9876500006"),
        ]

        for name, department, qualification, experience, email, phone in doctors:
            Doctor.objects.get_or_create(
                name=name,
                defaults={
                    "department": department_objects[department],
                    "qualification": qualification,
                    "experience": experience,
                    "email": email,
                    "phone": phone,
                    "available": True,
                },
            )

        patients = [
            ("rahul.demo", "Rahul Kumar", "rahul.demo@example.com", "9876510001"),
            ("priya.demo", "Priya Sharma", "priya.demo@example.com", "9876510002"),
            ("aman.demo", "Aman Singh", "aman.demo@example.com", "9876510003"),
            ("neha.demo", "Neha Verma", "neha.demo@example.com", "9876510004"),
            ("rohit.demo", "Rohit Gupta", "rohit.demo@example.com", "9876510005"),
            ("simran.demo", "Simran Patel", "simran.demo@example.com", "9876510006"),
            ("vikas.demo", "Vikas Mishra", "vikas.demo@example.com", "9876510007"),
        ]

        for username, full_name, email, phone in patients:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": email},
            )

            if created:
                user.set_password(demo_password)
                user.save()

            Profile.objects.update_or_create(
                user=user,
                defaults={
                    "full_name": full_name,
                    "phone": phone,
                    "address": "Accord-HMS Demo City",
                },
            )

        gallery_items = [
            (
                "Modern Hospital",
                "A welcoming hospital environment.",
                "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?auto=format&fit=crop&w=1200&q=80",
            ),
            (
                "Medical Consultation",
                "A doctor consulting with a patient.",
                "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=1200&q=80",
            ),
            (
                "Healthcare Team",
                "Healthcare professionals working together.",
                "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=1200&q=80",
            ),
        ]

        for title, description, image_url in gallery_items:
            Gallery.objects.get_or_create(
                title=title,
                defaults={"description": description, "image_url": image_url},
            )

        patient = User.objects.filter(username="rahul.demo").first()
        doctor = Doctor.objects.filter(name="Aarav Sharma").first()

        if patient and doctor:
            Appointment.objects.get_or_create(
                patient=patient,
                doctor=doctor,
                appointment_date=timezone.localdate() + timedelta(days=3),
                appointment_time="10:00",
                defaults={
                    "reason": "Routine consultation",
                    "status": "Confirmed",
                },
            )

        self.stdout.write(self.style.SUCCESS("Accord-HMS demo data created successfully."))
        self.stdout.write(f"Demo patient password: {demo_password}")
