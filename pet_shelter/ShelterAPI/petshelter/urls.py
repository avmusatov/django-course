from django.urls import path
from .views import PetView, DonationView, LeaderView


urlpatterns = [
    path('pets/', PetView.as_view()),
    path('pets/<int:id>', PetView.as_view()),
    path('donations/', DonationView.as_view()),
    path('donations/<int:id>',  DonationView.as_view()),
    path('leaders/', LeaderView.as_view()),
    path('leaders/<int:id>', LeaderView.as_view()),
]