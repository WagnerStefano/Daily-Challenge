""" import psycopg2

conn = psycopg2.connect(
    database = "rpg.sql",
    user=""
    password = ""
    host = ""
    port = ""
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE personagens (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50),
        classe VARCHAR(50),
        habilidade VARCHAR(50),
        vida INTEGER,
        poder INTEGER,
        defesa INTEGER,
        inventario TEXT[]
    );
""")

conn.commit()
conn.close() """

def duelo(personagem1, personagem2):
  """Simula um duelo entre dois personagens.

  Args:
    personagem1: Um dicionário representando o primeiro personagem.
    personagem2: Um dicionário representando o segundo personagem.

  Returns:
    O nome do vencedor do duelo.
  """

  while personagem1['vida'] > 0 and personagem2['vida'] > 0:
    personagem2['vida'] -= personagem1['poder']
    if personagem2['vida'] <= 0:
      return personagem1['nome']
    personagem1['vida'] -= personagem2['poder']
    if personagem1['vida'] <= 0:
      return personagem2['nome']

# Coletando dados dos personagens
personagem1 = {}
personagem1['nome'] = input("Insira o nome do primeiro Guerreiro: ")
# ... (coletar os demais dados para o personagem1)

personagem2 = {}
personagem2['nome'] = input("Insira o nome do segundo Guerreiro: ")
# ... (coletar os demais dados para o personagem2)

# Iniciando o duelo
vencedor = duelo(personagem1, personagem2)
print(f"O vencedor do duelo é: {vencedor}")