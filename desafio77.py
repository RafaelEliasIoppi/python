palavras = ('Gratis', 'Mercado', 'Programar', 'Cidade', 'Industria',
            'Brasil', 'Quimica', 'Laboratorio','Vida', 'Rafael')
for p in palavras:
    print(f'\nNa palavra: {p} temos as vogais ----> ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
