import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application


# Vercel uses temporary serverless instances. SQLite is stored in /tmp by
# config/settings.py, so the schema must be checked whenever the function
# starts. Running migrate is safe when the migrations are already applied.
if os.environ.get("VERCEL"):
    call_command("migrate", interactive=False, verbosity=0)
    call_command("seed_demo", verbosity=0)

app = get_wsgi_application()
