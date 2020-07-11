from django.urls import path
from . import views
# this is my changes
urlpatterns = [
    path('', views.home, name='home-page'),
    path('home/', views.home, name='home-page'),
    path('contact-us/', views.contact_us, name='contact_us-page'),
    path('compare/', views.compare, name='compare-page'),

]
