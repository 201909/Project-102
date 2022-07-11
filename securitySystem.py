import cv2
import time
import random
from cv2 import VideoCapture
import dropbox
start_time = time.time()

def snapshot():
    number = random.randint(0,100)
    vid = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi',fourcc, 5, (1280,720))

    while True:
          ret, frame = vid.read()
          cv2.imshow('vid.avi', frame)
          if ret == True:
            b = cv2.resize(frame,(800,400),fx=0,fy=0, insert = cv2.INTER_CUBIC)
            out.write(b)
          else:
            break
          vid.release()
          out.release()
          cv2.destroyAllWindows()
          print(start_time)
snapshot()
'''
def uploadFile(img):
    access_token = 'sl.BKHRb2u0Za3Wjo0qvwIFOar7fHVx41PmJXN60rhyOMr9KWluZHn-Oc4FiuIAGzXvkXnseuNp2UpGDDX9_Xh48c2nt1N9DCiASNHrZfyVRGHTilAa5v6xCn6ZTOcq02Emly0hscQ'
    file = img

    file_from = file
    file_to = "C:/Users/islam/Byju-coding/class/Class102"
    dbx = dropbox.Dropbox(access_token)


    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")
        

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = snapshot()
            uploadFile(name)
main()
'''