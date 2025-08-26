# orbital_playground/visualize.py
import matplotlib.pyplot as plt

def plot_dv_budget(required_mps: float, available_mps: float, title: str, out: str | None = None) -> None:
    """Simple bar chart comparing required vs available Δv (m/s)."""
    labels = ["Required", "Available"]
    vals = [required_mps, available_mps]

    plt.figure(figsize=(5, 4))
    plt.bar(labels, vals)
    plt.ylabel("Δv (m/s)")
    plt.title(title)
    plt.tight_layout()
    if out:
        plt.savefig(out, dpi=150)
    else:
        plt.show()
