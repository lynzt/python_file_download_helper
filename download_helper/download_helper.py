import os
import urllib
import utils
import shutil

def download_file_from_uri(uri, filename):
    with urllib.request.urlopen(uri) as response, open(filename, 'wb') as target:
        shutil.copyfileobj(response, target)

def delete_file(filename):
    os.remove(filename)

def get_file_details(file): # pass in filename or uri
    url_parsed = utils.parse_url_string(file)
    filename, ext = os.path.splitext(url_parsed.path)
    return {'filename': filename, 'extension': ext}

# return true/false
def file_exists(filename):
    return os.path.isfile(filename)
