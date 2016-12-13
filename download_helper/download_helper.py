import urllib
import os
from urlparse import urlparse

def download_file_from_uri(uri, filename):
    testfile = urllib.URLopener()
    testfile.retrieve(uri, filename)

def delete_file(filename):
    os.remove(filename)

def get_file_extension(file): # pass in filename or uri
    url_parsed = urlparse(file)
    filename, file_extension = os.path.splitext(url_parsed.path)
    return file_extension

# return true/false
def file_exists(filename):
    return os.path.isfile(filename)
