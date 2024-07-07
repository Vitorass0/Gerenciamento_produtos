# Alunos: Vítor Antônio Silvestre Santos
#         Kaynan Andrey Hermano Siqueira

from manager import salvar_produtos, campos 

produto = {'nome', 'preço', 'código'}
produtos = [produto]

#Função para vizualizar os produtos cadastrados.
def vizualizar(produtos):
    if len(produtos) == 0:
        print('Nenhum produto cadastrado')
    else:
        for produto in produtos:
            print(f"Nome:{produto['nome']}, Preço:{produto['preço']} , Código:{produto['código']}")
    

#Função para adicionar produtos.
def adicionar(produtos):
    nome = input('Digite o nome do produto: ')
    preco = str(input('Digite o preço do produto: '))
    codigo = str(input('Digite o código do produto: '))
    if len(nome) == 0  or len(preco) == 0 or len(codigo) == 0:
        print('Algum campo não foi preenchido, por favor tente novamente. ')
    else:
        produtos.append({"nome": nome, "preço": preco, "código": codigo})
        salvar_produtos(produtos)
        print("Produto cadadstrado com sucesso.")


#Função para remover os produtos.
def remover(produtos):
    nome = input("Digite o nome do produto a ser removida: ")
    remover = False
    for produto in produtos:
        if produto['nome'] == nome:
            remover = True
            indice = produtos.index(produto)
            del produtos[indice]
            salvar_produtos(produtos)
            print("Item removido com sucesso!")
        
    if not remover:
        print('Produto não encontrado.')



#Função para editar os produtos.
def editar(produtos):
    nome = input("Digite o nome do produto a ser editada: ")
    encontrado = False
    for produto in produtos:
        if produto['nome'] == nome:
            print('OBS:Se você não quer modificar um dos campos, basta reescrever o valor.\n')
            produto['preço']= str(input('Digite o novo preço do produto:'))
            produto['código'] = str(input('Digite o novo código do produto:'))
            if len(produto['preço']) == 0 or len(produto['código']) == 0:
                print('Algum campo não foi preenchido, por favor tente novamente. ')
            else:
                encontrado = True
                salvar_produtos(produtos)
                print("Item editado com sucesso!")

    if not encontrado:
        print('Produto não encontrado.')

#Função de buscar produtos.
def buscar(produtos):
    print("Escolha por qual característica do produto você quer buscar:")
    print("1.Nome")
    print("2.Preço")
    print("3.Código")
    opcao = input("Escolha uma opção (1, 2, 3): ")
    if opcao == "1":
        caracteristica = "Nome"
    elif opcao == "2":  
        caracteristica = "Preço"
    elif opcao == "3":
        caracteristica = "Código"
    else:
        print("Opção inválida. Tente novamente.")
        return
    valor = input(f"Digite o valor do {caracteristica} a ser buscado: ")
    resultados = [produto for produto in produtos if produto[str(caracteristica.lower())] == valor.lower()]
    if resultados:
        print("Resultados encontrados:")
        for produto in resultados:
            print(f"Nome:{produto['nome']},Preço:{produto['preço']},Código:{produto['código']}")
    else:
        print("Nenhum resultado encontrado.")
