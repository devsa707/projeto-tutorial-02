screen TopBar():
    frame:
        background None
        hbox:
            imagebutton:
                hover "ui/map/map_icon.png"
                idle "ui/map/map_icon.png"
                action ToggleVariable("navMenu")
                hovered tt.Action("Abrir o Mapa")
            textbutton "Próximo" action SetVariable("clickType","UI"), Return("next")
            