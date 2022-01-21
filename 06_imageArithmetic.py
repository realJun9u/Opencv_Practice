import cv2
import numpy as np
import matplotlib.pyplot as plt
# numpy는 modulo 연산, cv2.add는 saturation 연산
# # 이미지 더하기
# def addimage(imgfile1,imgfile2):
#     cv2.namedWindow('img1',cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO)
#     cv2.namedWindow('img2',cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO)
#     cv2.namedWindow('img1+img2',cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO)
#     cv2.namedWindow('cv2.add(img1,img2)',cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_KEEPRATIO)
#     img1=cv2.imread(imgfile1)
#     img2=cv2.imread(imgfile2)
    
#     cv2.imshow('img1',img1)
#     cv2.imshow('img2',img2)
    
#     add_img1 = img1+img2
#     add_img2 = cv2.add(img1,img2)
    
#     cv2.imshow('img1+img2',add_img1)
#     cv2.imshow('cv2.add(img1,img2)',add_img2)
    
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# addimage('lantern.jpg','bird1.jpg')

# # 이미지 블렌딩
# img1=cv2.imread('lantern.jpg')
# img2=cv2.imread('bird1.jpg')

# def onChange(x):
#     pass
# def imgBlending(img1,img2):
#     cv2.namedWindow('Blending Image')
#     cv2.createTrackbar('Blending','Blending Image',0,1000,onChange)

#     while True:
#         weight = cv2.getTrackbarPos('Blending','Blending Image')
#         img = cv2.addWeighted(img1,float(1000-weight)*0.001,img2,float(weight)*0.001,0)
#         cv2.imshow('Blending Image',img)
#         k = cv2.waitKey(1) & 0xFF
#         if k==27:
#             break
#     cv2.destroyAllWindows()

# imgBlending(img1,img2)

# 이미지 비트연산
def bitOperation_white_bg(hpos,vpos):
    img1=cv2.imread('lantern.jpg')
    img2=cv2.imread('opencv_logo.png')
    
    rows,cols,_ = img2.shape
    roi = img1[vpos:vpos+rows,hpos:hpos+cols]
    
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray,205,255,cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
    img2_fg = cv2.bitwise_and(img2,img2,mask=mask_inv)
    
    dst = cv2.add(img1_bg,img2_fg)
    img1[vpos:vpos+rows,hpos:hpos+cols] = dst
    
    b,g,r = cv2.split(img1)
    img1 = cv2.merge([r,g,b])
    
    plt.imshow(img1)
    plt.title('Result')
    plt.xticks([])
    plt.yticks([])
    plt.show()

bitOperation_white_bg(10,10)
    