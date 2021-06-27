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
