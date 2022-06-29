screen ClickyScreen():
    for q in Clickies:
        if q.location == Location:
            if q.isActive:
                imagebutton:
                    hover q.icon
                    idle q.icon
                    focus_mask True
                    action SetVariable("clickType", q.clickType), Return (q.clicked)
                    hovered tt.Action(q.name)
