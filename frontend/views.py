from django.shortcuts import render
from api.models import Category,Test
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    query=Category.objects.all()
    return render(request,"index.html",{"objects":query})

def marks(request,username):
    query=Test.objects.filter(username=username)
    return render(request,"marks.html",{"objects": query})

def studentmarks(request):
    query=User.objects.all()
    return render(request,"studentmarks.html",{"objects": query})


def questions(request):
    return render(request,"questions.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def logout(request):
    return render(request,"logout.html")
