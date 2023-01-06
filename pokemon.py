
import random
class Pokemon():
    def __init__(self, nome, tipo, hp, level):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.level = level
        self.movimento = "Ataque rápido"


class Eletrico(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "Eletrico"
        self._movimento ="Choque eletrico"

class Venenoso(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "Venenoso"
        self._movimento ="Picada venenosa"

class Inseto(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "Parasect"
        self._movimento ="Pó do sono"

class Treinador:
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolhaumpokemon(self):
        return random.choice(self._pokemons)

class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

def batalhadepokemon(treinador1, treinador2):

    p1 = treinador1._escolhaDoPokemon()
    p2 = treinador2._escolhaDoPokemon()
    

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1força}")
    print(f"{p2._nome} atacou com {p2._movimento} e forca {p2força}")
    

    p1força = p1._hp
    p2força = p2._hp
    

    print(f"O vencedor foi {p1.nome}")

    if (p1._hp) > (p2._hp):
        print(f"O vencedor foi {p1._hp}")

    elif (p2._hp) > (p1._hp):
        print(f"O vencedor foi {p2._hp}")

    else:
        print("Empate")

pokemon1 = Eletrico("Pikachu", "Eletrico", 35,1)
pokemon2 = Venenoso("Nidorino", "Venenoso",70,16)
pokemon3 = Inseto("Parasect", "Inseto", 60, 24)

jogador = Jogador ("Juliana", [pokemon1])
inimigo = Inimigo ("Joe", [pokemon2])

batalhadepokemon(jogador,inimigo)

    


    

    