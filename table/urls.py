from django.urls import path
from .import views
from .views import home

urlpatterns = [
    path('', views.home),
    path('<week_name>/', views.week),
]
