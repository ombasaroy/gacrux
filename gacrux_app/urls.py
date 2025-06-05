from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us/', views.contact, name='contact-us'),
    path('about-us/', views.about, name='about-us'),
    path('project-management/', views.projectManagement, name='project-management'),
    path('ict/', views.ict, name='ict'),
    path('services/', views.services, name='services'),
    path('business-compliance/', views.businessCompliance, name='business-compliance'),
    path('agriculture/', views.agriculture, name='agriculture'),
    path('business-development/', views.businessDevelopment, name='business-development'),
]
