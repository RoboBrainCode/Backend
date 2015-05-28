#bp Create your views here.
from django.http import HttpResponse
import json
from threading import Lock
from weaverGetNode import *
clientLock=Lock()
import unicodedata
def getNode(request):
	val=unicodedata.normalize('NFKD', dict(request.GET)['query'][0]).encode('ascii','ignore')
	val=val.strip()

	number=int(unicodedata.normalize('NFKD', dict(request.GET)['number'][0]).encode('ascii','ignore'))
	print val
	print number
	overwrite=int(unicodedata.normalize('NFKD', dict(request.GET)['overwrite'][0]).encode('ascii','ignore'))

	direction=str(unicodedata.normalize('NFKD', dict(request.GET)['directionVal'][0]).encode('ascii','ignore'))

	lines=""
	# with open('/home/siddhantmanocha/intern/code/Intern/roboBrain/Backend/graph/arctic.json') as f:
	# 	for line in f:
	# 		lines=lines+line.strip()
	with clientLock:
		result1,result2=getNodeEdge(name=val,num=number,overwrite=overwrite,directionVal=direction)
	#result1['nodes'][0]['root']='true'
	list1=result1['nodes']
        result=json.dumps(result1)
	import os.path
	Filename=os.path.abspath(os.path.join('./', os.pardir))+'/Frontend/app/sample_data/arctic.json'
	with open(Filename,'w') as f:
		f.write(result)

	result2['nodes'][0]['root']='true'
#	for i in result1['nodes']:
 #               if i['handle'][0]==val:
  #                      i['root']='true'
#			print 'Root added'
 #                       break

	# return HttpResponse(json.dumps(lines), content_type="application/json")
	return HttpResponse(json.dumps(result2), content_type="application/json")
