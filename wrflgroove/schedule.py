import urllib
import os

os.utime('/var/www/thingummajig_pythonanywhere_com_wsgi.py', None)

url = 'http://thingummajig.pythonanywhere.com/wrflgroove/update_playlist/'
r = urllib.urlopen(url).read()
