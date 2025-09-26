tarefas = []
print('''
         ---Menu---
         Adicionar[1]
         Remover[2]
         Tarefas[3]
         Sair[4]
         ''')

def adicionar_tarefa():
    print('--Adicione a tarefa--')
    nova_tarefa = input('Digite sua tarefa: ').lower()
    tarefas.append(nova_tarefa)
    print(f'Tarefa: {nova_tarefa}, inserida com sucesso ')
    
def remover_tarefa():
    print(tarefas)
    removida = input('Digite a tarefa a ser removida: ').lower()
    if removida in tarefas:
        tarefas.remove(removida)
        print(f'A tarefa "{removida}" foi removida com sucesso.')
    else:
        print(f'Erro: A tarefa "{removida}" não foi encontrada.')   
    
def visualizar_tarefas():
    print('\n--Tarefas--')
    if not tarefas:
        print('Não existem tarefas. ')
    else:
        for i, tarefa in enumerate(tarefas):
            print(f'{i+1}. {tarefa}')
        
           
while True:
    try:
        escolha = int(input("Digite sua escolha: ")) 
        if escolha == 1:
            adicionar_tarefa()       
        elif escolha == 2:
            print('==Remover tarefa==')
            remover_tarefa()
        elif escolha == 3:
            visualizar_tarefas()
        elif escolha == 4:
            print('Obrigado, ate mais!')
            break
        else:
            print('O valor inserido é inválido!')
    except ValueError:
        print('Erro: o valor inserido é inválido')