from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def service(request):
    return render(request, 'core/service.html')

def contact(request):
    return render(request, 'core/contact.html')

def feature(request):
    return render(request, 'core/feature.html')

def team(request):
    return render(request, 'core/team.html')

def quote(request):
    return render(request, 'core/quote.html')

def testimonial(request):
    return render(request, 'core/testimonial.html')

def f0f(request):
    return render(request, 'core/404.html')