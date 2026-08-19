from django.contrib import admin
from .models import Appointment, ContactMessage, Department, Doctor, Gallery, Profile


admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Profile)
admin.site.register(Appointment)
admin.site.register(Gallery)
admin.site.register(ContactMessage)
