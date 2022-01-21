import cv2
import numpy as np
import matplotlib.pyplot as plt
# HSV 형식
# H(Hue) : 색상. 일반적인 색을 의미. 색이 각도로 표현이 됨. [0,180]
# S(Saturation) : 채도. 색의 순수성을 의미. 짙다, 흐리다로 표현이 됨. [0,255]
# V(Value) : 명도. 색의 밝고 어두운 정도. 수직축의 깊이로 표현. 어둡다 밝다로 표현이 됨. [0,255]
# cv2.cvtColor(frame,cv2.COLOR_BGR2HSV): BGR 형식을 HSV형식으로 변환
# cv2.inRange(frame_hsv,lowerb,upperb[,dst]): HSV형식 이미지의 하한과 상한을 정하여 마스크 생성
def tracking():
    try:
        print("카메라 구동")
        cap = cv2.VideoCapture('Coastline.mp4')
        cv2.namedWindow('Original',cv2.WINDOW_GUI_NORMAL|cv2.WINDOW_KEEPRATIO)
        cv2.namedWindow('Blue',cv2.WINDOW_GUI_NORMAL|cv2.WINDOW_KEEPRATIO)
        cv2.namedWindow('Green',cv2.WINDOW_GUI_NORMAL|cv2.WINDOW_KEEPRATIO)
        cv2.namedWindow('Red',cv2.WINDOW_GUI_NORMAL|cv2.WINDOW_KEEPRATIO)
    except:
        print("카메라 구동 실패")
        return
    while True:
        ret, frame = cap.read()
        if ret:
            frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

            lower_blue = np.array([100,100,100])
            upper_blue = np.array([140,255,255])
            lower_green = np.array([40,100,100])
            upper_green = np.array([80,255,255])
            lower_red = np.array([-10,100,100])
            upper_red = np.array([30,255,255])

            mask_blue = cv2.inRange(frame_hsv,lower_blue,upper_blue)
            mask_green = cv2.inRange(frame_hsv,lower_green,upper_green)
            mask_red = cv2.inRange(frame_hsv,lower_red,upper_red)

            res1 = cv2.bitwise_and(frame,frame,mask=mask_blue)
            res2 = cv2.bitwise_and(frame,frame,mask=mask_green)
            res3 = cv2.bitwise_and(frame,frame,mask=mask_red)

            cv2.imshow('Original',frame)
            cv2.imshow('Blue',res1)
            cv2.imshow('Green',res2)
            cv2.imshow('Red',res3)

            k = cv2.waitKey(20) & 0xFF
            if k==27:
                break
        else:
            print("비디오 종료")
            break
    cap.release()
    cv2.destroyAllWindows()
tracking()