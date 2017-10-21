"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#

OPEN = [(200, 34), (200, 32), (200, 30), (400, 28), (300, 26)]
CLOSE = [(200, 15), (200, 15), (200, 15), (400, 11.428), (300, 13.333)]
DEFAULT = {200: 13.5, 300: 20, 400: 27, 600: 40, 1000: 75}


def round_num(raw):
    '''
    Args:
      raw: floating point value of distance / time
    Returns:
       rounds up or down the minutes from raw and returns as float
    '''
    # raw - decimal value
    hour = int(raw)
    # minutes rounded up
    minutes = ((raw - hour) * 60)
    minutes = (round(minutes) / 60)
    return (hour + minutes)


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    time = 0
    dist = control_dist_km
    arr_date = arrow.get(brevet_start_time)
    if(dist > brevet_dist_km):
        dist = brevet_dist_km
    for distance, speed in OPEN:
        if(dist > 0):
            if(dist > distance):
                raw = (distance / speed)
                time += round_num(raw)
                dist -= distance
            else:
                raw = (dist / speed)
                time += round_num(raw)
                dist -= distance
    return arr_date.shift(hours=time).isoformat()


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    time = 0
    dist = control_dist_km
    arr_date = arrow.get(brevet_start_time)
    if(dist >= brevet_dist_km):
        time = DEFAULT[brevet_dist_km]
    else:
        for distance, speed in CLOSE:
            if(dist > 0):
                if(dist > distance):
                    raw = (distance / speed)
                    time += round_num(raw)
                    dist -= distance
                else:
                    raw = (dist / speed)
                    time += round_num(raw)
                    dist -= distance
    return arr_date.shift(hours=time).isoformat()

    return arrow.now().isoformat()
