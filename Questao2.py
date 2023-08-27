#---------------QUESTÃO 2---------------
subttl = 0#recebe o valor a ser pago pelo cliente
print('Bem Vindo a Pizzaria do Odimar Ribeiro Carvalho')#indentificador pessoal

print('-' * 23, 'Cardápio', '-'*23)#menu
print('|', 'Código ', '|', 'Descrição  ', '|', 'Pizza Média ','|','Pizza Grande ','|')
print('|', '  21   ', '|','Napolitana ','|', '    R$ 20,00', '|', '     R$ 26,00','|')
print('|', '  22   ', '|','Margherita ','|', '    R$ 20,00', '|', '     R$ 26,00','|')
print('|', '  23   ', '|','Calabresa  ','|', '    R$ 25,00', '|', '     R$ 32,50','|')
print('|', '  24   ', '|','Toscana    ','|', '    R$ 30,00', '|', '     R$ 39,00','|')
print('|', '  25   ', '|','Portuguesa ','|', '    R$ 30,00', '|', '     R$ 39,00','|')
print('-'*56)

while True:
  tam = input('Qual o tamanho de pizza que deseja (M/G): ')
  if tam == 'M' or tam == 'G':
    cod = input('Entre com o código desejado: ')
    if cod == '21':
      if tam == 'M':
        subttl += 20
      if tam == 'G':
        subttl += 26
    elif cod == '22':
      if tam == 'M':
        subttl += 20
      if tam == 'G':
        subttl += 26
    elif cod == '23':
      if tam == 'M':
        subttl += 25
      if tam == 'G':
        subttl += 32
    elif cod == '24':
      if tam == 'M':
        subttl += 30
      if tam == 'G':
        subttl += 39
    elif cod == '25':
      if tam == 'M':
        subttl += 30
      if tam == 'G':
        subttl += 39
    else:
      print('Opção invalida')
      continue#verifica se o usuario digitou um código valido(volta para o começo do while)
    resposta = input('Deseja pedir mais alguma coisa? (s/n)')
    if resposta == 's':
      continue#verifica se o cliente deseja fazer um novo pedido(volta para o começo do while)
    else:
      print('O total a ser pago é: {:.2f}' .format(subttl))
      break#encerra o while
      
  else:
     print('Opção invalida')
     continue#verifica se o usuario digitou um tamanho valido(volta para o começo do while)
