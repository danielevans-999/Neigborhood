from django.shortcuts import render
from . models import *


def home(request):
    neigborhoods = Neigborhood.objects.all()
    return render(request,'neigborhood/index.html',{'neigborhoods':neigborhoods})

def single_neigborhood(request,id):
    single_hood = Neigborhood.objects.get(pk=id)
    return render (request, 'neigborhood/neigborhood.html',{'hood':single_hood})