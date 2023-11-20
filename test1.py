import clr 
clr.AddReference('protoGeonetry')
from Autodesk.DesignScript.Geonetry import *
dotProductlist=IN[0]
OUT=[]

for i in xrange(0,len(dotProductlist)):
    if dotProductlist[i]>.85:
        OUT.Add(true)
    else:
        OUT.Add(False)
