from __future__ import annotations

from orbital_playground.delta_v import hohmann_delta_v, plane_change_delta_v

def test_hohmann_raising_6778_to_7078():
    dv1, dv2, dvt = hohmann_delta_v(6778.0, 7078.0)
    assert abs(dvt - 0.16426) < 1e-3  # km/s

def test_plane_change_10deg_at_7p7():
    dv = plane_change_delta_v(7.7, 10.0)
    assert abs(dv - 1.341) < 0.02
