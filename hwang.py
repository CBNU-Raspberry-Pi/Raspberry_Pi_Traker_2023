
from PyQt5 import *
import cv2
import threading
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import sys


               
# class Thread3(QThread):
   
#     signal = pyqtSignal(str)
#     def __init__(self, parent):
#         super().__init__(parent)

#     def run(self):





form_class = uic.loadUiType('ui.ui')[0]
running = False

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.webcam = cv2.VideoCapture(0)


        self.btn1.clicked.connect(self.btnFun1)
        # self.btn_save.clicked.connect(self.btnFun_save)
        # self.btn_start.clicked.connect(self.btnFun_start)
        # self.btn_stop.clicked.connect(self.btnFun_stop)


    def btnFun1(self):
        print('ddd')


        
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

