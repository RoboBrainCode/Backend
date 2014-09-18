from django.db import models
from djangotoolbox.fields import ListField
from datetime import datetime
from django.db.models.signals import post_save

class BrainFeeds(models.Model):
	toshow = models.BooleanField(default=True)
	feedtype = models.TextField() #originally feedtype -> type
	text = models.TextField()
	media = ListField()
	source_text = models.TextField()
	source_url = models.TextField()
	hashtags = models.TextField(db_index=True)
	created_at = models.DateTimeField()
	meta = {'indexes':['hashtags']}
	jsonfeed_id = models.TextField()
	upvotes = models.IntegerField(default=0)

	def to_json(self):
		return {"_id":self.id,"toshow": self.toshow, "type":self.feedtype,"feedtype":self.feedtype,"text":self.text,"media":self.media,"source_text":self.source_text,"source_url":self.source_url,"hashtags":self.hashtags,"created_at":self.created_at.isoformat(),"jsonfeed_id":self.jsonfeed_id,"upvotes":self.upvotes}
		
	class Meta:
		db_table = 'brain_feeds'
		get_latest_by = 'created_at'


class JsonFeeds(models.Model):
	feedtype = models.TextField() #originally feedtype -> type
	text = models.TextField()
	media = ListField()
	mediamap = ListField()
	keywords = ListField()
	source_text = models.TextField()
	source_url = models.TextField()
	mediashow = ListField()
	created_at = models.DateTimeField()
	hashtags = models.TextField(default=datetime.now, blank=True)
	meta = {'indexes':['hashtags']}
	nodes = ListField()
	factors = ListField()
	upvotes = models.IntegerField(default=0)

	def to_json(self):
		return {"_id":self.id,"type":self.feedtype,"feedtype":self.feedtype,"text":self.text,"media":self.media,"mediamap":self.mediamap,"keywords":self.keywords,"source_text":self.source_text,"source_url":self.source_url,"mediashow":self.mediashow,"hashtags":self.hashtags,"created_at":self.created_at.isoformat(),"nodes":self.nodes,"factors":self.factors,"upvotes":self.upvotes}
	
	class Meta:
		db_table = 'json_feeds'

def postSaveJson(**kwargs):
	instance = kwargs.get('instance')
	print instance.to_json()
	#Extra stuff

post_save.connect(postSaveJson, JsonFeeds)

class ViewerFeed(models.Model):
	feedid = models.TextField()
	id = models.IntegerField(db_index=True,primary_key=True)
	meta = {'indexes':['id']}

	def to_json(self):
		return {"_id":self.id,"id":self.id,"feedid":self.feedid}

	class Meta:
		db_table = 'viewer_feeds'
