from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_create(request, email: str, name: str, username: str, password: str) -> User:
    try:
        user = User.objects.create_user(
            username, email, password)
        user.first_name = name
        user.save()
        messages.success(request, 'Sucessfully Created your account !')
        return user

    except Exception as e:

        messages.warning(request, e)
        return None


def user_login(request, username: str, password: str) -> User:
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Sucessfully Signed in your account !')

        return User
    else:
        messages.warning(request, 'Check your id and password')

        return None


def user_logout(request) -> None:
    auth.logout(request)
