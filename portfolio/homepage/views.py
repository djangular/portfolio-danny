from django.shortcuts import render


def home(request):
    title = 'Danny'

    context = {
        'title': title,
    }

    return render(request, 'index.html', context)

def about(request):
    title = 'About Danny'

    context = {
        'title': title,
    }

    return render(request, 'about-me.html', context)
