from django.shortcuts import render


def index(request):
    context ={
        'teste': 'Primeiro projeto em Django',
    }
    return render(request, 'index.html', context    )


def contact(request):
    return render(request, 'contact.html')
