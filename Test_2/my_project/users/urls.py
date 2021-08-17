from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path('', views.index_page, name = 'index_page'),

]