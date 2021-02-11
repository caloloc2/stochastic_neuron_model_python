import random 
import numpy as np 

class WalkRandom():

    def __init__(self, neuronas=1, C=1, p=0.7, pf=0.9, L=30, g=0.17, iteraciones=4000):
        self.__C = C
        self.__p = p
        self.__np = 1 - p
        self.__pf = pf 
        self.__L = L
        self.__g = g
        self.__neuronas = neuronas
        self.__posiciones = np.zeros((neuronas, iteraciones), dtype=float) ## [0] # posiciones con inicio en cero
        self.__posicion_actual = 0
        self.__pf_sel = [0, 4]
        self.__iteraciones = iteraciones           
    
    def genera(self):
        rr = np.random.random() # crea numeros randomicos
        upp = rr > self.__p # analiza segun probabilidad
        return rr, upp
    
    def obtener_sumatoria(self, neurona_actual, posicion):
        sumatoria = 0

        for n in range(self.__neuronas):
            if (n!=neurona_actual):
                sumatoria += (self.__posiciones[n][posicion - 1]) - (self.__posiciones[neurona_actual][posicion - 1])
        
        factor = self.__g * sumatoria

        if (factor>self.__C):        
            return factor
        else:
            return 0
    
    def procesa(self):    
        for n in range(self.__neuronas):
            for x in range(self.__iteraciones):
                valores, probabilidad = self.genera()                

                if self.__pf_sel[0] == 1:            
                    self.__posiciones[n][x] = (self.__posiciones[n][x-1] - self.__L) # Decrece en 1L
                    self.__pf_sel[1] -= 1                    

                    if (self.__pf_sel[1] == 0):
                        self.__pf_sel = [0, 4]
                elif self.__pf_sel[0] == -1:            
                    self.__posiciones[n][x] = (self.__posiciones[n][x-1] - (self.__L/5)) # Decrece en L/5
                    self.__pf_sel[1] -= 1                    

                    if (self.__pf_sel[1] == 0):
                        self.__pf_sel = [0, 4]
                elif self.__pf_sel[0] == 0:
                    factor = self.obtener_sumatoria(n, x)
                    
                    if (self.__posiciones[n][x - 1] < self.__L): # Si el valor es menor a L
                        if probabilidad:
                            self.__posiciones[n][x] = (self.__posiciones[n][x-1] + self.__C + factor) # Aumenta valor en C

                        else:
                            self.__posiciones[n][x] = (self.__posiciones[n][x-1]) # Mantiene el mismo valor
                    else:
                        if probabilidad:
                            self.__posiciones[n][x] = (self.__posiciones[n][x-1] + (3*self.__L)) # Sube a 3L
                            self.__pf_sel[0] = 1                            
                        else:
                            self.__posiciones[n][x] = (self.__posiciones[n][x-1] - (self.__L/5)) # Decrece en L/5
                            self.__pf_sel[0] = -1                            
    
    def obtener_caminata(self, neurona):
        return self.__posiciones[neurona]