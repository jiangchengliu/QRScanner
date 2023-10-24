from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='page'),
    path('qr_code/', views.get_qr_code, name='qr_code'),
]