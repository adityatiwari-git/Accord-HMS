from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User

from .forms import AppointmentForm, ProfileForm
from .models import Appointment, ContactMessage, Department, Doctor, Gallery, Profile


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def departments(request):
    departments = Department.objects.all()
    return render(request, "departments.html", {"departments": departments})


def doctors(request):
    doctors_list = Doctor.objects.select_related("department").filter(available=True)
    return render(request, "doctors.html", {"doctors": doctors_list})


def gallery(request):
    gallery_items = Gallery.objects.all()
    return render(request, "gallery.html", {"gallery_items": gallery_items})


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")
    return render(request, "contact.html")


@login_required
def book_appointment(request, doctor_id=None):
    initial = {}
    if doctor_id:
        initial["doctor"] = get_object_or_404(Doctor, pk=doctor_id, available=True)

    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
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
    appointment_list = Appointment.objects.filter(patient=request.user).select_related("doctor", "doctor__department")
    return render(request, "appointments.html", {"appointments": appointment_list})


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id, patient=request.user)
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


@login_required
def dashboard(request):
    appointment_list = Appointment.objects.filter(patient=request.user).select_related("doctor")
    context = {
        "total_appointments": appointment_list.count(),
        "pending_appointments": appointment_list.filter(status="Pending").count(),
        "confirmed_appointments": appointment_list.filter(status="Confirmed").count(),
        "recent_appointments": appointment_list[:5],
    }
    return render(request, "dashboard.html", context)
