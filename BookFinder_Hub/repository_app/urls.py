from django.urls import path
from . import views

urlpatterns = [
    path('repository/', views.repository, name='repository'),
    path('repository/success/', views.success, name='success'),
]