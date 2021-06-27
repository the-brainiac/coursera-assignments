#!/usr/bin/env python3
from PIL import Image
import os

#parent = '~'
path = os.path.join('./','opt/icons/')
print(path)
# print(os.path.join('.'))
os.makedirs(path)
files = os.listdir('./images')

for f in files:
	if '.' not in f:
		f_path = os.path.join('./images',f)
		im = Image.open(f_path)
		rgb_im = im.convert('RGB')
		out_path = os.path.join(path,f)
	# print(out_path)

		rgb_im.rotate(-90).resize((128,128)).save(out_path+'.jpeg')




#!/usr/bin/env python3
import os, glob
from PIL import Image
size = 128, 128
for f in glob.glob(os.getcwd()+"/images/ic_*"):
  im = Image.open(f).convert('RGB')
  print(f)
  print(im.format)
  new_name = os.path.basename(f)
  im.rotate(270).resize((size)).save("/opt/icons/" + new_name, "JPEG")
