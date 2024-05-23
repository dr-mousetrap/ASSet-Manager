from django.shortcuts import render
from django.http import HttpResponse
from datetime  import datetime
from .models import teacher
from .models import assets
# Create your views here.
def index(request):
    now= datetime.now()
    teach = teacher.objects.all()
    ass = assets.objects.all()

    return render(request, "MyApp1/index.html",{'content': teach,'things': ass})

def happy(request):
    return render(request,"MyApp1/CSS/happy.html")