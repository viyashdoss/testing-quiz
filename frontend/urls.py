from django.urls import path
from .views import *


urlpatterns=[
    path('',index,name="index"),
    path('login',login,name="login"),
    path('logout',logout,name="logout"),
    path('register',register,name="register"),
    path('questions1',questions,name="questions"),
    path('marks/<str:username>',marks,name="marks"),
    path('studentmarks',studentmarks,name="studentmarks")
]