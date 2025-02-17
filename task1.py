import numpy as np
import matplotlib.pyplot as plt


a = 0.1382
b = 3.19*10**(-5)
R = 8.314

def van_der_waals(V, T, a, b, R):
  return (R * T / (V - b)) - (a / (V**2))


tc = [-140, -130, -120, -110, -100]

tk = [T + 273.15 for T in tc]

V = np.linspace(b * 1.1, 10 * b, 500)

plt.figure(figsize=(10, 6))
plt.xlabel("Молярный объем")
plt.ylabel("Давление")

colors = ['blue', 'green', 'orange', 'red', 'purple']

for i in range(len(tc)):
    plt.plot(V, van_der_waals(V, tk[i], a, b, R), label=f"{tc[i]} °C", color=colors[i])

plt.show()