from django.urls import path
from . import views

app_name = 'bmi'

urlpatterns = [
    path('', views.bmi, name='bmi'),
]
