import csv
import json
f = csv.reader(open('csv/ss_parent_classes.csv', 'r'))
o = open('../static/data/venues-per-state.json', 'w')


lastVenue = "null"
d = {}
for row in f:
	a = row[0].split(';')
	try:
		if len(a[9]) == 4:
			state = a[9][1:3]
			try:
				d[state] = d[state] + 1
			except:
				d[state] = 1
	except:
		pass

print d
o.close()