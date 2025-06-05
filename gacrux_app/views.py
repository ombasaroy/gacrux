from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact-us.html')


def about(request):
    return render(request, 'about-us.html')


def projectManagement(request):
    return render(request, 'project-management.html')


def ict(request):
    return render(request, 'ict.html')


def services(request):
    return render(request, 'services.html')


def businessCompliance(request):
    return render(request, 'business-compliance.html')


def agriculture(request):
    return render(request, 'agriculture.html')


def businessDevelopment(request):
    return render(request, 'business-development.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)


