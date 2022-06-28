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

    Clickies = []

    Clickies.append(clicky("Book","book_01","casa","Object",True,"Green Book"))