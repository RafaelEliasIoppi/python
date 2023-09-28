preco = float(input('Digite o preço do produto: '))
print(""" CONDIÇÕES DE PAGAMENTO:
[ 1 ] A VISTA DINHHEIRO/CHeQUE
[ 2 ] A VISTA NO CARTÃO
[ 3 ] PARCELADO NO CARTÁO""")
pgto = int(input('Escolha a forma de pagamento: '))
if pgto == 1:
    dinheiro = preco - (preco * 0.1) # 10% DESCONTO
    print('Você tem um desconto de \033[4m10%\033[m do valor de: R$ \033[1;34m{}\033[m TOTAL A PAGAR =====> R$ \033[1;35m{}\033[m'.format(preco * 0.1, dinheiro))
elif pgto == 2:
    cartao = preco - (preco * 0.05) # 5% DESCONTO
    print('Você tem um desconto de \033[4m5%\033[m do valor de: R$ \033[1;34m{}\033[m TOTAL A PAGAR ====> R$ \033[1;35m{}\033[m'.format(preco * 0.5, cartao))
elif pgto == 3:
      parcela = int(input('INFORME O NÚMERO DE PARCELAS: '))
      if parcela > 2:
          juros = preco + (preco * 0.2)
          print('O valor da parcela será de: {:.2f} '.format((preco * 0.2) / parcela), end=' ')
          print('Você terá um acréscimo de \033[4m20%\033[m no valor de: R$ \033[34m{:.2f}\033[m O valor total do produto será de: R$ \033[35m{:.2f}\033[m'.format(preco * 0.2, juros))
      else:
          print('O valor da parcela será de: {:.2f} '.format((preco * 0.2) / parcela), end=' ')
          print(' Irá pagar o preço normal: R$ {:.2f}'.format(preco))
else:
    print('DIGITE UMA OPÇÃO VÁLIDA')



