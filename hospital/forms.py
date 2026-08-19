from django import forms
from .models import Appointment, Profile


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "appointment_date", "appointment_time", "reason"]
        widgets = {
            "appointment_date": forms.DateInput(attrs={"type": "date"}),
            "appointment_time": forms.TimeInput(attrs={"type": "time"}),
            "reason": forms.Textarea(attrs={"rows": 4, "placeholder": "Reason for visit (optional)"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["doctor"].queryset = self.fields["doctor"].queryset.filter(available=True).order_by("name")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "phone", "address"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number"}),
            "address": forms.Textarea(attrs={"rows": 4, "placeholder": "Address"}),
        }
