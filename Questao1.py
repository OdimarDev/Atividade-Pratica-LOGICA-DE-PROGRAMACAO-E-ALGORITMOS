#---------------QUESTÃO 1---------------
print('Bem vindo a loja do Odimar Ribeiro Carvalho')#indentificador pessoal

valor_un = float(input('Qual o valor do produto: ')) #recebe o valor do produto
qtd = int(input('Qual a quantidade do produto: ')) #recebe a quantidade de produtos
valor_ttl = valor_un * qtd #calcula o valor sem desconto
print('O valor sem desconto foi: {:.2f}'.format(valor_ttl))

if (qtd <= 4):
  valor_desc = valor_un * qtd #calcula o valor final com desconto se a quantidade for de até 4 produtos
  print('O valor com desconto foi: R$ {}(desconto 0%)'.format(valor_desc))
elif ((qtd > 4) and (qtd < 20)):
  valor_desc = (valor_un * 0.03 * qtd)#calcula o valor do desconto se a quantidade de produtos for entre 5 e 19
  valor_desc2 = (valor_ttl - valor_desc)#calcula o valor final com desconto se a quantidade de produtos for entre 5 e 19
  print('O valor com desconto foi: R$ {}(desconto 3%)'.format(valor_desc2))
elif ((qtd > 19) and (qtd < 100)):
  valor_desc = (valor_un * 0.06 * qtd)#calcula o valor do desconto se a quantidade de produtos for entre 20 e 99
  valor_desc3 = (valor_ttl - valor_desc)#calcula o valor final com desconto se a quantidade de produtos for entre 20 e 99
  print('O valor com desconto foi: R$ {}(desconto 6%)'.format(valor_desc3))
else: 
  qtd < 99
  valor_desc = (valor_un * 0.1 * qtd)#calcula o valor do desconto se a quantidade de produtos for maior do que 100
  valor_desc4 = (valor_ttl - valor_desc)#calcula o valor final com desconto se a quantidade de produtos for maior do que 100
  print('O valor com desconto foi: R$ {}(desconto 10%)'.format(valor_desc4))
