screen TopBar():
    frame:
        background None
        for q in UIElements:
            if q.isActive:
                imagebutton:
                    xpos q.x
                    ypos q.y
                    hover q.filepath
                    idle q.filepath
                    action SetVariable("clickType","UI"), Return(q.func)
                    hovered tt.Action(q.ttip)
                
            