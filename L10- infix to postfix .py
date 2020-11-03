def isgreater(e1,e2):
def isgreater(e1,e2):
	val = {'+': 1,
		'-': 1,
		'*': 2,
		'/': 2}
	if val[e1]>=val[e2]: return True
	return False


def infixtopostfix(s):
	char = []
	res = ""
	for i in s:
		if i not in "()*/-+":
			res+=i
		elif i in '*/+-':
			while char!=[] and char[-1]!='(' and isgreater(char[-1],i):
				res+=char.pop()
			char.append(i)
		elif i==')':
			while char!=[] and char[-1]!='(':
				res+=char.pop()
			char.pop()
		elif i=='(':
			char.append(i)

	while char:
		k = char.pop()
		res+=k
	print(res)

exp = input("Enter an infix expression : ")
infixtopostfix(exp)
