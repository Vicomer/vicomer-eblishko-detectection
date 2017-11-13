import cv2
import time
import requests

# camera setup
camera = cv2.VideoCapture(0)

while True:
    # camera capture
    return_value, image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imwrite('capt_face.jpg', image)

    # face recognition pattern
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    img = cv2.imread('capt_face.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # send post request to ubidots
    for (x, y, w, h) in faces:
        ct = time.asctime()
        payload = {'face': 1}
        r = requests.post('http://things.ubidots.com/api/v1.6/devices/DEVICE-NAME/?token=TOKEN-NAME',
                          data=payload)

    # time delay between camera captures
    time.sleep(5)

camera.release()
cv2.destroyAllWindows()





