from django.shortcuts import render
from . models import *


def home(request):
    neigborhoods = Neigborhood.objects.all()
    return render(request,'neigborhood/index.html',{'neigborhoods':neigborhoods})
