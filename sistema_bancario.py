menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 700
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:
	opcao = input(menu)

	if opcao == "d":
		valor = float(input("Informe o valor do depósito: "))

		if valor > 0:
			saldo += valor
			extrato += f"Depósito: R$ {valor:.2f}\n"

		else:
		 print("Operação falhou! O valor informado é inválido.")
   	

	elif opcao == "s":
		valor = float(input("Informe o valor do saque: "))

		excedeu_saldo = valor > saldo
		excedeu_limite = valor > limite	
		excedeu_saques = numero_saques >= LIMITE_SAQUES
        

		if excedeu_saldo:
			print("Operação falhou! Você não tem saldo insuficiente.")

		elif excedeu_limite:
			print("Operação falhou! O valor de saque excedeu o limete.")

		elif excedeu_saques:
			print("Operação falhou! Número máximo  de saques foi excedido.")

		elif valor > 0:
			saldo -= valor
			extrato +=f"Saque: R$ {valor:.2f}\n"
			numero_saques += 1

		else:
			print("Operação fahou! O valor infomado é inválido.")

	elif opcao == "e":
		print("\n_-*-__-*-__-*-__-*-_ EXTRATO _-*-__-*-__-*-__-*-_")
		print("Não foram realizadas movimentações " if not extrato else extrato)
		print(f"\nSaldo: R${saldo:.2f}")
		print("_-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-__-*-_")

	elif opcao == "q":

		break
        

	else:
		print("Operação inválida, por favor selecione novamente  a operação  desejada.")

print("Obrigado por utilizar nosso sistema de banco. ;)")
