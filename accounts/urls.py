from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginuser, name="login"),
    path("loginmobile", views.loginusermobile, name="loginmobil"),
    path("createuser", views.createUser, name="createuser"),
    path("getuser", views.getUser, name="getuser"),
    path('sendemail/<str:pk>', views.sendEmail, name='sendemail'),
    path("sendhtmlemail", views.sendHtmlEmail, name="sendhtmlemail"),
    path("accessusers/", views.SetAccessUsers, name="SetAccessUsers"),
]
