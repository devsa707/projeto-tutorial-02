init python:

    class UIElement(object):
        def __init__(self,x, y, filepath, func, ttip, isActive):
            self.x = x
            self.y = y
            self.filepath = filepath
            self.func = func
            self.ttip = ttip
            self.isActive = isActive

    UIElements = []

    UIElements.append(UIElement(1850,3,"ui/map_icon_small.png", "Nav","Toggle Nav Menu" ,True))
