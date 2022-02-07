from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginuser, name="login"),
    path("createuser", views.createUser, name="createuser"),
    path("getuser", views.getUser, name="getuser"),
    path('sendemail', views.sendEmail, name='sendemail'),
]
