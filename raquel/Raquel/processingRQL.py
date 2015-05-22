from web2rql import web2rql
from raquel import *
import sys
def processingRQL(query):
	if web2rql(query):
		dumpFile = 'output.txt'			# filename 
		outFile = open(dumpFile, 'w')
		orig_stdout = sys.stdout
		sys.stdout = outFile
		
		exec(query)
		# print locals()	#{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 0, '__package__': None}
		sys.stdout = orig_stdout
		outFile.close()

		outFile = open(dumpFile, 'r')
		val = outFile.read()
		outFile.close()
		val = val.replace('\n','<br>')
		return val
	else:
		return 'invalid query'

if __name__ == "__main__":
	print processingRQL("fetch(\"({handle:'wall'})-[e*1..2]->({handle:'metal'})\")")	
