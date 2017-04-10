import re
#import shapefile
from IPython import embed
import fiona
from shapely import geometry
import json
from shapely.geometry import shape, Point


with open ('/Users/prasad/Desktop/query.txt', 'r') as f:
    js = json.load(f)

# construct point based on lat/long returned by geocoder
point = Point(-73.916661142,40.828848333,  )

# check each polygon to see if it contains the point
#print "hi"
for feature in js['features']:
    polygon = shape(feature['geometry'])
    #print feature
    #print polygon
    if polygon.contains(point):
        print 'Found containing polygon:', feature['properties']