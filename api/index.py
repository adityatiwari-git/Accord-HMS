import os
from pathlib import Path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application


# Vercel's deployment directory is read-only, so settings.py points SQLite
# to /tmp. On a fresh serverless instance, create the schema and demo data
# before Django starts serving requests.
if os.environ.get("VERCEL"):
    database_path = Path("/tmp/accord_hms.sqlite3")
    if not database_path.exists():
        call_command("migrate", interactive=False, verbosity=0)
        call_command("seed_demo", verbosity=0)

app = get_wsgi_application()
