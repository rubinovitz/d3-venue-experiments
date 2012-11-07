import csv
add = csv.reader(open('csv/ss_classes.csv', 'r'))
for row in add:
	try:
		a = row[0].split(';')[:12]
		id = a[7]
		ticketsTotal = float(a[5])
		ticketsRemaining = float(a[6])
		price = a[4]
		startTime = a[1]
		success = (ticketsTotal - ticketsRemaining) / ticketsTotal
		print success
		print startTime



		print a 
	except:
		pass