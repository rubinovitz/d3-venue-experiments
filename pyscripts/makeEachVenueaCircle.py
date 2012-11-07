import csv
import json
f = csv.reader(open('csv/ss_venues.csv', 'r'))
o = open('data/states.json', 'w')


lastVenue = "null"
d = {}
for row in f:
	a = row[0].split(';')
	try:
		d[a[0]] = {'name': a[1], 'lat':a[5], 'lng':a[6]}
	except:
		pass
print d
j = "{\"type\":\"FeatureCollection\",\"features\":["
for key in d:
	s = "\"type\":\"Feature\""
	s += "'id':"+key +"'geometry':{'type':'Point','coordinates':'['"+d[key]['lat']+","+d[key]['lng']+"]},'properties':{'name':'Alabama','population':4447100}},"
	j += s
j = j + "]}"

json.dumps(j,o)


# put out Json indexed by state with all the data
add = csv.reader(open('csv/ss_classes.csv', 'r'))
for row in add:
	try:
		a = row[0].split(';')[:12]
	#	print a 
	except:
		pass

		

o.close()