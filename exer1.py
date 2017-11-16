import cv2
import numpy


def apply_noise(image):
    row, col = image.shape
    mean = 0
    var = 200
    sigma = var ** 0.5
    gauss = numpy.random.normal(mean, sigma, (row, col))
    gauss = gauss.reshape(row, col)
    gauss = numpy.array(gauss, dtype=numpy.uint8)
    noisy = image + gauss
    return noisy


def mse(imageA, imageB):
    err = numpy.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err

image = cv2.imread('imagens/lena.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
noisy_image = apply_noise(gray_image)
filter_image = cv2.GaussianBlur(noisy_image, (5,5), 0)

MSE_noisy = mse(gray_image, noisy_image)
MSE_filter = mse(gray_image, filter_image)

print('MSE noisy: %d' % MSE_noisy)
print('MSE filter: %d' % MSE_filter)

while(True):

    cv2.imshow('Original', gray_image)
    cv2.imshow('Noisy', noisy_image)
    cv2.imshow('Filter', filter_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

image.release()
cv2.destroyAllWindows()

