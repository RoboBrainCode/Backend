#!/usr/bin/python

import boto
import json
import traceback
from boto.sqs.message import RawMessage
from bson import json_util

conn = boto.sqs.connect_to_region(
    "us-west-2", 
    aws_access_key_id='AKIAIDKZIEN24AUR7CJA', 
    aws_secret_access_key='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')

feed_queue = conn.create_queue('feed_queue')

def add_feed_to_queue(json_feed):
    m = RawMessage()
    try:
        m.set_body(json.dumps(json_feed, default=json_util.default))
        feed_queue.write(m)
    except Exception, e:
        print traceback.format_exc()
        print json_feed

if __name__ == '__main__':
    add_feed_to_queue({
        "username" : "arzav",
        "_id": "546e6a2f5caae434656bbc36",
        "feedtype" : "",
        "mediashow" : [ ],
        "text" : "#Simhat_Torah is a synonym of  #Rejoicing_in_the_Law",
        "hashtags" : " simhat_torah rejoicing_in_the_law", 
        "mediatype" : [ ],
        "source_url" : "http://wordnet.princeton.edu/",
        "source_text" : "WordNet",
        "mediamap" : [ ],
        "media" : [ ],
        "keywords": ["Simhat_Torah","Rejoicing_in_the_Law","synonym","wordnet"], 
        "upvotes" : 0, 
        "graphStructure": ["#same_synset: #0 -> #1", "#same_synset: #1 -> #0"]})
