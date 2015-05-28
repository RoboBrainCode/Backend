import hashlib
from weaver import client
import json
c = client.Client('172.31.33.213', 2002) # Syslab
# c = client.Client('128.84.167.248', 2002) # Arpit's
# c = client.Client('127.0.0.1', 2002) # Syslab
def _get_unique_id(node_handle):
    m = hashlib.md5(node_handle.encode())
    return str(str(int(m.hexdigest(), 16))[0:16])

def getNodeEdge(name='phone',num=5,overwrite=1,directionVal='F'):
    retVal=dict()
    retVal1=dict()
    if not overwrite:
        lines=""
	import os.path
	Filename=os.path.abspath(os.path.join('./', os.pardir))+'/Frontend/app/sample_data/arctic.json'
#	print Filename        
	with open(Filename,'r') as f:
            for line in f:
                lines=lines+line
        retVal=dict(json.loads(lines))
	retVal1['nodes']=retVal['nodes']
	retVal1['edges']=list()
    else:
        retVal['nodes']=list()
        retVal['edges']=list()
        retVal1['nodes']=list()
        retVal1['edges']=list()

    nodename=name
    onehop=c.traverse(nodename).out_edge({'edgeDirection':directionVal}).node().execute()
#    print onehop
    nodeList=list()
    for nodeDict in retVal['nodes']:
        print '1:',nodeDict['caption']
        nodeList.append(nodeDict['caption'])
    edgeList=list()
    for edgeDict in retVal['edges']:
        edgeList.append(edgeDict['source']+','+edgeDict['target'])

    if not name in nodeList:
        nodeOb=c.get_node(node=name)
        data=dict(nodeOb.properties)
        data['id']=_get_unique_id(name)
        data['caption']=name
	if data['labels'][0][1:8]=='Concept':
		data['type']='Concept'
	else:
		data['type']='Media'
        retVal['nodes'].append(data)
	retVal1['nodes'].append(data)
        nodeList.append(name)
    
    counter=0
    for node in onehop:
        if not node in nodeList:
            print '2:',node
            counter=counter+1
            nodeOb=c.get_node(node=node)
            data=dict(nodeOb.properties)
            data['id']=_get_unique_id(node)
            data['caption']=node
	    if data['labels'][0][1:8]=='Concept':
                data['type']='Concept'
            else:
                data['type']='Media'

            retVal['nodes'].append(data)
            retVal1['nodes'].append(data)
            nodeList.append(node)
            if counter==num:
                break

    edges=c.get_edges(node=nodename,properties=[('edgeDirection',directionVal)])
    for edge in edges:
        props=dict()
        if edge.start_node in nodeList and edge.end_node in nodeList:
	    insertVal=""
	    if directionVal=='F':
		insertVal=(edge.start_node+','+edge.end_node)
	    else:
		insertVal=(edge.end_node+','+edge.start_node)

            if insertVal not in edgeList:
		edgeList.append(insertVal)
                if directionVal=='B':
                    props['source']=_get_unique_id(edge.end_node)
                    props['target']=_get_unique_id(edge.start_node)
                else:
                    props['source']=_get_unique_id(edge.start_node)
                    props['target']=_get_unique_id(edge.end_node)

                props['type']=edge.properties['label'][0]
		print edge.handle
                #props['id']=(edge.handle)
		props['handle']=edge.handle
		print props['source'],props['target']
                retVal['edges'].append(props)
		retVal1['edges'].append(props)
    print len(retVal['edges'])
    return retVal,retVal1

def getNode(name='phone'):
    nodename=name
    nodeOb=c.get_node(node=name)
    return nodeOb.properties
