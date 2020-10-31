from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.font import Font
#main widget
root1=Tk()
#title
root1.title("Bipasha")
#loaded photo from file
photo_start=PhotoImage(file="Frame.png")
photo_quiz=PhotoImage(file="quiz2.png")
photo_win=PhotoImage(file="ok.png")
photo_loss=PhotoImage(file="bad.png")
photo_correct=PhotoImage(file="correct.png")
photo_wrong=PhotoImage(file="wrong.png")
photo_miss=PhotoImage(file="miss.png")
photo_great=PhotoImage(file="great.png")
#font that use on mark page to show answer list
fonti=Font(family="Comicsansms",size=8,weight="bold",underline=1)
#login function that work when we click on next button on login page
def login():
    #empty mark list that append mark if answer is correct
    mark_list=[]
    #get the level that we click on login page
    l=lavel.get()
    #get the name that we write on login page
    n=enter_name1.get()
    #it create a txt file and store the name that we write 
    with open("quiz.txt","w") as qz:
        qz.write(n)
    #if you do not entry any name it shows error with the help of tkinter.messagebox module
    if n=="": 
        tmsg.showerror("ERROR","You did not enter any name.")
    #if level is easy it enter in this elif file
    elif l=="level1":
        #empty list that append the answers that we click
        answer_list=[]
        #empty list that changes the answer list at next
        answer_list2=[]
        #def of mark page 
        def finish():
            #def of showing answer page
            def seeAnswer():
                #destroy all the previous page frame that we used
                finish_frame1.destroy()
                finish_frame2.destroy()
                finish_frame3.destroy()
                #create new frame that we are going to use
                ans_frame=Frame(root1,bg="grey",bd=7)
                ans_frame.pack(side="left",fill="y")
                ans_frame1=Frame(root1,bg="grey",bd=7)
                ans_frame1.pack(side="right",fill="y")
                ans_frame2=Frame(root1,bg="grey",bd=7)
                ans_frame2.pack(side="bottom",fill="x")
                #for range that help to identify the question that we left   
                for i in answer_list:
                    if i=="none" or i=="none1" or i=="none2" or i=="none3" or i=="none4" or i=="none5" or i=="none6" or i=="none7":
                        i="You left that..."
                        #append answer list2 with the left question
                        answer_list2.append(i)
                    else:
                        #append answer list2 with answer taht we touch
                        answer_list2.append(i)
                #showing correct anwer
                correct_ans=Label(ans_frame,text="CORRECT ANS:-\n1.Sahara\n2.Mute Swan\n3.Blind Snake\n4.Venus\n5.Mars\n6.Mount Everest\n7.Five\n8.Seven",bg="grey",fg="maroon",font="Times 20 bold",justify="left")
                correct_ans.pack()
                #showing the answer that we write
                #here we donot have to use title function if we give value of all answer in capital letter
                your_ans=Label(ans_frame1,text="YOUR ANS:-\n1."+answer_list2[0].title()+"\n2."+answer_list2[1].title()+"\n3."+answer_list2[2].title()+"\n4."+answer_list2[3].title()+"\n5."+answer_list2[4].title()+"\n6."+answer_list2[5].title()+"\n7."+answer_list2[6].title()+"\n8."+answer_list2[7].title(),bg="grey",fg="maroon",font="Times 20 bold",justify="left")
                your_ans.pack()
                #showing thanks
                thanks=Label(ans_frame2,text="Thanks For Using This Quiz App...",bg="grey",fg="blue",font="Comicsansms 15 bold")
                thanks.pack(side="top",pady=5)
                #quit button
                quit11=Button(ans_frame2,text="QUIT",bg="black",fg="white",command=root1.quit)
                quit11.pack(side="bottom",pady=5)
                pass
            #destroy all the frame of answer page of ques 8
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            #call the name from txt file and save in a var.
            with open("quiz.txt","r") as qz1:
                qz2=qz1.readline()
            #sum of all mark
            total=sum(mark_list)
            #frames that we use on mark page
            finish_frame1=Frame(root1,bg="grey")
            finish_frame1.pack(side="top",fill="x",pady=5)
            finish_frame2=Frame(root1,bg="grey")
            finish_frame2.pack(side="top",fill="x",pady=5)
            finish_frame3=Frame(root1,bg="grey")
            finish_frame3.pack(side="top",fill="x",pady=5)
            #label to show txt 
            see_answer_label=Label(finish_frame3,text="To see the answer click ",bg="grey",fg="maroon",font=fonti)
            see_answer_label.pack(side="left",anchor="w")
            #button to go on answer page
            see_answer_button=Button(finish_frame3,text="here:-",bg="grey",fg="maroon",font="Comocsansms 8 bold",command=seeAnswer)
            see_answer_button.pack(side="left",anchor="w")
            #if mark is less then 8 or greater then 5
            if (total>=6) and (total<8):
                flabel2=Label(finish_frame1,image=photo_win)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="Congratulation! "+qz2.title()+"\nYou Win....\nyour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack(side="top",pady=3)
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
            #if the mark is 8
            elif total==8:
                flabel2=Label(finish_frame1,image=photo_great)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="WOWWWWW.....!\nYOU score full... "+qz2.title()+"\nYou Win....\nyour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack(side="top",pady=3)
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
            #if the mark is less then 6
            else:
                flabel2=Label(finish_frame1,image=photo_loss)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="Sorry! "+qz2.title()+"\nYou loss....\nTry your best in next appearence.\nYour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack()
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
                
            pass
        #def of eight answer page
        def eightha():
            #store answer of question 8 that we click  
            e51=e5.get()
            #append with the answer that we select
            answer_list.append(e51)
            #destroy the previous page layout
            q8f.destroy()
            q8bf.destroy()
            q8t.destroy()
            #global key help to destroy this frame in the other page
            global correctf1
            global correctf2
            global correctf3
            #make frame
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            #if correct answer
            if e51=="seven":
                #def to show time to next question
                def wait():
                    #get value of waiting time var
                    w=waiting_time.get()
                    #decrease 1 sec after 1 sec from 3 sec
                    w=w-1
                    #set this var with new value
                    waiting_time.set(w)
                    #update the label widget, where we store waitin time var
                    correctw2.update()
                    #after function that help to go wait function after 1 sec
                    correctw2.after(1000,wait)
                    #if waiting var is 0 go to the function that we return
                    if w==0:
                        return finish()
                #create a var with intvar
                waiting_time=IntVar()
                #set this var with 3 seconds
                waiting_time.set(3)
                #if the answer is correct a image shown on widget with this label
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                #if the answer is correct the correct tet will shown on widget
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                #text that show with the remaining time of next question
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                #time loop to go next question
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                #text that show with remaining time to go next question
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                #append 1 mark with mark list if answer is correct
                mark_list.append(1)
                #after function that help to go wait function after 1 sec
                correctw2.after(1000,wait)
            #if you do not click any option it gives none7 that set before with e51
            elif e51=="none7":
                #wait function similar with previous one
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                #if do not click any option it show a image
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                #if miss the answer a text will show on widget
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                #time loop to go next question similar to previous one
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                #if left mark list append 0
                mark_list.append(0)
                #after function of time loop similar to previous one
                correctw2.after(1000,wait)
            #if answer is wrong it will come to else part
            else:
                #same with the previous one
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        #function of question 8
        def eighthq():
            #destroy all the widget that appear before on root1 tk
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            #create a global function that help to destroy this frame in next
            global q8f
            global q8bf
            global q8t
            q8t=Frame(root1,bg="grey")
            q8t.pack(side="top",pady=2,fill="x")
            q8f=Frame(root1,bg="grey")
            q8f.pack(side="top",pady=100)
            q8bf=Frame(root1,bg="grey")
            q8bf.pack(side="bottom",pady=5,fill="x")
            #time loop to show remaining time to give answer
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return eightha()
            #time var with intvar
            timer=IntVar()
            #set it with 30
            timer.set(30)
            #timer show on the widget
            time=Label(q8t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            #text that show with time that left
            timee=Label(q8t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            #after function to go newtime function
            time.after(1000,new_time)
            #question label
            lab7=Label(q8f,text="8. How many continents are there in the world ?",bg="grey",font=font)
            lab7.pack(side="top",anchor="w",padx=5,pady=12)
            #global e5 to get the value of next function
            global e5
            #e5 with string var
            e5=StringVar()
            #e5 set with the value of none7
            #here we can set 'you left that' #if we set that we do not have to create answerlist 2 'a empty list' 
            #but before we do not think to show the answer that we click so we create it next with answer list 2 and for range
            e5.set("none7")
            #option with its value
            eighth=Radiobutton(q8f,text="Five",variable=e5,value="five",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            eighth=Radiobutton(q8f,text="Six",variable=e5,value="six",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            eighth=Radiobutton(q8f,text="Seven",variable=e5,value="seven",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            q8b=Button(q8bf,text="Next:-",fg="white",bg="black",font=font2,command=eightha)
            q8b.pack(anchor="e",padx=8,side="bottom")

            pass
        #function of seventh answer same with the eighta function means eight answer
        #level 1 other all function are same with this
        #below are the other question and answer in descending order
        def seventha():
            e41=e4.get()
            answer_list.append(e41)
            q7f.destroy()
            q7bf.destroy()
            q7t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e41=="five":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e41=="none6":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            
        #function of seventh question
        def seventhq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q7f
            global q7bf
            global q7t
            q7t=Frame(root1,bg="grey")
            q7t.pack(side="top",pady=2,fill="x")
            q7f=Frame(root1,bg="grey")
            q7f.pack(side="top",pady=100)
            q7bf=Frame(root1,bg="grey")
            q7bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return seventha()
            timer=IntVar()
            timer.set(30)
            time=Label(q7t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q7t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab6=Label(q7f,text="7. How many oceans are there in the world ?",bg="grey",font=font)
            lab6.pack(side="top",anchor="w",padx=5,pady=12)
            global e4
            e4=StringVar()
            e4.set("none6")
            seventh=Radiobutton(q7f,text="Four",variable=e4,value="four",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            seventh=Radiobutton(q7f,text="Five",variable=e4,value="five",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            seventh=Radiobutton(q7f,text="Six",variable=e4,value="six",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            q7b=Button(q7bf,text="Next:-",fg="white",bg="black",font=font2,command=seventha)
            q7b.pack(anchor="e",padx=8,side="bottom")
        #function of sixth answer
        def sixtha():
            e31=e3.get()
            answer_list.append(e31)
            q6f.destroy()
            q6bf.destroy()
            q6t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e31=="mount everest":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e31=="none5":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            
        #function of sixth question
        def sixthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q6f
            global q6bf
            global q6t
            q6t=Frame(root1,bg="grey")
            q6t.pack(side="top",pady=2,fill="x")
            q6f=Frame(root1,bg="grey")
            q6f.pack(side="top",pady=100)
            q6bf=Frame(root1,bg="grey")
            q6bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return sixtha()
            timer=IntVar()
            timer.set(30)
            time=Label(q6t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q6t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab5=Label(q6f,text="6. Which is the tallest mountain peak in the world ?",bg="grey",font=font)
            lab5.pack(side="top",anchor="w",padx=5,pady=12)
            global e3
            e3=StringVar()
            e3.set("none5")
            sixth=Radiobutton(q6f,text="Nanda Devi",variable=e3,value="nanda devi",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            sixth=Radiobutton(q6f,text="Mount Everest",variable=e3,value="mount everest",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            sixth=Radiobutton(q6f,text="Kamet",variable=e3,value="kamet",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            q6b=Button(q6bf,text="Next:-",fg="white",bg="black",font=font2,command=sixtha)
            q6b.pack(anchor="e",padx=8,side="bottom")

            pass
        #function of fifth answer
        def fiftha():
            e21=e2.get()
            answer_list.append(e21)
            q5f.destroy()
            q5bf.destroy()
            q5t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e21=="mars":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e21=="none4":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            
        #function of fifth question
        def fifthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            
            global q5f
            global q5bf
            global q5t
            q5t=Frame(root1,bg="grey")
            q5t.pack(side="top",pady=2,fill="x")
            q5f=Frame(root1,bg="grey")
            q5f.pack(side="top",pady=100)
            q5bf=Frame(root1,bg="grey")
            q5bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return fiftha()
            timer=IntVar()
            timer.set(30)
            time=Label(q5t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q5t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab4=Label(q5f,text="5. Which planet is known as the red planet ?",bg="grey",font=font)
            lab4.pack(side="top",anchor="w",padx=5,pady=12)
            global e2
            e2=StringVar()
            e2.set("none4")
            fifth=Radiobutton(q5f,text="Mars",variable=e2,value="mars",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            fifth=Radiobutton(q5f,text="Venus",variable=e2,value="venus",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            fifth=Radiobutton(q5f,text="Mercury",variable=e2,value="mercury",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            q5b=Button(q5bf,text="Next:-",fg="white",bg="black",font=font2,command=fiftha)
            q5b.pack(anchor="e",padx=8,side="bottom")

            pass
        #function of fourth answer
        def fourtha():
            e11=e1.get()
            answer_list.append(e11)
            q4f.destroy()
            q4bf.destroy()
            q4t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e11=="venus":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)

            elif e11=="none3":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
                

            
        #function of fourth question
        def fourthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            
            
            global q4f
            global q4bf
            global q4t
            q4t=Frame(root1,bg="grey")
            q4t.pack(side="top",pady=2,fill="x")
            q4f=Frame(root1,bg="grey")
            q4f.pack(side="top",pady=100)
            q4bf=Frame(root1,bg="grey")
            q4bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return fourtha()
            timer=IntVar()
            timer.set(30)
            time=Label(q4t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q4t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab3=Label(q4f,text="4. Which is the hottest planet in our solar system ?",bg="grey",font=font)
            lab3.pack(side="top",anchor="w",padx=5,pady=12)
            global e1
            e1=StringVar()
            e1.set("none3")
            fourth=Radiobutton(q4f,text="Pluto",variable=e1,value="pluto",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            fourth=Radiobutton(q4f,text="Jupiter",variable=e1,value="jupiter",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            fourth=Radiobutton(q4f,text="Venus",variable=e1,value="venus",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            q4b=Button(q4bf,text="Next:-",fg="white",bg="black",font=font2,command=fourtha)
            q4b.pack(anchor="e",padx=8,side="bottom")
        #function of third answer
        def thirda():
            ee=e.get()
            answer_list.append(ee)
            q3f.destroy()
            q3bf.destroy()
            q3t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if ee=="blind snake":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif ee=="none2":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        #function of third question
        def thirdq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            
            global q3f
            global q3bf
            global q3t
            q3t=Frame(root1,bg="grey")
            q3t.pack(side="top",pady=2,fill="x")
            q3f=Frame(root1,bg="grey")
            q3f.pack(side="top",pady=100)
            q3bf=Frame(root1,bg="grey")
            q3bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return thirda()
            timer=IntVar()
            timer.set(30)
            time=Label(q3t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q3t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab2=Label(q3f,text="3. Which is the smallest snake ?",bg="grey",font=font)
            lab2.pack(side="top",anchor="w",padx=5,pady=12)
            global e
            e=StringVar()
            e.set("none2")
            third=Radiobutton(q3f,text="Anaconda",variable=e,value="anaconda",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            third=Radiobutton(q3f,text="Blind Snake",variable=e,value="blind snake",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            third=Radiobutton(q3f,text="Black Mamba",variable=e,value="black mamba",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            q3b=Button(q3bf,text="Next:-",fg="white",bg="black",font=font2,command=thirda)
            q3b.pack(anchor="e",padx=8,side="bottom")

            pass
        #function of second question
        def seconda():
            w1=w.get()
            answer_list.append(w1)
            q2f.destroy()
            q2bf.destroy()
            q2t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if w1=="mute swan":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif w1=="none1":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

                
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
                
        #function of second question
        def secondq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            
            global q2f
            global q2bf
            global q2t
            q2t=Frame(root1,bg="grey")
            q2t.pack(side="top",pady=2,fill="x")
            q2f=Frame(root1,bg="grey")
            q2f.pack(side="top",pady=100)
            q2bf=Frame(root1,bg="grey")
            q2bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return seconda()
            timer=IntVar()
            timer.set(30)
            time=Label(q2t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q2t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab1=Label(q2f,text="2. Which is the haviest flying bird ?",bg="grey",font=font)
            lab1.pack(side="top",anchor="w",padx=5,pady=12)
            global w
            w=StringVar()
            w.set("none1")
            second=Radiobutton(q2f,text="Mute Swan",variable=w,value="mute swan",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            second=Radiobutton(q2f,text="Ostrich",variable=w,value="ostrich",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            second=Radiobutton(q2f,text="Humming Bird",variable=w,value="humming bird",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            q2b=Button(q2bf,text="Next:-",fg="white",bg="black",font=font2,command=seconda)
            q2b.pack(anchor="e",padx=8,side="bottom")
        #function of first answer
        def firsta():
            q1=q.get()
            answer_list.append(q1)
            q1f.destroy()
            q1bf.destroy()
            q1t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if q1=="sahara":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif q1=="none":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
                
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        

            pass
        #function of first question
        f1.destroy()
        f2.destroy()
        f3.destroy()
        f4.destroy()
        q1t=Frame(root1,bg="grey")
        q1t.pack(side="top",pady=2,fill="x")
        q1f=Frame(root1,bg="grey")
        q1f.pack(side="top",pady=100)
        q1bf=Frame(root1,bg="grey")
        q1bf.pack(side="bottom",pady=5,fill="x")
        def new_time():
            ti=timer.get()
            ti1=ti-1
            timer.set(ti1)
            time.update()
            time.after(1000,new_time)
            if ti==0:
                return firsta()
        timer=IntVar()
        timer.set(30)
        time=Label(q1t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
        time.pack(side="top",anchor="e")
        timee=Label(q1t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
        timee.pack(side="top",anchor="e")
        time.after(1000,new_time)
        lab0=Label(q1f,text="1. Which is the largest desert in the world ?",bg="grey",font=font)
        lab0.pack(side="top",anchor="w",padx=5,pady=12)
        q=StringVar()
        q.set("none")
        first=Radiobutton(q1f,text="Sahara",variable=q,value="sahara",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        first=Radiobutton(q1f,text="Thar",variable=q,value="thar",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        first=Radiobutton(q1f,text="Australia",variable=q,value="australia",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        q1b=Button(q1bf,text="Next:-",fg="white",bg="black",font=font2,command=firsta)
        q1b.pack(anchor="e",padx=8,side="bottom")
    #function of level 2 similar with level one 
    elif l=="level2":
        answer_list=[]
        answer_list2=[]
        def finish():
            def seeAnswer():
                finish_frame1.destroy()
                finish_frame2.destroy()
                finish_frame3.destroy()
                ans_frame=Frame(root1,bg="grey",bd=7)
                ans_frame.pack(side="left",fill="y")
                ans_frame1=Frame(root1,bg="grey",bd=7)
                ans_frame1.pack(side="right",fill="y")
                ans_frame2=Frame(root1,bg="grey",bd=7)
                ans_frame2.pack(side="bottom",fill="x")
                for i in answer_list:
                    if i=="none" or i=="none1" or i=="none2" or i=="none3" or i=="none4" or i=="none5" or i=="none6" or i=="none7":
                        i="You left that..."
                        answer_list2.append(i)
                    else:
                        answer_list2.append(i)

                correct_ans=Label(ans_frame,text="CORRECT ANS:-\n1.Graphite\n2.Nitrogen\n3.Thermometer\n4.Rudyard Kipling\n5.Christopher Columbus\n6.Operating System\n7.Soil\n8.No",bg="grey",fg="maroon",font="Times 20 bold",justify="left")
                correct_ans.pack()
                your_ans=Label(ans_frame1,text="YOUR ANS:-\n1."+answer_list2[0].title()+"\n2."+answer_list2[1].title()+"\n3."+answer_list2[2].title()+"\n4."+answer_list2[3].title()+"\n5."+answer_list2[4].title()+"\n6."+answer_list2[5].title()+"\n7."+answer_list2[6].title()+"\n8."+answer_list2[7].title(),bg="grey",fg="maroon",font="Times 20 bold",justify="left")
                your_ans.pack()
                thanks=Label(ans_frame2,text="Thanks For Using This Quiz App...",bg="grey",fg="blue",font="Comicsansms 15 bold")
                thanks.pack(side="top",pady=5)
                quit11=Button(ans_frame2,text="QUIT",bg="black",fg="white",command=root1.quit)
                quit11.pack(side="bottom",pady=5)
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            
            with open("quiz.txt","r") as qz1:
                qz2=qz1.readline()
            
            total=sum(mark_list)
            finish_frame1=Frame(root1,bg="grey")
            finish_frame1.pack(side="top",fill="x",pady=5)
            finish_frame2=Frame(root1,bg="grey")
            finish_frame2.pack(side="top",fill="x",pady=5)
            finish_frame3=Frame(root1,bg="grey")
            finish_frame3.pack(side="top",fill="x",pady=5)
            see_answer_label=Label(finish_frame3,text="To see the answer click ",bg="grey",fg="maroon",font=fonti)
            see_answer_label.pack(side="left",anchor="w")
            see_answer_button=Button(finish_frame3,text="here:-",bg="grey",fg="maroon",font="Comocsansms 8 bold",command=seeAnswer)
            see_answer_button.pack(side="left",anchor="w")
            if (total>=6) and (total<8):
                flabel2=Label(finish_frame1,image=photo_win)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="Congratulation! "+qz2.title()+"\nYou Win....\nyour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack(side="top",pady=3)
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
            elif total==8:
                flabel2=Label(finish_frame1,image=photo_great)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="WOWWWWW.....!\nYOU score full... "+qz2.title()+"\nYou Win....\nyour mark is "+str(total),bg="grey",font="Times 15 bold")
                flabel1.pack(side="top",pady=3)
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
            else:
                flabel2=Label(finish_frame1,image=photo_loss)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="Sorry! "+qz2.title()+"\nYou loss....\nTry your best in next appearence.\nYour mark is "+str(total),bg="grey",font="Times 15 bold")
                flabel1.pack()
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
                
            pass
        def eightha():
            e51=e5.get()
            answer_list.append(e51)
            q8f.destroy()
            q8bf.destroy()
            q8t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e51=="no":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e51=="none7":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def eighthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q8f
            global q8bf
            global q8t
            q8t=Frame(root1,bg="grey")
            q8t.pack(side="top",pady=2,fill="x")
            q8f=Frame(root1,bg="grey")
            q8f.pack(side="top",pady=100)
            q8bf=Frame(root1,bg="grey")
            q8bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return eightha()
            timer=IntVar()
            timer.set(30)
            time=Label(q8t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q8t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab7=Label(q8f,text="8. Is 1900 a leap year ?",bg="grey",font=font)
            lab7.pack(side="top",anchor="w",padx=5,pady=12)
            global e5
            e5=StringVar()
            e5.set("none7")
            eighth=Radiobutton(q8f,text="Yes",variable=e5,value="yes",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            eighth=Radiobutton(q8f,text="No",variable=e5,value="no",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            #eighth=Radiobutton(q8f,text="Seven",variable=e5,value="seven",bg="grey",font=font2)
            #eighth.pack(side="top",anchor="w",pady=1,padx=2)
            q8b=Button(q8bf,text="Next:-",fg="white",bg="black",font=font2,command=eightha)
            q8b.pack(anchor="e",padx=8,side="bottom")

            pass
        def seventha():
            e41=e4.get()
            answer_list.append(e41)
            q7f.destroy()
            q7bf.destroy()
            q7t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e41=="soil":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e41=="none6":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def seventhq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q7f
            global q7bf
            global q7t
            q7t=Frame(root1,bg="grey")
            q7t.pack(side="top",pady=2,fill="x")
            q7f=Frame(root1,bg="grey")
            q7f.pack(side="top",pady=100)
            q7bf=Frame(root1,bg="grey")
            q7bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return seventha()
            timer=IntVar()
            timer.set(30)
            time=Label(q7t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q7t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab6=Label(q7f,text="7. Plants receive their nutrients mainly from ?",bg="grey",font=font)
            lab6.pack(side="top",anchor="w",padx=5,pady=12)
            global e4
            e4=StringVar()
            e4.set("none6")
            seventh=Radiobutton(q7f,text="Chlorophyll",variable=e4,value="chlorophyll",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            seventh=Radiobutton(q7f,text="Light",variable=e4,value="light",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            seventh=Radiobutton(q7f,text="Soil",variable=e4,value="soil",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            q7b=Button(q7bf,text="Next:-",fg="white",bg="black",font=font2,command=seventha)
            q7b.pack(anchor="e",padx=8,side="bottom")
        def sixtha():
            e31=e3.get()
            answer_list.append(e31)
            q6f.destroy()
            q6bf.destroy()
            q6t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e31=="operating system":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e31=="none5":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def sixthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q6f
            global q6bf
            global q6t
            q6t=Frame(root1,bg="grey")
            q6t.pack(side="top",pady=2,fill="x")
            q6f=Frame(root1,bg="grey")
            q6f.pack(side="top",pady=100)
            q6bf=Frame(root1,bg="grey")
            q6bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return sixtha()
            timer=IntVar()
            timer.set(30)
            time=Label(q6t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q6t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab5=Label(q6f,text="6. 'OS' computer abbreviation usually means ?",bg="grey",font=font)
            lab5.pack(side="top",anchor="w",padx=5,pady=12)
            global e3
            e3=StringVar()
            e3.set("none5")
            sixth=Radiobutton(q6f,text="Open Software",variable=e3,value="open software",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            sixth=Radiobutton(q6f,text="Optical Sensor",variable=e3,value="optical sensor",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            sixth=Radiobutton(q6f,text="Operating System",variable=e3,value="operating system",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            q6b=Button(q6bf,text="Next:-",fg="white",bg="black",font=font2,command=sixtha)
            q6b.pack(anchor="e",padx=8,side="bottom")

            pass
        def fiftha():
            e21=e2.get()
            answer_list.append(e21)
            q5f.destroy()
            q5bf.destroy()
            q5t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e21=="christopher columbus":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e21=="none4":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def fifthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q5f
            global q5bf
            global q5t
            q5t=Frame(root1,bg="grey")
            q5t.pack(side="top",pady=2,fill="x")
            q5f=Frame(root1,bg="grey")
            q5f.pack(side="top",pady=100)
            q5bf=Frame(root1,bg="grey")
            q5bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return fiftha()
            timer=IntVar()
            timer.set(30)
            time=Label(q5t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q5t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab4=Label(q5f,text="5. Who first discovered America ?",bg="grey",font=font)
            lab4.pack(side="top",anchor="w",padx=5,pady=12)
            global e2
            e2=StringVar()
            e2.set("none4")
            fifth=Radiobutton(q5f,text="Galileo",variable=e2,value="galileo",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            fifth=Radiobutton(q5f,text="Christopher Columbus",variable=e2,value="christopher columbus",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            fifth=Radiobutton(q5f,text="Vasco Da Gama",variable=e2,value="vasco da gama",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            q5b=Button(q5bf,text="Next:-",fg="white",bg="black",font=font2,command=fiftha)
            q5b.pack(anchor="e",padx=8,side="bottom")

            pass
        def fourtha():
            e11=e1.get()
            answer_list.append(e11)
            q4f.destroy()
            q4bf.destroy()
            q4t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e11=="rudyard kipling":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)

            elif e11=="none3":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def fourthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q4f
            global q4bf
            global q4t
            q4t=Frame(root1,bg="grey")
            q4t.pack(side="top",pady=2,fill="x")
            q4f=Frame(root1,bg="grey")
            q4f.pack(side="top",pady=100)
            q4bf=Frame(root1,bg="grey")
            q4bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return fourtha()
            timer=IntVar()
            timer.set(30)
            time=Label(q4t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q4t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab3=Label(q4f,text="4. Who wrote 'Jungle Book' ?",bg="grey",font=font)
            lab3.pack(side="top",anchor="w",padx=5,pady=12)
            global e1
            e1=StringVar()
            e1.set("none3")
            fourth=Radiobutton(q4f,text="Rudyard Kipling",variable=e1,value="rudyard kipling",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            fourth=Radiobutton(q4f,text="Lewis Carroll",variable=e1,value="lewis carroll",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            fourth=Radiobutton(q4f,text="Charles Dickens",variable=e1,value="charles dickens",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            q4b=Button(q4bf,text="Next:-",fg="white",bg="black",font=font2,command=fourtha)
            q4b.pack(anchor="e",padx=8,side="bottom")
        def thirda():
            ee=e.get()
            answer_list.append(ee)
            q3f.destroy()
            q3bf.destroy()
            q3t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if ee=="thermometer":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif ee=="none2":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def thirdq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q3f
            global q3bf
            global q3t
            q3t=Frame(root1,bg="grey")
            q3t.pack(side="top",pady=2,fill="x")
            q3f=Frame(root1,bg="grey")
            q3f.pack(side="top",pady=100)
            q3bf=Frame(root1,bg="grey")
            q3bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return thirda()
            timer=IntVar()
            timer.set(30)
            time=Label(q3t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q3t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab2=Label(q3f,text="3. What Galileo invented ?",bg="grey",font=font)
            lab2.pack(side="top",anchor="w",padx=5,pady=12)
            global e
            e=StringVar()
            e.set("none2")
            third=Radiobutton(q3f,text="Barometer",variable=e,value="barometer",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            third=Radiobutton(q3f,text="Microscope",variable=e,value="microscope",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            third=Radiobutton(q3f,text="Thermometer",variable=e,value="thermometer",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            q3b=Button(q3bf,text="Next:-",fg="white",bg="black",font=font2,command=thirda)
            q3b.pack(anchor="e",padx=8,side="bottom")

            pass
        def seconda():
            w1=w.get()
            answer_list.append(w1)
            q2f.destroy()
            q2bf.destroy()
            q2t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if w1=="nitrogen":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif w1=="none1":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

                
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        

        def secondq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q2f
            global q2bf
            global q2t
            q2t=Frame(root1,bg="grey")
            q2t.pack(side="top",pady=2,fill="x")
            q2f=Frame(root1,bg="grey")
            q2f.pack(side="top",pady=100)
            q2bf=Frame(root1,bg="grey")
            q2bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return seconda()
            timer=IntVar()
            timer.set(30)
            time=Label(q2t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q2t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab1=Label(q2f,text="2. The gas usually filled in the electric bulb is:-",bg="grey",font=font)
            lab1.pack(side="top",anchor="w",padx=5,pady=12)
            global w
            w=StringVar()
            w.set("none1")
            second=Radiobutton(q2f,text="Nitrogen",variable=w,value="nitrogen",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            second=Radiobutton(q2f,text="Hydrogen",variable=w,value="hydrogen",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            second=Radiobutton(q2f,text="Oxygen",variable=w,value="oxygen",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            q2b=Button(q2bf,text="Next:-",fg="white",bg="black",font=font2,command=seconda)
            q2b.pack(anchor="e",padx=8,side="bottom")

            pass
        def firsta():
            q1=q.get()
            answer_list.append(q1)
            q1f.destroy()
            q1bf.destroy()
            q1t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if q1=="graphite":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif q1=="none":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
                
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        f1.destroy()
        f2.destroy()
        f3.destroy()
        f4.destroy()
        q1t=Frame(root1,bg="grey")
        q1t.pack(side="top",pady=2,fill="x")
        q1f=Frame(root1,bg="grey")
        q1f.pack(side="top",pady=100)
        q1bf=Frame(root1,bg="grey")
        q1bf.pack(side="bottom",pady=5,fill="x")
        def new_time():
            ti=timer.get()
            ti1=ti-1
            timer.set(ti1)
            time.update()
            time.after(1000,new_time)
            if ti==0:
                return firsta()
        timer=IntVar()
        timer.set(30)
        time=Label(q1t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
        time.pack(side="top",anchor="e")
        timee=Label(q1t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
        timee.pack(side="top",anchor="e")
        time.after(1000,new_time)
        lab0=Label(q1f,text="1. Which of the following is used in pencils ?",bg="grey",font=font)
        lab0.pack(side="top",anchor="w",padx=5,pady=12)
        q=StringVar()
        q.set("none")
        first=Radiobutton(q1f,text="Graphite",variable=q,value="graphite",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        first=Radiobutton(q1f,text="Silicon",variable=q,value="silicon",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        first=Radiobutton(q1f,text="Charcoal",variable=q,value="charcoal",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        q1b=Button(q1bf,text="Next:-",fg="white",bg="black",font=font2,command=firsta)
        q1b.pack(anchor="e",padx=8,side="bottom")
    #function of level 3 similar with level 3
    elif l=="level3":
        answer_list=[]
        answer_list2=[]
        def finish():
            def seeAnswer():
                finish_frame1.destroy()
                finish_frame2.destroy()
                finish_frame3.destroy()
                ans_frame=Frame(root1,bg="grey",bd=7)
                ans_frame.pack(side="left",fill="y")
                ans_frame1=Frame(root1,bg="grey",bd=7)
                ans_frame1.pack(side="right",fill="y")
                ans_frame2=Frame(root1,bg="grey",bd=7)
                ans_frame2.pack(side="bottom",fill="x")
                for i in answer_list:
                    if i=="none" or i=="none1" or i=="none2" or i=="none3" or i=="none4" or i=="none5" or i=="none6" or i=="none7":
                        i="You left that..."
                        answer_list2.append(i)
                    else:
                        answer_list2.append(i)
                correct_ans=Label(ans_frame,text="CORRECT ANS:-\n1.print('Hello World')\n2.#this is comment\n3.my-var\n4.Both of this correct\n5. .py\n6.def myfunction()\n7.upper()\n8. *",bg="grey",fg="maroon",font="Times 15 bold",justify="left")
                correct_ans.pack()
                #here i donot use any title function of string because all the answers are in small letter
                your_ans=Label(ans_frame1,text="YOUR ANS:-\n1."+answer_list2[0]+"\n2."+answer_list2[1]+"\n3."+answer_list2[2]+"\n4."+answer_list2[3]+"\n5."+answer_list2[4]+"\n6."+answer_list2[5]+"\n7."+answer_list2[6]+"\n8."+answer_list2[7],bg="grey",fg="maroon",font="Times 15 bold",justify="left")
                your_ans.pack()
                thanks=Label(ans_frame2,text="Thanks For Using This Quiz App...",bg="grey",fg="blue",font="Comicsansms 15 bold")
                thanks.pack(side="top",pady=5)
                quit11=Button(ans_frame2,text="QUIT",bg="black",fg="white",command=root1.quit)
                quit11.pack(side="bottom",pady=5)
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()

            with open("quiz.txt","r") as qz1:
                qz2=qz1.readline()
            
            total=sum(mark_list)
            finish_frame1=Frame(root1,bg="grey")
            finish_frame1.pack(side="top",fill="x",pady=5)
            finish_frame2=Frame(root1,bg="grey")
            finish_frame2.pack(side="top",fill="x",pady=5)
            finish_frame3=Frame(root1,bg="grey")
            finish_frame3.pack(side="top",fill="x",pady=5)
            see_answer_label=Label(finish_frame3,text="To see the answer click ",bg="grey",fg="maroon",font=fonti)
            see_answer_label.pack(side="left",anchor="w")
            see_answer_button=Button(finish_frame3,text="here:-",bg="grey",fg="maroon",font="Comocsansms 8 bold",command=seeAnswer)
            see_answer_button.pack(side="left",anchor="w")
            if (total>=6) and (total<8):
                flabel2=Label(finish_frame1,image=photo_win)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="Congratulation! "+qz2.title()+"\nYou Win....\nyour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack(side="top",pady=3)
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
            elif total==8:
                flabel2=Label(finish_frame1,image=photo_great)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="WOWWWWW.....!\nYOU score full... "+qz2.title()+"\nYou Win....\nyour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack(side="top",pady=3)
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
            else:
                flabel2=Label(finish_frame1,image=photo_loss)
                flabel2.pack()
                flabel1=Label(finish_frame2,text="Sorry! "+qz2.title()+"\nYou loss....\nTry your best in next appearence.\nYour mark is "+str(total),bg="grey",font="Times 20 bold")
                flabel1.pack()
                Button(finish_frame2,text="QUIT",bg="black",fg="white",command=root1.quit).pack(side="bottom",pady=3)
                
            pass
        def eightha():
            e51=e5.get()
            answer_list.append(e51)
            q8f.destroy()
            q8bf.destroy()
            q8t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e51=="*":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e51=="none7":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return finish()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to see the result.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        def eighthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q8f
            global q8bf
            global q8t
            q8t=Frame(root1,bg="grey")
            q8t.pack(side="top",pady=2,fill="x")
            q8f=Frame(root1,bg="grey")
            q8f.pack(side="top",pady=100)
            q8bf=Frame(root1,bg="grey")
            q8bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return eightha()
            timer=IntVar()
            timer.set(30)
            time=Label(q8t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q8t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab7=Label(q8f,text="8. Which operator is used to multiply numbers in python ?",bg="grey",font=font)
            lab7.pack(side="top",anchor="w",padx=5,pady=12)
            global e5
            e5=StringVar()
            e5.set("none7")
            eighth=Radiobutton(q8f,text="x",variable=e5,value="x",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            eighth=Radiobutton(q8f,text="%",variable=e5,value="%",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            eighth=Radiobutton(q8f,text="*",variable=e5,value="*",bg="grey",font=font2)
            eighth.pack(side="top",anchor="w",pady=1,padx=2)
            q8b=Button(q8bf,text="Next:-",fg="white",bg="black",font=font2,command=eightha)
            q8b.pack(anchor="e",padx=8,side="bottom")

            pass
        def seventha():
            e41=e4.get()
            answer_list.append(e41)
            q7f.destroy()
            q7bf.destroy()
            q7t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e41=="upper()":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e41=="none6":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return eighthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        def seventhq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q7f
            global q7bf
            global q7t
            q7t=Frame(root1,bg="grey")
            q7t.pack(side="top",pady=2,fill="x")
            q7f=Frame(root1,bg="grey")
            q7f.pack(side="top",pady=100)
            q7bf=Frame(root1,bg="grey")
            q7bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return seventha()
            timer=IntVar()
            timer.set(30)
            time=Label(q7t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q7t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab6=Label(q7f,text="7. Which method can be used to return a string in upper case letters ?",bg="grey",font=font)
            lab6.pack(side="top",anchor="w",padx=5,pady=12)
            global e4
            e4=StringVar()
            e4.set("none6")
            seventh=Radiobutton(q7f,text="upper()",variable=e4,value="upper()",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            seventh=Radiobutton(q7f,text="uppercase()",variable=e4,value="uppercase()",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            seventh=Radiobutton(q7f,text="toupper()",variable=e4,value="toupper()",bg="grey",font=font2)
            seventh.pack(side="top",anchor="w",pady=1,padx=2)
            q7b=Button(q7bf,text="Next:-",fg="white",bg="black",font=font2,command=seventha)
            q7b.pack(anchor="e",padx=8,side="bottom")
        def sixtha():
            e31=e3.get()
            answer_list.append(e31)
            q6f.destroy()
            q6bf.destroy()
            q6t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e31=="def myfunction()":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e31=="none5":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return seventhq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def sixthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q6f
            global q6bf
            global q6t
            q6t=Frame(root1,bg="grey")
            q6t.pack(side="top",pady=2,fill="x")
            q6f=Frame(root1,bg="grey")
            q6f.pack(side="top",pady=100)
            q6bf=Frame(root1,bg="grey")
            q6bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return sixtha()
            timer=IntVar()
            timer.set(30)
            time=Label(q6t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q6t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab5=Label(q6f,text="6. What is the correct way to create a function in python ?",bg="grey",font=font)
            lab5.pack(side="top",anchor="w",padx=5,pady=12)
            global e3
            e3=StringVar()
            e3.set("none5")
            sixth=Radiobutton(q6f,text="def myfunction",variable=e3,value="def myfunction",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            sixth=Radiobutton(q6f,text="create myfunction()",variable=e3,value="create myfunction()",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            sixth=Radiobutton(q6f,text="def myfunction()",variable=e3,value="def myfunction()",bg="grey",font=font2)
            sixth.pack(side="top",anchor="w",pady=1,padx=2)
            q6b=Button(q6bf,text="Next:-",fg="white",bg="black",font=font2,command=sixtha)
            q6b.pack(anchor="e",padx=8,side="bottom")

            pass
        def fiftha():
            e21=e2.get()
            answer_list.append(e21)
            q5f.destroy()
            q5bf.destroy()
            q5t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e21==".py":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif e21=="none4":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return sixthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        def fifthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q5f
            global q5bf
            global q5t
            q5t=Frame(root1,bg="grey")
            q5t.pack(side="top",pady=2,fill="x")
            q5f=Frame(root1,bg="grey")
            q5f.pack(side="top",pady=100)
            q5bf=Frame(root1,bg="grey")
            q5bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return fiftha()
            timer=IntVar()
            timer.set(30)
            time=Label(q5t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q5t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab4=Label(q5f,text="5. What is the correct file extension for python files ?",bg="grey",font=font)
            lab4.pack(side="top",anchor="w",padx=5,pady=12)
            global e2
            e2=StringVar()
            e2.set("none4")
            fifth=Radiobutton(q5f,text=".pt",variable=e2,value=".pt",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            fifth=Radiobutton(q5f,text=".py",variable=e2,value=".py",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            fifth=Radiobutton(q5f,text=".pyth",variable=e2,value=".pyth",bg="grey",font=font2)
            fifth.pack(side="top",anchor="w",pady=1,padx=2)
            q5b=Button(q5bf,text="Next:-",fg="white",bg="black",font=font2,command=fiftha)
            q5b.pack(anchor="e",padx=8,side="bottom")

            pass
        def fourtha():
            e11=e1.get()
            answer_list.append(e11)
            q4f.destroy()
            q4bf.destroy()
            q4t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if e11=="Both of this correct":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)

            elif e11=="none3":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fifthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        def fourthq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q4f
            global q4bf
            global q4t
            q4t=Frame(root1,bg="grey")
            q4t.pack(side="top",pady=2,fill="x")
            q4f=Frame(root1,bg="grey")
            q4f.pack(side="top",pady=100)
            q4bf=Frame(root1,bg="grey")
            q4bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return fourtha()
            timer=IntVar()
            timer.set(30)
            time=Label(q4t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q4t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab3=Label(q4f,text="4. How do you create a variable with the numeric value 5 ?",bg="grey",font=font)
            lab3.pack(side="top",anchor="w",padx=5,pady=12)
            global e1
            e1=StringVar()
            e1.set("none3")
            fourth=Radiobutton(q4f,text="x=int(5)",variable=e1,value="x=int(5)",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            fourth=Radiobutton(q4f,text="x=5",variable=e1,value="x=5",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            fourth=Radiobutton(q4f,text="Both of this correct.",variable=e1,value="Both of this correct",bg="grey",font=font2)
            fourth.pack(side="top",anchor="w",pady=1,padx=2)
            q4b=Button(q4bf,text="Next:-",fg="white",bg="black",font=font2,command=fourtha)
            q4b.pack(anchor="e",padx=8,side="bottom")
        def thirda():
            ee=e.get()
            answer_list.append(ee)
            q3f.destroy()
            q3bf.destroy()
            q3t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if ee=="my-var":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif ee=="none2":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return fourthq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

        def thirdq():
            
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q3f
            global q3bf
            global q3t
            q3t=Frame(root1,bg="grey")
            q3t.pack(side="top",pady=2,fill="x")
            q3f=Frame(root1,bg="grey")
            q3f.pack(side="top",pady=100)
            q3bf=Frame(root1,bg="grey")
            q3bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return thirda()
            timer=IntVar()
            timer.set(30)
            time=Label(q3t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q3t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab2=Label(q3f,text="3. Which is not a legel variable name ?",bg="grey",font=font)
            lab2.pack(side="top",anchor="w",padx=5,pady=12)
            global e
            e=StringVar()
            e.set("none2")
            third=Radiobutton(q3f,text="my_var",variable=e,value="my_var",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            third=Radiobutton(q3f,text="Myvar",variable=e,value="Myvar",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            third=Radiobutton(q3f,text="my-var",variable=e,value="my-var",bg="grey",font=font2)
            third.pack(side="top",anchor="w",pady=1,padx=2)
            q3b=Button(q3bf,text="Next:-",fg="white",bg="black",font=font2,command=thirda)
            q3b.pack(anchor="e",padx=8,side="bottom")

            pass
        def seconda():
            w1=w.get()
            answer_list.append(w1)
            q2f.destroy()
            q2bf.destroy()
            q2t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if w1=="#this is comment":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif w1=="none1":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)

                
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return thirdq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        def secondq():
            correctf1.destroy()
            correctf2.destroy()
            correctf3.destroy()
            global q2f
            global q2bf
            global q2t
            q2t=Frame(root1,bg="grey")
            q2t.pack(side="top",pady=2,fill="x")
            q2f=Frame(root1,bg="grey")
            q2f.pack(side="top",pady=100)
            q2bf=Frame(root1,bg="grey")
            q2bf.pack(side="bottom",pady=5,fill="x")
            def new_time():
                ti=timer.get()
                ti1=ti-1
                timer.set(ti1)
                time.update()
                time.after(1000,new_time)
                if ti==0:
                    return seconda()
            timer=IntVar()
            timer.set(30)
            time=Label(q2t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
            time.pack(side="top",anchor="e")
            timee=Label(q2t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
            timee.pack(side="top",anchor="e")
            time.after(1000,new_time)
            lab1=Label(q2f,text="2. How do you insert COMMENTS in python ?",bg="grey",font=font)
            lab1.pack(side="top",anchor="w",padx=5,pady=12)
            global w
            w=StringVar()
            w.set("none1")
            second=Radiobutton(q2f,text="//this is comment",variable=w,value="//this is comment",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            second=Radiobutton(q2f,text="#this is comment",variable=w,value="#this is comment",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            second=Radiobutton(q2f,text="/*this is comment*/",variable=w,value="/*this is comment*/",bg="grey",font=font2)
            second.pack(side="top",anchor="w",pady=1,padx=2)
            q2b=Button(q2bf,text="Next:-",fg="white",bg="black",font=font2,command=seconda)
            q2b.pack(anchor="e",padx=8,side="bottom")

            pass
        def firsta():
            q1=q.get()
            answer_list.append(q1)
            q1f.destroy()
            q1bf.destroy()
            q1t.destroy()
            global correctf1
            global correctf2
            global correctf3
            correctf1=Frame(root1,bg="grey")
            correctf1.pack(side="top")
            correctf2=Frame(root1,bg="grey")
            correctf2.pack(side="top")
            correctf3=Frame(root1,bg="grey")
            correctf3.pack(side="top",fill="x",pady=20)
            if q1=="print('Hello World')":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_correct)
                correctp.pack()
                correctc=Label(correctf2,text="CORRECT......",fg="blue",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(1)
                correctw2.after(1000,wait)
            elif q1=="none":
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_miss)
                correctp.pack()
                correctc=Label(correctf2,text="You miss to give answer...",fg="purple",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
                
            else:
                def wait():
                    w=waiting_time.get()
                    w=w-1
                    waiting_time.set(w)

                    correctw2.update()
                    correctw2.after(1000,wait)
                    if w==0:
                        return secondq()
                waiting_time=IntVar()
                waiting_time.set(3)
                correctp=Label(correctf1,image=photo_wrong)
                correctp.pack()
                correctc=Label(correctf2,text="SORRY...its wrong...\ntry the next one...",fg="red",bg="grey",font="Times 25 bold")
                correctc.pack(anchor="w")
                correctw1=Label(correctf3,text="seconds to generate next question.",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw1.pack(side="right",anchor="e")
                correctw2=Label(correctf3,textvariable=waiting_time,fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw2.pack(side="right",anchor="e")
                correctw3=Label(correctf3,text="wait for",fg="black",bg="grey",font="Comicsansms 8 bold")
                correctw3.pack(side="right",anchor="e")
                mark_list.append(0)
                correctw2.after(1000,wait)
        f1.destroy()
        f2.destroy()
        f3.destroy()
        f4.destroy()
        q1t=Frame(root1,bg="grey")
        q1t.pack(side="top",pady=2,fill="x")
        q1f=Frame(root1,bg="grey")
        q1f.pack(side="top",pady=100)
        q1bf=Frame(root1,bg="grey")
        q1bf.pack(side="bottom",pady=5,fill="x")
        def new_time():
            ti=timer.get()
            ti1=ti-1
            timer.set(ti1)
            time.update()
            time.after(1000,new_time)
            if ti==0:
                return firsta()
        timer=IntVar()
        timer.set(30)
        time=Label(q1t,textvariable=timer,bg="grey",fg="red",font="Comicsansms 20 bold")
        time.pack(side="top",anchor="e")
        timee=Label(q1t,text="second left",bg="grey",fg="black",font="Comicsansms 10 bold")
        timee.pack(side="top",anchor="e")
        time.after(1000,new_time)
        lab0=Label(q1f,text="1. What is the correct syntax to output 'Hello World' in python ?",bg="grey",font=font)
        lab0.pack(side="top",anchor="w",padx=5,pady=12)
        q=StringVar()
        q.set("none")
        first=Radiobutton(q1f,text="echo'Hello World'",variable=q,value="echo'Hello World'",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        first=Radiobutton(q1f,text="p'Hello World'",variable=q,value="p'Hello World'",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        first=Radiobutton(q1f,text="print('Hello World')",variable=q,value="print('Hello World')",bg="grey",font=font2)
        first.pack(side="top",anchor="w",pady=1,padx=2)
        q1b=Button(q1bf,text="Next:-",fg="white",bg="black",font=font2,command=firsta)
        q1b.pack(anchor="e",padx=8,side="bottom")
    #if l==level that i set on login widget with level string var it shows error means you do not click on any level and you can not access any of the level question  
    elif l=="lavel":
        tmsg.showerror("ERROR","You did not select any level")    
    
    pass
#creating a font # this is the only way to give underline all the letters in a line
font=Font(family="Times",size=15,weight="bold",underline=1)
font2=Font(family="Comicsansms",size=12,weight="bold")
#geometry of root1
root1.geometry("800x600")
#it maxsize is 800 and 600 means can not make it big from that 
root1.maxsize(800,600)
#minsize can not make it small
root1.minsize(800,600)
#root1 colour will be grey
root1.config(bg="grey")
#three frames 
f1=Frame(root1,bg="grey")
f1.pack(side="top",fill="x")
f2=Frame(root1,bg="grey")
f2.pack(side="top",fill="x")
f3=Frame(root1,bg="grey")
f3.pack(side="top",fill="x",pady=2)
f4=Frame(root1,bg="grey")
f4.pack(side="top",fill="x",pady=2)
#entry name string var
en=StringVar()
#set with no string it help to identify those who are not writing their name and show a error 
en.set("")
#entry name label
entr_name=Label(f2,text="Enter Name:-",bg="grey",fg="black",font=font)
entr_name.grid(row=2,column=1,padx=25,pady=40)
#name enter
enter_name1=Entry(f2,textvariable=en,width=40,font=font2)
enter_name1.grid(row=2,column=2,padx=5)
#it keeps the cursur on entry widget from begining
enter_name1.focus()
#level text
lav=Label(f3,text="Try Your Lavel:-",bg="grey",fg="black",font="Halvetica 15 italic")
lav.pack(side="top",pady=8,anchor="w",padx=15)
#level string var
lavel=StringVar()
#set with level
lavel.set("lavel")
#options of level
lv1=Radiobutton(f3,text="Lavel- Easy",variable=lavel,value="level1",bg="grey",font="Times 10 bold")
lv1.pack(side="top",pady=13,anchor="w",padx=3)
lv1=Radiobutton(f3,text="Lavel- Medium",variable=lavel,value="level2",bg="grey",font="Times 10 bold")
lv1.pack(side="top",pady=13,anchor="w",padx=3)
lv1=Radiobutton(f3,text="Lavel- Hard",variable=lavel,value="level3",bg="grey",font="Times 10 bold")
lv1.pack(side="top",pady=13,anchor="w",padx=3)
#button to log in
b1=Button(f3,image=photo_start,bg="grey",bd=3,relief=SUNKEN,command=login,width=150,height=40)
b1.pack(side="bottom")
lav2=Label(f1,image=photo_quiz,bg="grey",font="Comicsansms 23 bold")
lav2.pack(side="bottom")
#rules text
rules=Label(f4,text="Rules:- Enter your name and choose the level to start the quiz.\nEvery level have 8 questions carring 1 mark each\nand time is 30 seconds per question.\nIf you score 6 or above you will win\nelse you lose",bg="grey",fg="dark green",justify="left",font="Times 13 bold")
rules.pack(padx=4,pady=10,anchor="w")

root1.mainloop()
#in this app we do not use any user defined class