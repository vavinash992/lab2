def postfix(s):
	stack = []
	for i in s:
		if i not in "*/+-":
			stack.append(i)
		else:
			op1 = stack.pop()
			op2 = stack.pop()
			stack.append(op2+i+op1)
	print(''.join(stack))

expression = input("Enter the postfix expression you want to convert : ")
postfix(expression)
