screen Main_UI():
    use BG_Image
    use ClickyScreen
    use CharacterScreen
    frame:
        background None
        imagebutton:
            hover "ui/map/map_icon.png"
            idle "ui/map/map_icon.png"
            action ToggleVariable("navMenu")
            hovered tt.Action("Abrir o Mapa")

    if navMenu:
        use NavMap
    if Notification:
        add "ui/notif.png"
    use TipScreen