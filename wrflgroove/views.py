from bs4 import BeautifulSoup
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list
import urllib
from urllib2 import urlopen
from datetime import datetime
from models import DJ, Playlist
import html5lib
from json import load
import string

def getTinysongURL(artist, song):
    APIkey = '?format=json&key=KEY_GOES_HERE'
    baseUrl = 'http://tinysong.com/a/'
    trackInfo = (artist + ' ' + song).encode('utf-8').translate(None, string.punctuation)
    cleanUrl = (baseUrl + trackInfo + APIkey).replace(' ', '+')
    response = urlopen(cleanUrl)
    tinysongURL = load(response)
    return tinysongURL if tinysongURL else ''

def cleanDateTime(data):
    """
        Manipulates the string representing the date and time
        that a song was played in order to be compatible with
        datetime.strptime().
    """
    dateFormat = '%m/%d/%Y %I:%M %p'

    # For each sublist containing date and time information, removes the
    # <br> tag and joins the two remaining elements separated by a space.
    # Then, removes the dots in e.g. 'p.m.'.
    data = (' '.join(data[0::2])).replace('.', '')

    # If the format of the time is x:yy
    if (':' in data):
        if len(data[11:(data.index(':'))]) == 1:
            data = data[:11] + '0' + data[11:]
    # The time reads "noon" at 12:00 pm for some ungodly reason
    elif ('n' in data):
        data = data[:11] + '12:00 pm'
    # If the format of the time is the hour with no proceding minutes
    else:
        data = data[:13] + ':00 ' + data[14:]
    # e.g. '02/08/2013 03:28 pm' -> '(2013, 02, 08, 15, 28, 00)'
    data = datetime.strptime(data, dateFormat)
    return data

def getDJ(dj_name):
    return DJ.objects.get(name=dj_name)

def track_list(request, dj_name):
    deejay = DJ.objects.get(name=dj_name) 
    queryset = Playlist.objects.filter(dj=DJ(id=deejay.id))
    return object_list(request, queryset=queryset, paginate_by = 50, extra_context = { 'deejay': deejay })

def update_playlist(data):
    url = 'http://wrfl.fm/playlist/'
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html5lib")
    t = soup.find('tbody')
    data = ([[c.contents[0].contents for c in row.findAll('td')] for row in t.findAll('tr')])
    for track in data[0:30]:
        try:
            playlist = Playlist.objects.get(playtime = cleanDateTime(track[0]))
        except:
            dj, created = DJ.objects.get_or_create(name=(track[4][0]).encode('utf-8'))
            dj_id = dj.id
            playlist = Playlist(
                                dj          = DJ(id=dj_id),
                                artist      = track[1][0],
                                album       = track[3][0],
                                song        = track[2][0],
                                playtime    = cleanDateTime(track[0]),
                                url         = getTinysongURL(track[1][0], track[2][0]),
                                )
            playlist.save()
    playlist_list = Playlist.objects.all()
    return render_to_response('update_playlist.html', {'playlist_list': playlist_list })
