from django.urls import path, include, re_path
# importing Views for routing
from . import views

urlpatterns = [
    path('', views.PlacesClass.as_view()),
    path('<int:pk>/', views.PlacesDetail.as_view()),
]
