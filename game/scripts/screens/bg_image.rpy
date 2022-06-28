screen BG_Image():
    $ Background = "images/places/backgrounds/default.jpg"
    for q in Locations:
        if q.name == Location:
            $ Background = q.bg_image                
    add Background