import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application


# Database schema and demo catalog are managed in the dedicated Supabase
# Accord-HMS database. The Vercel function only needs to initialize Django.
app = get_wsgi_application()
