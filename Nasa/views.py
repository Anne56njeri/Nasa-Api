from django.shortcuts import render
from .request import all_images,all_camera,all_rover
from .models import Sources
# Create your views here.

def landing (request):
    title='Nasa-Api'
    all_rovers=all_images()
    camera_details=all_camera(all_rovers)

    rover_details=all_rover(all_rovers)
    for details in rover_details:
        landing_date=details.landing
    return render (request,'Nasa/landing.html',{"all_rovers":all_rovers,"camera_details":camera_details,"landing_date":landing_date})
