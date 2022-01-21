import cv2
import numpy as np
import math
from random import shuffle

# 캔버스 만들기
# img=np.full((512,512,3),255,np.uint8)
# 선 그리기
# cv2.line(img,pt1,pt2,color[,thickness[,lineType[,shift]]])
# img: 캔버스 pt1: 좌상단 pt2: 우하단 color: BGR 색
# thickness: 선 두께(음수면 도형 안쪽 채우기)
# lineType: 선 표현 방법(default: cv2.LINE_8)
# 사각형 그리기
# cv2.rectangle(img,pt1,pt2,color[,thickness[,lineType[,shift]]])
# 원 그리기
# cv2.circle(img,center,radius,color[,[,[,]]])
# center: 원의 중심 radius: 원의 반지름
# 타원 그리기
# cv2.ellipse(img,center,axes,angle,startAngle,endAngle,color[,[,[,]]])
# axes: 장축과 단축의 반의 길이(튜플)
# angle: 타원이 기울어지는 각도
# startAngle: 타원을 그리기 시작하는 각도
# endAngle: 타원이 마치는 각도
# 텍스트 넣기
# cv2.putText(img,text,org,fontFace,fontScale,color[,thickness[,lineType[,bottomLeftOrigin]]])
# text: 텍스트 org: 텍스트 이미지의 좌하단 꼭지점
# fontFace: 폰트 스타일
# fontScale: 폰트 크기
# thickness: 폰트 굵기

def drawing():
    img = np.full((512,512,3),255,np.uint8)

    cv2.line(img,(0,0),(511,511),(255,0,0),5)
    cv2.rectangle(img,(384,8),(504,200),(0,255,0),10)
    cv2.circle(img,(128,128),63,(0,0,255),-1)
    cv2.ellipse(img,(256,256),(100,50),30,90,180,(255,0,255),-1)

    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500),font,4,(0,255,255),3)

    cv2.imshow('Drawing',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 마우스로 도형 그리기
# cv2.setMouseCallback(winname,onMouse[,param])
# onMouse: 마우스 이벤트를 처리할 함수 이름 지정. 마우스 콜백함수
# param : Callback 함수에 전달되는 데이터 지정
# MouseCallback::def onMouse(event,x,y,flags,param)
# event: cv::MouseEventTypes
# cv2.EVENT_MOUSEMOVE: 포인터 움직임
# cv2.EVENT_LBUTTONDOWN 왼쪽 누르기, cv2.EVENT_LBUTTONUP 왼쪽 떼기
# cv2.EVENT_LBUTTONDBLCLK 왼쪽 더블클릭
# x,y : 이벤트 발생 위치
# flags: cv::MouseEventFlags
# cv2.EVENT_FLAG_LBUTTON: 왼쪽 눌림
# cv2.EVENT_FLAG_CTRLKEY: ctrl 키 눌림
# cv2.EVENT_FLAG_ALTKEY: alt 키 눌림
# cv2.EVENT_FLAG_SHIFTKEY: shify 키 눌림

img = np.full((512,512,3),255,np.uint8)
b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]
mode = True # 사각형 모드, 원 모드
draw = False
ix,iy = -1,-1
def onMouse(event,x,y,flags,param):
    global ix,iy,draw,mode,b,g,r
    img = param
    if event == cv2.EVENT_LBUTTONDOWN:
        draw=True
        ix,iy = x,y
        shuffle(b), shuffle(g), shuffle(r)
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            if mode:
                cv2.rectangle(img,(ix,iy),(x,y),(b[0],g[0],r[0]),-1)
                cv2.imshow('Paint_mode',img)
            else:
                radius = int(math.sqrt((ix-x)**2 + (iy-y)**2))
                cv2.circle(img,(ix,iy),radius,(b[0],g[0],r[0]),-1)
                cv2.imshow('Paint_mode',img)
    elif event == cv2.EVENT_LBUTTONUP:
        if draw:
            draw=False

def mouseBrush():
    global img,mode

    cv2.namedWindow('Paint_mode')
    cv2.setMouseCallback('Paint_mode',onMouse,img)

    while True:
        cv2.imshow('Paint_mode',img)
        k = cv2.waitKey(0) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break
    cv2.destroyAllWindows()

# drawing()
mouseBrush()
