from django.shortcuts import render
from .request import all_images
from .models import Sources
# Create your views here.

def landing (request):
    title='Nasa-Api'
    all_rovers=all_images()
    
    return render (request,'Nasa/landing.html',{"all_rovers":all_rovers})
