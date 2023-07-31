from django.urls import path
from app.views import *
app_name='nothing'
urlpatterns=[
    path('new1/',new1,name='new1'),
    path('new2/',new2,name='new2'),
    path('string/',string,name='string'),
]