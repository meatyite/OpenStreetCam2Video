import requests
import json
import os
import urllib.request
from sys import argv


def download_photos(track_id):
    r = requests.post("http://api.openstreetcam.org/details", data={'id': track_id}).content.decode()
    j = json.loads(r)
    # j_pretty = json.dumps(j, indent=4)
    # open('test.json', 'w').write(j_pretty)
    folder_path = './' + str(track_id) + '/'
    if not(os.path.isdir(folder_path)):
        os.mkdir(folder_path)
    print("Downloading photos of track id %s..." % str(track_id))
    for photo in j['osv']['photos']:
        url = "https://api.openstreetcam.org/" + photo['lth_name']
        file_name = photo['sequence_index'] + '.jpg'
        file_path = folder_path + file_name
        if os.path.isfile(file_path):
            print('Already downloaded %s, Skipping.' % file_name)
        else:
            try:
                urllib.request.urlretrieve(url, file_path)
                print('Downloaded %s.' % file_name)
            except Exception as e:
                print("ERROR DOWNLOADING %s: %s" % (file_name, str(e)))


download_photos(int(argv[1]))
