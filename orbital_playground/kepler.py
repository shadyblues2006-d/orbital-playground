import math
from .constants import MU_EARTH


def orbital_period(semi_major_axis: float) -> float:
    """
    Compute the orbital period of a satellite using Kepler's Third Law.

    Parameters
    ----------
    semi_major_axis : float
        Semi-major axis of the orbit [m]

    Returns
    -------
    T : float
        Orbital period [s]
    """
    return 2 * math.pi * math.sqrt(semi_major_axis**3 / MU_EARTH)
# orbital_playground/kepler.py
import math
from .constants import MU_EARTH, R_EARTH_EQUATOR

def circular_velocity(altitude_m: float) -> float:
    """
    Circular orbital velocity at given altitude [m/s].
    """
    r = R_EARTH_EQUATOR + altitude_m
    return math.sqrt(MU_EARTH / r)

def mean_motion(altitude_m: float) -> float:
    """
    Mean motion (rad/s) for circular orbit at given altitude.
    """
    r = R_EARTH_EQUATOR + altitude_m
    return math.sqrt(MU_EARTH / r**3)
