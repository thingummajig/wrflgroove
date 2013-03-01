import urllib
import os

url = 'http://thingummajig.pythonanywhere.com/wrflgroove/update_playlist/'
r = urllib.urlopen(url).read()

os.utime('/var/www/thingummajig_pythonanywhere_com_wsgi.py', None)
