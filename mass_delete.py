import os
import requests


# why not?
def exodus():
    mydir = "./media/uploads/"

    ext = [".png", ".jpg", ".jpeg", ".gif", ".webp"]

    filelist = [ f for f in os.listdir(mydir) if f.endswith(tuple(ext)) ]
    for f in filelist:
        os.remove(os.path.join(mydir, f))


def mock_request():

    url = 'http://127.0.0.1:8000/api/upload/'

    files = {'image': open('media/avatars/cat.png', 'rb')}

    headers = {'Authorization': 'Token 1d4bc590c88c75b288e84d216a7945bddb022ce6'}

    r = requests.post(url, files=files, headers=headers)

    print(r.text)