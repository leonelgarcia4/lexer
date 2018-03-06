import re


class lexer(object):

	lisline=[]
	listokens=[]
	cont=0
	propias=[]
	variable=re.compile("[$][a-z]\w*$")
	funcion=re.compile("[$][a-z]\w*[(][)]$")
	oplogicos=[]
	oparitmeticos=[]
	oprelacionales=[]
	tokenvalido=None

	def iniciar(self):	
		listalineas=open("entrada.lex","r")
		listalogicos=open("operadoreslogicos.lex","r")
		listaaritmeticos=open("operadoresaritmeticos.lex","r")
		listarelacionales=open("operadoresrelacionales.lex","r")

		for linea in listalineas.readlines():
			temp=len(linea)		
			self.lisline.append(linea[:temp -1])
		listalineas.close()	

		for linea in listalogicos.readlines():
			temp=len(linea)		
			self.oplogicos.append(linea[:temp -1])
		listalogicos.close()	
		print(self.oplogicos)

		for linea in listaaritmeticos.readlines():
			temp=len(linea)		
			self.oparitmeticos.append(linea[:temp -1])
		listaaritmeticos.close()	
		print(self.oparitmeticos)

		for linea in listarelacionales.readlines():
			temp=len(linea)		
			self.oprelacionales.append(linea[:temp -1])
		listarelacionales.close()	
		print(self.oprelacionales)

	def listarTokens(self):
		
		for linea in self.lisline:
			self.listokens=linea.split(" ")
			self.lisline[self.cont]=self.listokens
			self.cont+=1	
		self.cont=0

	def tipoLexema(self,token):
		if token in self.oplogicos:
			return "operador logico"

		if token in self.oparitmeticos:
			return "operador aritmetico"

		if token in self.oprelacionales:
			return "operador relacional"

		if self.confirmarfuncion(token):
			return self.tokenvalido	
			

		if self.confirmarVariable(token)==True:
			return "identificador"

		

	def confirmarfuncion(self,aver):
		if self.funcion.match(aver):
			self.tokenvalido="funcion"
			return self.tokenvalido
		else:
			return self.tokenvalido	
		
			

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
ar=""
print(programa.tipoLexema(ar))


