# orbital_playground/__init__.py

"""
Orbital Playground – minimal, Mission Mangal–style tools.
"""

# Core physics
from .delta_v import hohmann_delta_v

# Rocket utilities
from .rockets import rocket_delta_v, list_rockets, get_rocket, ROCKETS

# Mission planning
from .missions import (
    DESTINATIONS,
    FUTURE_MISSIONS,
    list_destinations,
    required_delta_v,
    explain_mission,
)

__all__ = [
    # Core
    "hohmann_delta_v",
    # Rockets
    "rocket_delta_v",
    "list_rockets",
    "get_rocket",
    "ROCKETS",
    # Missions
    "DESTINATIONS",
    "FUTURE_MISSIONS",
    "list_destinations",
    "required_delta_v",
    "explain_mission",
]

__version__ = "0.1.0"
