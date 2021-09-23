import datetime, pytz

# get local date and time
local_dt = datetime.datetime.now()
print(local_dt)

# get the current date and time in UTC
date_time_utc = datetime.datetime.now(tz=pytz.UTC)

# convert local_dt to 'Asia/Manila' timezone
manila_dt = local_dt.astimezone(pytz.timezone('Asia/Manila'))
print(manila_dt)

# format and beautify the result
manila_dt = manila_dt.strftime('%d %B, %Y')
print(manila_dt)

# get a list of all timezones
# for timezone in pytz.all_timezones:
#     print(timezone) 