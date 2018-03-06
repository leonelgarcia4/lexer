import re


class lexer(object):

	lisline=[]
	listokens=[]
	cont=0
	propias=[]
	variable=re.compile("[$][a-z]\w*$")
	funcion=re.compile("[$][a-z]\w*[(][)]$")
	numeros=re.compile("\d+")
	oplogicos=[]
	oparitmeticos=[]
	oprelacionales=[]
	tokenvalido=None
	sw=0


	def iniciar(self):	
		listalineas=open("entrada.lex","r")
		listalogicos=open("operadoreslogicos.lex","r")
		listaaritmeticos=open("operadoresaritmeticos.lex","r")
		listarelacionales=open("operadoresrelacionales.lex","r")

		for linea in listalineas.readlines():
			temp=len(linea)	
			aux=linea.split(" ")
			if aux[0]=="/*":
				
				self.sw=1
			
			if (aux[0]!="//") and (self.sw==0):
				self.lisline.append(linea[:temp -1])

			if aux[0]=="*/":
					self.sw=0		

				
			self.cont+=1
		self.cont=0	
		listalineas.close()	
		

		for linea in listalogicos.readlines():
			temp=len(linea)		
			self.oplogicos.append(linea[:temp -1])
		listalogicos.close()	
		

		for linea in listaaritmeticos.readlines():
			temp=len(linea)		
			self.oparitmeticos.append(linea[:temp -1])
		listaaritmeticos.close()	
		

		for linea in listarelacionales.readlines():
			temp=len(linea)		
			self.oprelacionales.append(linea[:temp -1])
		listarelacionales.close()	
		

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

		if token in self.propias:
			return "reservada"	

		if self.numeros.match(token):
				aux=len(self.numeros.search(token).group())
				if aux==len(token):
					return "numerico"
				

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

	def borrarenblanco(self):
		c=0
		aux=[]
		for linea in self.lisline:
			
			for token in linea:
				aux=self.lisline[self.cont].split(" ")
				t=aux.count("")
				for x in range(0,t):
					aux.remove("")
				
				
				
				
				c+=1
			self.cont+=1
		self.cont=0	
		
	def imprimirArchivo(self):
			self.cont+=1
			self.listokens=[]
			for linea in self.lisline:
					print(self.cont)
					print(linea)
					for token in linea:
						self.listokens.append(token)
						
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

	def verificartoken(self,tok):
			if self.tipoLexema(tok):
					True	
			else:
				False	
	def posicionToken(self,token):
		self.cont=0
		for linea in self.lisline:
			if token in linea[self.cont]:
				return (self.cont+1)
			self.cont+=1					


programa=lexer()

programa.iniciar()
programa.borrarenblanco()
programa.listarTokens()
programa.imprimirArchivo()
programa.subirReservadas()
print("----------------------------------------------------------------")
print("\t \t \t LISTA DE LOS TOKEN")
print("----------------------------------------------------------------")
for token in programa.listokens:
	if token!="":
		print("lexema: ", token, "tipo: ", programa.tipoLexema(token))

print("----------------------------------------------------------------")
print("\t \t \t LISTA DE LOS ERRORES")
print("----------------------------------------------------------------")
"""
for token in programa.lisline:
	if programa.verificartoken(token)!=True:
		print(token, "token invalido")
	"""
		





