"""
join parent class to category id as a dictionary
"""

import csv

def getSkills():
	d = {}
	o = csv.reader(open('./csv/ids_of_classes.csv'))
	for row in o:
		try:
			r = row[0].split(';')[:2]
			classId = r[0]
			skill = r[1]
			try:
				int(classId)
				int(skill)
				d[classId] = skill
			except:
				pass
		except:
			pass

	return d