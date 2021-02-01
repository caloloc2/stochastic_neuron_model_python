from walk_random import WalkRandom
import matplotlib.pyplot as plt

# prob = [0.3, 0.7]
# prob = [0.1, 0.9]
# prob = [0.5, 0.5]
# prob = [0.9, 0.1]

iteraciones = 4000
n0 = WalkRandom(p=0.7, iteraciones=iteraciones)
n1 = WalkRandom(p=0.5, iteraciones=iteraciones)
n2 = WalkRandom(p=0.1, iteraciones=iteraciones)

val0 = 0
val1 = 0
val2 = 0

for i in range(iteraciones):
    val0 = n0.analiza(i, val2)
    val1 = n1.analiza(i, val0)
    val2 = n2.analiza(i, val1)    

walk0 = n0.obtener_caminata()
walk1 = n1.obtener_caminata()
walk2 = n2.obtener_caminata()

fig, axs = plt.subplots(3)
axs[0].plot(walk0, label = "n0", color="green")
axs[1].plot(walk1, label = "n1", color="red")
axs[2].plot(walk2, label = "n2", color="blue")
plt.show()