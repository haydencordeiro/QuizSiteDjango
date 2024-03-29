from django.http import HttpResponse
from django.shortcuts import render
from .services import *
from .selectors import *
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse


def index(request):
    context = {
        'questions': []
    }
    if request.user.is_authenticated:
        context['questions'] = get_questions()

    return render(request, 'index.html', context)


def login(request):
    if request.method == "POST":
        if(user_login(request, request.POST['username'], request.POST['password'])):
            return HttpResponsePermanentRedirect(reverse('index'))

    return render(request, 'login.html')


def register(request):
    # equest, email: str, name: str, username: str, password: str)
    if request.method == "POST":
        print(request.POST['email'])
        user_create(request, request.POST['email'], request.POST['name'],
                    request.POST['username'], request.POST['password'])
        return HttpResponsePermanentRedirect(reverse('login'))
    else:
        return render(request, 'register.html')


def logoutfromsite(request):
    user_logout(request)
    return HttpResponsePermanentRedirect(reverse('index'))
