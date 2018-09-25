from django.shortcuts import render

# Create your views here.

def landing (request):
    title='Nasa-Api'
    return render (request,'Nasa/landing.html',{"title":title})
