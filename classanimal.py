
class Pokemon:
    def __init__(self, level, nome, hp, ataque):
        self.level = level
        self.nome = nome
        self.nome = hp
        self.nome = ataque
        print("Pokemon criado.")
    def atacar(self):
        print("O Pokemon atacou")
    def checarVantagem(self, pokemoninimigo):
        

        if(pokemoninimigo.tipo == "Fogo"):
            print(f"O pokemon {self.nome} perdeu para o {pokemoninimigo.tipo}")
        elif(pokemoninimigo.tipo == "Agua"):
            print(f"O pokemon {self.nome} ganhou do pokemon de tipo {pokemoninimigo.tipo}")
        elif(pokemoninimigo.tipo == "Eletrico"):
            print(f"O pokemon {self.nome} perdeu para o pokemon de tipo {pokemoninimigo.tipo}")
        elif(pokemoninimigo.tipo == "Grama"):
            print(f"O pokemon {self.nome} perdeu para o  pokemon de tipo {pokemoninimigo.tipo}")
        else:
            print("Tipo de pokemon inválido")
        




class PokemonAquatico(Pokemon):    
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level, nome, hp, ataque)
        self.tipo = "Aquatico"
        print("Pokemon do tipo aquático foi criado.")
    def atacar(self):
        print(f"O Pokemon self.nome usou um jato d'agua para atacar.")

class PokemonEletrico(Pokemon):
    def __init__(self,level, nome, hp, ataque):
        super().__init__(level, nome, hp, ataque)
        self.tipo = "Eletrico"
        print("Pokemon do tipo eletrico foi criado.")
    def atacar(self):
        print(f"O Pokemon self.nome usou um choque para atacar.")

class PokemonGrama(Pokemon):
    def __init__(self, level, nome, hp, ataque):
        super().__init__(level, nome, hp, ataque)
        self.tipo = "Grama"
        print(f"Pokemon do tipo Grama foi criado.")
    def atacar(self):
        print(f"O Pokemon self.nome usou uam chuva de gramas para atacar.")



    

if __name__ == "__main__":
    pokemon1 = Pokemon(10, "pokemon1", 50, 20)
    pokemon2 = PokemonAquatico(15, "Pokemon2", 60, 10)
    pokemon3 = PokemonEletrico(18, "pokemon3", 70, 30)
    pokemon4 = PokemonGrama(20, "pokemon4", 20, 40 )
    pokemon2.atacar()
    pokemon3.atacar()
    pokemon4.atacar()

