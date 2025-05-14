from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hi),
    path('info/', views.class_info)
]
