from __future__ import annotations
from math import radians, sqrt, sin
from typing import Tuple

from .constants import MU_EARTH

def hohmann_delta_v(r1_km: float, r2_km: float, mu: float = MU_EARTH) -> Tuple[float, float, float]:
    """Hohmann transfer Δv (dv1, dv2, total) in km/s."""
    a_t = 0.5 * (r1_km + r2_km)
    v1 = sqrt(mu / r1_km)
    v2 = sqrt(mu / r2_km)
    v_peri = sqrt(mu * (2.0 / r1_km - 1.0 / a_t))
    v_apo  = sqrt(mu * (2.0 / r2_km - 1.0 / a_t))
    dv1 = v_peri - v1
    dv2 = v2 - v_apo
    return dv1, dv2, abs(dv1) + abs(dv2)

def circularization_delta_v(r_circ_km: float, a_ell_km: float, mu: float = MU_EARTH) -> float:
    """Δv to circularize at r_circ from an elliptical orbit with semi-major axis a_ell."""
    v_ell  = sqrt(mu * (2.0 / r_circ_km - 1.0 / a_ell_km))
    v_circ = sqrt(mu / r_circ_km)
    return abs(v_circ - v_ell)

def plane_change_delta_v(v_kms: float, delta_i_deg: float) -> float:
    """Δv for plane change at speed v: Δv = 2 v sin(Δi/2)."""
    return 2.0 * v_kms * sin(radians(delta_i_deg) * 0.5)
