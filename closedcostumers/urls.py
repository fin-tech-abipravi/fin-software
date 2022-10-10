from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView
# importing Views for routing
from . import views

urlpatterns = [
    path('costumer/<str:pk>/', views.ClosedCostumerView.as_view()),
    path('costumerdetail/<str:pk>/', views.ClosedCostumerDetailView.as_view()),
    path('loan/<str:pk>/', views.ClosedLoanView.as_view()),
    path('loandetail/<int:pk>/', views.ClosedLoanDetailView.as_view())
]
