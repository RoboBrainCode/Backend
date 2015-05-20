# # Create your views here.
from django.http import HttpResponse
import unicodedata
import json
from Raquel.raquel import *
def rachQuery(request):
	val=unicodedata.normalize('NFKD', dict(request.GET)['query'][0]).encode('ascii','ignore')
	query=val.strip()
	val=unicodedata.normalize('NFKD', dict(request.GET)['qtype'][0]).encode('ascii','ignore')
	qtype=val.strip()
	print query
	print qtype
	return HttpResponse(json.dumps({'success':1}), content_type="application/json")


