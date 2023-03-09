from app8.views import *
from django.urls import path 
app_name='hii'
urlpatterns=[
    path('power_star/',power_star,name='power_star'),
]