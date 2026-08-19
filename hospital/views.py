from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def departments(request):

    departments = Department.objects.all()

    return render(
        request,
        "departments.html",
        {"departments": departments}
    )