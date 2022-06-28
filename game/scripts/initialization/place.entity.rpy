init python:

    class place(object):
        def __init__(self,name,cfname,isActive):
            self.name = name
            self.cfname = cfname
            self.isActive = isActive

        @property
        def bg_image(self):
            FilePath = "images/places/backgrounds/" + self.cfname + ".jpg"
            return FilePath
    
        def unLock(self):
            self.isActive = True
        
        def lock(self):
            self.isActive = False
            
    Locations = []

    Locations.append(place("Banco","banco",False))
    Locations.append(place("Posto de Gasolina","posto_gasolina",False))
    Locations.append(place("Hotel Paraíso","hotel",False))
    Locations.append(place("Minha Casa","casa",False))
    Locations.append(place("Meu Jardim","jardim",False))

    def CodeFriendlyLocationName():
        global Location
        global Locations
        for q in Locations:
            if Location == q.name:
                return q.cfname
        return ""

    def CodeFriendlyLocationNumber():
        global Location
        global Locations
        for q,i in enumerate(Locations):
            if Location == q.name:
                return i
        return -1