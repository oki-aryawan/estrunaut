import cv2

cam1 = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cam3 = cv2.VideoCapture(2, cv2.CAP_DSHOW)


while(True):
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    ret3, frame3 = cam3.read()

    if (ret1):
        cv2.imshow('cam1', frame1)
        cv2.imshow('cam2', frame2)
        cv2.imshow('cam3', frame3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam1.release()
cam2.release()
cam3.release()
cv2.destroyAllWindows()
