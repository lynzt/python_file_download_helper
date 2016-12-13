import urllib
import os
# import os.path
from urlparse import urlparse

def download_file_from_uri(uri, filename):
    testfile = urllib.URLopener()
    testfile.retrieve(uri, filename)

def delete_file(filename):
    os.remove(filename)

def get_extension_from_uri(uri):
    url_parsed = urlparse(uri)
    filename, file_extension = os.path.splitext(url_parsed.path)
    return file_extension

# return true/false
def file_exists(filename):
    return os.path.isfile(filename)
