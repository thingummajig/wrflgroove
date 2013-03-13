from django.db import models

class DJ(models.Model):
    name = models.CharField(max_length = 25) 
    # in case the track is a part of a show
    show = models.CharField(max_length = 50, blank = True, null = True)

    def __unicode__(self):
        return self.name

class Playlist(models.Model):
    dj = models.ForeignKey(DJ)
    artist = models.CharField(max_length = 50)
    album = models.CharField(max_length = 50)
    song = models.CharField(max_length = 100)
    playtime = models.DateTimeField()
    url = models.CharField(max_length = 200)

    def __unicode__(self):
        return u'%s - %s (%s, %s)' % (self.artist, self.song, self.dj, self.playtime)
