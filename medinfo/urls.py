from django.urls import path
from . import views

app_name = 'medinfo'

urlpatterns = [
    path('', views.med_view, name='medinfo'),
]
