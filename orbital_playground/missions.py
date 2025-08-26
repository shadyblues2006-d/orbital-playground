# orbital_playground/missions.py

"""
Mission planning data & utilities.
"""

# --- Required Δv values for missions (m/s) ---
DESTINATIONS = {
    # Earth & Near-Earth
    "LEO": 9400,
    "GEO": 11800,
    "Moon": 16000,
    "Mars": 18000,
    "Venus": 17000,
    "Mercury": 18000,
    "Near-Earth Asteroid": 13000,

    # Outer Planets & Moons
    "Ceres": 19000,
    "Jupiter": 30000,
    "Saturn": 32000,
    "Uranus": 35000,
    "Neptune": 37000,
    "Pluto": 42000,
    "Europa": 27000,
    "Ganymede": 27500,
    "Callisto": 26000,
    "Titan": 29000,
    "Enceladus": 30000,
    "Triton": 36500,
    "Halley": 25000,

    # Far Solar System
    "Oort Cloud": 100000,
    "Solar Gravitational Lens": 550000,

    # Interstellar
    "Alpha Centauri": 3000000,
    "Barnard's Star": 3600000,
    "TRAPPIST-1": 4000000,
    "Kepler-186f": 4500000,
    "55 Cancri e": 5000000,
    "Proxima b": 3100000,

    # Cosmic & Speculative
    "Sagittarius A*": 1.0e9,
    "Andromeda Galaxy": 2.5e9,
    "Dyson Sphere": 9.0e9,
    "Wormhole": 1.0e12,
    "Schwarzschild Black Hole": 1.0e12,
}

# --- Explanations & mission context ---
FUTURE_MISSIONS = {
    "LEO": "First step for any mission. Within reach of all modern rockets.",
    "GEO": "Geostationary orbit for communication satellites. Needs precise transfer burns.",
    "Moon": "Apollo’s target. Requires translunar injection and orbit insertion.",
    "Mars": "Target of NASA and SpaceX plans. Needs orbital refueling for human missions.",
    "Venus": "Thick atmosphere and extreme heat. Soviet landers survived minutes.",
    "Mercury": "Close to the Sun. Hard due to gravity well and solar heating.",
    "Near-Earth Asteroid": "Lower gravity target. OSIRIS-REx has already returned samples.",
    "Ceres": "Largest asteroid. Visited by Dawn. Possible resource mining site.",
    "Europa": "Icy moon with subsurface ocean. Europa Clipper launches soon.",
    "Ganymede": "Largest moon in the Solar System. Target of ESA’s JUICE mission.",
    "Callisto": "Radiation-safe compared to Europa/Io. Candidate for outposts.",
    "Titan": "Saturn’s moon with methane lakes. Dragonfly rotorcraft mission planned.",
    "Enceladus": "Water plumes with organics suggest life. Top astrobiology target.",
    "Uranus": "Decadal Survey’s top mission priority. Requires decades of travel.",
    "Neptune": "Only visited by Voyager 2. Proposed orbiters would reveal its system.",
    "Pluto": "New Horizons flyby showed ice mountains. Orbiters proposed but difficult.",
    "Triton": "Captured moon of Neptune with geysers. Possible ocean world.",
    "Halley": "Famous comet. Reached by Giotto in 1986. Returns in 2061.",
    "Oort Cloud": "Comet reservoir far beyond Pluto. Requires advanced propulsion.",
    "Solar Gravitational Lens": "At 550+ AU, the Sun acts as a telescope. Proposed probe concepts exist.",
    "Alpha Centauri": "Nearest star system (4.3 ly). Laser sail concepts proposed.",
    "Proxima b": "Closest exoplanet, in habitable zone. Breakthrough Starshot target.",
    "Barnard's Star": "6 ly away. Only feasible with future interstellar probes.",
    "TRAPPIST-1": "Exoplanet system with 7 worlds. Habitable zone planets discovered.",
    "Kepler-186f": "Earth-sized exoplanet in habitable zone. Currently unreachable.",
    "55 Cancri e": "Super-Earth with lava oceans. Only remote study possible.",
    "Sagittarius A*": "Milky Way’s central black hole. Purely speculative target.",
    "Andromeda Galaxy": "2.5 million ly away. Requires faster-than-light travel.",
    "Dyson Sphere": "Hypothetical megastructure. Target for SETI searches.",
    "Wormhole": "Hypothetical spacetime shortcut. Entirely speculative.",
    "Schwarzschild Black Hole": "Extreme physics environment. Purely theoretical mission.",
}


# --- Functions ---

def list_destinations():
    """Return list of all possible mission destinations."""
    return list(DESTINATIONS.keys())


def required_delta_v(target: str) -> float:
    """Get the required delta-v for a mission target."""
    if target not in DESTINATIONS:
        raise ValueError(f"Unknown destination '{target}'. Try one of: {list_destinations()}")
    return DESTINATIONS[target]


def explain_mission(target: str) -> str:
    """Return explanation/context for the mission target."""
    return FUTURE_MISSIONS.get(target, "No mission context available.")
