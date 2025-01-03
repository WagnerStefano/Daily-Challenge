def gerenciador_inventario():
    inventario = []  # Inicializa o inventário como uma lista vazia

    while True: # Loop principal para interação contínua
        acao = input("Digite a ação ('adicionar', 'remover', 'listar' ou 'sair'): ").lower()

        if acao == 'adicionar':
            item = input("Digite o nome do item a adicionar: ")
            inventario.append(item)
            print("Item adicionado com sucesso.")
        elif acao == 'remover':
            item = input("Digite o nome do item a remover: ")
            if item in inventario:
                inventario.remove(item)
                print("Item removido com sucesso.")
            else:
                print("Erro: Item não encontrado no inventário.")
        elif acao == 'listar':
            if inventario: # Verifica se a lista não está vazia
                print("Inventário:")
                for item in inventario:
                    print(f"- {item}")
            else:
                print("Inventário vazio.")
        elif acao == 'sair':
          break # Sai do loop e encerra o programa
        else:
            print("Ação inválida. Tente novamente.")

# Chama a função principal para iniciar o gerenciador
gerenciador_inventario()