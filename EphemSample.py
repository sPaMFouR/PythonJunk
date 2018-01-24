##############################################################
#       Convert RA, DEC, LAT, LONG, UT Into ALT, AZ          #
############################################################## 


# COORDINATE CLASSES:

# 1) Equatorial

#     ha    -  Right Ascension, in DEGREES
#     dec   -  Declination, in DEGREES
#     epoch -  Epoch Of The Coordinate

# 2) Ecliptic

#     lon   -  Ecliptic Longitude (+E)
#     lat   -  Ecliptic Latitude (+N)

# 3) Galactic

#     lon   -  Galactic Longitude (+E)
#     lat   -  Galactic Latitude (+N)
#     epoch -  Epoch Of The Coordinate

# SAMPLE CONVERSIONS

# lowell = ephem.Observer()
# lowell.lon = '-111:32.1'
# lowell.lat = '35:05.8'
# lowell.elevation = 2198
# lowell.date = '1986/3/13'
# j = ephem.Jupiter()
# j.compute(lowell)
# print(j.circumpolar)
# False
# print(j.neverup)
# False
# print('%s %s' % (j.alt, j.az))
# 0:57:44.7 256:41:01.3


# lowell.compute_pressure()
# lowell.pressure
# 775.6025138640499
# boston = ephem.city('Boston')
# print('%s %s' % (boston.lat, boston.lon))
# 42:21:30.4 -71:03:35.2


# sitka = ephem.Observer()
# sitka.date = '1999/6/27'
# sitka.lat = '57:10'
# sitka.lon = '-135:15'
# m = ephem.Mars()
# print(sitka.next_transit(m))
# 1999/6/27 04:22:45
# print('%s %s' % (m.alt, m.az))
# 21:18:33.6 180:00:00.0
# print(sitka.next_rising(m, start='1999/6/28'))
# 1999/6/28 23:28:25
# print('%s %s' % (m.alt, m.az))
# -0:00:05.8 111:10:41.6


# previous_transit()
# next_transit()
# previous_antitransit()
# next_antitransit()
# previous_rising()
# next_rising()
# previous_setting()
# next_setting()


# line1 = "IRIDIUM 80 [+]"
# line2 = "1 25469U 98051C   09119.61415140 -.00000218  00000-0 -84793-4 0  4781"
# line3 = "2 25469  86.4029 183.4052 0002522  86.7221 273.4294 14.34215064557061"
# iridium_80 = ephem.readtle(line1, line2, line3)
# boston.date = '2009/5/1'
# info = boston.next_pass(iridium_80)
# print("Rise time: %s azimuth: %s" % (info[0], info[1]))
# Rise time: 2009/5/1 00:22:15 azimuth: 104:36:16.0
# Info is a six element tuple
# 0  Rise time
# 1  Rise azimuth
# 2  Maximum altitude time
# 3  Maximum altitude
# 4  Set time
# 5  Set azimuth


# madrid = ephem.city('Madrid')
# madrid.date = '1978/10/3 11:32'
# print(madrid.sidereal_time())
# 12:04:28.09
# ALT,AZ into RA, DEC ->
# ra, dec = madrid.radec_of(0, '90')
# print('%s %s' % (ra, dec))
# 12:05:35.12 40:17:49.8


# d1 = ephem.next_equinox('2000')
# print(d1)
# 2000/3/20 07:35:17
# d2 = ephem.next_solstice(d1)
# print(d2)
# 2000/6/21 01:47:51
# t = d2 - d1
# print("Spring lasted %.1f days" % t)
# Spring lasted 92.8 days


# a = ephem.degrees('180:00:00')
# print(a)
# 180:00:00.0
# a
# 3.141592653589793
# print("180° is %f radians" % a)
# 180° is 3.141593 radians
# h = ephem.hours('1:00:00')
# deg = ephem.degrees(h)
# print("1h right ascension = %s°" % deg)
# 1h right ascension = 15:00:00.0°



#Describes a position on Earth’s surface.

#Pass to the compute() method of a Body.

#These are the attributes you can set:
#date — Date and time
#epoch — Epoch for astrometric RA/dec
#lat — Latitude (+N)
#lon — Longitude (+E)
#elevation — Elevation (m)
#temp — Temperature (°C)
#pressure — Atmospheric pressure (mBar)

#The date defaults to now().

#The epoch defaults to '2000'.

#The temp defaults to 25°C.

#The pressure defaults to 1010mBar.

#Other attributes default to zero.


import ephem

hct = ephem.observer()
hct.lon = "78:57:51"
hct.lat = "32:46:46"
hct.elevation = "4500"
hct.date = raw_input("What's the date?")
supernova = ephem.readdb("ASASSN14dq, f|Y|IIP, 21:57:59.9 24:16:8.1")
supernova.compute(hct.date)
print supernova.alt, supernova.az

