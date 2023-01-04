class Pokemon():
    def __init__(self, nome, tipo, hp, level):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.level = level




pokemon1 = Pokemon("Pikachu", "Eletrico", "35","1")
pokemon2 = Pokemon("Nidorino", "Venenoso","70","16")
pokemon3 = Pokemon("Parasect", "Inseto", "60", "24")

while True:
    Inicio = input("Escolha um Pokemon. Pikachu is 1, Nidorino is 2 and Parasect is 3 ")
    if Inicio > "3" or Inicio <"1":
        print("Por favor tente novamente")
    else:
        print("Preparar para a batalha")
        match Inicio:
            case "1":
                print(vars(pokemon1))
            case "2":
                print(vars(pokemon2))
            case "3":
                print(vars(pokemon3))
            
        break

    

    