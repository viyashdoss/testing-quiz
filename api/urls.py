from django.urls import path
from .views import *


urlpatterns= [
    path('test',test),
    path('category',category),
    path('question/<str:name>',question)
]