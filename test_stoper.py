from stoper import Time
from pytest import raises


def test_create_typical_time():
    time = Time(50, 40, 30)
    assert time.get_hours() == 50
    assert time.get_minutes() == 40
    assert time.get_seconds() == 30


def test_create_invalid_time():
    with raises(ValueError):
        Time(-50, 40, 30)


def test_add_times():
    time1 = Time(50, 40, 30)
    time2 = Time(40, 45, 30)
    time3 = time1 + time2
    assert str(time3) == '91:26:00'


def test_str_time():
    time = Time(0, 4, 6)
    assert str(time) == '0:04:06'


def test_sub_time_valid():
    time1 = Time(10, 20, 10)
    time2 = Time(9, 30, 30)
    assert str(time1-time2) == '0:49:40'


def test_sub_time_invalid():
    time1 = Time(0, 20, 0)
    time2 = Time(0, 30, 0)
    with raises(ValueError):
        time1 - time2


def test_add_hours():
    time1 = Time(2, 80, 4)
    time1.add_hours(50)
    assert str(time1) == '53:20:04'


def test_add_minutes():
    time1 = Time(6, 80, 70)
    time1.add_minutes(50)
    assert str(time1) == '8:11:10'


def test_add_seconds():
    time1 = Time(0, 0, 3600)
    time1.add_seconds(3600)
    assert str(time1) == '2:00:00'


def test_sub_hours():
    time1 = Time(6, 50, 70)
    time1.sub_hours(4)
    assert str(time1) == '2:51:10'


def test_sub_hours_invalid():
    time1 = Time(6, 50, 70)
    with raises(ValueError):
        time1.sub_hours(8)


def test_sub_minutes():
    time1 = Time(6, 50, 00)
    time1.sub_minutes(180)
    assert str(time1) == '3:50:00'


def test_sub_minutes_invalid():
    time1 = Time(2, 30, 00)
    with raises(ValueError):
        time1.sub_minutes(180)


def test_sub_seconds():
    time1 = Time(0, 50, 00)
    time1.sub_seconds(200)
    assert str(time1) == '0:46:40'


def test_sub_seconds_invalid():
    time1 = Time(0, 50, 00)
    with raises(ValueError):
        time1.sub_seconds(5000)
