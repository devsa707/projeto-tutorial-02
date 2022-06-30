init python:

    class people(object):
        def __init__(self,firstName,surName, cfName,location,isActive):
            self.fName = firstName
            self.sName = surName
            self.cfName = cfName
            self.location = location
            self.isActive = isActive

        @property
        def fullName(self):
            output = self.fName + " " + self.sName
            return output
        
        def unLock(self):
            self.isActive = True
        
        def lock(self):
            self.isActive = False

        @property
        def avatar(self):
            global Location
            global Sequence
            global Chapter
            outputA = "images/avatars/" + self.cfName + "_" + CodeFriendlyLocationName() +".png"
            outputB = "images/avatars/" + self.cfName + "_" + CodeFriendlyLocationName() + "_" + str(Chapter) +"_" + str(Sequence) + ".png"
            if renpy.loadable(outputB):
                return outputB
            return outputA

        @property
        def isLocal(self):
            if self.location == CodeFriendlyLocationNumber():
                return True
            return False


    Characters = []

    Characters.append(people("Lili","Fedida", "lili",4, True))
    Characters.append(people("Frank","Smith", "frank_smith",2, False))
    Characters.append(people("Jenny","Williams", "jenny_williams",0, False))
    Characters.append(people("Zoey","Moore","zoey_moore" ,1, False))