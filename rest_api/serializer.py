from django.forms import widgets
from rest_framework import serializers
from feed.models import JsonFeeds
from djangotoolbox.fields import ListField,DictField

import drf_compound_fields.fields as drf
from datetime import datetime

class TagFieldS(serializers.Serializer):
    media = serializers.CharField(required=False) 
  
	
class FeedSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    feedtype = serializers.CharField(required=False)
    text = serializers.CharField(required=False)
    source_text = serializers.CharField(required=False)
    source_url = serializers.CharField(required=False)
    hashtags = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    upvotes = serializers.IntegerField(required=False)                     
    media = drf.ListField(serializers.CharField(),required=False)# serializers.CharField(required=False,many=True)
    mediamap = drf.ListField(serializers.CharField(),required=False)    
    mediatype = drf.ListField(serializers.CharField(),required=False)
    keywords = drf.ListField(serializers.CharField(),required=False)
    graphStructure = drf.ListField(serializers.CharField(),required=False)
    mediashow = drf.ListField(serializers.CharField(),required=False)
    username = serializers.CharField(required=False)
    nodeProps= drf.DictField(drf.DictField(serializers.CharField()),required=False)
    edgeProps= drf.DictField(drf.DictField(serializers.CharField()),required=False)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            #instance.feedtype = attrs.get('feedtype', instance.feedtype)
            #instance.code = attrs.get('code', instance.code)
            #instance.linenos = attrs.get('linenos', instance.linenos)
            #instance.language = attrs.get('language', instance.language)
            #instance.style = attrs.get('style', instance.style)
            return instance

        # Create new instance
        attrs['created_at']=datetime.now()
        return JsonFeeds(**attrs)
