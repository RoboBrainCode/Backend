import pymongo as pm

import sys
sys.path.insert(0,'/var/www/Backend/Backend/')
import settings as setfile
host = setfile.DATABASES['default']['HOST']
dbname = setfile.DATABASES['default']['NAME']
port = int(setfile.DATABASES['default']['PORT'])



client = pm.MongoClient(host,port)
db = client[dbname]
brain_feeds = db['brain_feeds']
different_projects = brain_feeds.distinct('source_url')
different_projects = sorted(different_projects,key=len) 
feeds_each_project = {}
feeds_count = {}
for url in different_projects:
	 feeds_each_project[url] = brain_feeds.find({'source_url':url},{'created_at':1}).sort('created_at',pm.DESCENDING)
	 feeds_count[url] = feeds_each_project[url].count()

feeds_to_push = []
overall_counter = 0
level = 0
viewer_feeds = db['viewer_feeds']
first_time = True
while True:
	toBreak = True
	remaining_projects = []
	for url in different_projects:
		if feeds_count[url] > level:
			print url
			new_feed = {}
			new_feed['_id'] = overall_counter
			new_feed['feedid'] = feeds_each_project[url][level]['_id'].__str__()
			feeds_to_push.append(new_feed)
			overall_counter += 1
			remaining_projects.append(url)
			toBreak = False
			if overall_counter % 100 == 0:
				if first_time:
					viewer_feeds.drop()
					first_time = False
				viewer_feeds.insert(feeds_to_push)
				feeds_to_push = []
	different_projects = remaining_projects

	if toBreak:
		break


	level += 1
