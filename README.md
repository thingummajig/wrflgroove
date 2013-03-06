wrflgroove
==========
Frequently Asked Questions
----------
### What is WRFLgroove?
WRFLgroove is a web application that allows users to access the music of the
University of Kentucky's radio station ([WRFL](http://wrfl.fm/))at any time. 
WRFLgroove creates a [Grooveshark](http://grooveshark.com/) playlist for each
student DJ and automatically updates the playlist with the music played on-air.
### How does it work?
Once an hour, on the hour, WRFLgroove scrapes the [WRFL playlist page]
(http://wrfl.fm/playlist/) and produces a list of lists. Each inner list contains
the time each song was played, as well as the artist, album, and song name as well
as the DJ who played it. After a bit of housekeeping with the formatting, each such
list is inserted as a row into the database. I'll tell you how the rest works
once I write it.
### What technologies were used to create WRFLgroove?
WRFLgroove is written in Python on the Django framework. The web scraper utility
primarily uses BeautifulSoup4, with a little help from urllib and html5lib. 
WRFLgroove makes use of the official [Grooveshark API]
(http://developers.grooveshark.com) to dynamically generate the DJ playlists.
Information is stored and retrieved in an SQLite database. The front-end
uses Twitter Bootstrap to beautify things a bit.
MIT Open Source License
-----------------------
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
