from django.contrib import admin
from django.urls import path, include
from .views import noticesView, notice_detail, add_cr_notice

urlpatterns = [
    path('', noticesView, name='notices'),
    path('notice/<int:notice_id>/', notice_detail, name='notice_detail'),
    path('add_notice/', add_cr_notice, name='add_cr_notice'),
 
   
]