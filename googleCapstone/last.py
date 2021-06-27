####ExAMPLE_UPLOAD

#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})

########
# ChangeImage.py
##########################

#!/usr/bin/env python3
import os, glob
from PIL import Image
size = 600, 400
for f in glob.glob("~/supplier-data/images/0*"):
  im = Image.open(f).convert('RGB')
  print(f)
  print(im.format)
  new_name = f.replace('tiff','jpeg')
  print(new_name)
  im.resize((size)).save(new_name)


###############################################
# Image Upload.python3

#!/usr/bin/env python3
import requests
from PIL import Image
import os, glob
url = "http://localhost/upload/"
for f in glob.glob("~/supplier-data/images/*.jpeg"):
    im = open(f, 'rb')
    r = requests.post(url, files={'file': im})
    im.close()

##################


#! /usr/bin/env python3
import json
import os, glob
import requests

for f in glob.glob("~/supplier-data/descriptions/*"):
        file = open(f)
        data = file.readlines()
        im_name = os.path.basename(f).replace('txt','jpeg')
        d = {"name":data[0].strip(),"weight":int(data[1].strip()[:-3]),"description"$
        j = json.dumps(d)
        print(j)
        jl = json.loads(j)
        r = requests.post('http://localhost/fruits/',json=jl)
        #print(r.request.url)
        #print(r.request.body)
        file.close()

#!/usr/bin/env python3
import os, glob
import requests
t = []
for f in glob.glob("~/supplier-data/descriptions/*"):
        file = open(f)
        data = file.readlines()
        im_name = os.path.basename(f).replace('txt','jpeg')
        d = [data[0].strip(),int(data[1].strip()[:-3])]
        t.append(d)
print(t)







