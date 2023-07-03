
from PyQt5 import *
import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sys
import contours as ct
import draw_contours as dr

               
# class Thread3(QThread):
   
#     signal = pyqtSignal(str)
#     def __init__(self, parent):
#         super().__init__(parent)

#     def run(self):


form_class = uic.loadUiType('ui.ui')[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn1.clicked.connect(self.btnFun1)
        self.StartBtn.clicked.connect(self.StartFun)
        self.StopBtn.clicked.connect(self.StopFun)
        self.ObSize.sliderReleased.connect(self.ChangeSize)
        self.GrayContours.sliderReleased.connect(self.ChangeCon)
        self.StartBtn_2.clicked.connect(self.StartFun2)
        self.StopBtn_2.clicked.connect(self.StopFun2)


    def btnFun1(self):
        print('save')

    def StartFun(self):
        global frame
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,730)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,500)

        while cv2.waitKey(33)<0:
            ret,frame = self.capture.read()
            if ret :
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                img = QImage(frame,frame.shape[1],frame.shape[0],QImage.Format_RGB888)
                pixmap=QPixmap.fromImage(img)
                self.CLabel.setPixmap(pixmap)
            else :
                print("error: Could not read frame")
                break

    def StopFun(self):
        if not self.capture.isOpened():
            return
        self.capture.release()
        self.CLabel.clear()

    def ChangeSize(self):
        global Size
        Size = self.ObSize.value()
        self.sizenum.setText(str(Size))

        
    def ChangeCon(self):
        global con
        con = self.GrayContours.value()
        self.connum.setText(str(con))

    def StartFun2(self):
        GrayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) ## 새로받은 이미지 흑백처리
        GrayFrame = cv2.GaussianBlur(src=GrayFrame, ksize=(5, 5), sigmaX=0)

        #여기 고쳐야 됨.
        pre_frame = GrayFrame
        total_sketch = frame

        ctr = ct.find_contours(pre_frame,GrayFrame,int(Size))
        img = dr.draw_contours(total_sketch,ctr,int(con))
        Qimg = QImage(img,frame.shape[1],frame.shape[0],QImage.Format_RGB888)
        pixmap=QPixmap.fromImage(Qimg)
        self.CLabel.setPixmap(pixmap)


        print('good job')

    def StopFun2(self):
        print('bbb')

        

        
#     def btnFun_save(self):




#     def btnFun_start(self):

#         self.gogo = Thread1(self)
#         self.gogo.signal.connect(self.funcEmit)
#         self.gogo.start()

#         self.movie = QMovie('ongoing.gif', QByteArray(), self)
#         self.movie.setCacheMode(QMovie.CacheAll)
#         self.progress.setMovie(self.movie)
#         self.movie.start()



#     def btnFun_stop(self):
#         try :
#             self.gogo.thread_stop()
#             self.progress.setText(' ')
#         except :
#             pass        

#     def funcEmit(self, now_ma1, now_ma2, now_ma3, now_ma4, next_step, trade_num):
#         self.trade_num.setText(trade_num)
#         self.next_step.setText(next_step)
#         self.now_ma1.setText(now_ma1)
#         self.now_ma2.setText(now_ma2)
#         self.now_ma3.setText(now_ma3)
#         self.now_ma4.setText(now_ma4)

# ##    def funcEmit1(self, save_status):
# ##        self.save_status.setText(save_status)

#     def funcEmit2(self, my_1_1, my_1_2, my_2_1, my_2_2, my_3_1, my_3_2, login_status, my_money):
#         self.my_1_1.setText(my_1_1)
#         self.my_1_2.setText(my_1_2)
#         self.my_2_1.setText(my_2_1)
#         self.my_2_2.setText(my_2_2)
#         self.my_3_1.setText(my_3_1)
#         self.my_3_2.setText(my_3_2)
#         self.login_status.setText(login_status)
#         self.my_money.setText(my_money)

   
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

