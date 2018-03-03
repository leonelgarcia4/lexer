class token(object):
	"""docstring for token"""
	def __init__(self, arg):
		super(token, self).__init__()
		self.arg = arg
	
	def analizarToken():
		pass


listaReservados=[]
listaReservados=open("reservadas.lex","r")
lis=[]

for linea in listaReservados.readlines():
	temp=len(linea)
	lis.append(linea[:temp -1])
if lis[3]=="var":
	print(lis)
