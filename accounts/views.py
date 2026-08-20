from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username:
            messages.error(request, "Username is required.")
            return redirect("register")

        if len(password) < 8:
            messages.error(request, "Password must contain at least 8 characters.")
            return redirect("register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register.html")


def login_view(request):
    next_url = request.POST.get("next") or request.GET.get("next")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if next_url and next_url.startswith("/") and not next_url.startswith("//"):
                return redirect(next_url)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html", {"next": next_url})


@login_required
def dashboard(request):
    from hospital.views import dashboard as hospital_dashboard
    return hospital_dashboard(request)


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
