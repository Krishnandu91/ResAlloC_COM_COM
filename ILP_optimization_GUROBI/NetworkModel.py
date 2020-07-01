# Importing the packages

from gurobipy import *
from itertools import chain,combinations
import math

# Defining the powerset Function

def powerset(V):
    return chain.from_iterable(combinations(V, r) for r in range(len(V)+1))

# Defining the function to calculate the euclidean distance between two lat lon points

def funHaversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    # Radius of earth in kilometers is 6371
    m = 1000 * 6371* c
    # print(" dist: " + str(km))
    return m  
        
#List of lat lon between n points

ll=[
[23.559106, 87.284918],
[23.555351, 87.290684],
[23.550067, 87.285045],
[23.546400, 87.292909],
[23.555209, 87.298574],
[23.548584, 87.300969],
[23.536040, 87.295786],
[23.535683, 87.271865],
[23.549808, 87.269972],
[23.557508, 87.274820],
[23.563244, 87.280249],
[23.565731, 87.290716],
[23.568418, 87.298785],
[23.572856, 87.290914],
[23.577394, 87.298893],
[23.572225, 87.282966],
[23.571980, 87.277705],
[23.582372, 87.275742],
[23.566703, 87.266364],
[23.561511, 87.253375]
]

# Inputs 
'''
 Provide different Scenarios here
'''
V = 18
R = 4
C = 4
G = 4

# Dictionary of euclidean distance

dij={}
for i in range(V):
    for j in range(V):
        dij[i,j]=funHaversine(ll[i][0],ll[i][1],ll[j][0],ll[j][1])/1000

# List of distances between n points

d=[
[999, 0.7, 1.9 ,2.7 ,1.5, 1.0, 1.4, 3.2, 1.2, 2.4, 1.9, 3.2 ,4.1 ,3.4, 3.6, 2.4, 4.0, 5.4, 4.1, 4.7],
[0.7 ,999 ,1.4 ,2.8 ,1.6, 1.3, 3.0, 3.8, 1.0, 2.5, 2.9 ,4.2 ,4.2 ,3.3 ,3.4 ,2.1 ,2.8 ,4.1 ,3.9, 5.0],
[1.9, 1.4, 999 ,3.5 ,2.5, 2.0, 3.6, 4.1 ,2.1 ,3.2, 3.5, 4.8, 2.6, 3.6, 3.9, 2.5, 1.7 ,3.1 ,2.6 ,4.9],
[2.7 ,2.8 ,3.5 ,999 ,1.9, 3.4, 5.7 ,7.6 ,5.9 ,2.0 ,5.2 ,6.4 ,2.1 ,7.2 ,6.9 ,5.4 ,3.0, 4.9, 4.5 ,7.4],
[1.5, 1.6, 2.5, 1.9, 999,2.5 ,4.3, 6.3, 3.7, 2.3, 3.9, 5.0, 2.7, 5.9, 6.2, 4.8, 3.7, 5.0, 5.1, 6.9],
[1.0 ,1.3, 2.0 ,3.4 ,2.5 ,999,1.8, 3.8, 2.1, 2.1 ,1.7 ,2.9 ,3.6, 4.3, 4.5 ,3.3 ,4.5 ,6.3 ,5.2, 5.6],
[1.4 ,3.0, 3.6, 5.7, 4.3, 1.8 ,999 ,2.2 ,3.0 ,3.1, 0.9, 1.9 ,5.4 ,2.5, 3.3, 4.8, 5.1, 6.4 ,5.1 ,3.8],
[3.2 ,3.8 ,4.1 ,7.6, 6.3 ,3.8 ,2.2 ,999 ,2.7 ,5.2 ,2.4 ,2.4 ,5.7 ,1.7 ,2.5 ,4.6 ,4.9 ,6.2 ,4.9 ,3.1],
[1.2, 1.0, 2.1, 5.9 ,3.7 ,2.1, 3.0 ,2.7 ,999, 2.6, 2.9, 4.0, 4.3, 2.5 ,2.9, 2.9, 3.2, 4.5, 3.2, 3.6],
[2.4 ,2.5 ,3.2, 2.0 ,2.3 ,2.1, 3.1, 5.2, 2.6, 999 ,2.8 ,3.9 ,4.0 ,4.8, 5.2, 5.2, 5.0, 6.8 ,5.5 ,5.9],
[1.9, 2.9, 3.5, 5.2 ,3.9 ,1.7 ,0.9, 2.4, 2.9 ,2.8, 999 ,1.2 ,5.2 ,3.3 ,4.0, 5.6, 5.9, 7.3, 5.9, 4.6],
[3.2 ,4.2 ,4.8, 6.4 ,5.0, 2.9, 1.9 ,2.4, 4.0, 3.9 ,1.2, 999, 6.6, 3.9, 4.8, 6.8 ,7.4 ,8.6 ,7.2 ,5.4],
[4.1, 4.2 ,2.6, 2.1, 2.7, 3.6, 5.4, 5.7, 4.3, 4.0, 5.2 ,6.6, 999, 5.2, 4.9, 3.3, 1.0 ,2.9, 2.4, 5.3],
[3.4, 3.3 ,3.6, 7.2, 5.9, 4.3 ,2.5 ,1.7 ,2.5, 4.8 ,3.3 ,3.9 ,5.2, 999, 0.75 ,3.2 ,4.2 ,5.5 ,4.0 ,1.3],
[3.6, 3.4, 3.9 ,6.9, 6.2, 4.5, 3.3 ,2.5 ,2.9 ,5.2, 4.0, 4.8, 4.9, 0.75, 999, 2.7, 3.8, 5.1, 3.5, 0.80],
[2.4 ,2.1 ,2.5, 5.4 ,4.8 ,3.3, 4.8 ,4.6 ,2.9 ,5.2, 5.6 ,6.8 ,3.3 ,3.2 ,2.7, 999 ,2.2 ,3.4 ,2.1 ,2.6],
[4.0, 2.8, 1.7, 3.0, 3.7, 4.5, 5.1, 4.9, 3.2, 5.0, 5.9, 7.4, 1.0, 4.2, 3.8, 2.2, 999, 1.9, 1.4, 4.4],
[5.4 ,4.1 ,3.1 ,4.9 ,5.0 ,6.3 ,6.4 ,6.2 ,4.5 ,6.8 ,7.3 ,8.6 ,2.9 ,5.5 ,5.1 ,3.4 ,1.9 ,999 ,1.5 ,4.1],
[4.1, 3.9, 2.6, 4.5, 5.1, 5.2, 5.1, 4.9, 3.2, 5.5, 5.9, 7.2, 2.4, 4.0, 3.5, 2.1, 1.4, 1.5, 999, 2.9],
[4.7, 5.0 ,4.9 ,7.4, 6.9 ,5.6, 3.8 ,3.1 ,3.6 ,5.9 ,4.6 ,5.4 ,5.3 ,1.3 ,0.80 ,2.6 ,4.4, 4.1 ,2.9, 999]
]

