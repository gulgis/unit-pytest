from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    point_01 = Point('Brasília', -15.7784, -47.9286)
    assert point_01.get_lat_long() == (-15.7784, -47.9286)
