import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def cn(f, L, n):
    def funcao(x):
        return f(x) * np.sin((n * np.pi * x) / L)
    return (2 / L) * integrate.quad(funcao, 0, L)[0]

def u(f, x, n_max, L):
    alpha = 1; T1 = 20; T2 = 50
    if t == 0:
        return 60 - 2 * x
    else:
        somatorio = 0
        for n in range(1, n_max + 1):
            somatorio += (
                cn(f, L, n)
                * np.exp((-(n**2) * np.pi**2 * alpha**2 * t) / (L**2))
                * np.sin(n * np.pi * x / L)
            )
        return somatorio + (T2 - T1) * x / L + T1

def f(x):
    return 40 - 3 * x

L = 30
x_intervalo = np.linspace(0, 30, 2500, endpoint=False)
testes_fourier = [0, 6, 10, 30, 100]
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 3D
X, T = np.meshgrid(x_intervalo, testes_fourier)
U = []
for t in testes_fourier:
    U.append(u(f, x_intervalo, t, L))
U = np.array(U)
ax_3d = fig.add_subplot(122, projection="3d")
ax_3d.plot_surface(X, T, U, cmap="viridis")
ax_3d.set_xlabel("x")
ax_3d.set_ylabel("t")
ax_3d.set_zlabel("u(x, t)")
ax_3d.set_title("3D")

# Plot 2D
for t in testes_fourier:
    y_fourier = u(f, x_intervalo, t, L)
    axes[0].plot(x_intervalo, y_fourier, label=f"t = {t}")
axes[0].set_xlabel("x")
axes[0].set_ylabel("u(x, t)")
axes[0].set_title("2D")
axes[0].legend()
axes[0].grid(True)
axes[0].set_title("2D")
axes[0].set_xlim(0, 30)
axes[0].set_ylim(0, 60)
plt.tight_layout()
plt.show()
