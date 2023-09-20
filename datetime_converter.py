import datetime


def tz_to_timestamp(tz):
    try:
        return datetime.datetime.strptime(tz, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError as e:
        print(tz)
