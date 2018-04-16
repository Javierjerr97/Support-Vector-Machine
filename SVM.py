#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

class SVM:
	def __init__(self, visual=True):
		self.visual = visual
		self.colors = {1:'r',-1:'b'}
		if self.visual:
			self.fig = plt.figure()
			self.ax = self.fig.add_subplot(1,1,1)

	# Entrenamiento del SVM		
	def llenar(self, datos):
		self.datos = datos

		# Diccionario de Optimizacion
		opt_dict = {}


		# Se aplicaran a los vectores de w
		transformacion = [[1,1],[-1,1],[-1,-1],[1,-1]]


		#Para los rangos maximos y minimos de los puntos
		datos_tot = []
		for yi in self.datos:
			for valores in self.datos[yi]:
				for valor in valores:
					datos_tot.append(valor)

		self.valor_max = max(datos_tot)
		self.valor_min = min(datos_tot)		
		datos_tot = None
	

		# Tamano de las divisiones a evaluar
		tam_pasos = [self.valor_max * 0.1, self.valor_max * 0.01, self.valor_max * 0.001,]
		b_rango = 5
		b_mult = 5

		
		# El ultimo vector mas optimo que se pudo conseguir
		optimo = self.valor_max*10


		for tam in tam_pasos:
			w = np.array([optimo,optimo])
			optimizado = False
			while not optimizado:
				for b in np.arange(-1*(self.valor_max*b_rango), self.valor_max*b_rango, tam*b_mult):
					for trans in transformacion:
						w_t = w*trans
						opc = True
						for i in self.datos:
							for xi in self.datos[i]:
								yi = i
								if not yi*(np.dot(w_t,xi)+b) >= 1:
									opc = False
						if opc:
							opt_dict[np.linalg.norm(w_t)] = [w_t,b]
				if w[0] < 0:
					optimizado = True
					print ('Paso de optimizacion realizado.')
				else:
					w = w - tam
			# Se  organiza del menor al mayor 
			norms = sorted([n for n in opt_dict])
			eleccion_optima = opt_dict[norms [0]]
			self.w = eleccion_optima[0]
			self.b = eleccion_optima[1]
			optimo = eleccion_optima[0][0]+tam*2

	
	def prediccion(seld, resultado):
		# Buscar el signo basandose en la formula de un hiperplano = x.w.b
		clasificacion = np.sing(np.dot(np.array(resultados),self.w)+self.b)
		if clasificacion != 0 and self.visual:
			self.ax.scatter(resultado[0], resultado[1], s=200, marker='*', c=self.colors[clasificacion])
		return clasificacion

	# Aca se Grafica el hiperplano
	def ver(self):
		[[self.ax.scatter(x[0],x[1],s=100,color=self.colors[i]) for x in dic_datos[i]] for i in dic_datos]
		def hiperplano(x,w,b,v):
			return (-w[0]*x-b+v)/w[1]

		rango_datos = (self.valor_min*0.9, self.valor_max*1.1)
		hiper_x_min = rango_datos[0]
		hiper_x_max = rango_datos[1]
		
		# Valores positivos
		vp1 = hiperplano(hiper_x_min, self.w, self.b, 1)
		vp2 = hiperplano(hiper_x_max, self.w, self.b, 1)
		self.ax.plot([hiper_x_min, hiper_x_max],[vp1,vp2],'k')

		# Valores negativos
		vn1 = hiperplano(hiper_x_min, self.w, self.b, -1)
		vn2 = hiperplano(hiper_x_max, self.w, self.b, -1)
		self.ax.plot([hiper_x_min, hiper_x_max],[vn1,vn2],'k')

		# Valores de decison (iguales a 0)
		vd1 = hiperplano(hiper_x_min, self.w, self.b, 0)
		vd2 = hiperplano(hiper_x_max, self.w, self.b, 0)
		self.ax.plot([hiper_x_min, hiper_x_max],[vd1,vd2],'y--')

		plt.show()

dic_datos = {-1:np.array([[1,7],[2,8],[3,8],]),1:np.array([[5,1],[6,-1],[7,3],])}



Support_Vector_Machine = SVM()
Support_Vector_Machine.llenar(datos=dic_datos)
Support_Vector_Machine.ver()

