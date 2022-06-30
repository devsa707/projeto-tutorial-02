init python:

    class place(object):
        def __init__(self,name,cfName,isActive):
            self.name = name
            self.cfName = cfName
            self.isActive = isActive

        @property
        def bg_image(self):
            FilePath = "images/places/backgrounds/" + self.cfName + ".jpg"
            if renpy.loadable(FilePath):
                return FilePath
            else:
                return "images/places/backgrounds/default.jpg"
    
        def unLock(self):
            self.isActive = True
        
        def lock(self):
            self.isActive = False
            
        @property
        def mapIcon(self):
            global Chapter
            global Sequence
            defOutput = "images/places/icons/none.png"
            output = "images/places/icons/" + self.cfName + ".png"
            altOutput = "images/places/icons/" + self.cfName + "_" + str(Chapter) + "_" + str(Sequence) + ".png"
            if renpy.loadable(altOutput):
                return altOutput
            if renpy.loadable(output):
                return output
            return defOutput

    Locations = []

    Locations.append(place("Parada de Onibus","onibus",True))
    Locations.append(place("Posto de Gasolina","posto_gasolina",True))
    Locations.append(place("Hotel Paraíso","hotel",True))
    Locations.append(place("Minha Casa","casa",True))
    Locations.append(place("Meu Jardim","jardim",True))

    def CodeFriendlyLocationName():
        global Location
        global Locations
        for q in Locations:
            if Location == q.name:
                return q.cfName
        return ""

    def CodeFriendlyLocationNumber():
        global Location
        global Locations
        for i,q in enumerate(Locations):
            if Location == q.name:
                return i
        return -1

    def Next():
        global Chapter
        global Sequence
        Sequence += 1