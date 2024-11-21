class Place():
    phone = ""
    address = ""
    mapsLink = ""
    webLink = ""
    name = ""
    imgSrc = ""

    def __init__(self, phone, address, maps, web, name, gID):
        self.phone = phone
        self.address = address
        self.mapsLink = maps
        self.webLink = web
        self.name = name
        self.gID = gID
        
        self.imgSrc = self.get_image_src()

    def get_image_src(self):
        print("get_image_src not implemented")
        # make API call to get image from Google Places Photos (New) using self.gID
        return None
    
    def __str__(self):
        return f"=== Place ===\nName: {self.name}\nAddress: {self.address}\nPhone: {self.phone}\nGoogleMaps: {self.mapsLink}\nWebsite: {self.webLink}\nImage Src: {self.imgSrc}\n============="
    
test = Place("(555) 5555 5555", "123 Test Street", "Test Map Link", "Test Web Link", "Test's Center for Health Testing", "Google ID for finding images")