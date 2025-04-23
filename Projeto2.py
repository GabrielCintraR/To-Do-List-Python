#To-Do List Simples em Python!

tarefas = [] #Lista onde tarefas serão guardadas

#Menu simples com algumas opções
while True:
    print("\n --- MENU ---")
    print("1 - Ver Tarefas")
    print("2 - Adicionar Tarefas")
    print("3 - Fechar Programa")

    #Input onde recebe a opção do usuário
    opcao = input("Escolha uma opção: ") 

    if opcao == "1":
        print("\n --- SUAS TAREFAS ---")
        if len(tarefas) == 0: #Se a lista estiver vazia
            print("Nenhuma tarefa encontrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}") #Vai adicionando tarefas e somando com +1
    elif opcao == "2":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa Adicionada")
    elif opcao == "3":
        print("Programa Encerrado")
        break
    else:
        print("Opção Inválida")