#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs("plots", exist_ok=True)
L = 1
m = 1
hbar = 1
n_max = 5
n_values = list(range(1, n_max+1))      
x = np.linspace(0, L, 1000)

# Defining Energy and Psi functions

def energy(n, L=L, m=m, hbar=hbar):
    return (n**2*np.pi**2*hbar**2)/(2*m*L**2)
energies = [energy(n) for n in n_values]
def psi(n, x, L=L):
    return np.sqrt(2/L) * np.sin(n*np.pi*x/L)

# Plotting Energy Levels

def plot_energy_levels(n_values, energies):
    plt.figure(figsize = (8,5))
    plt.plot(n_values, energies, marker = 'o', linestyle = ':')
    plt.xlabel('Quantum number  $n$')
    plt.ylabel('Energy $E_n$ (arbitrary units)')
    plt.title('Energy Levels of a Particle in a 1D Infinite Potential Well')
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig('plots/energy_levels.png')
    plt.show()

# Plotting Wavefunctions

def plot_wavefunctions(n_values, x):
    plt.figure(figsize = (8,5))
    for n in n_values:
        plt.plot(x, psi(n, x), label=f"$n={n}$")
    plt.xlabel("Position $x$ (arbitrary units)")
    plt.ylabel("Wavefunction $\\psi_n(x)$")
    plt.title("Wavefunctions of a Particle in a 1D Infinite Potential Well")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig('plots/wavefunctions.png')
    plt.show()

# Plotting Probability Density

def plot_probability_density(n_values, x):
    plt.figure(figsize=(8,5))
    for n in n_values:
        prob_density = psi(n, x)**2
        plt.plot(x, prob_density, label=f"$n={n}$")
    plt.xlabel("Position $x$ (arbitrary units)")
    plt.ylabel("Probability Density $|\psi_n(x)|^2$")
    plt.title("Probability Densities of a Particle in a 1D Infinite Potential Well")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig('plots/prob_density.png')
    plt.show()
plot_energy_levels(n_values, energies)
plot_wavefunctions(n_values, x)
plot_probability_density(n_values, x)

# Plotting effect of changing box length L

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
plt.savefig("plots/effect_L.png")
plt.show()

# Plotting effect of changing mass m

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
plt.savefig("plots/effect_m.png")
plt.show()

# Check normalization

print('Normalization check(should be 1):')
for n in range(1, n_max + 1):
    norm = np.trapezoid(psi(n, x)**2, x)
    print(f'n = {n}, ∫|ψ_n(x)|^2 dx = {norm:.6f}')


# In[ ]:




