from datetime import timedelta



def units_between(dt, unit):
    now = datetime.now()
    if dt < now:
        td = now - dt
    else:
        td = dt - now
    seconds = td.total_seconds()
    minutes = seconds / 1440
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    lookup = {
        "seconds": seconds,
        "minutes": minutes,
        "hours": hours,
        "days": days,
        "weeks": weeks
    }
    val = lookup.get(unit)
    if val is None:
        raise ValueError("Unsupported unit. You gave us {}, expected one of: {}".format(unit, ', '.join(lookup.keys())))

    print("There are {:.2f} {} between now and {}".format(val, unit, dt.strftime("%c")))


units_between(datetime(year=2000, month=5, day=20), "months")
