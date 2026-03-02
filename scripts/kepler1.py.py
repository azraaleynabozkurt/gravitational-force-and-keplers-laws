import numpy as np
import matplotlib.pyplot as plt

a = 1.0  
b = 0.7   
c = np.sqrt(a**2 - b**2)  

t = np.linspace(0, 2*np.pi, 600)
x = a * np.cos(t)
y = b * np.sin(t)

theta_planet = 1.2
planet_x = a * np.cos(theta_planet)
planet_y = b * np.sin(theta_planet)

plt.figure(figsize=(7,7))

plt.plot(x, y, label="Orbit", linewidth=2)

plt.scatter([-c, c], [0, 0], color="gray", label="Foci")

plt.scatter([c], [0], color="orange", s=150, label="Sun")

plt.scatter([planet_x], [planet_y], color="green", s=80, label="Planet")

plt.title("Keplers First Law: The orbits of planets are elliptical")
plt.axis("equal")
plt.legend()
plt.grid(True)
plt.show()