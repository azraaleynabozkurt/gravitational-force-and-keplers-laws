import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54]) 
T = np.sqrt(a**3)

plt.figure(figsize=(7,5))
plt.scatter(a, T, color="red", s=80, label="Planets")

a_smooth = np.linspace(0, 10, 400)

plt.plot(a_smooth, np.sqrt(a_smooth**3), "k--", label="T = a^(3/2)")

plt.xlabel("Semi-major axis a (AU)")
plt.ylabel("Period T (years)")
plt.title("Keplers Third Law: T² = a³")
plt.legend()
plt.grid(True)
plt.show()

