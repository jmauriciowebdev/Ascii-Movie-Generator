import cv2
import os, sys, glob


def masterfun(root, fps):
    image_folder = os.getcwd()
    video_name = root+'\\video.avi'

    images = glob.glob("Final*")
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))
    i = 1
    for image in images:
        try:
            video.write(cv2.imread(os.path.join(image_folder, "final - " + str(i-1) + ".jpg")))
            print("Adding frame " + str(i-1) + " out of " + str((len(images)-1)))
        except:
            print("Failed at " + str(i-1) + " out of " + str((len(images)-1)))
            break
        i += 1

    cv2.destroyAllWindows()
    print("Releasing video!")
    video.release()