
from fastapi import FastAPI
import requests
import json
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(middleware=middleware)

headers = {
    'authority': 'march-api1.vercel.app',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.5',
    'origin': 'https://www.ashanime.pro',
    'referer': 'https://www.ashanime.pro/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
}

@app.get("/")
async def main():
  url="https://harrynull.tech/api/wallpapers/random_anime_wallpaper?download=true"
  r=requests.get(url)
  k=r.json()
  return k

@app.get('/trending/{pgno}')
async def main(pgno:int):
  
   # https://api.consumet.org/meta/anilist/trending?page={page}&perPage={perPage}




  # response = requests.get('https://march-api1.vercel.app/meta/anilist/trending', params=params, headers=headers) 
  url=f"https://march-api1.vercel.app/meta/anilist/trending?page={pgno}&provider=gogoanime"
  r=requests.get(url,headers=headers)
  k=r.json()
  return k

@app.get('/popular/{pgno}')
async def main(pgno:int):

 
#   url=f"https://api.consumet.org/meta/anilist/popular?page={pgno}&perPage=20"

  url=f"https://march-api1.vercel.app/meta/anilist/popular?page={pgno}&provider=gogoanime&perPage=20"

  r=requests.get(url,headers=headers)
  k=r.json()
  return k

@app.get('/latestep')
async def main(pgno:int =1):

 
#   url=f"https://api.consumet.org/meta/anilist/recent-episodes?page={pgno}provider=gogoanime&perPage=20"


  url=f"https://march-api1.vercel.app/meta/anilist/recent-episodes?page={pgno}&provider=gogoanime&perPage=20"
  r=requests.get(url,headers=headers)
  k=r.json()
  return k

@app.get('/detail/{id}/{dub}')
async def main(id:int,dub: str):

 
  url=f"https://march-api1.vercel.app/meta/anilist/info/{id}?fetchFiller=true&dub={dub}"
  r=requests.get(url,headers=headers)
  k=r.json()
  return k

@app.get('/watch/{str}')
async def main(str: str):

#   https://api.consumet.org/meta/anilist/watch/{episodeId}

 
  url=f"https://march-api1.vercel.app/meta/anilist/watch/{str}"
  r=requests.get(url,headers=headers)
  k=r.json()
  return k


