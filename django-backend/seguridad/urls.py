from django.urls import path
from .login import LoginPageView

urlpatterns = [
    path('login', LoginPageView.as_view(), name='login'),
]
