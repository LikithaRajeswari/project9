from django.urls import path
from app2.views import *
app2_name='wasted'
urlpatterns=[
    path('new5/',new5,name='new5'),
    path('new6/',new6,name='new6'),
]