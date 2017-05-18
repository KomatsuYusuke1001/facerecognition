# -*- coding: utf-8 -*-
"""
Created on Mon May 15 09:39:27 2017

@author: komatsu
"""

import os
import sys
import cv2
from PIL import Image, ImageOps, ImageDraw

save_dir = '/Users/komatsu/.spyder/figs/'
# the absolute path of the directory, means "folder" , in which you save figures 
check = os.path.exists(save_dir)
# if the directry is exists check = 1, otherwise check = 0

if check == 0:
    os.mkdir(save_dir)
"""
if check == 1:
    print ""
    print "the indicated directory already exists. Please delete that directory."
    print ""
    sys.exit()    
"""

pict_dir = "/Users/komatsu/.spyder/picts/"
check2 = os.path.exists(pict_dir)
if check == 0:
    print ""
    print "the indicated directory already exists. Please delete that directory."
    print ""
    sys.exit()  

#get the name of every data file as an array 
pict_dirs = sorted(os.listdir(pict_dir))
print pict_dirs

for pict in pict_dirs:
# Get user supplied values

    imagePath = pict_dir+pict
    print imagePath    
    cascPath = "haarcascade_frontalface_default.xml"
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)
    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
                                         gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(20, 20)
                                         )
    print("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        """
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        """
        cv2.ellipse(image, ((x+x+w)/2,(y+y+h)/2), (w/2,h/2),0,0,360,(256,256,256),2)
    
    name, ext = os.path.splitext(pict)
    print name, ext
    cv2.imwrite(save_dir+name+".png", image[y:y+h, x:x+w])
    

    size = (w,h)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=0)
    im = Image.open(save_dir+name+".png")
    output = ImageOps.fit(im, mask.size, centering=((x+x+w)/2,(y+y+h)/2))
    output.putalpha(mask)
    output.save(save_dir+name+".png")
    
    """
    cv2.imshow("Faces found", image)
    print faces
    cv2.waitKey(0)
    """

    





































