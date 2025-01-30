import random

# Gerando um número aleatório entre 1 e 100
randomNumber = random.randint(1, 100)
numberTry = 0
maxAttempts = 5  # Número máximo de tentativas

while numberTry < maxAttempts:
    try:
        number = int(input(f"Tentativa {numberTry + 1}/{maxAttempts} - Digite um número entre 1 e 100: "))
    except ValueError:
        print("❌ Entrada inválida! Digite um número válido.")
        continue  # Se o usuário digitar algo inválido, volta ao início do loop

    numberTry += 1  # Incrementa o número de tentativas

    if number == randomNumber:
        print(f"🎉 Parabéns! Você acertou! O número era {randomNumber}.")
        break  # Sai do loop imediatamente se acertar
    elif numberTry < maxAttempts:  # Só dá dicas se ainda houver tentativas restantes
        if number < randomNumber:
            print("📈 Tente um número maior.")
        else:
            print("📉 Tente um número menor.")

# Se o jogador não acertou dentro das tentativas, exibe a resposta correta
if number != randomNumber:
    print(f"😞 Fim de jogo! O número correto era {randomNumber}.")
