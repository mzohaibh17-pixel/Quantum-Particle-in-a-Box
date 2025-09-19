import numpy as np
import matplotlib.pyplot as plt
L = 1
m = 1
hbar = 1
n_max = int(input('Enter the maximum quantum number n:'))

# Energy levels of particle in a 1D infinite potential well
# Formula: E_n = (n^2 * π^2 * ħ^2) / (2mL^2)

def energy(n, L=L, m=m, hbar=hbar):
    return (n**2*np.pi**2*hbar**2)/(2*m*L**2)
n_values = list(range(1, n_max+1))                      # Generate quantum numbers (n = 1, 2, ..., n_max)
energies = [energy(n) for n in n_values]                # Compute energy for each quantum number

# Plot energy levels vs quantum number

plt.figure(figsize = (8,5))
plt.plot(n_values, energies, marker = 'o', linestyle = ':')
plt.xlabel('Quantum number  $n$')
plt.ylabel('Energy $E_n$ (arbitrary units)')
plt.title('Energy Levels of a Particle in a 1D Infinite Potential Well')
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig('C:/Users/Zohaib Hassan/Downloads/Projects/Particle Box/plots/energy_levels.png')
plt.show()

# Calculate wavefunction ψ_n(x)
# Formula: ψ_n(x) = sqrt(2/L) * sin(nπx / L)

x = np.linspace(0, L, 1000)
def psi(n, x, L=L):
    return np.sqrt(2/L) * np.sin(n*np.pi*x/L)

# Plot wavefunctions for n

plt.figure(figsize = (8,5))
for n in range(1, n_max+1):
    psi_n = psi(n,x)
    plt.plot(x, psi_n, label=f"$n={n}$")
plt.xlabel("Position $x$ (arbitrary units)")
plt.ylabel("Wavefunction $\\psi_n(x)$")
plt.title("Wavefunctions of a Particle in a 1D Infinite Potential Well")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig('C:/Users/Zohaib Hassan/Downloads/Projects/Particle Box/plots/wavefunctions.png')
plt.show()

# Probability Density Plots

plt.figure(figsize=(8,5))
for n in range(1, n_max+1):
    psi_n = psi(n, x)
    prob_density = psi_n**2
    plt.plot(x, prob_density, label=f"$n={n}$")
plt.xlabel("Position $x$ (arbitrary units)")
plt.ylabel("Probability Density $|\psi_n(x)|^2$")
plt.title("Probability Densities of a Particle in a 1D Infinite Potential Well")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig('C:/Users/Zohaib Hassan/Downloads/Projects/Particle Box/plots/prob_density.png')
plt.show()

# Check normalization

print('Normalization check(should be 1):')
for n in range(1, n_max + 1):
    psi_n = psi(n,x)
    norm = np.trapezoid(psi_n**2, x)
    print(f'n = {n}, ∫|ψ_n(x)|^2 dx = {norm:.6f}')

# Effect of changing box length L

L_values = [0.5, 1.0, 2.0]
plt.figure(figsize=(8,5))
for L_new in L_values:
    energies_L = [energy(n, L=L_new, m=m) for n in n_values]
    plt.plot(n_values, energies_L, marker='o', linestyle=':', label=f"L = {L_new}")
plt.xlabel("Quantum number $n$")
plt.ylabel("Energy $E_n$ (arbitrary units)")
plt.title("Effect of Box Length L on Energy Levels")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig("C:/Users/Zohaib Hassan/Downloads/Projects/Particle Box/plots/effect_L.png")
plt.show()

# Plot effect of changing mass m

m_values = [0.5, 1.0, 2.0]
plt.figure(figsize=(8,5))
for m_new in m_values:
    energies_m = [energy(n, L=L, m=m_new) for n in n_values]
    plt.plot(n_values, energies_m, marker='o', linestyle=':', label=f"m = {m_new}")
plt.xlabel("Quantum number $n$")
plt.ylabel("Energy $E_n$ (arbitrary units)")
plt.title("Effect of Particle Mass m on Energy Levels")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig("C:/Users/Zohaib Hassan/Downloads/Projects/Particle Box/plots/effect_m.png")
plt.show()