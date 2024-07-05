numero_decimal= input('digite um numero decimal pra saber seu numero Hexadecimal correspondente: ')

numero_decimal = int(numero_decimal)

numero_hexadecimal = hex(numero_decimal)[2:] 
print(f"O número decimal {numero_decimal} em hexadecimal é {numero_hexadecimal}")