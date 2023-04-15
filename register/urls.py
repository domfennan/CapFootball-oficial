from django.urls import path
from . import views

urlpatterns = [
    path('', views.load, name="load"),
    path('cadastro/', views.cadastro, name="cadastro")

    ]

