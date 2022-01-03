from django.urls import path
from .views import home

#single page application
urlpatterns = [
  path('',home,name='yoga-home'),
]