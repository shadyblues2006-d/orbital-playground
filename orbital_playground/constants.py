from __future__ import annotations
import math

# Gravitational parameter of Earth in km^3/s^2 (WGS-84)
MU_EARTH: float = 398600.4418

# Mean equatorial radius of Earth in km (WGS-84)
R_EARTH_EQUATOR: float = 6378.137

# Earth's sidereal rotation rate in rad/s
OMEGA_EARTH: float = 7.2921159e-5

# J2 for Earth (dimensionless)
J2_EARTH: float = 1.08262668e-3

# Useful constants
TWOPI: float = 2.0 * math.pi
DEG2RAD: float = math.pi / 180.0
RAD2DEG: float = 180.0 / math.pi
