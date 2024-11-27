from place import *
from api_calls import *

print(test)
print("\n\n")

# places = text_search_from(36.663024, -121.769599, 3, 5000)

# print("\n\n")
# for place in places:
#     print(place)
#     place.show_img()

places = text_search_from(36.663024, -121.769599, 10, 5000)

print("\n\n")
for place in places:
    print(place)
    place.show_img()