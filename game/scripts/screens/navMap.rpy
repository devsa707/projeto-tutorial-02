screen NavMap():
    frame:
        background None
        yalign 1
        xalign 1
        xsize 1000
        ysize 600
        add "ui/map/map_bg.png"
        for q in Locations:
            if q.isActive:
                imagebutton:
                    hover q.mapIcon
                    idle q.mapIcon
                    focus_mask True                    
                    action SetVariable("clickType", "Nav"), ToggleVariable("navMenu"), Return (q.name)
                    hovered tt.Action("Ir para " + q.name)