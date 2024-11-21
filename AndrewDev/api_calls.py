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
        'X-Goog-FieldMask': 'places.nationalPhoneNumber,places.formattedAddress,places.googleMapsUri,places.websiteUri,places.displayName,places.photos'
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

    place_array = []
    
    for place in json_places:
        phone = place.get("nationalPhoneNumber", None)
        print(phone)

def make_api_call_json(url, headers, payload):
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json().get("places", [])
    