#---------------QUESTÃO 3---------------

#---------------COMEÇO VOLUMEFEIJOADA---------------
def volumeFeijoada():
  while True:
    try:#try para evitar erro quando o usuario digitar um valor não numérico
      volFeijoada = int(input('Entre com a quantidade que deseja(ml):'))
      if volFeijoada > 299 and volFeijoada < 5001: #verifica se o usuario digitou um volume dentro da faixa com a ql o restaurante trabalha
        return volFeijoada * 0.08
      else:
        print('Não aceitamos porções menores que 300ml ou maiores 5l. Tente novamente!') 
    except ValueError:
      print('Digite um valor numérico.')
#---------------FIM VOLUMEFEIJOADA---------------

#---------------COMEÇO OPCAOFEIJOADA---------------
def opcaoFeijoada():
  print('b- Básica (Feijão + paiol + costelinha')
  print('p- Premiun (Feijão + paiol + costelinha + partes de porco')
  print('s- Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon')
  while True:#retorna o multiplicador de acordo com a opção selecionada
    opcaoF = input('Entre com a opção de Feijoada:\n>> ')
    if opcaoF == 'b': 
      return 1.00
    elif opcaoF == 'p':
      return 1.25
    elif opcaoF == 's':
      return 1.50
    else:
      print('Escolha uma opção valida: ')
      continue #retorna para o começo da while
#---------------FIM OPCAOFEIJOADA---------------

#---------------COMEÇO ACOMPANHAMENTOFEIJOADA---------------
def acompanhamentoFeijoada():
  print('0- não desejo mais acompanhamentos (encerrar pedido)')
  print('1- 200g de arroz')
  print('2- 150g de farofa especial')
  print('3- 100g de couve cozida')
  print('4- 1 laranja descascada')
  soma = 0;
  
  while True: #retorna o valor do adicional de acordo com a opção selecionada
    try:#try para verificar se o usuario digitou uma opção valida
      acompF = int(input('Deseja mais algum acompanhamento:\n>> '))
      if acompF == 1:
        soma += 5.00
        continue
      elif acompF == 2:
        soma += 6.00
        continue
      elif acompF == 3:
        soma += 7.00
        continue
      elif acompF == 4:
        soma += 3.00
        continue
      elif acompF == 0:
        break
      else:
        print('Digite uma opção valida:')
      continue
    except ValueError:
      print('Digite uma opção valida:')
  return soma
#---------------COMEÇO ACOMPANHAMENTOFEIJOADA---------------

#---------------COMEÇO MAIN---------------
print('Bem Vindo ao Programa de Feijoada do Odimar Ribeiro Carvalho')
volume = volumeFeijoada() #subtotal do multiplicador do volume
opcao = opcaoFeijoada() #subtotal do multiplicador da opção
acomp = acompanhamentoFeijoada() #subtotal do acompanhamento
total = volume * opcao + acomp #total a ser pago pelo usuario
#print('{}'.format(volume))
#print('{}'.format(opcao))
#print('{}'.format(acomp))
print('O valor total foi de: {}'.format(total))
#---------------FIM MAIN---------------
