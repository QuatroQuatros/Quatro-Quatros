import random
import math
from decimal import Decimal, localcontext

def terminal(numero):
	r = (numero * (1 + numero))/2
	return r

n = float(input('digite o numero: '))
fatorial = 'math.factorial(4)'
algarismos = ['4', 'math.sqrt(4)', 'math.factorial(4)', 'terminal(4)', 'terminal(terminal(4))', 'math.sqrt(terminal(4))', 'terminal(math.factorial(4))', 'terminal(math.sqrt(4))']
operacoes = ['+', '-', '*', '/']

for i in range(100001):
	with localcontext() as ctx:
		ctx.prec = 100
	conta_base = (f'{random.choice(algarismos)} {random.choice(operacoes)} {random.choice(algarismos)} {random.choice(operacoes)} {random.choice(algarismos)} {random.choice(operacoes)} {random.choice(algarismos)}')
	conta_base2 = (f'44 {random.choice(operacoes)} {random.choice(algarismos)} {random.choice(operacoes)} {random.choice(algarismos)}')
	conta_base3 = (f'4 ** {random.choice(algarismos)} {random.choice(operacoes)} {random.choice(algarismos)} {random.choice(operacoes)} {random.choice(algarismos)}')
	conta = Decimal(eval(conta_base))
	conta2 = Decimal(eval(conta_base2))
	conta3 = Decimal(eval(conta_base3))
	print(conta_base, '= ',conta)
	print(conta_base2, '= ', conta2)
	print(conta_base3, '= ', conta3)
	if conta == n:
		print('numero encontrado!')
		print(conta_base, '= ',conta)
		break
	elif conta2 == n:
		print('numero encontrado!')
		print(conta_base2, '= ',conta2)
		break
	elif conta3 == n:
		print('numero encontrado!')
		print(conta_base3, '= ',conta3)
		break
	elif n == 4444:
		print('4444 = 4444')
		break
	else:
		print('não consegui encontrar o numero, tente novamente')