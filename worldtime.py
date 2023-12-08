from datetime import datetime
import pytz

def show_time_in_timezones():
    timezones = ['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']

    utc_time = datetime.utcnow().replace(tzinfo=pytz.utc)

    print("time")

    for timezone in timezones:
        local_time = utc_time.astimezone(pytz.timezone(timezone))
        print(f"{timezone}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

show_time_in_timezones()
