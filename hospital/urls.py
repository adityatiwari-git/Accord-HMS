from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("departments/", views.departments, name="departments"),
    path("departments/<int:department_id>/", views.department_detail, name="department_detail"),
    path("doctors/", views.doctors, name="doctors"),
    path("doctors/<int:doctor_id>/", views.doctor_detail, name="doctor_detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("appointments/book/", views.book_appointment, name="book_appointment"),
    path("appointments/book/<int:doctor_id>/", views.book_appointment, name="book_doctor"),
    path("appointments/", views.appointments, name="appointments"),
    path("appointments/<int:appointment_id>/cancel/", views.cancel_appointment, name="cancel_appointment"),
    path("profile/", views.profile, name="profile"),
]
