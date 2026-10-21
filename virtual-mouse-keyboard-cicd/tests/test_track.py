import math
import track


def test_distance_is_zero_for_same_point():
    assert track.get_distance(((0.5, 0.5), (0.5, 0.5))) == 0


def test_right_angle_is_approximately_90_degrees():
    assert math.isclose(track.getangle((0, 0), (1, 0), (1, 1)), 90.0)
