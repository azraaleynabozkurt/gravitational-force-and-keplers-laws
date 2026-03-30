import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 600)
r = 1 / (1 + 0.6 * np.cos(theta))

t1 = 0
t2 = 0.7 

theta1 = t1
theta2 = t2

theta_fill = np.linspace(theta1, theta2, 200)
r_fill = 1 / (1 + 0.6 * np.cos(theta_fill))

plt.figure(figsize=(7,7))
ax = plt.subplot(111, projection='polar')

ax.plot(theta, r, label="Orbit")

ax.fill(theta_fill, r_fill, color="red", alpha=0.4, label="Equal Area")

planet_r = 1 / (1 + 0.6 * np.cos(theta2))
ax.scatter([theta2], [planet_r], color="blue", s=80, label="Planet")

plt.title("Keplers Second Law: Planets sweep out equal areas in equal times")
plt.legend()
plt.show()