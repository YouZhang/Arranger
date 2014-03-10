# -*- coding: cp936 -*-
import urllib2,urllib;
from bs4 import BeautifulSoup
import string
from urllib2 import quote;
# reload(sys)
# sys.setdefaultencoding( "utf-8" )
# test_url = 'http://www.midishow.com/search/midi?title=';

host = 'http://www.midishow.com/search/midi?title=';
download_host = 'http://www.midishow.com/midi/file/value.mid'
song = raw_input('input a song:');
song = song.replace(' ','+');
print song
test_url =host+ song
print test_url
# web = urllib2.Request.urlopen(quote(test_url));

req = urllib2.Request(test_url);
web = urllib2.urlopen(req);
content = web.read().decode('utf-8','ignore');
print content;
soup = BeautifulSoup(content);
value = [];
for i in soup.find_all('input',type = 'checkbox'):
    key = i['value'];
    value.append(key);
    key = str(key);
print value;
temp = download_host.replace('value',value[0]);
urllib.urlretrieve(temp,'test.mid');


