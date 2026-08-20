from datetime import datetime

from django import forms
from django.utils import timezone

from .models import Appointment, ContactMessage, Profile


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "appointment_date", "appointment_time", "reason"]
        widgets = {
            "appointment_date": forms.DateInput(attrs={"type": "date"}),
            "appointment_time": forms.TimeInput(attrs={"type": "time"}),
            "reason": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Reason for visit (optional)"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = (
            self.fields["doctor"].queryset
            .filter(available=True)
            .order_by("name")
        )

    def clean(self):
        cleaned_data = super().clean()
        doctor = cleaned_data.get("doctor")
        appointment_date = cleaned_data.get("appointment_date")
        appointment_time = cleaned_data.get("appointment_time")

        if doctor and not doctor.available:
            self.add_error("doctor", "This doctor is currently unavailable.")

        if appointment_date and appointment_date < timezone.localdate():
            self.add_error("appointment_date", "Please choose today or a future date.")

        if appointment_date and appointment_time:
            appointment_datetime = datetime.combine(
                appointment_date, appointment_time
            )
            appointment_datetime = timezone.make_aware(
                appointment_datetime,
                timezone.get_current_timezone(),
            )

            if appointment_datetime <= timezone.now():
                self.add_error("appointment_time", "Please choose a future time.")

        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "phone", "address"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "address": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Address"}
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
