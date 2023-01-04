
import random
listaNomes = ("Jorge", "Maria", "Lucas", "Joana")

Pokemons = ("Pikachu", "Nidorino", "Parasect")

class Treinador:
    def __init__(self,nome, pokemons=[]):
        self._pokemons = pokemons
        if nome == "":
            self._nome = random.choice(listaNomes)
        else:
            self._nome = "nome"

    def mostrarpokemons(self):
        print(self._pokemons)

    def capturarpokemons(self):
        if len(self._pokemons) < 6:
            self._pokemons.append(f"Pokemon {random.randinit(1,155)}")
        else:
            print("O treinador já tem pokemons demais")

class Jogador(Treinador):
    def __init__(self, nome ='', pokemons=[]):
        super().__init__(nome,pokemons)

        if(len(self._pokemons) == 0):
            print('''Escolha um dos seguintes pokemons:
            1- Pikachu
            2- Nidorino
            3- Parasect''')
            pokemonEscolhido = input("Sua escolha:")

            match pokemonEscolhido:
                case 1:
                    self._pokemons.append("Pikachu")
                    print("Voce escolheu o Pikachu")
                case 2:
                    self._pokemons.append("Nidorino")
                    print("Voce escolheu o Nidorino")
                case 3:
                    self._pokemons.append("Parasect")
                    print("Voce escolheu o Parasect")
                case _:
                    print("Você não escolheu um pokemon válido.")

class Inimigo(Treinador):
    def __init__(self,nome="", pokemons=[]):
        super().__init__(nome,pokemons)

if __name__ == "__main__":
    
    jogador = Jogador()
    inimigo = Inimigo()

    jogador.mostrarPokemons()
