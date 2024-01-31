import datetime

def test_calculate_days_between_dates():
    # Test case 1: Start date and end date are the same
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 1, 1)
    assert calculate_days_between_dates(start_date, end_date) == 0

    # Test case 2: Start date is before end date
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 1, 10)
    assert calculate_days_between_dates(start_date, end_date) == 9

    # Test case 3: Start date is after end date
    start_date = datetime.date(2022, 1, 10)
    end_date = datetime.date(2022, 1, 1)
    assert calculate_days_between_dates(start_date, end_date) == -9

    # Test case 4: Start date and end date are in different years
    start_date = datetime.date(2021, 12, 31)
    end_date = datetime.date(2022, 1, 1)
    assert calculate_days_between_dates(start_date, end_date) == 1

    # Test case 5: Start date and end date are in different months
    start_date = datetime.date(2022, 1, 31)
    end_date = datetime.date(2022, 2, 1)
    assert calculate_days_between_dates(start_date, end_date) == 1

    # Test case 6: Start date and end date are in different years and months
    start_date = datetime.date(2021, 12, 31)
    end_date = datetime.date(2022, 2, 1)
    assert calculate_days_between_dates(start_date, end_date) == 32

    print("All test cases passed!")

test_calculate_days_between_dates()import datetime

def test_calculate_days_between_dates():
    # Test case 1: Start date and end date are the same
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 1, 1)
    assert calculate_days_between_dates(start_date, end_date) == 0

    # Test case 2: Start date is before end date
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2022, 1, 10)
    assert calculate_days_between_dates(start_date, end_date) == 9

    # Test case 3: Start date is after end date
    start_date = datetime.date(2022, 1, 10)
    end_date = datetime.date(2022, 1, 1)
    assert calculate_days_between_dates(start_date, end_date) == -9

    # Test case 4: Start date and end date are in different years
    start_date = datetime.date(2021, 12, 31)
    end_date = datetime.date(2022, 1, 1)
    assert calculate_days_between_dates(start_date, end_date) == 1

    # Test case 5: Start date and end date are in different months
    start_date = datetime.date(2022, 1, 31)
    end_date = datetime.date(2022, 2, 1)
    assert calculate_days_between_dates(start_date, end_date) == 1

    # Test case 6: Start date and end date are in different years and months
    start_date = datetime.date(2021, 12, 31)
    end_date = datetime.date(2022, 2, 1)
    assert calculate_days_between_dates(start_date, end_date) == 32

    print("All test cases passed!")

test_calculate_days_between_dates()