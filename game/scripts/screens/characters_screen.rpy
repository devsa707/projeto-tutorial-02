screen CharacterScreen():
    for q in Characters:
        if q.isActive and q.isLocal:
            imagebutton:
                hover q.avatar
                idle q.avatar
                focus_mask True
                action SetVariable("clickType", "Character"), Return (q.cfName)
                hovered tt.action(q.fullName)