import urllib.request,json
from .models import Sources,Camera

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
def all_camera():
    all_camera=nasa.base.url.format(api_key)
    with urllib.request.urlopen(all_camera) as url:
        all_camera_details=url.read()
        get_camera_reponse=json.load(all_camera_details)

        if get_camera_reponse['camera']:
            camera_result=get_camera_reponse['camera']
    return camera_result        
