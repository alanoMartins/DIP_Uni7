import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def my_filter(image):
    kernel = np.array([[1,1,1], [1,1,1], [1,1,1]])
    return cv2.filter2D(image, cv2.CV_8U, kernel)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sorbelX = cv2.Sobel(gray, cv2.CV_8U, 1, 0)
    sorbelY = cv2.Sobel(gray, cv2.CV_8U, 0, 1)

    scharrX = cv2.Scharr(gray, cv2.CV_8U, 1, 0)
    scharrY = cv2.Scharr(gray, cv2.CV_8U, 0, 1)

    myfilter = my_filter(gray)

    canny = cv2.Canny(gray, 130, 200)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thresh_adaptative = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)



    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imshow('sorbelX', sorbelX)
    cv2.imshow('sorbelY', sorbelY)
    cv2.imshow('ScharrX', scharrX)
    cv2.imshow('ScharrY', scharrY)

    cv2.imshow('myfilter', myfilter)

    cv2.imshow('canny', canny)
    cv2.imshow('otsu', thresh)
    cv2.imshow('thresh', thresh_adaptative)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()