import numpy as np
from findiff import FinDiff
from scipy.sparse.linalg import inv, eigs
from scipy.sparse import csc_matrix, eye, diags
import matplotlib.pyplot as plt

# Space-Time discretization

xs, dx = np.linspace(-5, 5, 1000, retstep=True)
ts, dt = np.linspace(0, 2*np.pi, 300, retstep=True)

# FinDiff makes a derivative operator 

# H = -1/2 * d/dx^2 + 1/2 x**2 for Harmonic Potential
H = -0.5 * FinDiff(
    0,      # Index of variable on which to differentiate (in this case x)
    dx,     # Separation between two lattice points
    2       # Order of differential
).matrix(xs.shape) + diags(0.5*xs**2)

# Boundary modifications

H[0, :] = H[-1, :] = 0
H[0, 0] = H[-1, -1] = 1

# Building the Crank-Nelson propogator

# Forward Euler approximation
I_plus  = csc_matrix(eye(xs.shape[0]) + 1j*dt/2. * H)
# Backward Euler approximation
I_minus = csc_matrix(eye(xs.shape[0]) - 1j*dt/2. * H)
# Crank Nicholson Unitary
U = inv(I_minus).dot(I_plus)

# Initial state : Gaussian wavepacket

a = -2
psi = np.exp(-(xs-a)**2) / np.sqrt(np.pi) # Wavepacket centered at a with variance 1

# Animating the waveform



for it, t in enumerate(ts):
    psi = U.dot(psi)
    psi[0] = psi[-1] = 0
    if it % 4 == 1:
        fig = plt.figure(figsize=(8, 6))
        plt.xlabel('x')
        plt.xlim((-5.1, 5.1))
        plt.ylim((-0.01, 0.35))
        plt.ylabel(r'$|\psi|^{2}$')
        plt.title(f"t = {it*dt:5.2f}")
        plt.grid()
        plt.plot(xs, np.abs(psi)**2)
        plt.savefig(f"{it//4:03d}.jpg", bbox_inches='tight', dpi=180)
        plt.close()