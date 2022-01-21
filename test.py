# Image Blurring
# 이미지에 LPF를 적용하여 고주파 영역을 제거하면
# 노이즈를 제거하거나 경계를 흐릴 수 있다.
# 4가지의 Blurring 방법
# 1. Averaging
# Box 형태의 커널을 이미지에 적용한 후 평균값을 Box의 중심점에 적용
# cv2.blur(src,ksize) -> dst : 위 예제와 동일한 역할
# cv2.boxFilter() 사용 가능
# ksize는 튜플 형태 (3,3 등)
# 2. Gaussian Filtering
# Gaussian Filter는 Gaussian 함수를 이용한 값으로 이루어진 커널 사용
# cv2.GaussianBlur(img,ksize,sigmaX)
# ksize는 width,height가 다를 수 있지만 양수의 홀수이어야 함
# 3. Median Filtering
# 커널내의 값들을 정렬한 후 중간값을 선택하여 적용
# cv2.medianBlur(src,ksize)
# ksize는 1보다 큰 홀수(3,5 등)
# 4. Bilateral Filtering(양방향 필터)
# 지금까지의 Blur처리와 달리 경계선을 유지하며 Gaussian Blur처리
# Gaussian 필터를 적용하고 또 하나의 Gaussian 필터를 주변 픽셀까지 고려하여 적용하는 방식
# cv2.bilateralBlur(src,d,sigmaColor,sigmaSpace)
# src : 8비트, 1 or 3 채널 이미지
# d : 필터링시 고려할 주변 픽셀 지름
# sigmaColor : 색을 고려할 공간. 숫자가 크면 멀리 있는 색도 고려
# sigmaSpace : 숫자가 크면 멀리 있는 픽셀도 고려

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('squirrel1.jpg')
# pyplot을 위해 BGR -> RGB 변환
b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])

# 1. Averaging
dst1 = cv2.blur(img,(7,7))
# 2. Gaussian Blur
dst2 = cv2.GaussianBlur(img,(5,5),0)
# 3. Median Blur
dst3 = cv2.medianBlur(img,9)
# 4. Bilateral Filtering
dst4 = cv2.bilateralFilter(img,9,75,75)

images = [img,dst1,dst2,dst3,dst4]
titles = ['Original','Blur(7X7)','Gaussian Blur(5X5)','Median Blur','Bilateral']

for i in range(5):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
plt.tight_layout()
plt.show()