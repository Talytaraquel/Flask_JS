cont = 0

novo = input("Deseja entrar na festa? (sim/não)").upper()

while novo == "SIM":
    n=int(input("Digite sua idade:"))

    if n >= 16:
        print("Bem-vindo a festa!")
        cont+=1
    else:
        print("Você é menor de idade! Não pode entrar na festa :(")

    perg = input("Você quer vê quantas pessoastem a na festa?(sim/não)").upper()

    if perg == 'SIM':
        print(f"Já tem {cont} na festa!")
    novo = input("Deseja entrar na festa? (sim/não)").upper()


