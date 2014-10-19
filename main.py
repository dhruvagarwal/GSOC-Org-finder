from json import loads,dumps

def fetchdetails(db,years,text):
	lines = text.split('\n')
	for line in lines:
		if line == "":
			continue
		details = line.split(',')
		keyword = details[0].split('/')[-1]
		name = details[1]
		ideas = details[-1]
		tags = [det.strip() for det in details[2:-1]]
		tags[0] = tags[0][1:]
		tags[-1] = tags[-1][:-1]
		year = details[0].split('/')[-2][-4:]
		if keyword not in db:
			db[keyword] = {
				'keyword':keyword,
				'name':name,
				'tags':tags,
				'ideas':ideas,
				'count':1
			}
			years[keyword] = [year,]
		else:
			years[keyword].append(year)
			db[keyword]['tags'] = tags
			db[keyword]['count'] += 1

def traverelists():
	db = {}
	years = {}
	for i in range(2009,2015):
		# change year range acc. to req.
		text = open('lists/'+str(i)+'.txt').read()
		fetchdetails(db,years,text)
		print str(i) + ' done!'

	with open('data/db.json','wb+') as f:
		f.write(dumps(db,indent=4))
	with open('data/years.json','wb+') as f:
		f.write(dumps(years,indent=4))
	print 'data fetched and stored successfully !'

def update(year):
	# for future use
	db = loads('data/db.json')
	years = loads('data/years.json')
	text = open('lists/'+str(year)+'.txt').read()
	fetchdetails(db,years,text)
	with open('data/db.json','wb+') as f:
		f.write(dumps(db,indent=4))
	with open('data/years.json','wb+') as f:
		f.write(dumps(years,indent=4))
	print str(year) + ' updated!'

if __name__ == '__main__':
	print 'Welcome to GSOC ORG LIST ORGANISER'
	print 'Process starts in a while, hang tight!'
	traverelists()