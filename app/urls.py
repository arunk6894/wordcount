from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name = 'countwords'),
    path('count/', views.count, name = 'count'),
    path('about/', views.aboutus, name = 'aboutus'),
]