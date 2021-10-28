from django.contrib import admin
from django.urls import path
from .views import Login, Register

urlpatterns = [
    path('login/', Login.as_view()),
    path('accounts/', Register.as_view()),
]
