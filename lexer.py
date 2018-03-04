class lexer(object):

	lisline=[]
	listokens=[]
	cont=0

	def iniciar(self):

		
		listalineas=open("entrada.lex","r")
		

		for linea in listalineas.readlines():
			temp=len(linea)
			
			self.lisline.append(linea[:temp -1])
		listalineas.close()	

	def listarTokens(self):
		
		tam=len(self.lisline)
		
		while self.cont<tam:
			
			x=self.lisline[self.cont].split(" ")
			
			for y in x:
				
				self.listokens.append(y)
			self.cont=self.cont+1	
				
	"""docstring for lexer"""
	def __init__(self):
		super(lexer, self).__init__()
		
		


	def imprimirLineas(self):
		print(self.lisline)

	def imprimirTokens(self):
			print(self.listokens)	

programa=lexer()
programa.iniciar()
programa.listarTokens()
programa.imprimirLineas()
programa.imprimirTokens()

