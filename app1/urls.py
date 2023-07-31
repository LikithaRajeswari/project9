from django.urls import path
from app1.views import *
app1_name='awesome'
urlpatterns=[
    path('new3/',new3,name='new3'),
    path('new4/',new4,name='new4'),
    path('string/',string,name='string'),
]