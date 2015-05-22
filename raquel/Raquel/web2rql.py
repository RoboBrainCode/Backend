# transaction1 = " fetch ( \" ( v : `Concept` { handle : 'wall' } ) - [ e : `HAS_MATERIAL` ] -> ( b { handle : 'wall' } ) \" ) "
# transaction1 = " fetch ( \" ( v : `Concept` { handle : 'wall' } ) - [ e : `HAS_MATERIAL` ] -> ( b: `Media` { handle : 'wall' } ) \" ) "
# transaction1 = " fetch(\"(a{handle:'wall'})-[:`HAS_MATERIAL`]->(v{src:'HAS_AFFORDANCE'})\") "
# transaction2 = " objects =  fetch ( \" ( { handle : 'wall' } ) - [ e : `HAS_MATERIAL` ] -> ( b ) \" ) "


functions = ['fetch','SortBy','imap','ifilter','len','Belief','parents','handle']

def web2rql(transaction):
	query = transaction.split('\n')
	status = False
	for line in query:
		# print line
		found = False
		import re
		usr_defined_check = re.compile(r'=\s*lambda')
		m = usr_defined_check.search(line)
		if m:
			# print 'reached'
			status = regex_check(line,'usr_defined')		#for a stricter check
			if status == False:
				return False

		else:	
			for item in functions:
				if line.find(item) != -1 and found == False:
					found = True
					status = regex_check(line,item)
					if status == False:
						return False
				
	return True

# print web2rql(transaction)

def regex_check(transaction,funcName):
	import re
	# print transaction, funcName
	
	if funcName == 'usr_defined':
		
		'''usr_defined functions can be declared 
			affordance = lambda n: fetch("{handle :'" + n + "'}) - [:`HasAffordance` ] -> (v)") '''

		usr_defined_reg = re.compile(r'\s*\w+\s*'r'=\s*lambda'r'\s+\w+\s*:.*')
		m = usr_defined_reg.search(transaction)
		if m:
			if m.start() == 0:
				return True
			else: 
				return False
		else:
			return False	
	
	##fetch 
	elif funcName == 'fetch':
		# print 'i m in'

		## pure fetch cases
		fetch_reg = re.compile(r'\s*(\b\w*\s*=)?\s*fetch'r'\s*[(]\s*\"\s*[(]\s*(\s*(\w+)?\s*(:\s*`\w+`)?)?\s*({\s*(\w+\s*:\s*\'\w+\'\s*)?})?\s*[)]'r'\s*-\s*[[]\s*\w*\s*((\*([0-9])?\.\.([0-9])?)|(:\s*`\w+`\s*{\s*(\w+\s*:\s*\'\w+\'\s*)?}))?\s*[]]'r'\s*->\s*[(]\s*\w*\s*(:\s*`\w+`)?\s*({\s*(\w+\s*:\s*\'\w+\'\s*)?})?\s*[)]'r'\s*\"\s*[)]')

		m = fetch_reg.search(transaction)
		if m:
			if m.start() == 0:
				return True
			else: 
				return False
		else:
			return False

	elif funcName == 'Belief' or funcName == 'len':
		
		Belief_reg = re.compile(r'\s*(\b\w*\s*=)?\s*Belief|len'r'\s*[(]\s*\w+\s*[)]')
		m = Belief_reg.search(transaction)
		if m:
			if m.start() == 0:
				return True
			else: 
				return False
		else:
			return False

	elif funcName == 'SortBy':
		#SortBy(results,'Belief') #to call
		SortBy_reg = re.compile(r'\s*(\b\w*\s*=)?\s*SortBy'r'\s*[(]\s*\w+\s*,(\'Belief\')?\s*[)]')
		m = SortBy_reg.search(transaction)
		if m:
			if m.start() == 0:
				return True
			else: 
				return False
		else:
			return False

	elif funcName == 'imap':
		'''iter = imap( lambda u: affordances(u) ,objects) 	#to call
			iter.next()'''
		imap_reg = re.compile(r'\s*(\b\w*\s*=)?\s*imap'r'\s*[(]\s*lambda\s+\w+:\s*.*,\s*\w+\s*[)]')
		m = imap_reg.search(transaction)
		if m:
			if m.start() == 0:
				global imap
				from itertools import imap
				return True
			else: 
				return False
		else:
			return False

	elif funcName == 'ifilter':
		'''iter = ifilter( lambda u: len(parents(u)) == 1 ,objects) 	#to call
			iter.next()'''
		imap_reg = re.compile(r'\s*(\b\w*\s*=)?\s*ifilter'r'\s*[(]\s*lambda\s+\w+:\s*.*')		#not complete
		m = imap_reg.search(transaction)
		if m:
			if m.start() == 0:
				global imap
				from itertools import ifilter
				return True
			else: 
				return False
		else:
			return False	
	
	
if __name__ == "__main__":
	# print regex_check(transaction1,'fetch')		
	# print web2rql(transaction1)
	# print web2rql('path = SortBy(results,\'Belief\')')
	# print web2rql("affordance = lambda n: fetch(\"{handle :'\" + n + \"'}) - [:`HasAffordance` ] -> (v)\")")
	# print web2rql("iter = ifilter( lambda u: affordances(u),objects)")
	# print web2rql("objects = fetch(\"({handle:'wall'})-[e*1..2]->({handle:'metal'})\")\nSortBy(objects,'Belief')")
	print	web2rql("len(objects)")