from django.urls import path
from login_lab.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]
