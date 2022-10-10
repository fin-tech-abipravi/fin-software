from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('<str:token>/', views.PartiesView.as_view()),
    path('detail/<str:pk>/', views.PartiesViewDetail.as_view()),
    path('partyloans/<str:token>/', views.PartiesLoanView.as_view()),
    path('detail/<str:pk>/',
         views.PartiesLoanViewDetail.as_view()),
]
