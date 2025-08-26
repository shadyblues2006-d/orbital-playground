import matplotlib.pyplot as plt
import numpy as np
from orbital_playground.delta_v import hohmann_delta_v

# Example values
r1 = 7000  # km (LEO ~ 622 km altitude)
r2 = 15000 # km (MEO)

# Compute Δv
dv1, dv2, dvtot = hohmann_delta_v(r1, r2)

# Angles for plotting
theta = np.linspace(0, 2*np.pi, 500)

# Define orbits
orbit1_x = r1 * np.cos(theta)
orbit1_y = r1 * np.sin(theta)

orbit2_x = r2 * np.cos(theta)
orbit2_y = r2 * np.sin(theta)

# Transfer ellipse parameters
a = (r1 + r2) / 2
b = np.sqrt(r1 * r2)  # approximation for ellipse
transfer_x = a * np.cos(theta)
transfer_y = b * np.sin(theta)

# Plotting
plt.figure(figsize=(6,6))
plt.plot(orbit1_x, orbit1_y, label=f"Orbit 1 (r={r1} km)")
plt.plot(orbit2_x, orbit2_y, label=f"Orbit 2 (r={r2} km)")
plt.plot(transfer_x, transfer_y, "--", label="Transfer orbit")

# Add Earth at center
earth = plt.Circle((0,0), 6371, color="blue", alpha=0.3, label="Earth")
plt.gca().add_artist(earth)

# Formatting
plt.gca().set_aspect("equal")
plt.xlabel("x [km]")
plt.ylabel("y [km]")
plt.legend()
plt.title(f"Hohmann Transfer: Δv1={dv1:.2f} km/s, Δv2={dv2:.2f} km/s")

plt.show()
