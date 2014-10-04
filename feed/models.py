from django.db import models
from djangotoolbox.fields import ListField
from datetime import datetime
from django.db.models.signals import post_save
#from feed.models import BrainFeeds

class BrainFeeds(models.Model):
	toshow = models.BooleanField(default=True)
	feedtype = models.TextField() #originally feedtype -> type
	text = models.TextField()
	source_text = models.TextField()
	source_url = models.TextField()
	media = ListField()
	mediatype = ListField()
	created_at = models.DateTimeField(default=datetime.now())
	hashtags = models.TextField(db_index=True)
	meta = {'indexes':['hashtags']}
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	jsonfeed_id = models.TextField()
<<<<<<< HEAD

=======
	username = models.TextField()

>>>>>>> e4c5a494d5934572b23c3bf688230282fbd927ad
	def to_json(self):
		return {"_id":self.id,
			"toshow":self.toshow,
			"feedtype":self.feedtype,
			"text":self.text,
			"source_text":self.source_text,
			"source_url":self.source_url,
			"media":self.media,
			"mediatype":self.mediatype,
			"created_at":self.created_at.isoformat(),
			"hashtags":self.hashtags,
			"upvotes":self.upvotes,
<<<<<<< HEAD
			"downvotes":self.downvotes,
			"jsonfeed_id":self.jsonfeed_id
=======
			"jsonfeed_id":self.jsonfeed_id,
			"username":self.username
>>>>>>> e4c5a494d5934572b23c3bf688230282fbd927ad
			}

	class Meta:
		db_table = 'brain_feeds'
		get_latest_by = 'created_at'


class JsonFeeds(models.Model):
	feedtype = models.TextField() #originally feedtype -> type
	text = models.TextField()
	source_text = models.TextField()
	source_url = models.TextField()
	mediashow = ListField()
	media = ListField()
	mediatype = ListField()
	mediamap = ListField()
	keywords = ListField()
	graphStructure = ListField()

	created_at = models.DateTimeField()
	hashtags = models.TextField(default=datetime.now, blank=True)
	meta = {'indexes':['hashtags']}
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	username = models.TextField()

	def to_json(self):
		return {"_id":self.id,
			"feedtype":self.feedtype,
			"text":self.text,
			"source_text":self.source_text,
			"source_url":self.source_url,
			"mediashow":self.mediashow,
			"media":self.media,
			"mediatype":self.mediatype,
			"mediamap":self.mediamap,
			"keywords":self.keywords,
			"graphStructure":self.graphStructure,
			"created_at":self.created_at.isoformat(),
			"hashtags":self.hashtags,
			"upvotes":self.upvotes,
			"downvotes":self.downvotes
			"username":self.username
			}

	class Meta:
		db_table = 'json_feeds'

def postSaveJson(**kwargs):
	instance = kwargs.get('instance')
	print instance.to_json()

	#Saving JsonFeed to BrainFeed
	brain_feed = BrainFeeds(
		feedtype=instance.feedtype,
		text=instance.text,
		source_text=instance.source_text,
		source_url=instance.source_url,
		hashtags=instance.hashtags,
		jsonfeed_id=instance.id,
		username=instance.username
	)

	media = []
	mediatype = []

	for mediashow,_media,_mediatype in zip(instance.mediashow,instance.media,instance.mediatype):
		if mediashow.lower() == 'true':
			media.append(_media)
			mediatype.append(_mediatype)
	brain_feed.media = media
	brain_feed.mediatype = mediatype
	brain_feed.save()


	#Saving viewer feed
	"""
	numitem = ViewerFeed.objects.all().count()
	viewer_feed = ViewerFeed(
		id = numitem,
		feedid = brain_feed.id
	)
	viewer_feed.save()
	"""
	#Saving JsonFeed to GraphDB

post_save.connect(postSaveJson, JsonFeeds)

class ViewerFeed(models.Model):
	feedid = models.TextField()
	id = models.IntegerField(db_index=True,primary_key=True)
	meta = {'indexes':['id']}

	def to_json(self):
		return {"_id":self.id,"id":self.id,"feedid":self.feedid}

	class Meta:
		db_table = 'viewer_feeds'
