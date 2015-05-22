import re
m = re.match(r"[M][A][T][C][H] [(]([a-zA-Z0-9]*)[{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}][)][-]", "MATCH (a{wall:'hellasf123',wall1:'hello'})-")
# print m.group(1)
# print m.group(2)
m1 = re.match(r"[\[][\ ]*(([a-zA-Z0-9_]*)[:]([`][a-zA-Z0-9_]+[`])*([{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}])*)*[\]]", "[asd:`A`{a:'sg',s:'cn'}]")
# print m1.group(2)
# print m1.group(3)
# print m1.group(4)
m2=re.match(r"[-][>][(]([a-zA-Z0-9]*)[{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}][)][\ ]*[R][E][T][U][R][N][A-Za-z0-9\ _]", "->(asd{a:'sg',s:'cn'}) RETURN fvv")
# print m2.group(1)
# print m2.group(2)
# print m2.group(2)


# [:`HAS_MATERIAL`]

query="MATCH (a{wall:'hellasf123',wall1:'hello'})-[asd:`A`{a:'sg',s:'cn'}]->(node{a:'node',s:'node'}) RETURN fvv"
mF = re.match(r"[M][A][T][C][H][\ ]*[(]([a-zA-Z0-9]*)[{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}][)][-][\[][\ ]*(([a-zA-Z0-9_]*)[:]([`][a-zA-Z0-9_]+[`])*([{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}])*)*[\]][-][>][(]([a-zA-Z0-9]*)[{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}][)][\ ]*[R][E][T][U][R][N][A-Za-z0-9\ _]",query)
# print mF.group(0)
# print 

print mF.group(1)
print '{'+mF.group(2)+'}'
print 

# print mF.group(3)
# print mF.group(4)
# print mF.group(5)
# print 

print mF.group(6)
print mF.group(7)
print mF.group(8)

print 

# print mF.group(9)

# print 

# print mF.group(10)
# print mF.group(11)

print 
print mF.group(12)
print '{'+mF.group(13)+'}'



matchQuery="[M][A][T][C][H][\ ]*"

leftNode="[(]([a-zA-Z0-9]*)[{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}][)]"

connector1="[-]"

edge="[\[][\ ]*(([a-zA-Z0-9_]*)[:]([`][a-zA-Z0-9_]+[`])*([{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}])*)*([\*]([0-9]*)[\.][\.]([0-9]+))*[\]]"

connector2="[-][>]"

rightNode="[(]([a-zA-Z0-9]*)[{](([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+['][,])*([a-zA-Z0-9]+[:]['][a-zA-Z0-9]+[']){0,1})[}][)]"

returnSt="[\ ]*[R][E][T][U][R][N][A-Za-z0-9\ _]"

mF = re.match(edge,query)


patternStr=matchQuery+leftNode+connector1+edge+connector2+rightNode+returnSt