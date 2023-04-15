from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('dados/<str:id>/', views.dados, name="dados"),
    path('logado/', views.logado, name="logado"),
    path('updados/<str:id>/', views.updados, name="updados"),
    path('delete/<str:id>/', views.delete, name="delete")
]
