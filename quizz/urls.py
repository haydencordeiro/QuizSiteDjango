from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logoutfromsite', views.logoutfromsite, name='logoutfromsite'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
