from makeParentClassCategoryDict import *
import json
d = getSkills()
f = csv.reader(open('./csv/classparentcat.csv'))
j = []
o = open('../static/data/categories.json','w')

ss = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 22:'u', 23:'v', 24:'w', 25:'x', 26:'y', 27:'z', 28:'aa', 29:'ab', 30:'ac',31:'ad', 32:'ae', 33:'af', 34:'ag', 35:'ah', 36:'ai', 37:'aj'}


for row in f:
	try:
		r = row[0].split(';')[:4]


		id = r[0]
		parent = r[1]
		lat = r[2]
		lng = r[3]

		skillset = ss[int(d[parent])]
		j.append({'type':'Feature','id':'01','geometry':{'type':'Point','coordinates':[float(lng), float(lat)]}, "properties":{"skillset":skillset}})

	except:
		pass

json.dump({'type':'featureCollection','features':j}, o)