from django.shortcuts import render
import requests
# Create your views here.

def landing (request):
    title='Nasa-Api'
    response=requests.get('https://api.nasa.gov/planetary/apod?api_key=EPZMQv6VmlTFXhcGrZ4Jhu1BLZkIjbdjjqVRR2ck')
    data=response.json()
    one=data.get('date')

    return render (request,'Nasa/landing.html',{"title":title,"one":one})
