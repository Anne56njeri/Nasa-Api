from django.db import models

# Create your models here.
class Sources:
    def __init__(self,id,sol,camera,earth_date,img_src):
        self.id=id
        self.sol=name
        self.camera=camera
        self.earth_date=earth_date
        self.img_src=img_src
class Camera:
    def __init__(self,id,name,full_name):
        self.id=id
        self.name=name
        self.full_name=full_name
class Rover:
    def __init__(self,id,name,landing):
        self.id=id
        self.name=name
        self.landing=landing
