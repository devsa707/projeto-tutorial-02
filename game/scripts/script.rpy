label start:
    $ Playing = True
    while Playing:
        menu:
            "Escolha um destino:"
            "Parada de Onibus":
                $ Location = "Parada de Onibus"
                
            "Minha Casa":
                $ Location = "Minha Casa"

            "Posto de Gasolina":
                $ Location = "Posto de Gasolina"

            "Meu Jardim":
                $ Location = "Meu Jardim"

            "Hotel Paraíso":
                $ Location = "Hotel Paraíso"

            "Motel":
                $ Location = "Motel"

    return
