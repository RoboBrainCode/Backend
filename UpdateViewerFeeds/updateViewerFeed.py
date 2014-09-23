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
for url in different_projects:
	 feeds_each_project[url] = brain_feeds.find({'source_url':url}).sort('created_at',pm.DESCENDING)
feeds_to_push = []
overall_counter = 0
level = 0
while True:
	toBreak = True
	for url in different_projects:
		if feeds_each_project[url].count() > level:
			print url
			new_feed = {}
			new_feed['_id'] = overall_counter
			new_feed['feedid'] = feeds_each_project[url][level]['_id'].__str__()
			feeds_to_push.append(new_feed)
			overall_counter += 1
			toBreak = False
	if toBreak:
		break
	level += 1


#db.create_collection('copy_viewer')

viewer_feeds = db['viewer_feeds']
viewer_feeds.drop()
viewer_feeds.insert(feeds_to_push)


