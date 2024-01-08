import random
from palavras import palavras

userKey = [];
chances = 4;
dicas = 2;
chutes = 1;
ganhou = False;

def randomizerWord():
    randomWord = random.randint(0, len(palavras)-1);
    return palavras[randomWord];

palavra = randomizerWord();
while True:
    ganhou = True;
    for letra in palavra:
        if letra.lower() in userKey:
            print(letra, end=' ');
        elif letra == '-':
            print('-', end=' ');
            userKey.append('-');
        elif letra == ' ':
            print(' ', end=' ');
        else:
            print('_', end=' ');
    
    print('\n' + '\033[94m' + f"Você tem {chances} chances, {dicas} dicas e {chutes} chutes" + '\033[0m');

    tentativa = input("Digite uma Letra, digite dica ou digite chute: ");

    if tentativa.lower() == 'chute' and chutes != 0:
        tentativaChute = input("Digite a palavra: ");
        while type(tentativaChute) != str or len(tentativaChute) > len(palavra):
            tentativaChute = input("Digite a palavra novamente: ");
        if tentativaChute.lower() == palavra.lower():
            break;
        else:
            ganhou = False;
            # chutes -= 1;
            print('\033[91m' + "Você errou!" + '\033[0m');
            break;
    
    elif tentativa == 'dica':
        if dicas == 0:
            print('\033[91m' + 'Você está sem dicas!'+'\033[0m');
        else:
            dicas -= 1;
            available_tips = [letra for letra in palavra.lower() if letra not in userKey]
            
            if available_tips:
                tip = random.choice(available_tips)
                userKey.append(tip)
                print('\033[95m' + f"Dica: '{tip.upper()}'" + '\033[0m')
            else:
                print("Você já usou todas as letras disponíveis como dicas.")
    
    elif len(tentativa) != 1 or type(tentativa) != str:
        print('\033[91m' + 'Digite algo condizente a brincadeira!'+'\033[0m');

    
    else:
        userKey.append(tentativa.lower());
        if tentativa.lower() not in palavra.lower():
            chances -= 1;
    
    for letra in palavra:
            if letra.lower() not in userKey:
                ganhou = False;
    
    if chances == 0 or ganhou:
        break;

if ganhou:
    print("\033[92m" + f'Parabéns, Você acertou! A palavra era {palavra}'+ '\033[0m');
else:
    print('\033[91m' + f'Parabéns, você errou! a palavra era {palavra}' + '\033[0m');