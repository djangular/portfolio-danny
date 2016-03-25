from django.shortcuts import render
from django.contrib import messages
from .models import Photo, Message

def home(request):
    title = 'Danny'
    gallery = Photo.objects.all()

    context = {
        'title': title,
        'gallery': gallery,
    }

    return render(request, 'index.html', context)

def about(request):
    title = 'About Me'

    context = {
        'title': title,
    }

    return render(request, 'about-me.html', context)

def contact(request):
    title = 'Reach Out'

    context = {
        'title' : title,
    }

    return render(request, 'contact-2.html')

def sendmessage(request):
    try:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        new_message = Message.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        new_message.save()

        messages.success(request, 'Thanks for reaching out!')
        return render(request, 'contact-2.html')

    except:
        messages.failure(request, 'Something went wrong, please try again later')
        return render(request, 'contact-2.html')
