import cv2
import numpy as np
import os

# cv2.imread(filename,[,flag])
# flag에는 이미지 파일 읽는 방식
# cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED

# cv2.imshow(winname,image object)

# cv2.waitKey([,delay])
# waitKey(0)은 입력이 들어올 때 까지 대기
# 입력된 문자의 아스키 코드를 반환한다
# ESC는 27

# cv2.destroyAllWindows()

# COLOR
def showImage_color(img_file):
    img = cv2.imread(img_file,cv2.IMREAD_COLOR) # image load
    cv2.imshow('Show Image',img) # image show
    cv2.waitKey(0) # wait keyboard input
    cv2.destroyAllWindows() # close all window
# GRAYSCALE
def showImage_gray(img_file):
    img = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE) # image load
    cv2.imshow('Show Image',img) # image show
    cv2.waitKey(0) # wait keyboard input
    cv2.destroyAllWindows() # close all window
# UNCHANGED
def showImage_with_alpha_channel(img_file):
    img = cv2.imread(img_file,cv2.IMREAD_UNCHANGED) # image load
    cv2.imshow('Show Image',img) # image show
    cv2.waitKey(0) # wait keyboard input
    cv2.destroyAllWindows() # close all window
# 위 세 함수는 크기 조절 불가
# cv2.namedWindow(winname,[,flag])
# cv2.imwrite(filename,image object,[,params])
def showImage_scale_adjust(img_file):
    img = cv2.imread(img_file,cv2.IMREAD_UNCHANGED) # image load
    cv2.namedWindow('Show Image with Scale Adjust', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.imshow('Show Image with Scale Adjust',img) # image show
    cv2.waitKey(0) # wait keyboard input
    cv2.destroyAllWindows() # close all window
def store_Image(img_file):
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)
    cv2.imshow('Show Image',img)
    k = cv2.waitKey(0) & 0xFF # convert ascii(in x64 os)
    if k == 27: # 27 is ESC
        cv2.destroyAllWindows()
    elif k == ord('c'): # c is writing
        store_img_file = img_file[:-4] + '_copy.jpg'
        print(store_img_file)
        cv2.imwrite(store_img_file,img)
        cv2.destroyAllWindows()

path=os.getcwd() # get pwd
img_name=os.path.join(path,'lantern.jpg') # set image path
# showImage_color(img_name)
# showImage_gray(img_name)
# showImage_with_alpha_channel(img_name)
# showImage_scale_adjust(img_name)
store_Image(img_name)