import os
import urllib
import utils
import shutil

def download_file_from_uri(uri, filename):
    req = urllib.request.Request(
        uri, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36'
        }
    )

    with urllib.request.urlopen(req) as response, open(filename, 'wb') as target:
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
