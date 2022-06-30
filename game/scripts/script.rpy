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
        if clickType == "Character":
            $ LabelToCall = UIreturn + "_" + str(Chapter) + "_" + str(Sequence)
            $ LabelDefault = UIreturn + "_default"
            if renpy.has_label(LabelToCall):
                call expression LabelToCall
            else:
                call expression LabelDefault 
        if clickType == "UI":
            if UIreturn == "next":
                $ Next()
            if UIreturn == "Nav":
                $ navMenu = not navMenu
    return
