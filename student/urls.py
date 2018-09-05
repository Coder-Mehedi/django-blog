from django.urls import path, include
from .views import StudentResultView

urlpatterns = [
    path('result/<int:roll>', StudentResultView.as_view()),
]
