import urllib.request,json
from .models import Sources,Camera
from functools import reduce

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

def all_camera(sources_result):
    camera_results=[]
    for results in sources_result:
        details=results.get('camera')
        id=details.get('id')
        name=details.get('name')
        full_name=details.get('full_name')
        print(full_name)
        camera_object=Camera(id,name,full_name)
        camera_results.append(camera_object)




    return camera_results
