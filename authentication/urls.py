from .views import UserRegistration, UserLogin

from django.urls import path

urlpatterns = [
    path('login', UserLogin.as_view()),
    path('signup', UserRegistration.as_view()),
]
