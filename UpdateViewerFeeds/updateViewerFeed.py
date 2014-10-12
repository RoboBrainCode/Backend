import ConfigParser
import pymongo as pm
from datetime import datetime 
import numpy as np
import importlib
import sys
sys.path.insert(0,'/var/www/Backend/Backend/')

def readConfigFile():
    """
        Reading the setting file to use.
        Different setting files are used on Production and Test robo brain
    """

    global setfile
    config = ConfigParser.ConfigParser()
    config.read('/tmp/backend_uwsgi_setting')
    env = config.get('uwsgi','env')
    setting_file_name = env.strip().split('.')[1]
    setfile = importlib.import_module(setting_file_name)	

def establishConnection():
    """
        Establishes connection to remote db
    """
    
    global brain_feeds, viewer_feeds
    client = pm.MongoClient(host,port)
    db = client[dbname]
    brain_feeds = db['brain_feeds']
    viewer_feeds = db['viewer_feeds']

def viewerFeedsUpdate():
    """
        Sorts Brain Feeds on Basis of score and pushes them to ViewerFeeds table
    """

    feeds_ordered = brain_feeds.find().sort('score',pm.DESCENDING)
    overall_counter = 0
    feeds_to_push = []
    first_time = True

    for feeds in feeds_ordered:
        new_feed = {}
        new_feed['_id'] = overall_counter
        new_feed['feedid'] = feeds['_id'].__str__()
        feeds_to_push.append(new_feed)
        overall_counter += 1
        print "{0}  {1} {2}".format(overall_counter,feeds['score'],feeds['source_url'])
        if overall_counter % 100 == 0:
            if first_time:
                viewer_feeds.drop()
                first_time = False
            viewer_feeds.insert(feeds_to_push)
            feeds_to_push = []
            raw_input('pressenter')

def viewerFeedsUpdate_deprecated():
    """
        DEPRECATED
        Equally represent each project
    """
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

if __name__=="__main__":
    global host, dbname, port, setfile, brain_feeds, viewer_feeds

    # Reading the setting file for db address
    readConfigFile()
    host = setfile.DATABASES['default']['HOST']
    dbname = setfile.DATABASES['default']['NAME']
    port = int(setfile.DATABASES['default']['PORT'])
    
    # Extablishing connection to remote db 
    establishConnection()
    
    viewerFeedsUpdate()
