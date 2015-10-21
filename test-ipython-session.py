# coding: utf-8
import fiona
c = fiona.open('shapefiles/cb_2013_us_ua10_500k.shp','r')
c
next(x)
next(c)
next(c)
len(list(c))
c = fiona.open('shapefiles/cb_2013_us_ua10_500k.shp','r')
c.driver
c.next()
len(c.next())
c.next()[0]
c.next()[1]
c.next()
type(c.next())
c.next().iteritems()
c.next().items()
len(c.next().items())
c.next().type
c.next()['type']
c.next()['properties']['NAME10']
c.next()['properties']['NAME10']
c.next()['properties']['NAME10']
c.next()['properties']['NAME10']
c.next()['properties']['NAME10']
c.next()['properties']['NAME10']
c.next()['properties']['NAME10']
c.next()
a = c.next()
a
a = c.next()
a
a = c.next()
a
a = c.next()
a
a
import shapely
from shapely.geometry import Polygon
p = Polygon(a['geometry'
]['coordinates'])
p = Polygon(a['geometry'
]['coordinates'][0])
p
p.area
p.bounds
p.interiors
list(p.interiors)
p.contains([-97.58,27.94])
from shapely.geometry import Point
b = Point([-97.58,27.94])
b
p.contains(b)
get_ipython().magic(u'save test-ipthon-session.py')
