import random 
import numpy as np 

class WalkRandom():

    def __init__(self, C=1, p=0.7, pf=0.9, L=30, g=0.17, iteraciones=4000):
        self.__C = C
        self.__p = p
        self.__np = 1 - p
        self.__pf = pf 
        self.__L = L
        self.__g = g
        self.__posiciones = np.zeros(iteraciones) ## [0] # posiciones con inicio en cero
        self.__posicion_actual = 0
        self.__pf_sel = [0, 4]
        self.__iteraciones = iteraciones
        self.__sumatoria = 0
        self.__randomicos = self.__genera()
    
    def __genera(self):
        rr = np.random.random(self.__iteraciones) # crea numeros randomicos
        upp = rr > self.__p # analiza cada punto segun probabilidad
        return rr, upp
    
    def analiza(self, pos, vecino):
        valores = self.__randomicos[0][pos]
        probabilidad = self.__randomicos[1][pos]

        if self.__pf_sel[0] == 1:            
            self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L
            self.__pf_sel[1] -= 1

            if (self.__pf_sel[1] == 0):
                self.__pf_sel = [0, 4]
        elif self.__pf_sel[0] == -1:            
            self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
            self.__pf_sel[1] -= 1

            if (self.__pf_sel[1] == 0):
                self.__pf_sel = [0, 4]
        elif self.__pf_sel[0] == 0:
            self.__sumatoria = self.__posiciones[pos - 1] + vecino
            factor = self.__g * self.__sumatoria
            # print(self.__posiciones[pos - 1], vecino, factor)
            if (self.__posiciones[pos - 1] < self.__L): # Si el valor es menor a L
                if probabilidad:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] + self.__C) # Aumenta valor en C
                else:
                    self.__posiciones[pos] = (self.__posiciones[pos-1]) # Mantiene el mismo valor
            else:
                if probabilidad:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] + (3*self.__L)) # Sube a 3L
                    self.__pf_sel[0] = 1
                else:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__pf_sel[0] = -1  

        return self.__posiciones[pos]    

    def analiza2(self, pos, vecino):
        valores = self.__randomicos[0][pos]
        probabilidad = self.__randomicos[1][pos]

        if probabilidad:
            if self.__posiciones[pos-1] < self.__L:
                self.__posiciones[pos] = (self.__posiciones[pos-1] + self.__C) # Aumenta el valor en C
            else:               
                if valores > self.__pf:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] + (3*self.__L)) # Sube a 3L
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L     
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L     
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L     
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L
                else:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
        else:
            if self.__posiciones[pos-1] < self.__L:
                self.__posiciones[pos] = (self.__posiciones[pos-1]) # Se mantiene en el mismo valor
            else:
                if valores > self.__pf:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] + (3*self.__L)) # Sube a 3L
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L     
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L     
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L     
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - self.__L) # Decrece en 1L
                else:
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones[pos] = (self.__posiciones[pos-1] - (self.__L/5)) # Decrece en L/5

        return self.__posiciones[pos]
    
    def obtener_caminata(self):
        return self.__posiciones
    
    def analiza_back(self):
        rr = np.random.random(self.__iteraciones) # crea numeros randomicos
        upp = rr > self.__p # analiza cada punto segun probabilidad
        
        for iupp in upp:        
            if iupp:
                if self.__posiciones[-1] < self.__L:
                    self.__posiciones.append(self.__posiciones[-1] + self.__C) # Aumenta el valor en C
                else:
                    self.__posiciones.append(self.__posiciones[-1] + (3*self.__L)) # Sube a 3L
                    self.__posiciones.append(self.__posiciones[-1] - self.__L) # Decrece en 1L     
                    self.__posiciones.append(self.__posiciones[-1] - self.__L) # Decrece en 1L     
                    self.__posiciones.append(self.__posiciones[-1] - self.__L) # Decrece en 1L     
                    self.__posiciones.append(self.__posiciones[-1] - self.__L) # Decrece en 1L     
            else:
                if self.__posiciones[-1] < self.__L:
                    self.__posiciones.append(self.__posiciones[-1]) # Se mantiene en el mismo valor
                else:            
                    self.__posiciones.append(self.__posiciones[-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones.append(self.__posiciones[-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones.append(self.__posiciones[-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones.append(self.__posiciones[-1] - (self.__L/5)) # Decrece en L/5
                    self.__posiciones.append(self.__posiciones[-1] - (self.__L/5)) # Decrece en L/5

        return self.__posiciones
