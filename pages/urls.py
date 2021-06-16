from django.urls import path

#add url for homepage
from . import views #from all import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]