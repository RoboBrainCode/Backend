# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feed.models import JsonFeeds
from rest_api.serializer import FeedSerializer
from datetime import datetime    

@api_view(['GET', 'POST'])
def feed_list(request):
    #List all snippets, or create a new snippet.
    if request.method == 'GET':
        feeds = JsonFeeds.objects.all()
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FeedSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



