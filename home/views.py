from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    views = {}
    views['feedbacks'] = Feedback.objects.all()  # query set bhanxa yo lai
    return render(request, 'index.html', views)


def about(request):
    return render(request, 'about.html')


def contact(request):
    views = {}
    views['informations'] = Information.objects.all()
    if request.method == 'POST':
        na = request.POST['name']
        em = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        data = Contact.objects.create(
            name=na,
            email=em,
            subject=sub,
            message=msg
        )
        data.save()
        views['message'] = {'message': 'your message is sent'}
        return render(request, 'contact.html', views)
    return render(request, 'contact.html', views)


def blog(request):
    return render(request, 'blog-single.html')


def bloghome(request):
    return render(request, 'blog-home.html')


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def price(request):
    return render(request, 'price.html')


def services(request):
    return render(request, 'services.html')
