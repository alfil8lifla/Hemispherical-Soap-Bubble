import numpy as np
import matplotlib.pyplot as plt

n = 2          # Period=2π/n
epsilon = 0.1  # Amplitude of the small sinusoidal thermal fluctuation at the equatorial region

phi_0 = np.pi / 500

def coth(x):
    return np.cosh(x) / np.sinh(x)

def cot(x):
    return np.cos(x) / np.sin(x)

def T(theta, phi, epsilon=epsilon, n=n):
    return (1 + epsilon * np.sin(n * theta)) * (
        np.cosh(n * np.arctanh(np.cos(phi))) -
        coth(n*np.log(cot(phi_0))) * np.sinh(n * np.arctanh(np.cos(phi)))
    )

theta_vals = np.linspace(0, 2 * np.pi, 200)
phi_vals = np.linspace(phi_0, np.pi / 2, 200)
Theta, Phi = np.meshgrid(theta_vals, phi_vals)

T_vals = T(Theta, Phi)

plt.figure(figsize=(8, 7))
c = plt.contourf(Theta, Phi, T_vals, levels=50, cmap="coolwarm")
plt.xlabel("θ")
plt.ylabel("$\Phi$")
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["0", "π/2", "π", "3π/2", "2π"])
plt.yticks([0, np.pi/4, np.pi/2], ["0", "π/4", "π/2"])
plt.title("Contour Plot de T(θ, $\Phi$)")
plt.gca().invert_yaxis()
plt.show()
