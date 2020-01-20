from django.urls import path, include
from my_app import views
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('drugs.com', RedirectView.as_view(url = 'https://www.drugs.com/')),
    path('pgrc', RedirectView.as_view(url='http://pgrc.inje.ac.kr/')),

]

