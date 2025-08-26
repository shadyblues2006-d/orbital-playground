import math

G0 = 9.80665  # m/s^2

def rocket_delta_v(m0: float, mf: float, isp_s: float) -> float:
    """
    Tsiolkovsky rocket equation (delta-v in m/s).

    m0: initial mass (kg) = dry + propellant + payload
    mf: final mass  (kg) = dry + payload
    isp_s: specific impulse (s)

    Returns: delta-v (m/s)
    """
    if m0 <= mf:
        raise ValueError("m0 must be greater than mf")
    if isp_s <= 0:
        raise ValueError("Isp must be positive")
    ve = isp_s * G0
    return ve * math.log(m0 / mf)
