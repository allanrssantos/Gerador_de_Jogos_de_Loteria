from random import sample

jogos = int(input('Quantos jogos você quer fazer? '))
numeros = int(input('Quantos números em cada aposta (Ex.: mega-sena: min: 06 e max: 15)? '))
dezena_final = int(input('Qual a dezena final do jogo (Ex.: mega-sena: 60)? '))
for _ in range(jogos):
    print(f'\nJOGO {_+1}: ', end='')
    for jogo in sorted(sample(range(1, dezena_final + 1),numeros)):
        print(jogo, end=' ') 