import os
import cv2
from tkinter import filedialog
from tkinter import messagebox

def LoadFile():

    #파일 불러오기
    while True:
        files = filedialog.askopenfilenames(initialdir='/',\
                                            title='Select file',\
                                                filetypes=(('media files','*.mp4'), ('all files','*.*')))
        
        #취소 버튼일 시 오류 메세지가 뜨지 않도록
        if len(files) != 0:

            #확장자 확인
            file_path = str(files[0])   #파일 경로
            ext_name = os.path.splitext(file_path)  #확장자명

            if ext_name[1] == '.mp4':   #확장자명이 mp4일 경우 while break
                break
            else:   #확장자명이 mp4가 아닐 경우 while continue
                messagebox.showwarning('경고', '동영상 파일이 아닙니다.')
                continue
        else:
             break

def SaveFile():

    #파일_선택하기
        files = filedialog.asksaveasfilename(initialdir="/",\
                                            title=('Save file'),\
                                                filetypes=(('media files','*.mp4'), ('all files', ('*.*'))))