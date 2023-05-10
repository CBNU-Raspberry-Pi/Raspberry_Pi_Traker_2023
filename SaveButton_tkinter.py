from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

class UI():
    def __init__(self):
        self.window = Tk()
        self.window.title('2023 프로젝트')
        self.window.geometry('950x700')

        # 비디오 위치
        self.video_label = Label(self.window, bg='red', width=640, height=380)  
        self.video_label.pack()
        self.video_label.place(x=0, y=0)

        # 불러오기 버튼
        self.SaveButton = Button(self.window, text='저장', width=15, height=3)
        self.SaveButton.pack()
        self.SaveButton.place(x=640, y=20)
        self.load_button = Button(self.window, text='불러오기', width=15, height=3, command=self.open_file)
        self.load_button.pack()
        self.load_button.place(x=790, y=20)

    def open_file(self):
        # 파일 선택 대화상자 생성
        file_path = filedialog.askopenfilename()
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
            # OpenCV에서 읽은 이미지를 PIL 이미지로 변환
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)

            # 이미지 크기 조정
            width, height = self.video_label.winfo_width(), self.video_label.winfo_height()
            img = img.resize((width, height))

            img = ImageTk.PhotoImage(img)

            # 비디오 라벨에 이미지 설정
            self.video_label.configure(image=img)
            self.video_label.image = img

        # 33밀리초마다 비디오 재생
        self.video_label.after(33, self.play_video)

if __name__ == '__main__':
    ui = UI()
    ui.window.mainloop()