class Linea(object):

	

	"""docstring for Linea"""
	def __init__(self, arg):
		super(Linea, self).__init__()
		self.tokens=arg.split(" ")
			
	

	def imprimir(self):
		
		print(self.tokens)
		


line=Linea(input("digite una linea \n"))
line.imprimir()