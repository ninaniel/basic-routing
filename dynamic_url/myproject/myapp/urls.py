from django.urls import path
from .views import default_greeting, greeting

urlpatterns = [
    path('', default_greeting),
    path('<str:name>/', greeting),
]