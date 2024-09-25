import funcoes

produtos = []
def menu():
    opcao_escolhida = opcao()
    while opcao_escolhida != 'S':
        if opcao_escolhida == 'V':
            funcoes.vizualizar(produtos)
        elif opcao_escolhida == 'A':
             funcoes.adicionar(produtos)
        elif opcao_escolhida == 'R':
             funcoes.remover(produtos)
        elif opcao_escolhida == 'E':
            funcoes.editar(produtos)
        elif opcao_escolhida == 'B':
             funcoes.buscar(produtos)
        else:
            print('Opção inválida.')
        opcao_escolhida = opcao()
  

def opcao():
    print('\n')
    print('[V]izualizar produtos cadastrados')
    print('[A]dicionar um produto')
    print('[R]emover um produto')
    print('[E]ditar um produto')
    print('[B]uscar um produto')
    print('[S]air')
    return input('Escolha a opção desejada: ').upper()

menu()