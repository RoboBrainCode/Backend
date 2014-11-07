#!/usr/bin/python

import boto
import json
from boto.sqs.message import RawMessage

conn = boto.sqs.connect_to_region(
    "us-west-2", 
    aws_access_key_id='<aws access key>', 
    aws_secret_access_key='<aws secret key>')

feed_queue = conn.create_queue('feed_queue')

def add_feed_to_graph(json_feed):
    m = RawMessage()
    m.set_body(json.dumps(json_feed))
    status = feed_queue.write(m)

if __name__ == '__main__':
    add_feed_to_graph({'a': 1})