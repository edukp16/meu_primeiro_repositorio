import random
import time
print('Bem vindo ao criador de senhas!')
time.sleep(1)
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho_senha = int(input('Quantos caracteres sua senha terá?'))
senha = ""
for i in range(tamanho_senha):
    senha += random.choice(caracteres)
    
print('Sua senha gerada é: ', senha)
