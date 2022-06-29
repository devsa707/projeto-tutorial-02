label start:
    $ Playing = True
    while Playing:
        window hide
        $ Notification = False
        $ clickType = ""
        $ UIreturn = renpy.call_screen("Main_UI")
        if clickType == "Nav":
            $ Location = UIreturn
        if clickType == "Object":
            call expression UIreturn
    return
