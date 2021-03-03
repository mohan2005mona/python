class stack:
	def __init__(self):
		self.elements = [ ]
	
	def push(self,element):
		self.elements.append(element)
	
	def pop(self):
		print("performing pop operation",self.elements[-1])
		del self.elements[-1]
	
	def peek(self):
		return self.elements[-1]
	
	def is_empty(self):
		return self.elements == []

def get_matching_brackets(c):
	rules= {
			'}' : '{',
			')' : '(',
			']' : '[',
	}
	#return {'}' : '{',	')' : '(',']' : '[',}[c]
	return rules[c]

	
def is_balanced(brackets):
	b_stack=stack()
	for bracket in brackets:
		if bracket in '({[':
			b_stack.push(bracket)
		else:
			try:
				if b_stack.peek() == get_matching_brackets(bracket):
					b_stack.pop()
			except IndexError:
				return False
	return b_stack.is_empty()

def main():
	tests= ['{}[]()','{[]}(()']
	
	for test in tests:
		if is_balanced(test):
			print(f'{test} expression is valid')
		else:
			print(f"{test} Expression is invalid")

if __name__ == '__main__':
	main()






				






	
