#importing the required modules
from threading import Thread
import sys
import numpy
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from copy import *

class videoStreamPI:


  #the class initializer 
  def __init__(self,resolution='720p',framerate=40):
    self.ready=0
    self.frame=numpy.zeros((2,2,2))
    self.stopped=False
    rawReady=0
    try:
      #starting the picamera
      self.cam=PiCamera()
      self.ready=1

      #setting the camera parameters
      self.cam.resolution=resolution
      self.cam.framerate=framerate
     
      #raw stream
      self.raw=PiRGBArray(self.cam, size=resolution)
      rawReady=1
      self.stream=self.cam.capture_continuous(self.raw, format="bgr", use_video_port=True)
    except:
      #close the camera and streams if opened already
      if self.ready:
        self.cam.close()
      if rawReady:
        self.raw.close()
      self.ready=0
    else:
      time.sleep(0.5)


  #thread starting function
  def start(self):
    if self.ready:
      try:
        Thread(target=self.update,args=()).start()
        return 1
      except:
        return 0
    else:
      return 0


  #the thread function
  def update(self):
    for f in self.stream:
        
      self.frame=f.array
      self.raw.truncate(0)
      
      if self.stopped:
        self.stream.close()
        self.raw.close()
        self.cam.close()
        self.ready=0
        #this breaks the infinite loop of the thread function thereby ending it
        break


  #the thread stop function
  def stop(self):
    self.stopped=True
  

  #the frame read function
  def read(self):
    _frame=deepcopy(self.frame)
    return _frame
