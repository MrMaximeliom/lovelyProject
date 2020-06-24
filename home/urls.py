from django.urls import path
from . import views
# this is my changes
urlpatterns = [
    path('', views.home, name='home-page'),
    path('home/', views.home, name='home-page'),

]
