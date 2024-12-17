class Place():
    phone = None
    address = None
    mapsLink = None
    webLink = None
    name = None
    imgSrc = None

    # def show_img(self):
    #     if self.imgSrc is not None:
    #         self.imgSrc.show()
    #     else:
    #         print("No Image Available")

    def __init__(self, phone, address, maps, web, name, gID, src):
        print("Creating new Place object...")
        self.phone = phone
        self.address = address
        self.mapsLink = maps
        self.webLink = web
        self.name = name
        self.gID = gID
        self.imgSrc = src
        print("Place object created")
    
    def __str__(self):
        return f"=== Place ===\nName: {self.name}\nAddress: {self.address}\nPhone: {self.phone}\nGoogleMaps: {self.mapsLink}\nWebsite: {self.webLink}\nGoogleID: {self.gID}\nImage Src: {self.imgSrc}\n============="
    
test = Place("(555) 5555 5555", "123 Test Street", "Test Map Link", "Test Web Link", "Test's Center for Health Testing", "Google ID for finding images", "TestSource.png")