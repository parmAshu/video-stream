from threading import Thread
import cv2
import sys
import numpy
import time
from copy import *

class videoStreamCV:

  #class constructor 
  def __init__(self,source):
    self.ready=0
    self.frame=numpy.zeros((2,2,2))
    self.stopped=False
    try:
      self.vobj=cv2.VideoCapture(source)
    except:
      pass
    else:
      time.sleep(1)
      self.ready=1

  
  #thread start function
  def start(self):
    #if the video stream had started successfully then proceed 
    if self.ready:
      #if there is some error in starting the stream then, return 0
      try:
        Thread(target=self.update,args=()).start()
        return 1
      except:
        return 0
    else:
      return 0


  #this thread function will start only when the camera had started before calling the start function
  def update(self):
    while True:
      #reading the frames
      ret,self.frame=self.vobj.read()
      
      if self.stopped:
        self.vobj.release()
        self.ready=0
        cv2.destroyAllWindows()
        #this breaks the infinite loop of the thread function thereby ending it
        break
 

  #stopping function
  def stop(self):
    self.stopped=True


  #reading the image frames
  def read(self):
    _frame=deepcopy(self.frame)
    return _frame
