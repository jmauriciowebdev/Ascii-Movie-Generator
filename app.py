import os, sys, glob
import cv2
import frametoascii as fta
import imgtovid as itv

imagelist = []

print(cv2.__version__)
video = input("What is the video name?: ")
vidcap = cv2.VideoCapture(video)
fps = vidcap.get(cv2.CAP_PROP_FPS) # GET THE FREAKING FPS
#vidcap.set(cv2.cv.CV_CAP_PROP_FPS, fps) # I no longer know what this is
success,image = vidcap.read()
count = 0
success = True
if not os.path.exists("trial"):
    os.makedirs("trial")

root = os.getcwd()
os.chdir("trial")

while success:
    cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    print ('Currently found ', count, 'frames')
    count += 1
counter = 0
filelist = os.listdir()
count = 0
for file in filelist:
    try:
        imagelist.append(fta.masterfunc("frame%d.jpg" % count, counter))
        count += 1
        counter += 1
    except:
        print("Tried to convert frame%d.jpg" % count)
        pass
print("Finished converting frames")
itv.masterfun(root, fps)
os.chdir(root)