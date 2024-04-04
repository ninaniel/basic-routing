from django.urls import path
from .views import index, odd_or_even

urlpatterns = [
    path('', index),
    path('<slug:n>/', odd_or_even),
]