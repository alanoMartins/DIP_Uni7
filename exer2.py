import cv2

image = cv2.imread('imagens/lena.jpg')

while(True):

    pimage = image.copy()
    pyramid = [pimage]
    for i in range(0,6):
        pimage = cv2.pyrDown(pimage)
        pyramid.append(pimage)
        cv2.imshow('Pyramid % d' % i, pimage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

image.release()
cv2.destroyAllWindows()

