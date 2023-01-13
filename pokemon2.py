import random

#Requisito 1 - Modelar classe Pokemon
# O trecho de código a seguir é a modelagem da classe Pokemon
# A classe possui os seguintes atributos: nome, tipo, ataque, hp, level e movimento

class Pokemon:  
    def __init__(self, nome, tipo, hp, level):
        self._nome = nome 
        self._tipo = tipo
        self._hp = hp
        self._level = level
        self._movimento = "Ataque rápido"

# Criar 3 subclasses de Pokemon

class Eletrico(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
    
        self._tipo = "elétrico"
        self._movimento = "Choque elétrico"

class Venenoso(Pokemon):
    def __init__(self, nome, especie, hp, level):
        super().__init__(nome, especie, hp, level)
        self._tipo = "venenoso"
        self._movimento = "Picada venenosa"

class Inseto(Pokemon):
    def __init__(self, nome, especie, hp, level):
        super().__init__(nome, especie, hp, level)
        self._tipo = "inseto"
        self._movimento = "Pó do sono"

class Treinador:#3 - Modelar classe Treinador
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons

    def escolherPokemon(self):
        return random.choice(self._pokemons)

#4 - Modelar as subclasses Jogador e Inimigo
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)

    def escolherPokemon(self): 
        while True:
            print(f"Escolha seu pokemon: ")

            for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")

            pokemonEscolhido = input("Digite o número do pokemon escolhido: ")

            #return self._pokemons[int(pokemonEscolhido)-1] <<< Só precisa dessa linha

            #Esses ifs são extra
            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um número inválido")

    def capturarPokemon(self, pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")
    
    def listarPokemons(self):
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")
      

class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
 

    p1Forca = (p1._hp + p1._level) * random.randint(1,3)
    p2Forca = (p2._hp + p2._level) * random.randint(1,3)

    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e força {p2Forca}")

    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {treinador1._nome}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {treinador2._nome}")
    else:
        print("Empate")

pokemonsDisponiveis = [
Eletrico("Pikachu", "Eletrico", 35, 1),
Venenoso("Nidorino", "Venenoso", 70, 16),
Inseto("Parasect", "Inseto", 60, 24),
]

jogador = Jogador("Juliana", [pokemonsDisponiveis[0], pokemonsDisponiveis[1], pokemonsDisponiveis[2]])
inimigo = Inimigo("Joe", pokemonsDisponiveis)


jogador.listarPokemons()
jogador.capturarPokemon(pokemonsDisponiveis[3])
jogador.listarPokemons()