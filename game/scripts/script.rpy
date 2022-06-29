label start:
    $ Playing = True
    while Playing:
        window hide
        $ clickType = ""
        $ UIreturn = renpy.call_screen("Main_UI")
        if clickType == "Nav":
            $ Location = UIreturn
    return
