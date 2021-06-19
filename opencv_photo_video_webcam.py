"""
Salom hammaga!
Bu faylda Pythonnning opencv methodidan foydalanamiz.
Birinchi bo'limda rasm ustida bajariladigan bir qancha hossalarini ko'rib chiqamiz.
Ikkinchi bo'limda videoni chiqarishni ko'rib chiqamiz.
Uchinchi bo'limda web kamerani ekranga chiqarish bilan shug'ullanamiz.

"""

"""
Hello everybody!
In this file we will use Pythonn's opencv method.
In the first section, we will look at a number of properties that can be performed on an image.
In the second section, we’ll look at video release.
In the third section, we will deal with the display of the webcam.
"""

"""
Привет всем!
В этом файле мы будем использовать метод Pythonn opencv.
В первом разделе мы рассмотрим ряд свойств, которые можно применить к изображению.
Во втором разделе мы рассмотрим выпуск видео.
В третьем разделе мы займемся отображением веб-камеры.
"""


import cv2

"""
* Leopard rasmini kulrang qilib chiqaramiz.
* Let's make a picture of a leopard gray.
* Сделаем картинку леопарда серого цвета.
"""

#imgleopard = cv2.imread("Leopard.jpg")
#leopardGrey = cv2.cvtColor(imgleopard, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Leopard Grey", leopardGrey)
#
#cv2.waitKey(0)



"""
* Kulrang leopardning rasmini bizor o'zgartirib chiqaramiz.
* We will change the image of the gray leopard.
* Изменим образ серого леопарда.
"""

#imgleopard = cv2.imread("Leopard.jpg")
#leopardGrey = cv2.cvtColor(imgleopard, cv2.COLOR_BGR2GRAY)
#leopardBlur = cv2.GaussianBlur(leopardGrey,(7,7),0)
#cv2.imshow("Leopard Blur", leopardBlur)
#
#cv2.waitKey(0)


"""
* Leopardning rasmini shakl berib qilib chiqaramiz.
* Let's make a picture of a leopard by shaping it.
* Давайте сделаем рисунок леопарда, придав ему форму.

"""

#imgleopard = cv2.imread("Leopard.jpg")
#leopardcanny = cv2.Canny(imgleopard,10,10)
#cv2.imshow("Leopard Canny", leopardcanny)
#
#cv2.waitKey(0)

  

#kernal = np.ones((5,5),np.uint8)    
#imgleopard = cv2.imread("Leopard.jpg")
#leopardGrey = cv2.cvtColor(imgleopard, cv2.COLOR_BGR2GRAY)
#leopardDialation = cv2.dilate(leopardGrey,kernal,iterations=1)
#cv2.imshow("Leopard Dialation", leopardDialation)
#
#cv2.waitKey(0)



#kernal = np.ones((5,5),np.uint8)    
#imgleopard = cv2.imread("Leopard.jpg")
#leopardEroded = cv2.erode(leopardDialation, kernal, iterations=1)
#cv2.imshow("Eroded Grey", leopardEroded)
#
#cv2.waitKey(0)


# Video  /  video  /   видео


cap = cv2.VideoCapture("VIDEO.mp4")

while True:
    succes, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break

            
 
# Web kamera /  Webcamera  /  веб-лагерь

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    succes, img = cap.read()
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break

               
