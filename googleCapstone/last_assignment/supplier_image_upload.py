#!/usr/bin/env python3
import requests
from PIL import Image
import os, glob
url = "http://localhost/upload/"
for f in glob.glob("~/supplier-data/images/*.jpeg"):
    im = open(f, 'rb')
    r = requests.post(url, files={'file': im})
    im.close()
