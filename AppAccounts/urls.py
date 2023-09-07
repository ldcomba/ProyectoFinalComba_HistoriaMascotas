
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


app_name = 'AppAccounts'
urlpatterns = [
    # ...
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/',login_request, name='login'),
    path('register/', register, name='register'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    #path('cambiarPass/',cambiarPass, name='cambiarPass'),
    path('cambiarPass/', CambiarContrasenaView.as_view(), name='cambiarPass'),
]