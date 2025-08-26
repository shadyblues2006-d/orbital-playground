# Super simple delta-v budgets (m/s). Educational, not precise.
MISSION_DV = {
    "LEO": 9400.0,          # launch to LEO (for comparison)
    "LEO_to_GTO": 2400.0,   # from LEO to GTO
    "LEO_to_Mars": 3800.0,  # LEO to TMI (trans-Mars injection) ballpark
    "LEO_to_Escape": 3200.0,
    "AlphaCentauri": 3.0e7, # playful sci-fi target ~0.1c scale (impossible with chem)
}

def required_delta_v(target: str) -> float:
    try:
        return MISSION_DV[target]
    except KeyError as e:
        raise ValueError(f"Unknown target '{target}'. "
                         f"Choices: {', '.join(MISSION_DV)}") from e
