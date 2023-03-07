# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, fonsePageView, results, homePost

urlpatterns = [
    path('', homePageView, name='fonse'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
