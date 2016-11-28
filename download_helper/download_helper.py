import urllib
import os

def download_file_from_uri(uri, filename):
    testfile = urllib.URLopener()
    testfile.retrieve(uri, filename)

# return true/false
def file_exists(filename):
    return os.path.isfile(filename)

def delete_file(filename):
    os.remove(filename)
