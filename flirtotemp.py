# FLIR 열화상,컬러 이미지 받아서 온도 값 출력
# Face Detection 코드 출처 : https://github.com/serengil/tensorflow-101/blob/master/python/opencv-dnn-face-detection.ipynb
# 45 * 34
# 55 * 43
import cv2
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract

# string to float
def str2float(str):
    new_str = ''
    for c in str:
        if c.isdigit():
            new_str += c
    return int(new_str)/10

# convert grayscale to temperature
def max_mean(img_thresh,minval,maxval):
    img_temp = np.round(img_thresh * (maxval-minval)/255 + minval,1)
    rows, columns = img_thresh.shape
    r_max,c_max = np.where(img_temp >= np.max(img_temp))
    r_nose = int(rows * 1/2)
    r_chin = int(rows * 4/5)
    img_overnose = img_temp[:r_nose]
    img_underchin = img_temp[r_chin:]
    print(f"이마 ~ 코 최대 온도 : {np.max(img_overnose)}, 평균 온도 : {np.round(np.mean(img_overnose[img_overnose>minval]),1)}")
    print(f"턱 ~ 목 최대 온도 : {np.max(img_underchin)}, 평균 온도 : {np.round(np.mean(img_underchin[img_underchin>minval]),1)}")
    img_thresh = cv2.cvtColor(img_thresh,cv2.COLOR_GRAY2RGB)
    cv2.line(img_thresh,(0,r_nose),(columns-1,r_nose),(0,255,0),1)
    cv2.line(img_thresh,(0,r_chin),(columns-1,r_chin),(0,255,0),1)
    for x,y in zip(c_max,r_max):
        cv2.circle(img_thresh,(x,y),1,(255,0,0),1)
    return img_thresh

# make face area
def makefacearea(image):
    detector = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")
    base_img = image.copy()
    original_size = image.shape
    target_size = (300, 300)
    gray_size = (240, 320)
    image = cv2.resize(image, target_size)
    aspect_ratio_x = (original_size[1] / target_size[1])
    aspect_ratio_y = (original_size[0] / target_size[0])
    gray_ratio_x = (gray_size[1] / original_size[1])
    gray_ratio_y = (gray_size[0] / original_size[0])
    imageBlob = cv2.dnn.blobFromImage(image = image)
    detector.setInput(imageBlob)
    detections = detector.forward()
    detections_df = pd.DataFrame(detections[0][0]
        , columns = ["img_id", "is_face", "confidence", "left", "top", "right", "bottom"])
    detections_df = detections_df[detections_df['is_face'] == 1] #0: background, 1: face
    detections_df = detections_df[detections_df['confidence'] >= 0.90]
    points=[]
    for _, instance in detections_df.iterrows():
        left = int(instance["left"] * 300 * aspect_ratio_x)
        bottom = int(instance["bottom"] * 300 * aspect_ratio_y)
        right = int(instance["right"] * 300 * aspect_ratio_x)
        top = int(instance["top"] * 300 * aspect_ratio_y)
        left_gray = int(left * gray_ratio_x)
        bottom_gray = int(bottom * gray_ratio_y)
        right_gray = int(right * gray_ratio_x)
        top_gray = int(top * gray_ratio_y)
        points.append((top_gray,bottom_gray,left_gray,right_gray))
        cv2.rectangle(base_img, (left,top),(right,bottom), (255, 255, 255), 1)
    base_img = cv2.resize(base_img,(320,240))
    return base_img, points

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Insufficient arguments")
        sys.exit()
    file1 = sys.argv[1]
    file2 = file1[:4] + str(int(file1[4:8])+1).rjust(4,'0') + file1[-4:]
    # image read
    img_thermal = cv2.imread(file1)
    img_thermal_gray = cv2.cvtColor(img_thermal,cv2.COLOR_BGR2GRAY)
    img_color = cv2.imread(file2)

    # temperature image processing
    min_img = img_thermal_gray[215:235,280:315]
    max_img = img_thermal_gray[5:25,280:315]
    min_img = cv2.threshold(min_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    max_img = cv2.threshold(max_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    min_img = 255 - min_img
    max_img = 255 - max_img

    # Tesseract (OCR)
    # min
    filename ="{}.png".format(os.getpid())
    cv2.imwrite(filename, min_img)
    minval = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    # max
    filename ="{}.png".format(os.getpid())
    cv2.imwrite(filename, max_img)
    maxval = pytesseract.image_to_string(Image.open(filename), lang=None)
    os.remove(filename)

    try:
        minval = str2float(minval)
        maxval = str2float(maxval)

        # resize color image
        rh = 34/43 * 0.9
        rw = 45/55 * 0.9
        h,w,_ = img_color.shape
        img_color = img_color[h//2-int((h*rh)//2):h//2+int((h*rh)//2),w//2-int((w*rw)//2)+15:w//2+int((w*rw)//2)+15]

        # face detection
        img_color, points= makefacearea(img_color)
        # extract face area
        img_fg = img_thermal_gray[points[0][0]:points[0][1],points[0][2]:points[0][3]]
        # thresholding thermal image
        _, mask_thresh = cv2.threshold(img_fg,200,255,cv2.THRESH_BINARY)
        img_thresh = cv2.bitwise_and(img_fg,img_fg,mask=mask_thresh)
        # print max, mean
        img_thresh = max_mean(img_thresh,minval,maxval)
        # Plot
        img_thermal = cv2.cvtColor(img_thermal,cv2.COLOR_BGR2RGB)
        img_color = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)
        img_fg = cv2.cvtColor(img_fg,cv2.COLOR_GRAY2RGB)
        titles = ["Thermal Image","Color Image","Face","Thresh"]
        images = [img_thermal,img_color,img_fg,img_thresh]
        plt.figure(figsize=(8,8))
        for i in range(len(images)):
            plt.subplot(2,2,i+1)
            plt.imshow(images[i])
            plt.title(titles[i])
            plt.axis('off')
        plt.tight_layout()
        plt.show()
    except ValueError as e:
        print('OCR 실패',e)
        print(f'minval : {minval}\n maxval : {maxval}')
        plt.figure(figsize=(8,8))
        plt.subplot(1,2,1)
        plt.imshow(min_img,cmap='gray')
        plt.subplot(1,2,2)
        plt.imshow(max_img,cmap='gray')
    except IndexError as e:
        print('ResNet 얼굴 인식 실패',e)
        plt.figure(figsize=(8,8))
        img_thermal = cv2.cvtColor(img_thermal,cv2.COLOR_BGR2RGB)
        img_color = cv2.cvtColor(img_color,cv2.COLOR_BGR2RGB)
        plt.subplot(1,2,1)
        plt.imshow(img_thermal)
        plt.subplot(1,2,2)
        plt.imshow(img_color)

