import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_to_sketch(img:np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    neg = cv2.bitwise_not(gray)
    gauss = cv2.GaussianBlur(neg,(125,125),25,25)
    final = cv2.divide(gray,255-gauss,scale=256)
    plt.figure(figsize=(15,5))
    plt.title('Sketch')
    plt.imshow(final,cmap='gray')
    plt.axis('off')
    plt.show()
    #print(final.shape)
    return final

if __name__ == "__main__":
    img = cv2.imread('images.png')
    res = image_to_sketch(img)
    cv2.imwrite('Sketch.png',res)