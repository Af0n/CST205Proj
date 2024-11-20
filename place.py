class Place():
    phone = ""
    address = ""
    mapsLink = ""
    webLink = ""
    name = ""
    imgSrc = ""

    def __init__(self, phone, address, maps, web, name, src):
        self.phone = phone
        self.address = address
        self.mapsLink = maps
        self.webLink = web
        self.name = name
        self.imgSrc = src

    def __str__(self):
        return f"=== Place ===\nName: {self.name}\nAddress: {self.address}\nPhone: {self.phone}\nGoogleMaps: {self.mapsLink}\nWebsite: {self.webLink}\nImage Src: {self.imgSrc}"