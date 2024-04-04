from django.urls import path
from .views import main_page, home_page, about_page, contact_page

urlpatterns = [
    path('', main_page),
    path('home', home_page),
    path('about', about_page),
    path('contact', contact_page),
]

