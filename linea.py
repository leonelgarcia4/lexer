

class Linea(object):
	
	"""docstring for Linea"""
	def __init__(self, arg):
		super(Linea, self).__init__()
		self.tokens=arg.split(" ")
				
	def imprimir(self):
		
		print(self.tokens)
		


listaReservados=[]
listaReservados=open("reservadas.lex","r")
lis=[]

for linea in listaReservados.readlines():
	temp=len(linea)
	lis.append(linea[:temp -1])
listaReservados.close()	
if lis[3]=="var":
	print(lis)