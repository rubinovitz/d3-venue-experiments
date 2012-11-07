import csv
from geopy import geocoders
g = geocoders.Google()
f = csv.reader(open('csv/ss_venues.csv', 'r'))
o = open('data/statedict', 'w')
lastVenue = "null"
venueStateDict = {}
for row in f:
	a = row[0].split('\t')
	print a

	venueName = a[1]
	venueId = a[0]

	if venueName != lastVenue:
		lastVenue = venueName
		for i in a:
			if len(str(i)) == 2:
				try:
					int(i)
				except:
					state = i
			if len(str(i)) == 5:
				try:
					int(i)
					zipcode = i
				except:
					pass
			try:
				int(i[0])
				if len(str(i)) > 9:
					streetAddress = i
			except:
				pass
				


			try:
				#o.write(venueName + ' ' + streetAddress + ' ' + state + ' ' + zipcode + '\n')
				place, (lat, lng) = g.geocode(venueName + ' ' + streetAddress + ' ' + state + ' ' + zipcode )  
				#print "%s: %.5f, %.5f" % (place, lat, lng)  
			#	o.write("%s: %.5f, %.5f" % (place, lat, lng))

			
			except:
				pass
		venueStateDict[venueId] = {'lat':lat,  'lng':lng, 'name': venueName }
		print venueStateDict[venueId]
		print venueStateDict
o.write(venueStateDict)


		