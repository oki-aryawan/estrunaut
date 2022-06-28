import cv2
import time
import os

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
i = 0
b = 10
path = 'A:\1.PROJECT\PKM\estrunaut\cam-capture\result'

while (cam.isOpened()):
    ret, frame = cam.read()
    if ret == False:
        break

    cv2.imwrite('cattle' + str(i) + '.jpg', frame)
    print('Frame ' + str(i) + ' saved')
    time.sleep(1)
    i += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()