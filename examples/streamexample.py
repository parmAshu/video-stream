import videoStreamCV as vs
import cv2

camera=vs.videoStreamCV()
if not camera.start():
  print("error while starting thread")

else:
  while True:
    img=camera.read()

    if img.shape==(2,2,2):
      continue

    cv2.imshow('Image',img)

    k=cv2.waitKey(30) & 0xff
    if k==27:
      break

  camera.stop()

