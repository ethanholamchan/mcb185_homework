# Fibonacci

def fibonacci10():
	num1 = 0
	num2 = 1
	num3 = 0
	print(num1)
	print(num2)
	for i in range(8):
		num3 = num1 + num2
		num1 = num2
		num2 = num3
		print(num2)
fibonacci10()
		
