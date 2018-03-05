import re


class lexer(object):

	lisline=[]
	listokens=[]
	cont=0
	propias=[]
	variable=re.compile("[a-z]\w*")
	funcion=re.compile("[$][a-z]\w*[(][)]")

	def iniciar(self):	
		listalineas=open("entrada.lex","r")

		for linea in listalineas.readlines():
			temp=len(linea)		
			self.lisline.append(linea[:temp -1])
		listalineas.close()	

	def listarTokens(self):
		
		for linea in self.lisline:
			self.listokens=linea.split(" ")
			self.lisline[self.cont]=self.listokens
			self.cont+=1	
		self.cont=0



	def confirmarfuncion(self,averificar):
		if self.funcion.match(averificar)==None:
			False
		else:
			True	

	"""docstring for lexer"""
	def __init__(self):
		super(lexer, self).__init__()
		
	def imprimirArchivo(self):
			self.cont+=1
			for linea in self.lisline:
					print(self.cont)
					print(linea)
						
					self.cont+=1
			self.cont=0		

	def confirmarVariable(self,averificar):
		if self.variable.match(averificar)==None:
			return False
		else:
			return True			

	def imprimirLineas(self):
		print(self.lisline)

	def imprimirTokens(self):
			print(self.listokens)	

	def subirReservadas(self):
		listalineas=open("reservadas.lex","r")

		for linea in listalineas.readlines():
			temp=len(linea)		
			self.propias.append(linea[:temp -1])
		listalineas.close()

	def imprimirPropias(self):
			print(self.propias)	


programa=lexer()
programa.iniciar()
programa.listarTokens()
programa.imprimirArchivo()
programa.subirReservadas()
programa.imprimirPropias()



