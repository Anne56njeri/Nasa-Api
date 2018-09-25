import urllib.request,json
from .models import Sources

api_key = 'EPZMQv6VmlTFXhcGrZ4Jhu1BLZkIjbdjjqVRR2ck'

nasa_base_url= 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key={}'

def all_images():
    all_images=nasa_base_url.format(api_key)
    with urllib.request.urlopen(all_images) as url:
        all_nasa_images=url.read()
        get_source_response=json.loads(all_nasa_images)


        if get_source_response['photos']:
            sources_result=get_source_response['photos']
    return sources_result
