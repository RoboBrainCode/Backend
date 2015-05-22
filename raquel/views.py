# Create your views here.
from django.http import HttpResponse
import unicodedata
import json
from Raquel.processingRQL import *
def rachQuery(request):
	val=unicodedata.normalize('NFKD', dict(request.GET)['query'][0]).encode('ascii','ignore')
	query=val.strip()
	result= processingRQL(query) 
#	print result 
	return HttpResponse(json.dumps({'result':result}), content_type="application/json")


