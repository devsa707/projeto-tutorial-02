init python:

    class clicky(object):
        def __init__(self,name,cfName, location, clickType, isActive, tip):
            self.name = name
            self.cfName = cfName
            self.location = location
            self.clickType = clickType
            self.isActive = isActive
            self.tip = tip

        @property
        def image(self):
            output = "images/clickys/" + self.cfName + "_" + self.location + ".png"
            return output

        @property
        def icon(self):
            global Chapter
            global Sequence
            outputA = "images/Items/" + CodeFriendlyLocationName() + "_" + self.cfName + ".png"
            outputB = "images/Items/" + CodeFriendlyLocationName() + "_" + self.cfName + "_" + str(Chapter) + "_" + str(Sequence) + ".png"
            if renpy.loadable(outputB):
                return outputB
            if renpy.has_label(outputA):
                return outputA
            return "NoLabel"
            
        @property
        def clicked(self):
            global Chapter
            global Sequence
            outputA = self.cfName + "_Clicked"
            outputB = self.cfName + "_" + str(Chapter) + "_" + str(Sequence)
            if renpy.has_label(outputB):
                return outputB
            return outputA

    Clickies = []

    Clickies.append(clicky("Livros","livro","Minha Casa","Object",True,"Ler"))
