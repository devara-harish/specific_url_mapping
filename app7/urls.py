from app7.views import *
from django.urls import path 
app_name='hello'
urlpatterns=[
    path('pspk/',pspk,name='pspk'),
    path('harish/',harish,name='harish'),
]