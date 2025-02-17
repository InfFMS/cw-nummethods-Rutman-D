import numpy as np
import matplotlib.pyplot as plt

a = 0.1382
b = 3.19 * 10**(-5)
R = 8.314

V = np.linspace(b + 10**(-5), 10**(-3), 1000)

t = [-140, -130, -120, -110, -100]

Tk = (8 * a) / (27 * R * b)
Vk = 3 * b
Pk = a / (27 * b**2)
def van_der_waals(V, T, a, b, R):
    return R * T / (V - b) - a / V**2


Ts = -130 + 273.15
Ps = van_der_waals(V, Ts, a, b, R)


dP_dV = np.diff(Ps) / np.diff(V)
extrema = np.where(np.diff(np.sign(dP_dV)) != 0)[0]


Ve = V[extrema + 1]  # +1 из-за np.diff



d2P_dV2 = np.diff(dP_dV) / np.diff(V[1:])
if d2P_dV2[0] < 0:
  Vmax = Ve[0]
  Vmin = Ve[1]

else:
  Vmax = Ve[1]
  Vmin = Ve[0]

Pmax = van_der_waals(Vmax, Ts, a, b, R)
Pmin = van_der_waals(Vmin, Ts, a, b, R)

print(f"Локальный максимум при V = {Vmax:.6e}, P = {Pmax:.6e}")
print(f"Локальный минимум при V = {Vmin:.6e}, P = {Pmin:.6e}")

plt.figure(figsize=(10, 6))
plt.plot(V, Ps)
plt.plot(Vmax, Pmax)
plt.plot(Vmin, Pmin)
plt.xlabel('V')
plt.ylabel('P')
plt.show()