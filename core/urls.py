from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('team/', views.team, name='team'),
    path('quote/', views.quote, name='quote'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('f0f/', views.f0f, name='f0f'),
]
