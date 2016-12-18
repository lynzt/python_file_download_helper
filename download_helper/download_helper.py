import urllib2
import os
from urlparse import urlparse

def download_file_from_uri(uri, filename):
    u = urllib2.urlopen(uri)
    localFile = open(filename, 'w')
    localFile.write(u.read())
    localFile.close()

def delete_file(filename):
    os.remove(filename)

def get_file_details(file): # pass in filename or uri
    url_parsed = urlparse(file)
    filename, ext = os.path.splitext(url_parsed.path)
    return {'filename': filename, 'extension': ext}

# return true/false
def file_exists(filename):
    return os.path.isfile(filename)
