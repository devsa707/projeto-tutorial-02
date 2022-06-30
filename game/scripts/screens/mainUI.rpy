screen Main_UI():
    use BG_Image
    use ClickyScreen
    use CharacterScreen

    if navMenu:
        use NavMap
    use TopBar
    if Notification:
        add "ui/notif.png"
    use TipScreen