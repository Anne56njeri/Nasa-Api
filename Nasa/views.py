from django.shortcuts import render
import requests
# Create your views here.

def landing (request):
    title='Nasa-Api'
    response=requests.get('https://api.nasa.gov/planetary/apod?api_key=EPZMQv6VmlTFXhcGrZ4Jhu1BLZkIjbdjjqVRR2ck')
    data=response.json()
    title1=data.get('title')
    one=data.get('date')
    images=data.get('url')
    hdu=data.get('hdurl')

    return render (request,'Nasa/landing.html',{"title1":title1,"one":one,"images":images,"hdu":hdu})
