import cv2
import numpy
from matplotlib import pyplot as plt

def plotHistRGB(image):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def create_mask(image):
    mask = numpy.zeros(image.shape[:2], numpy.uint8)
    mask[200:300, 200:400] = 255
    return mask

def apply_mask(image):
    return cv2.bitwise_and(image, image, mask=create_mask(image))

image_color = cv2.imread('imagens/lena.jpg')
image = cv2.imread('imagens/lena.jpg', 0)
mask_image = apply_mask(image)

while(True):
    #plotHistRGB(image)
    mask = create_mask(image)

    hist_full = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_mask = cv2.calcHist([image], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(image, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(mask_image, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])

    plt.show()

    plotHistRGB(image_color)


    cv2.imshow('Image', image)
    cv2.imshow('Image Color', image_color)
    cv2.imshow('Mask Image', mask_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

image.release()
cv2.destroyAllWindows()



