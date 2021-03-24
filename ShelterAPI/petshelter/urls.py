from django.urls import path
from .views import PetView


urlpatterns = [
    path('pets/', PetView.as_view()),
    path('pets/<int:id>', PetView.as_view()),
]