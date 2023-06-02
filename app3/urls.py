from django.urls import path
from app3.views import *
app_name='app3'
urlpatterns=[
    path('masha/',masha,name='masha'),
    path('bear/',bear,name='bear'),
]