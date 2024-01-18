from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', noticesView, name='notices'),
    path('notice/<int:notice_id>/', notice_detail, name='notice_detail'),
 
   
]