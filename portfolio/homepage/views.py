from django.shortcuts import render, HttpResponseRedirect
from .models import Photo

from django.contrib import messages
from django.core.mail import send_mail


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

    return render(request, 'contact.html', context)

def send_message(request):
    email    = request.POST['email']
    subject  = request.POST['subject']
    message  = request.POST['message']

    send_mail (
        subject,
        message,
        email,
        ['danny@duendeinraw.com'],
        fail_silently=False
    )
    messages.success(request, 'Thanks for reaching out!')

    return HttpResponseRedirect('/contact')
