from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 800, 600)

        # QLabel 위젯 추가
        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 50, 700, 500)

        # 파일 불러오기 액션 추가
        file_action = QAction("Open File", self)
        file_action.triggered.connect(self.open_file)
        self.menuBar().addAction(file_action)

    def open_file(self):
        # 파일 선택 대화상자 생성
        file_dialog = QFileDialog()
        # 다이얼로그 타이틀 설정
        file_dialog.setWindowTitle("Open File")
        # 파일 필터 설정 (여기서는 mp4 파일)
        file_dialog.setNameFilter("mp4 files (*.mp4)")
        # 대화상자 띄우기
        if file_dialog.exec_() == QFileDialog.Accepted:
            # 선택된 파일 경로 출력
            file_path = file_dialog.selectedFiles()[0]
            print(file_path)
            # 선택된 파일을 QLabel에 출력
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    sys.exit(app.exec_())
