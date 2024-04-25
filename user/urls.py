from django.urls import path
from user import views

urlpatterns = [
    path('get-users/', views.getusers, name='get-users'),
]