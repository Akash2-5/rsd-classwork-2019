import times

def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_class_time():
    range1 = times.time_range("2019-10-31 10:00:00","2019-10-31 13:00:00")
    range2 = times.time_range("2019-10-31 10:05:00","2019-10-31 12:55:00",3,600)
    result = times.overlap_time(range1,range2)
    expected = [("2019-10-31 10:05:00","2019-10-31 10:55:00"),("2019-10-31 11:05:00","2019-10-31 11:55:00"),("2019-10-31 12:05:00","2019-10-31 12:55:00")]
    assert result == expected


