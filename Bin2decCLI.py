print("------- Programa Bin2Dec -------")
print("\nEste programa converte uma sequência binária de até 8 bits em decimal.\n") 
binario = input("Digite a sequência binária 0 ou 1:")
while True:
    
    if not all(i == '0' or i == '1' for i in binario):
        print("A sequência binária deve conter apenas 0 e 1.")
    elif len(binario) > 8:
        print("A sequência binária deve ter no máximo 8 bits.")
    else:
        break

    binario = input("Digite a sequência binária: ")
            


def bin2dec(binario):
    inverter = binario[::-1]
    decimal = 0
    bit = []
    posicao = 0
    for i in inverter:
        bit.append(int(i)*(2**posicao))
        posicao += 1
    decimal = sum(bit)
    return decimal

print(f"O valor decimal é: {bin2dec(binario)}")