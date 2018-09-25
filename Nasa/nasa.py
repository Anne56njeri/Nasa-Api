import random

from aiohttp import web,ClientSession
from aiohttp.web import HTTPFound

NASA_API_KEY='DEMO_KEY'
ROVER_URL='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
async def get_mars_image_url_from_nasa():
    while True:
        sol=random.randint(0,1722)
        params= {'sol':sol,'api_key':NASA_API_KEY}
        async with ClientSession() as session:
            async with session.get(ROVER_URL, params=params) as resp:
                resp_dict=await resp.json()
        if 'photos' not in resp_dict:
            raise Exception
        photos= resp_dict['photos']
        if not photos:
            continue
        return random.choice(photos)['img_src']

async def get_mars_photo(request):
    url=await get_mars_image_url_from_nasa()
    return HTTPFound(url)
app=web.Application()
app.router.add_get('/',get_mars_photo,name='mars_photo')

web.run_app(app, host='127.0.0.1', port=8080)
