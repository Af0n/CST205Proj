import requests
import json
from place import *
from secret import key

places = []

def text_search_from(lat, long):
    url = "https://places.googleapis.com/v1/places:searchText"

    api_key = key
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': 'places.nationalPhoneNumber,places.formattedAddress,places.googleMapsUri,places.websiteUri,places.displayName,places.name,places.photos'
    }

    payload = {
        "textQuery": "Mental Health Services",
        "locationBias": {
            "circle": {
            "center": {
                "latitude": lat,
                "longitude": long
            },
            "radius": 5000
            }
        },
        "maxResultCount": 10,
        "rankPreference": "DISTANCE"
    }

    json_places = make_api_call_json(url, headers, payload)
    print(json_places)

    place_array = []
    
    for place in json_places:
        phone = place.get("nationalPhoneNumber", None)
        address = place.get("formattedAddress", None)
        maps = place.get("googleMapsUri", None)
        web = place.get("googleMapsUri", None)
        gID = place.get("name", None)

        name = place.get("displayName", None) # displayName is a dictionary
        name = name["text"] # extracting the name text from the displayName dictionary
        

        new_place = Place(phone, address, maps, web, name, gID)

        print(new_place)

def make_api_call_json(url, headers, payload):
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json().get("places", [])
    