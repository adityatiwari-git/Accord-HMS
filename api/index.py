import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.core.wsgi import get_wsgi_application


# Initialize Django first so the app registry and database configuration are
# ready before management commands are used.
app = get_wsgi_application()


# Vercel uses temporary serverless storage. The SQLite database is therefore
# created in /tmp and its migrations/demo data are prepared when the function
# starts. Running migrate repeatedly is safe because Django skips migrations
# that have already been applied.
if os.environ.get("VERCEL"):
    from django.core.management import call_command

    call_command("migrate", interactive=False, verbosity=0)
    call_command("seed_demo", verbosity=0)
