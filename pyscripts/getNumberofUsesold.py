import csv
import datetime


"""
Returns the day of the week of any given date
args:
	y: int, year
	m: int, month
	d: int, day
"""
def dayOfWeek(y, m, d):
	return datetime.datetime(y, m, d).weekday()

f = csv.reader(open('csv/ss_classes.csv', 'r'))
for row in f:
	#try:
	a = row[0].split(';')[:11]
	print a
	print a[1]
	dateSplit = a[1].split('-')
	y = int(dateSplit[0])
	m = int(dateSplit[1])
	d =  int(dateSplit[2][:2])

#	except:
#		pass
	print dayOfWeek(y, m, d)







#DS
# d = { venue_id { monday: [] , tuesday: [], wednesday: []}}