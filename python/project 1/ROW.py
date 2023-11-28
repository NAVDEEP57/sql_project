from tkinter import * 

def save_info():
    question_info = question.get()
    choices_info = choices.get()
    correct_answer_info = correct_answer.get()
    marks_info = marks.get()
    time_info = time.get()
    
    #print('all values')
    
    file = open("user.txt","w")
    
    file.write(question_info)
    
    file.write("\n")
    
    file.write(choices_info)
    
    file.write("\n")
    
    file.write(correct_answer_info)
    
    file.write("\n")
    
    file.write(str(marks_info))
    
    file.write("\n")
    
    file.write(str(time_info))
    
    file.close()
    
    

app = Tk()

app.geometry("600x600")

app.title("Assesment Question")

heading = Label(text="Enter the Asked Information",fg="black",bg="yellow",width="500",height="3",font="10")

heading.pack()

question_text = Label(text="Question")
choices_text = Label(text="Choices separated by #")
correct_answer_text = Label(text="Correct Answer")
marks_text = Label(text='Marks')
time_text = Label(text="Time in seconds")

question_text.place(x=15,y=70)
choices_text.place(x=15,y=140)
correct_answer_text.place(x=15,y=210)
marks_text.place(x=15,y=280)
time_text.place(x=15,y=350)

question = StringVar()
choices = StringVar()
correct_answer = StringVar()
marks = IntVar()
time = IntVar()

question_entry = Entry(textvariable=question,width="30")
choices_entry = Entry(textvariable=choices,width="30")
correct_answer_entry = Entry(textvariable=correct_answer,width="30")
marks_entry = Entry(textvariable=marks,width="30")
time_entry = Entry(textvariable=time,width="30")

question_entry.place(x=15,y=100)
choices_entry.place(x=15,y=180)
correct_answer_entry.place(x=15,y=240)
marks_entry.place(x=15,y=300)
time_entry.place(x=15,y=380)

button = Button(app,text="Submit Data",command=save_info,width="30",height="2",bg="grey")

button.place(x=15,y=420)


mainloop()