# Dictionary of distances

dist={(r,i,j):d[i][j] for r in range(R) for i in range(V) for j in range(V)}

# Defining a model

model=Model("Network Model")

# Defining the gurobi variables

x=model.addVars(R,V,V,obj=dist,vtype=GRB.BINARY,name='x')
a=model.addVars(V,V,vtype=GRB.BINARY,name='a')
s=model.addVars(R,V,vtype=GRB.BINARY,name='s')
y=model.addVars(V,vtype=GRB.BINARY,name='y')
z=model.addVars(V,vtype=GRB.BINARY,name='z')
xn=model.addVar(vtype=GRB.INTEGER,name='xn')
model.update()

# Adding the Constraints

model.addConstr(quicksum(z[i] for i in range(V))<=C,"C4")
for r in range(R):
    for i in range(V):
        model.addConstr(s[r,i]<=z[i],"C5")
for r in range(R):
    model.addConstr(quicksum(s[r,i]for i in range(V))==1,"C6")
for r in range(R):
    for i in range(V):
        model.addConstr(s[r,i]<=quicksum(x[r,i,j] for j in range(V)),"C7")
for r in range(R):
    for p in range(V):
        model.addConstr(quicksum(x[r,i,p] for i in range(V) if(i!=p))-quicksum(x[r,p,j] for j in range(V) if(j!=p))==0,"C8")
for i in range(V):
    model.addConstr(y[i]<=quicksum(x[r,i,j] for r in range(R) for j in range(V))+z[i],"C10")
model.addConstr(quicksum(y[i] for i in range(V))==V,"C11")
model.addConstr(quicksum(a[i,j] for i in range(V) for j in range(V) if i!=j)>=quicksum(z[p] for p in range(V))-1,"C14")
for i in range(V):
    for j in range(V):
        if(dij[i,j]==0):
            continue
        model.addConstr(a[i,j]<=math.floor(G/dij[i,j]),"C13")
for i in range(V):
    for j in range(V):
        model.addConstr(a[i,j]<=z[i],"C12a")
for i in range(V):
    for j in range(V):
        model.addConstr(a[i,j]<=z[j],"C12b")
subset=list(powerset(list(range(V))))
a1=set()
c=set(range(V))
for r in range(R):
    for S in subset[1:]:
        a1=set(S)
        a1=c-a1
        if(len(a1)==0):
            continue
        model.addConstr(quicksum(x[r,i,j] for r in range(R) for i in S for j in a1) >= 1,"C9")
for S in subset[1:]:
    model.addConstr(quicksum(a[i,j] for i in S for j in S)<=len(S)-1,"C15")
for r in range(R):
    model.addConstr(xn >= quicksum(x[r,i,j] for i in range(V) for j in range(V)),"C#")

# Optimizing the Model

model.setObjective(xn)
model.optimize()

# Printing the path of the data mules Depot location and Tower location

print('Optimal cost: %g' % model.objVal)
vals = model.getAttr('x', x)
dp = model.getAttr('x',s)
depots = list(i for r,i in dp.keys() if dp[r,i]>0.5)
print("Path of each Mule ")
for k in range(R):
    selected=tuplelist((r,i,j) for r,i,j in vals.keys() if vals[r,i,j]>0.5 and r==k)
    print("DM%s"%(k),": ",selected)    
print("Depots : ",depots)
to = model.getAttr('x',z)
towers = list(i for i in to.keys() if to[i]>0.5)
print("Towers : ",towers)
vals = model.getAttr('x',a)
aij = list([i,j] for i,j in vals.keys() if vals[i,j]>0.5)
print("Value of a[i,j] : ",aij)

# Writing the Files

model.write("Model.lp")
model.write("Solution.sol")