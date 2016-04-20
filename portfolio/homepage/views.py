from django.shortcuts import render, HttpResponseRedirect
from .models import Photo

from django.contrib import messages
from django.core.mail import EmailMessage

def home(request):
    title   = 'DuendeInRaw | Danny Nieto'
    gallery =  Photo.objects.all()
    context = {
        'title'   : title,
        'gallery' : gallery,
    }
    return render(request, 'index.html', context)

def about(request):
    title   = 'About |  Danny Nieto'
    context = {
        'title' : title,
    }

    return render(request, 'about.html', context)

def contact(request):
    title   = 'Booking | Danny Nieto'
    context = {
        'title' : title,
    }

    if request.POST:
        name    = request.POST['contact_name']
        email   = request.POST['mail']
        subject = request.POST['website']
        message = request.POST['comment']

        full_message = "New Email From %s =  Name: %s  \n Message: %s" %(email, name, message)

        to_send = EmailMessage(subject, full_message, to=['danny@duendeinraw.com'])
        to_send.send()

        messages.success(request, 'Thanks for reaching out!')

        return HttpResponseRedirect('/')

    return render(request, 'contact.html', context)
