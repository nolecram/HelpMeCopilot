import datetime

def calculate_days_between_dates(start_date, end_date):
    """
    Calculates the number of days between two dates.

    Args:
        start_date (datetime.date): The start date.
        end_date (datetime.date): The end date.

    Returns:
        int: The number of days between the start and end dates.
    """
    delta = end_date - start_date
    return delta.days
