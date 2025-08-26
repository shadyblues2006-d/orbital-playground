# orbital_playground/cli.py

import sys
from .rockets import list_rockets, get_rocket
from .missions import list_destinations, required_delta_v, explain_mission


def _pick(prompt: str, options: list[str]) -> str:
    """Show numbered options and return the chosen name."""
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    raw = input("\nType number: ").strip()
    try:
        idx = int(raw) - 1
        if 0 <= idx < len(options):
            return options[idx]
    except ValueError:
        pass
    print("Invalid choice. Exiting.")
    sys.exit(1)


def main() -> None:
    print("Orbital Playground — Mini Mission Planner")
    print("=" * 48)

    # 1) pick rocket
    rockets = list_rockets()
    rocket_name = _pick("\nAvailable Rockets:", rockets)
    rocket = get_rocket(rocket_name)
    dv_av_mps = rocket.delta_v()  # m/s

    # 2) pick destination
    destinations = list_destinations()
    dest_name = _pick("\nDestinations:", destinations)
    dv_req_mps = required_delta_v(dest_name)

    # 3) results
    print("\nMission Analysis")
    print("-" * 48)
    print(f"Rocket:       {rocket.name}")
    print(f"Destination:  {dest_name}")
    print(f"→ Rocket Δv:   {dv_av_mps:.0f} m/s")
    print(f"→ Required Δv: {dv_req_mps:.0f} m/s")

    if dv_av_mps >= dv_req_mps:
        print("Result: ✅ Mission possible with this rocket.")
    else:
        short = (dv_req_mps - dv_av_mps) / 1000.0
        print(f"Result: ❌ Not possible (short by {short:.2f} km/s).")

    # 4) context paragraph
    print("\nMission Context")
    print("-" * 48)
    print(explain_mission(dest_name))


if __name__ == "__main__":
    main()
