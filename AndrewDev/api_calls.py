import requests
import json

places = []

def text_search_from(lat, long):
    url = "https://places.googleapis.com/v1/places:searchText"

    api_key = "AIzaSyCEFg5vEo2LHnwTf4NkQlrs9F0e8RNuAYI"
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': 'places.displayName,places.formattedAddress'
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

    places = make_api_call(url, headers, payload)
    print(places)

def make_api_call(url, headers, payload):
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json().get("places", [])
    