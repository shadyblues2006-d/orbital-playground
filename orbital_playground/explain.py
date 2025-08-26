# orbital_playground/explain.py
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any

# --- Categories your missions.py can tag targets with (see TARGET_META below) ---
INTERSTELLAR = {"Alpha Centauri", "Barnard's Star", "TRAPPIST-1 system", "Kepler-186f", "55 Cancri e", "Andromeda Galaxy"}
EXTREME_PHYSICS = {"Wormhole", "Schwarzschild Black Hole", "Sagittarius A*"}
DEEP_SOLAR_SYSTEM = {"Oort Cloud", "Solar Gravitational Lens"}
OUTER_PLANETS = {"Uranus", "Neptune", "Pluto", "Europa", "Enceladus", "Titan"}

# --- Future-tech “suggestions” by category ---
FUTURE_TECH: Dict[str, List[str]] = {
    "interstellar": [
        "Laser sail (e.g., Starshot): push gram–kg craft to ~0.1–0.2c",
        "Fusion propulsion (Daedalus/Icarus): pulsed ICF pellets for high Δv",
        "Beamed electric sail / magsail: long-duration low-thrust acceleration",
        "Nuclear electric (ion/vasimr): multi-year continuous thrust",
    ],
    "outer_planets": [
        "Gravity assists (e.g., Venus/Earth/Jupiter) to cut Δv",
        "Aerocapture where possible to save insertion Δv",
        "Nuclear electric propulsion for cruise efficiency",
    ],
    "deep_solar_system": [
        "Fast solar sail perihelion dive (‘sundiver’) for high exit speeds",
        "Nuclear electric + Jupiter Oberth to reach 500+ AU",
    ],
    "extreme_physics": [
        "Exotic matter / negative energy (speculative) for spacetime shortcuts",
        "Warp-metric research (Alcubierre-type) under energy constraints",
    ],
    "near_planets": [
        "In-orbit refueling & staging",
        "Aerobraking/aerocapture (where atmospheres exist)",
        "High-Isp upper stages (nuclear thermal, methane vac engines)",
    ],
}

@dataclass
class Explanation:
    feasible: bool
    reason_short: str
    margin_mps: float
    future_paths: List[str]
    paragraph: str

def _bucket_for_target(target: str) -> str:
    if target in INTERSTELLAR:
        return "interstellar"
    if target in EXTREME_PHYSICS:
        return "extreme_physics"
    if target in DEEP_SOLAR_SYSTEM:
        return "deep_solar_system"
    if target in OUTER_PLANETS:
        return "outer_planets"
    # fallback
    return "near_planets"

def _fmt_kms(x_mps: float) -> str:
    return f"{x_mps/1000:.2f} km/s"

def explain_feasibility(target: str, dv_required_mps: float, dv_available_mps: float) -> Explanation:
    margin = dv_available_mps - dv_required_mps
    feasible = margin >= 0
    bucket = _bucket_for_target(target)
    techs = FUTURE_TECH[bucket]

    # --- Reasoning templates (short & hopeful) ---
    if feasible:
        reason = f"Available Δv ({_fmt_kms(dv_available_mps)}) exceeds requirement ({_fmt_kms(dv_required_mps)})."
        para = (
            f"{target}: Feasible with today’s staging and high‑Isp upper stages. "
            "Refueling, gravity assists, and aerobraking can further improve margins."
        )
    else:
        gap = _fmt_kms(abs(margin))
        if bucket == "interstellar":
            reason = f"Interstellar distance implies Δv needs orders of magnitude beyond chemical rockets (shortfall {gap})."
            para = (
                f"{target}: Current rockets top out at single‑digit km/s, while interstellar travel needs a different playbook. "
                "Active research explores beamed‑energy laser sails and fusion‑driven concepts to cut centuries to decades."
            )
        elif bucket == "extreme_physics":
            reason = f"Physics constraints dominate; Δv framing breaks down (shortfall {gap})."
            para = (
                f"{target}: Rockets can’t address spacetime shortcuts. Work in exotic energy, traversable metrics, and quantum gravity "
                "is speculative but aims to turn ‘impossible’ into engineering one day."
            )
        elif bucket == "deep_solar_system":
            reason = f"Distance to hundreds of AU makes chemical cruise impractical (shortfall {gap})."
            para = (
                f"{target}: Concepts like fast solar sails and nuclear‑electric propulsion, plus Jupiter Oberth maneuvers, "
                "are proposed to reach these distances within a career timescale."
            )
        elif bucket == "outer_planets":
            reason = f"Large insertion Δv and long cruise time with chemical stages (shortfall {gap})."
            para = (
                f"{target}: Feasibility improves with gravity assists and aerocapture. Nuclear‑electric propulsion can provide "
                "high total Δv over years with reasonable mass."
            )
        else:
            reason = f"Insufficient Δv margin for this profile (shortfall {gap})."
            para = (
                f"{target}: Consider refueling, lighter payloads, or higher‑Isp stages; gravity assists can reduce the Δv bill."
            )

    return Explanation(
        feasible=feasible,
        reason_short=reason,
        margin_mps=margin,
        future_paths=techs,
        paragraph=para,
    )
