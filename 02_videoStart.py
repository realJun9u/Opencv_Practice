import cv2
import numpy as np
import os

# cv2.VideoCapture(devindex)
# VideoCapture 객체 생성
# index는 카메라 장치 인덱스

# VidepCapture객체.set(propId,value)
# VideoCapture 객체의 속성 정의
# 3 : cv2.CAP_PROP_POS_AVI_WIDTH 비디오 스트림 가로 길이 설정
# 4 : cv2.CAP_PROP_POS_AVI_HEIGHT 비디오 스트림 세로 길이 설정

# VidepCapture객체.read()
# 재생되는 비디오 한 프레임 읽기
# retval : 읽기 성공 여부
# image : 불러온 프레임

# VidepCapture객체.isOpened()
# VidepCapture객체.open()
# cap이 초기화 되지 않음을 체크하여 False면 open하면 됨

# cv2.cvtColor(frame,color)

# VideoCaptrue객체.release()
# VideoCapture객체 닫기
def showVideo():
    try:
        print("카메라 구동")
        cap = cv2.VideoCapture(0)
    except:
        print("카메라 구동 실패")
        return
    cap.set(3,1280)
    cap.set(4,720)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("비디오 읽기 오류")
            break
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Show Video',img_gray)

        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break

    print(cap.get(3))
    print(cap.get(4))
    cap.release()
    cv2.destroyAllWindows()

# cv2.VideoCapture(filename) : 파일에 대한 객체 생성
def readVideo(video_file):
    try:
        cap2 = cv2.VideoCapture(video_file)
        print("영상을 불러옵니다")
    except:
        print("영상을 불러오는데 실패했습니다")
        return

    while True:
        ret, frame = cap2.read()
        if not ret:
            print("영상 재생에 실패했습니다")
            break
        cv2.namedWindow('Play Video',cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.imshow('Play Video',frame)
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break
    print(cap2.get(3))
    print(cap2.get(4))
    cap2.release()
    cv2.destroyAllWindows()

# cv2.VideoWriter(filename,fourcc,fps,frameSize)
# cv2.VideoWriter_fourcc : 영상 코덱 지정
# cv2.flip(src),flipCode,[, dst]) : 0 : 상하 1: 좌우
# VideoWriter객체.write(imageobj) : 비디오 저장
def writeVideo():
    try:
        print("카메라 구동")
        cap = cv2.VideoCapture(0)
    except:
        print("카메라 구동 실패")
        return
    fps = 20.0 # 저장할 초당 프레임
    width = int(cap.get(3)) # 프레임 사이즈 지정
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D','I','V','X')

    out = cv2.VideoWriter('mycam.mp4',fcc,fps,(width,height))
    print('녹화 시작')
    while True:
        ret, frame = cap.read()

        if not ret:
            print('비디오 읽기 오류')
            break

        frame = cv2.flip(frame, 1) # 반전
        cv2.imshow('Video', frame)
        out.write(frame)

        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            print('녹화 종료')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# showVideo()
# readVideo('Sand.mp4')
writeVideo()
