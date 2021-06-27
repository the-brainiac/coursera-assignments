
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
