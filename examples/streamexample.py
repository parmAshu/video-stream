import videoStreamCV
import cv2

camera=videoStreamCV.videoStreamCV()
if not camera.start():
  print("error while starting thread")
  if camera.ready:
    camera.stop()

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

