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