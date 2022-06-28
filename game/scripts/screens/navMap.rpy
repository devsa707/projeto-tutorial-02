screen NavMap():
    frame:
        background None
        yalign 0.5
        xalign 0.5
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
                    hovered tt.Action("Go to " + q.name)