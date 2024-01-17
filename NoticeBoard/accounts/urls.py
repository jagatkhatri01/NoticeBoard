from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('signUp/', signUp, name='signup'),
    path('login/', login_view, name='login'),
    path('demo/', demo, name='demo'),
    
   
]