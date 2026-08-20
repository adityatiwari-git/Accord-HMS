from django.contrib import admin

from .models import Appointment, ContactMessage, Department, Doctor, Gallery, Profile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "qualification", "experience", "available")
    list_filter = ("department", "available")
    search_fields = ("name", "qualification")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "appointment_date", "appointment_time", "status")
    list_filter = ("status", "appointment_date")
    search_fields = ("patient__username", "doctor__name")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "phone")
    search_fields = ("user__username", "full_name", "phone")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "description")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)
