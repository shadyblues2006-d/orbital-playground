import numpy as np

G0 = 9.80665  # m/s², standard gravity

def rocket_delta_v(m0: float, mf: float, isp: float) -> float:
    if m0 <= mf:
        raise ValueError("Initial mass must be greater than final mass.")
    return isp * G0 * np.log(m0 / mf)

class Rocket:
    def __init__(self, name, m0_kg, mf_kg, isp_s):
        self.name = name
        self.m0_kg = m0_kg
        self.mf_kg = mf_kg
        self.isp_s = isp_s

    def delta_v(self) -> float:
        return rocket_delta_v(self.m0_kg, self.mf_kg, self.isp_s)

ROCKETS = {
    "PSLV": Rocket("PSLV", m0_kg=320_000, mf_kg=120_000, isp_s=280),
    "Falcon9": Rocket("Falcon9", m0_kg=550_000, mf_kg=150_000, isp_s=311),
    "SaturnV": Rocket("SaturnV", m0_kg=2_800_000, mf_kg=200_000, isp_s=421),
    "SLS": Rocket("SLS", m0_kg=2_600_000, mf_kg=220_000, isp_s=452),
    "Starship": Rocket("Starship", m0_kg=1_200_000, mf_kg=150_000, isp_s=380),
}

def list_rockets():
    return list(ROCKETS.keys())

def get_rocket(name: str):
    if name not in ROCKETS:
        raise ValueError(f"Unknown rocket '{name}'. Try one from the list: {list_rockets()}")
    return ROCKETS[name]
