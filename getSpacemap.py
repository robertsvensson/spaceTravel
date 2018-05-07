from contentful import Client
import os

SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
ACCESS_TOKEN = os.getenv('CONTENTFUL_ACCESS_TOKEN')
ASSET_ID = os.getenv('CONTENTFUL_SPACEMAP_ASSET_ID')

def getSpacemap():
    client = Client(SPACE_ID, ACCESS_TOKEN)
    asset = client.asset(ASSET_ID)
    return asset.url(q=50, w=300)
