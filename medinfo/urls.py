from django.urls import path
from . import views
from .views import Medicine_view

app_name = 'medinfo'

urlpatterns = [
    path('', views.med_view, name='medinfo'),
    path('api/<str:name>', Medicine_view.as_view()),

]