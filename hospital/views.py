from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AppointmentForm, ContactForm, ProfileForm
from .models import Appointment, Department, Doctor, Gallery, Profile


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def departments(request):
    department_list = Department.objects.all().order_by("name")
    return render(request, "departments.html", {"departments": department_list})


def department_detail(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    doctors_list = department.doctors.filter(available=True).order_by("name")
    return render(
        request,
        "department.html",
        {"department": department, "doctors": doctors_list},
    )


def doctors(request):
    doctors_list = Doctor.objects.select_related("department").filter(available=True)
    return render(request, "doctors.html", {"doctors": doctors_list})


def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(
        Doctor.objects.select_related("department"),
        pk=doctor_id,
        available=True,
    )
    return render(request, "doctor.html", {"doctor": doctor})


def gallery(request):
    gallery_items = Gallery.objects.all()
    return render(request, "gallery.html", {"gallery_items": gallery_items})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


@login_required
def book_appointment(request, doctor_id=None):
    initial = {}
    if doctor_id:
        initial["doctor"] = get_object_or_404(Doctor, pk=doctor_id, available=True)

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data["doctor"]
            appointment_date = form.cleaned_data["appointment_date"]
            appointment_time = form.cleaned_data["appointment_time"]

            already_booked = Appointment.objects.filter(
                doctor=doctor,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                status__in=["Pending", "Confirmed"],
            ).exists()

            if already_booked:
                form.add_error(
                    None,
                    "This doctor already has an appointment at that date and time. "
                    "Please choose another time.",
                )
            else:
                appointment = form.save(commit=False)
                appointment.patient = request.user
                appointment.save()
                messages.success(request, "Appointment booked successfully.")
                return redirect("appointments")
    else:
        form = AppointmentForm(initial=initial)

    return render(request, "book_appointment.html", {"form": form})


@login_required
def appointments(request):
    appointment_list = (
        Appointment.objects.filter(patient=request.user)
        .select_related("doctor", "doctor__department")
    )
    return render(request, "appointments.html", {"appointments": appointment_list})


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, pk=appointment_id, patient=request.user
    )

    if request.method == "POST" and appointment.status not in ["Completed", "Cancelled"]:
        appointment.status = "Cancelled"
        appointment.save(update_fields=["status"])
        messages.success(request, "Appointment cancelled.")

    return redirect("appointments")


@login_required
def profile(request):
    profile_obj, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile_obj)

    return render(request, "profile.html", {"form": form})
