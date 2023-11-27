import datetime as dt
# x = dt.datetime.now()
# print(x)

# x = dt.datetime(2023,10,13)
# print(x)

x = dt.datetime.now()
print(x.strftime("%M"))
print(x.strftime("%m"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%B"))
print(x.strftime("%b"))

# %Y - Full Year 2023
# %y - Only Last Two 23
# %B - October
# %b - Oct
# %m - Month No.
# %M - Minute 40
# %H - Hour In 24 Hour Clock
# %I - Hour In 12 Hour Clock
