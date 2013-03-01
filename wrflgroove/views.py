from bs4 import BeautifulSoup
from django.shortcuts import render_to_response
import urllib
from datetime import datetime
from models import DJ, Playlist
import html5lib

url = 'http://wrfl.fm/playlist/'
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html5lib")

def update_playlist(data):

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
        #data[i][0] = (' '.join(data[i][0][0::2])).replace('.', '')
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
            data = data[:12] + ':00 ' + data[13:]
        # e.g. '02/08/2013 03:28 pm' -> '(2013, 02, 08, 15, 28, 00)'
        data = datetime.strptime(data, dateFormat)
        return data

    t = soup.find('tbody')
    data = ([[c.contents[0].contents for c in row.findAll('td')] for row in t.findAll('tr')])
    for track in data:
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
                                playtime    = cleanDateTime(track[0])
                                )
            playlist.save()
    playlist_list = Playlist.objects.all()
    return render_to_response('update_playlist.html', {'playlist_list': playlist_list })
