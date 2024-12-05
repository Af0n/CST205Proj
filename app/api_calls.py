import requests
import json
from place import Place
from secret import key
from PIL import Image

# returns a PIL image object from API
def picture_search(gID):
    api_key = key
    url = f"https://places.googleapis.com/v1/{gID}/media?key={api_key}&maxHeightPx=4800&skipHttpRedirect=true"
    response = requests.get(url)
    src = response.json().get("photoUri", None)
    return src

# returns an array of Place objects based on the top results from the API
# radius is in meters, max 50000
def text_search_from(lat, long, number, radius):
    if radius < 0:
        radius = 0

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
            "radius": min(radius, 50000)
            }
        },
        "maxResultCount": number,
        "rankPreference": "DISTANCE"
    }

    json_places = make_api_call_json(url, headers, payload)
    # print(json_places)

    place_array = []
    
    for place in json_places:
        phone = place.get("nationalPhoneNumber", None)
        address = place.get("formattedAddress", None)
        maps = place.get("googleMapsUri", None)
        web = place.get("googleMapsUri", None)

        gID = place.get("photos", None) # photos is an array of dictionaries
        if gID is not None:
            gID = gID[0]["name"] # grab the name
            src = picture_search(gID) # get actual image
            print(src)
        else:
            print("No photos")
            src = None

        name = place.get("displayName", None) # displayName is a dictionary
        if name is not None:
            name = name["text"] # extracting the name text from the displayName dictionary

        new_place = Place(phone, address, maps, web, name, gID, src)

        place_array.append(new_place)
    
    return place_array

def make_api_call_json(url, headers, payload):
    print(f"=== API Call ===\nURL: {url}\nHEADERS: {headers}\nPAYLOAD:{payload}")
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Call successfull")
    else:
        print("Failure")
    print("================")
    return response.json().get("places", [])
    