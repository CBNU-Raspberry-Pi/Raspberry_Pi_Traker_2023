from tkinter import*
import SaveButton_tkinter as SB_tk

class UI():
    window=Tk()
    window.title('2023 프로젝트')
    window.geometry('950x700')

    #사진,영상 같은거 위치 75,25의 크기가 너무 작아 영상의 크기가 다른 문제 수정해야함!!!!!!!!!!!!!!!!!!
    ImageLabel=Label(window,bg='red',width=75,height=25)  
    ImageLabel.pack()
    ImageLabel.place(x=0,y=0)
    #영상 저장, 불러오기 버튼
    SaveButton=Button(window,text='저장',width=15,height=3, command=SB_tk.SaveFile)
    SaveButton.pack()
    SaveButton.place(x=600, y=20)
    LoadButton=Button(window,text='불러오기',width=15,height=3, command=SB_tk.LoadFile)
    LoadButton.pack()
    LoadButton.place(x=750,y=20)

    window.mainloop()


UI