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
        def Avatar(self):
            global Location
            Output = "images/avatars/" + self.cfName + "_" + CodeFriendlyLocationName() +".png"

    Characters = []

    Characters.append(people("Davey","Jones", "davey_jones",0, True))
    Characters.append(people("Frank","Smith", "frank_smith",2, True))
    Characters.append(people("Jenny","Williams", "jenny_williams",0, True))
    Characters.append(people("Zoey","Moore","zoey_moore" ,1, True))