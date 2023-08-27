#---------------QUESTÃO 4---------------

listaProdutos = [] #lista onde os produtos cadastrados serão regitrados

#--------------COMEÇO CADASTRARPRODUTO--------------
def cadastrarProduto(cod):
  print('Bem Vindo ao cadastro de produtos')
  print('O código do produto a ser cadastrado é: {}'.format(cod))
  nome = input('Digite o nome do produto: ')
  fabricante = input('Digite o fabricante do produto: ')
  valor = float(input('Digite o valor do produto: '))
  dicionarioProduto = {'Código'    : cod,
                       'nome'      : nome,
                       'fabricante': fabricante,
                       'valor'     : valor}
  listaProdutos.append(dicionarioProduto.copy())#adiciona os produtos a lista
#--------------FIM CADASTRARPRODUTO--------------

#------------COMEÇO CONSULTARPRODUTO------------
def consultarProduto():
  while True:
    try:#try para evitar erro quando o usuario digitar um valor que não seja valido
      print('Bem Vindo ao CONSULTAR de produtos')
      consultar = int(input('Entre com a opção desejada:\n1-Cosultar Todos os Produtos\n2-Consultar Produto por Código\n3-Consultar Produto(s) por Fabricante\n4-Retonar\n>> '))
      if consultar == 1: 
        print('Bem vindo a consultar TODOS')
        for produto in listaProdutos: #selecionar cada dicionario da minha lista de produtos
          for key, value in produto.items():#selecionar cada conjunto chave : valor do dicionario
            print('{} : {}'.format(key, value))
      elif consultar == 2:
        print('Bem vindo a consultar PRODUTO POR CÓDIGO')
        entrada = int(input('Digite o código desejado: '))
        for produto in listaProdutos:#selecionar cada dicionario da minha lista de produtos
          if(produto['Código'] == entrada): 
            for key, value in produto.items(): #selecionar o conjunto chave : valor do dicionario
              print('{} : {}'.format(key, value))
      elif consultar == 3:
        print('Bem vindo a consultar PRODUTO(s) POR FABRICANTE')
        entrada = input('Digite o fabricante desejado: ')
        for produto in listaProdutos:#selecionar cada dicionario da minha lista de produtos
          if(produto['fabricante'] == entrada): 
            for key, value in produto.items(): #selecionar o conjunto chave : valor do dicionario
              print('{} : {}'.format(key, value))
      elif consultar == 4:
        return
      else:
        print('Opção invalida')
    except ValueError:
      print('Opção invalida')
#-------------FIM CONSULTARPRODUTO--------------

#-------------COMEÇO REMOVERPRODUTO-------------
def removerProduto():
  print('Bem Vindo ao REMOVER de produtos')
  entrada = int(input('Digite o código do produto que deseja remover: '))
  for produto in listaProdutos:#selecionar cada dicionario da minha lista de produtos
    if(produto['Código'] == entrada): 
      listaProdutos.remove(produto) #selecionar o conjunto chave : valor do dicionario
#-------------FIM REMOVERPRODUTO-------------

#-------------COMEÇO MAIN---------------
print('Bem Vindo ao Controle de Estoque da Mercearia do Odimar Ribeiro Carvalho')
codigoprod = 0
while True:
  try:#try para evitar erro quando o usuario digitar um valor que não seja valido
    opcao = int(input('Digite a opção desejada:\n1-Cadastrar Produto\n2-Consultar Produto\n3-Remover Produto\n4-Sair\n>>'))
    if opcao == 1:
      codigoprod = codigoprod + 1
      cadastrarProduto(codigoprod)
    elif opcao == 2:
      consultarProduto()
    elif opcao == 3:
      removerProduto()
    elif opcao == 4:
      print('Finalizado')
      break
    else:
      print('Opção invalida')
  except ValueError:
    print('Opção invalida')
#-------------FIM MAIN---------------
