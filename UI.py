from tkinter import*

class UI():
    window=Tk()
    window.title('2023 프로젝트')
    window.geometry('950x700')

    #사진,영상 같은거 위치
    ImageLabel=Label(window,bg='red',width=75,height=25)  
    ImageLabel.pack()
    ImageLabel.place(x=0,y=0)
    #영상 저장, 불러오기 버튼
    SaveButton=Button(window,text='저장',width=15,height=3)
    SaveButton.pack()
    SaveButton.place(x=600, y=20)
    LoadButton=Button(window,text='불러오기',width=15,height=3)
    LoadButton.pack()
    LoadButton.place(x=750,y=20)

    window.mainloop()


UI