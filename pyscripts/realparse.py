import csv
import json

f = csv.reader(open('csv/classes.csv'))
j = []
o = open('../static/data/us-venues.json','w')





for row in f:
	try:
		r = row[0].split(';')[:8]
		lat = r[-2]
		lng = r[-1]
		try:
			print lat
			print lng
			float(lat)
			float(lng)
			j.append({'type':'Feature','id':'01','geometry':{'type':'Point','coordinates':[float(lng), float(lat)]}, 'properties':{}})
		except:
			pass
	except:
		pass

json.dump({'type':'featureCollection','features':j}, o)


def calculateSuccess():
	pass