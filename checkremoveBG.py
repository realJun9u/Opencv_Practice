# 각도에 따른 백그라운드 제거(열화상,실화상)
import cv2
import matplotlib.pyplot as plt
from cvzone.SelfiSegmentationModule import SelfiSegmentation

# resize color image
rh = 34/43 * 0.9
rw = 45/55 * 0.9
h,w,_ = 480,640,3
titles=[]
images=[]
segmentor = SelfiSegmentation()

for i in range(10):
    filename = 'FLIR' + str(106+i).rjust(4,'0') + '.jpg'
    img = cv2.imread(filename)
    if i % 2 == 1:
        img = img[h//2-int((h*rh)//2):h//2+int((h*rh)//2),w//2-int((w*rw)//2)+15:w//2+int((w*rw)//2)+15]
        img = cv2.resize(img,(320,240))
    img_out = segmentor.removeBG(img)
    img_out = cv2.cvtColor(img_out,cv2.COLOR_BGR2RGB)
    images.append(img_out)
    titles.append(filename)
plt.figure(figsize=(8,16))
for i in range(len(images)):
    plt.subplot(5,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    # plt.axis('off')
plt.tight_layout()
plt.show()