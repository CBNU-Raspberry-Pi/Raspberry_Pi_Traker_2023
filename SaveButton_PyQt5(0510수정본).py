import sys
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHeaderView

class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('2023 프로젝트')
        self.setGeometry(0, 480, 640, 850)

        # 비디오 위치 (x,y,가로,세로)
        self.video_label = QLabel(self)
        self.video_label.setGeometry(0, 0, 640, 380)
        self.video_label.setStyleSheet("background-color: red;")

        # 불러오기 버튼
        self.SaveButton = QPushButton('저장', self)
        self.SaveButton.setGeometry(650, 20, 100, 50)
        self.load_button = QPushButton('불러오기', self)
        self.load_button.setGeometry(750, 20, 100, 50)
        self.load_button.clicked.connect(self.open_file)

        # 표 생성
        self.table = QTableWidget(self)
        self.table.setGeometry(0, 480, 640, 400)  # 표의 위치와 크기 지정
        self.table.setRowCount(3)  # 행 수 설정
        self.table.setColumnCount(4)  # 열 수 설정

        # 표 데이터 입력
        data = [
            ['A1', 'B1', 'C1', 'D1'],
            ['A2', 'B2', 'C2', 'D2'],
            ['A3', 'B3', 'C3', 'D3']
        ]

        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(item))

        # 열의 넓이 조정
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        
        # 행의 높이 조정
        for i in range(3):
            self.table.verticalHeader().setSectionResizeMode(i, QHeaderView.Fixed)
            self.table.verticalHeader().resizeSection(i, 160)
        
        # 글자 크기 조정
        font = QFont('Arial', 20)  # 글자 크기를 20으로 설정
        self.table.setFont(font)  # 전체 표의 글자 크기를 설정
                
        # 표 크기 조정
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
        # 저장 버튼에 클릭 이벤트 연결
        self.SaveButton.clicked.connect(self.save_document)

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

    def save_document(self):
        # 파일 저장 대화상자 생성
        file_path, _ = QFileDialog.getSaveFileName(self, "Save document", "", "Text Files (*.txt)")

        if file_path:
            # 동영상 재생 시간 가져오기
            video_duration = self.cap.get(cv2.CAP_PROP_FRAME_COUNT) / self.cap.get(cv2.CAP_PROP_FPS)
            video_duration_sec = int(video_duration)  # 재생 시간을 정수로 변환

            # 표의 내용 가져오기
            table_data = []
            for i in range(self.table.rowCount()):
                row_data = []
                for j in range(self.table.columnCount()):
                    item = self.table.item(i, j)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                table_data.append(row_data)

            # 문서로 저장
            with open(file_path, 'w') as file:
                file.write(f'동영상 재생 시간: {video_duration_sec}초\n')
                file.write('표의 내용:\n')
                for row in table_data:
                    file.write('\t'.join(row) + '\n')

            print('문서 저장이 완료되었습니다.')

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
