import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 임계처리, 이진화
# cv2.threshold(src,thresh,maxval,type) -> retval,dst
# src: 입력 싱글 채널 이미지(GrayScale)
# thresh: 임계값
# maxval: 임계값을 넘었을 때 적용 값
# type: thresholding type
# 1. cv2.THRESH_BINARY: maxval or 0
# 2. cv2.THRESH_BINARY_INV: 0 or maxval
# 3. cv2.THRESH_TRUNC: thresh or 그대로
# 4. cv2.THRESH_TOZERO: 그대로 or 0
# 5. cv2.THRESH_TOZERO_INV: 0 or 그대로

img = cv2.imread('gradation.png',0)

ret, thresh1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255, cv2.THRESH_TOZERO_INV)

titles =['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]
for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap='gray',interpolation='bicubic')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()