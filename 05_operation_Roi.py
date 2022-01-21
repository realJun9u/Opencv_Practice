import cv2
import numpy as np

# 이미지 속성
# 1. img.shape: 해상도 및 채널 수
# 2. img.size: 이미지 크기 (바이트 단위)
# 3. img.dtype: 이미지 데이터 타입
img = cv2.imread('lantern.jpg')
# print(img.shape)
# print(img.size)
# print(img.dtype)
# cv2.imshow('Show Image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 이미지 픽셀 값 얻고 수정
# px = img[500,900]
# print('BGR',px)
# print('b',px[0])
# print('g',px[1])
# print('r',px[2])
# # 최적화된 방법
# B = img.item(500,900,0)
# G = img.item(500,900,1)
# R = img.item(500,900,2)
# BGR = [B, G, R]
# print(BGR)
# # 픽셀 값 수정
# img.itemset((500,900,2),100)
# print(px)
# 이미지 채널 분리
# 채널이 각각 하나이므로 흑색 이미지로 보임
img = cv2.imread('milk.jpg')
# img_copy = img.copy()
# b, g, r = cv2.split(img_copy)
# cv2.imshow('Blue Channel',b)
# cv2.imshow('Green Channel',g)
# cv2.imshow('Red Channel',r)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 채널 교체 1
# img_copy = img.copy()
# b, g, r = cv2.split(img_copy)
# b_zero = np.full(img.shape[0:2],0,np.uint8)
# img_bzero = cv2.merge((b_zero,g,r))
# cv2.imshow('Merge Image',img_bzero)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 채널 교체 2
# img_bzero = img.copy()
# img_bzero[:,:,0] = 0
# cv2.imshow('Blue Zero Image',img_bzero)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # ROI
# img = cv2.imread('lantern.jpg')
# x,y = 430, 980
# h,w = 560, 350
# subimg = img[x:x+h,y:y+w]
# cv2.imshow('ROI',subimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.rectangle(subimg,(0,0),(w-1,h-1),(0,255,255),5)
# cv2.imshow('ROI BOX',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 마우스 이벤트로 ROI 지정
img = cv2.imread('milk.jpg')
drag = False
ix,iy=-1,-1
blue, yellow = (255,0,0),(0,255,255)

def onMouse(event,x,y,flags,param):
    global drag,ix,iy,blue,yellow
    if event == cv2.EVENT_LBUTTONDOWN:
        drag = True
        ix,iy=x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drag:
            img_draw = param.copy()
            cv2.rectangle(img_draw,(ix,iy),(x,y),blue,2)
            cv2.imshow('Show Image',img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if drag:
            drag = False
            w = x - ix
            h = y - iy
            if w > 0 and h > 0:
                cv2.rectangle(param,(ix,iy),(x,y),yellow,2)
                cv2.imshow('Show Image',param)

                roi=param[iy:iy+h,ix:ix+w]
                cv2.imshow('ROI',roi)
                cv2.moveWindow('ROI',500,250)
                cv2.imwrite('ROI.jpg',roi)
cv2.imshow('Show Image',img)
cv2.setMouseCallback('Show Image',onMouse,param=img)
cv2.waitKey(0)
cv2.destroyAllWindows()
