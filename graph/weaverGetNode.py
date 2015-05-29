import hashlib
from weaver import client
import json
c = client.Client('172.31.33.213', 2002)

def _get_unique_id(node_handle):
    m = hashlib.md5(node_handle.encode())
    return str(str(int(m.hexdigest(), 16))[0:16])

def ProcessNodeData(dataObj,name):
    data=dict(dataObj)
    data['id']=name
    data['caption']=name
    if data['labels'][0][1:8]=='Concept':
        data['type']='Concept'
    else:
        data['type']='Media'
    return data

def ProcessEdgeData():
    props=dict()
    if directionVal=='B':
        props['source']=edge.end_node
        props['target']=edge.start_node
    else:
        props['source']=edge.start_node
        props['target']=edge.end_node

    props['type']=edge.properties['label'][0]
    props['handle']=edge.handle


def getNodeEdge(name='phone',num=5,directionVal='F'):
    retVal=dict(),retVal['nodes']=list(),retVal['edges']=list(),nodeList=list()
    nodename=name
    onehop=c.traverse(nodename).out_edge({'edgeDirection':directionVal}).node().execute()
    nodeOb=c.get_node(node=name)
    retVal['nodes'].append(ProcessNodeData(nodeOb.properties,name))
    counter=0
    nodeList.append(name)

    for node in onehop:
        counter=counter+1
        nodeOb=c.get_node(node=node)
        data=dict(nodeOb.properties)
        retVal['nodes'].append(ProcessData(nodeOb.properties,node))
        nodeList.append(node)
        if counter==num:
            break

    edges=c.get_edges(node=nodename,properties=[('edgeDirection',directionVal)])

    for edge in edges:
        if edge.start_node in nodeList and edge.end_node in nodeList:
            retVal['edges'].append(ProcessEdgeData(edge))

    return retVal
        

def getNode(name='phone'):
    nodename=name
    nodeOb=c.get_node(node=name)
    return nodeOb.properties
