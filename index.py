from random_walk import WalkRandom
import matplotlib.pyplot as plt

clase = WalkRandom(neuronas=3, iteraciones=1500, C=1, g=0.17, L=30, p=0.5, pf=0.9)

clase.procesa()

walk0 = clase.obtener_caminata(0)
walk1 = clase.obtener_caminata(1)
walk2 = clase.obtener_caminata(2)

plot.plot(walk2, label = "n2", color="blue")
plt.show()

plot.plot(walk2, label = "n2", color="blue")
plt.show()

plot.plot(walk2, label = "n2", color="blue")
plt.show()


fig, axs = plt.subplots(4)
axs[0].plot(walk0, label = "n0", color="green")
axs[1].plot(walk1, label = "n1", color="red")
axs[2].plot(walk2, label = "n2", color="blue")
axs[3].plot(walk0, label = "n0", color="green")
axs[3].plot(walk1, label = "n1", color="red")
axs[3].plot(walk2, label = "n2", color="blue")
plt.show()
