from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_ML, name='predict_ML'),
]