#nome = input ("Insira o nome do seu Guerreiro: ")
#classe = input ("Insira a Classe do seu Guerreiro: ")
#vida = int (input("Defina a quantidade de vida do seu Guerreiro(1 a 100):    "))
#habildiade = input ("Informe o Poder / Habilidade especial do seu Guerreiro: ")
#poder = int (input("Informe o poder de seu Guerreiro(1 a 100):    "))
#
#print (f" o Duelo entre {nome}, de Classe {classe}, com {vida} pontos de vida, com sua habilidade {habildiade} e {poder} pontos de ataque")
#podemos também inserir uma seleção de personagens com suas habilidades e caracteristicas
#Por Exemplo: Might Knight, Cavaleiro, Habilidade Glorious Burst, Vida 98, Poder de Ataque 75, Defesa 32.

personagens = [
    {"nome: " "Might Knight", "classe: " "Cavaleiro", "habilidade: " "Glorious Burst", "vida: " "98", "poder de Ataque" "75", "Defesa" "32"},
    {"nome:" "Golden Potato", "classe:" "Tuberculo Mutante", "habilidade:" "Amido Acido", "vida: " "100", "poder de Ataque: ""35" , "Defesa:""50" },
    {"nome:" "Colossu", "classe: " "Gigante", "habilidade: " "Esbarrão", "vida:" "99", "poder de Ataque:" "62", "Defesa:" "80"},
    {"nome:" "Austalopithecus", "classe: " "Hominideo", "habilidade: " "Primeira Chama", "vida:" "60" , "poder de Ataque:" "72" , "Defesa:" "50" },
]

def selecione_um_personagem(personagens):
    print ("Escolha seu personagem:")
    for i, personagem in enumerate(personagens):
        print(f"{i+1}. {personagem["nome"]}")

    escolha = int(input("Digite o número do personagem: ")) -1
    return personagens [escolha]