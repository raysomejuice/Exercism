import datetime

DELTA = datetime.timedelta(seconds=1e9)


def add(moment: datetime.datetime) -> datetime.datetime:
    """Determine the date and time one gigasecond after a certain date.
    
    :param moment: datetime - an entered date and time.
    :return: datetime - the date and time one billion seconds later.
    """
    return moment + DELTA
