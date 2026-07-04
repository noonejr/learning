"""
Calculate the gravitational force between Earth and Venus
"""

G = 6.67e-11

mass_1 = 6e24
mass_2 = 4.9e24
distance = 4.1e10

force = (G * mass_1 * mass_2) / (distance**2)

print(force)