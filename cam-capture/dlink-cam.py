import cv2

cam = cv2.VideoCapture('rtsp://admin:dslab2022@192.168.1.17:554/play1.sdp')

# rtsp://admin:dslab2022@192.168.1.17:554/play1.sdp  rtsp://admin:dslab@192.168.0.1/H264?ch=1&subtype=0 http://192.168.0.1:80/video?x.mjpeg

while(True):
    ret, frame = cam.read()
    cv2.imshow('test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()