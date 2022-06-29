screen Main_UI():
    use BG_Image
    use ClickyScreen
    frame:
        background None
        imagebutton:
            hover "ui/map/map_icon.png"
            idle "ui/map/map_icon.png"
            action ToggleVariable("navMenu")
            hovered tt.Action("Abrir o Mapa")

    if navMenu:
        use NavMap
    use TipScreen