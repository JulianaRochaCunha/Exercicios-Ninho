#Requisito 1 - Modelar classe Pokemon
# A classe possui os seguintes atributos: nome, tipo, ataque, hp, level e movimento
import random
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
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "venenoso"
        self._movimento = "Picada venenosa"

class Inseto(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "inseto"
        self._movimento = "Pó do sono"

class Grama(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "grama"
        self._movimento = "Lança grama"

class Fogo(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "Fogo"
        self._movimento = "Poder solar"

class Psiquico(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "Psiquico"
        self._movimento = "Controle da mente"

class Lutador(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
        self._tipo = "Lutador"
        self._movimento = "Espirito vital"



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


            if (pokemonEscolhido.isnumeric()):
                if (int(pokemonEscolhido) <= len(self._pokemons)):
                    return self._pokemons[int(pokemonEscolhido)-1]
                else:
                    print("Você escreveu um número maior do que o disponível.")
            else: 
                print("Você escreveu um número inválido")

    def capturarPokemon(self, pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você conseguiu capturar o {pokemonCapturado._nome}")
    
    def listarPokemons(self):
        print("Sua lista de pokemons: ")
        for i in range(len(self._pokemons)):
                print(f"{i+1}. {self._pokemons[i]._nome}")
    
    def salvarPokemon(self, pokemonSalvo):
        self._pokemons.append(pokemonSalvo)
        print(f"Você salvou o {pokemonSalvo._nome}")
      

class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)


def batalhaDePokemon(treinador1, treinador2):

    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()
 

    print(f"{p1._nome} atacou com {p1._movimento}")
    print(f"{p2._nome} atacou com {p2._movimento}")

    if (p1._hp > p2._hp):
        print(f"O vencedor foi {p1._nome} do treinador {treinador1._nome}")
    elif (p1._hp < p2._hp):
        print(f"O vencedor foi {p2._nome} do treinador {treinador2._nome}")
    else:
        print("Empate, nao houve um vencedor")

pokemonsDisponiveis = [
Eletrico("Pikachu", "Eletrico", 35, 1),
Venenoso("Nidorino", "Venenoso", 70, 16),
Inseto("Parasect", "Inseto", 60, 24),
Grama("Bulbasaur", "Grama", 45, 1),
Fogo("Charmander", "Fogo", 39, 1),
Psiquico("Alakazam", "psiquico", 55,36),
Lutador("Mankey", "Lutador", 40,1)
]


nomeJogador = input("Digite seu nome: ")

print("Escolha seu Pokemon inicial: ")

for i in range(7):
    print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")

pokemonInicial = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]

print(f"O pokemon escolhido foi o {pokemonInicial._nome}")

jogador = Jogador("Juliana", [pokemonsDisponiveis[0], pokemonsDisponiveis[1], pokemonsDisponiveis[2], pokemonsDisponiveis[3],
pokemonsDisponiveis[4], pokemonsDisponiveis[5], pokemonsDisponiveis[6]])
inimigo = Inimigo("Joe", pokemonsDisponiveis)


while True:

    print("""
    Escolha o que você quer fazer:
    1. Ver seus pokemons
    2. Capturar um novo Pokemon
    3. Batalhar contra um oponente
    4. Salvar um pokemon
    0. Fim de jogo
    """)

    menu = input("Digite a opção escolhida:")

    if menu =="0":
        print("Fim de jogo.")
        break
    elif menu=="1":
        jogador.listarPokemons()
        print("Veja seus pokemons:")
    elif menu=="2":
        print("Capturando um pokemon: ")
    
        for i in range(len(pokemonsDisponiveis)):
            print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")
        
        capturado = pokemonsDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)

    elif menu =="3":
        batalhaDePokemon(jogador,inimigo)

    elif menu == "4":

        for i in range(len(pokemonsDisponiveis)):
            print(f"{i+1}. {pokemonsDisponiveis[i]._nome}")
        salvo = pokemonsDisponiveis[int(input("Digite o pokemon a ser salvo: "))-1]
        jogador.salvarPokemon(salvo)

    else:
        print("Deu algo errado, tente novamente.")
    

        
