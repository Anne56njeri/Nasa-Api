from django.shortcuts import render
from .request import all_images,all_camera
from .models import Sources
# Create your views here.

def landing (request):
    title='Nasa-Api'
    all_rovers=all_images()
    camera_details=all_camera()
    return render (request,'Nasa/landing.html',{"all_rovers":all_rovers,"camera_details":camera_details})
