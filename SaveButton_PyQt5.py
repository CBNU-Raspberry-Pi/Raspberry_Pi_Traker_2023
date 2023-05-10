import sys
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('2023 프로젝트')
        self.setGeometry(100, 100, 950, 700)

        # 비디오 위치
        self.video_label = QLabel(self)
        self.video_label.setGeometry(0, 0, 640, 380)
        self.video_label.setStyleSheet("background-color: red;")

        # 불러오기 버튼
        self.SaveButton = QPushButton('저장', self)
        self.SaveButton.setGeometry(650, 20, 100, 50)
        self.load_button = QPushButton('불러오기', self)
        self.load_button.setGeometry(750, 20, 100, 50)
        self.load_button.clicked.connect(self.open_file)

    def open_file(self):
        # 파일 선택 대화상자 생성
        file_path, _ = QFileDialog.getOpenFileName(self, "Open video file", "", "Video Files (*.mp4 *.avi *.mov)")

        if file_path:
            # OpenCV로 비디오 파일 열기
            self.cap = cv2.VideoCapture(file_path)

            # 비디오 사이즈 조정
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 380)

            # 비디오 재생
            self.play_video()

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            # OpenCV에서 읽은 이미지를 QImage로 변환
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            q_image = QImage(rgb_image, w, h, ch*w, QImage.Format_RGB888)

            # QImage를 QPixmap으로 변환
            pixmap = QPixmap.fromImage(q_image)

            # 이미지 크기 조정
            pixmap = pixmap.scaled(self.video_label.width(), self.video_label.height())

            # 비디오 라벨에 이미지 설정
            self.video_label.setPixmap(pixmap)

        # 33밀리초마다 비디오 재생
        QTimer.singleShot(33, self.play_video)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
