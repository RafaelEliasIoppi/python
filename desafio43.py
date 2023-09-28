peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
     print('IMC: {}  --> "Você está abaixo do peso"'.format(imc))
elif 18.5 < imc < 25:
     print('IMC: {:.2f} --> "Você está no peso ideal"'.format(imc))
elif 25 < imc < 30:
     print('IMC: {:.2f} -->  "Você está com sobrepeso"'.format(imc))
elif 30 < imc < 40:
     print('IMC: {:.2f} -->  "Você está com obesidade"'.format(imc))
else:
     print('IMC: {:.2f} --> "Você está com obesidade morbida"'.format(imc))
