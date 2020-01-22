from django.urls import path, include
from my_app import views
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name='home'),
    path('new_search', views.new_search, name='new_search'),
    path('drugs.com', RedirectView.as_view(url = 'https://www.drugs.com/')),
    path('pgrc', RedirectView.as_view(url='http://pgrc.inje.ac.kr/')),
    path('spmed', RedirectView.as_view(url='https://www.spmed.kr/')),
    path('cyp2d6', RedirectView.as_view(url='http://bioinformatics.vn:3838/spmed/cyp2d6')),
    path('nat2', RedirectView.as_view(url='http://bioinformatics.vn:3838/spmed/nat2')),
    path('var_anno', RedirectView.as_view(url='http://bioinformatics.vn:3838/spmed/variant-interpreter/')),

]

