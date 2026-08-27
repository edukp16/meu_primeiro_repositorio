import time
meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            'VDD': 'abreviação da palavra "verdade"',
            'BISCOITAR': 'postar algo apenas para chamar a atenção',
            'HATER': 'pessoa que está constantemente criticando os outros',
            'VLW': 'abreviação da palavra "valeu"'
            }
print('Bem vindo ao tradutor de palavras modernas!')
while True:
    time.sleep(2)
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print('Palavra não encontrada')
