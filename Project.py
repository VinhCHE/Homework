# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:45:13 2020

@author: mrptv
"""

from tkinter import *
from datetime import date, datetime
from os import path
root = Tk()
dfDay=0
#varible section

dName= {       
       -7:"Monday",
       -6:"Tuesday",
       -5:"Wednesday",
       -4:"Thursday",
       -3:"Friday",
       -2:"Saturday",
       -1:"Sunday",
       0:"Monday",
       1:"Tuesday",
       2:"Wednesday",
       3:"Thursday",
       4:"Friday",
       5:"Saturday",
       6:"Sunday",
       7:"Monday",
       8:"Tuesday",
       9:"Wednesday",
       10:"Thursday",
       11:"Friday",
       12:"Saturday",
       13:"Sunday"
       }
mName= {
       1:"January",
       2:"February",
       3:"March",
       4:"April",
       5:"May",
       6:"June",
       7:"July",       
       8:"August",
       9:"September",
       10:"October",
       11:"November",
       12:"December",
       }
InputDate=0
########class
detailF=Frame(root)
homeF=Frame(root)
dateF =""
timeF =""
dInput=StringVar()
nameInput=StringVar()
detailInput=StringVar()
hourInput=IntVar()
minuteInput=IntVar()
fileRead=[]
selection=-1

class openingClass:
#    global dfDay
    def pushIn(var):
        global dfDay
        print((date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+var)*86400)))
        global InputDate
        global dInput,eDetail
        InputDate=(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+var)*86400))
        print(dfDay)
        dInput.set(str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+var)*86400).strftime("%Y/%m/%d")))
#   Function of button
    def textProcess(inP):
        group=inP.split("###$#$##$###$##$#",1)
        v0=group[0]
        group=group[-1].split("###$#$##$###$##$#",1)
        v1=group[0]
        group=group[-1].split("###$#$##$###$##$#",1)
        v2=group[0]
        group=group[-1].split("###$#$##$###$##$#",1)
        v3=group[0]
        return openingClass.textFormat(v0,v1,v2,v3)
    def textFormat(v0,v1,v2,v3):
        result=""
        result="{0:10} AT {1:6}  Event name: {2:^20} detail: {3:>}".format(v0,v1,v2,v3)
        test=v0[1:2]
        return result
    def changeB(inP,h,m):
        global nameInput, detailInput,hourInput, minuteInput, root, selection, fileRead
        if  len(detailInput.get())==0 or len(nameInput.get())==0:
            return
        if hourInput.get()>23 or hourInput.get()<0 or minuteInput.get()>59 or minuteInput.get()<0:
            return
        inP=(dInput.get()+"###$#$##$###$##$#"+str(hourInput.get())+":"+str(minuteInput.get())+"###$#$##$###$##$#"+nameInput.get()+"###$#$##$###$##$#"+detailInput.get()+"\n")
        openingClass.FindModify(fileRead[selection],inP,"modify")        
        openingClass.Home()
    def SaveB(inP,h,m):
        if isinstance(h.get(), int) and isinstance(m.get(), int):
            if h.get()>=0 and h.get()<=23 and m.get()>=0 and m.get()<=59:
                i=openingClass.Save(inP,h,m)
                if i == 0:
                    return
                else:
                    openingClass.Home()
            else:
                print("ERROR Value is out of range in SaveB")
        else:
            print("ERROR value is not an integer")
    def decode(inP):
        global fileRead
        inP=fileRead[inP]
        group=inP.split("###$#$##$###$##$#")
        print(group)
        return group      
    def encode(date,name,detail,h,m):
        pass         
    def Save(inP,h,m):
        global detailInput,nameInput
        global dInput
        s=nameInput.get()
        if len(detailInput.get())==0 or len(nameInput.get())==0:
            return 0
        print(dInput.get()+"###$#$##$###$##$#"+str(h.get())+":"+str(m.get())+"###$#$##$###$##$#"+s+"###$#$##$###$##$#"+detailInput.get())
        f = open("data.project", "a")
        f.write(dInput.get()+"###$#$##$###$##$#"+str(h.get())+":"+str(m.get())+"###$#$##$###$##$#"+s+"###$#$##$###$##$#"+detailInput.get()+"\n")
        f.close()
    def deleteB():
        openingClass.FindModify(fileRead[selection],"No input","delete")        
        openingClass.Home()
    def FindModify(inP_old,inP,mode):
        print(inP_old,inP,mode)
        f = open("data.project", "r+")
        file=f.readlines()
        print("finish readline")
        count=0
        if mode == "modify":
            print("Modifying: ",inP)
            f.write(inP)
            f.close()
            f = open("data.project", "r+")
            file=f.readlines()
        elif mode == "delete":
            pass
        else:
            print("ERROR: Cannot find mode in function FindModify")
        for line in file:
            if line.strip("\n") == inP_old.strip("\n"):
                print("Going to delete",file[count], count)
                
                del file[count]
                f.close()
                f = open("data.project", "w+")
                for line in file:
                    f.write(line)
                f.close()
                return
            else:
                print(line.strip("\n"))
                print(inP_old.strip("\n"))
                print(line.strip("\n") == inP_old.strip("\n"))
            count = count+1
        f.close()        
    def edit():
        openingClass.InputFrame(1)
        global dInput, nameInput, eDetail,detailInput,detailF, timeF, hourInput, minuteInput, root, selection
        print(selection)
        inP=openingClass.decode(selection)
        strDetail=inP[3]
        detailInput.set(strDetail[0:-1])
        nameInput.set(inP[2])
        hourInput.set(int(inP[1].split(":")[0]))
        minuteInput.set(int(inP[1].split(":")[1]))
        dInput.set(datetime.now().strftime("%Y/%m/%d"))
        detailF.destroy()
        detailF=Frame(root)
        detailF.grid(row=3, column =1)
        spacing2=Label(detailF,padx=5).grid(row=14,column=1)
        dateLanel=Label(detailF,textvariable=dInput).grid(row=15,column=2)
        nameLabel=Label(detailF,text="Even Name:", height=3).grid(row=16, column=1)
        eDate = Entry(detailF, width=100, textvariable=nameInput).grid(row=16, column=2)        
        detailLabel=Label(detailF,text="Even Detail:", height=1).grid(row=17, column=1)
        eDetail = Entry(detailF, width=100,textvariable=detailInput).grid(row=17, column=2)         
        spacing2=Label(detailF,pady=20).grid(row=18,column=1)
        bSave=Button(detailF,text="Change",command=lambda : openingClass.changeB(detailF,hourInput,minuteInput)).grid(row=20,column=3)        
        bCancel=Button(detailF,text="Cancel", command= openingClass.Home).grid(row=20,column=4)
        lHour=Label(detailF, text="  24-based hour:").grid(row=16,column=3)
        sbHour=Entry(detailF,textvariable=hourInput).grid(row=16,column=4)
        lMinute=Label(detailF,text="  Minute:").grid(row=17,column=3)
        sbMinute=Entry(detailF,textvariable=minuteInput).grid(row=17,column=4)
    def Home():
        var1=StringVar()
        var2=StringVar()
        global root
        global detailF,homeF
        detailF.grid_forget()
        homeF.grid_forget()
        homeF=Frame(root)        
        homeF.grid(row=4, column =1)
        f = open("data.project", "r")
        global fileRead
        fileRead=[]
        for count in f.readlines():
            fileRead.append(count)
        fileRead.sort()
        def inputlb(a):
            global fileRead, selection
            selection1=lb.curselection()
            selection= selection1[0]
            var2.set(lb.get(selection)) #get file into variable                     
            T1.config(text=("Currently select: "+var2.get()))
        lb=Listbox(homeF, listvariable=var1, width=100,height=10)
        for items in fileRead:
            result=openingClass.textProcess(items)
            lb.insert("end",result)
        lb.grid(row=6, column=1)
        T1=Label(homeF,text=("Currently select: "+var2.get()))
        menuF2=Frame(homeF).grid(row=6,column=2)
        createB=Button(homeF,text="Create Event",command=lambda : openingClass.InputFrame(0)).grid(row=12,column=0)
        editB=Button(homeF,text="Edit Event", command=openingClass.edit).grid(row=12,column=1)
        deleteB=Button(homeF,text="Delete Event", command= openingClass.deleteB).grid(row=12,column=2)        
        space=Label(homeF,text=" ").grid(row=13,column=2) 
        T1.grid(row=11,column=1)
        lb.bind("<<ListboxSelect>>",lambda e:inputlb(1)) 
     #   Starting Function
    def __init__ (self,master):
        self.master = master
        master.title = "Project 1"
        global dateF
        dateF=Frame(master)
        dateF.grid(row=1,column=1)
        bToday=Button(dateF,height=1,width=5,bg="white",text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + 0*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(0)).grid(row=5, column=5)
        bPlus1=Button(dateF,height=1,width=5,text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + 1*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(1)).grid(row=5, column=6)
        bPlus2=Button(dateF,height=1,width=5,text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + 2*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(2)).grid(row=5, column=7)
        bPlue3=Button(dateF,height=1,width=5,text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + 3*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(3)).grid(row=5, column=8)
        bMinus1=Button(dateF,height=1,width=5,text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - 1*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(-1)).grid(row=5, column=4)
        bMinus2=Button(dateF,height=1,width=5,text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - 2*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(-2)).grid(row=5, column=3)
        bMinus3=Button(dateF,height=1,width=5,text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - 3*86400).day), font=("arial", 28),command=lambda : openingClass.pushIn(-3)).grid(row=5, column=2)
        bNext=Button(dateF,text="Next",command=self.fNext).grid(row=5, column=9)
        bBack=Button(dateF,text="Back",command=self.fBack).grid(row=5, column=1)
#title
        mToday=Label(dateF,pady=3,width=15,text=str(mName[date.fromtimestamp(datetime.timestamp(datetime.now())+86400*(dfDay)).month]+" "+str(date.fromtimestamp(datetime.timestamp(datetime.now())+86400*dfDay).year))).grid(row=3, column=5)
        lToday=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())])).grid(row=4, column=5)        
        lPlus1=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+1])).grid(row=4, column=6)
        lPlus2=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+2])).grid(row=4, column=7)
        lPlue3=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+3])).grid(row=4, column=8)
        lMinus1=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-1])).grid(row=4, column=4)
        lMinus2=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-2])).grid(row=4, column=3)
        lMinus3=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-3])).grid(row=4, column=2)
        openingClass.Home()        

#detail
    def InputFrame(x):

        global dInput, nameInput, eDetail,detailInput,detailF, timeF, hourInput, minuteInput, root
        if x == 0:
            nameInput.set("")
            detailInput.set("")
            hourInput.set(0)
            minuteInput.set(0)
        else:
            pass
        detailF.grid_forget()        
        dInput.set(datetime.now().strftime("%Y/%m/%d"))
        detailF=Frame(root)
        detailF.grid(row=3, column =1)
        spacing2=Label(detailF,padx=5).grid(row=14,column=1)
        dateLanel=Label(detailF,textvariable=dInput).grid(row=15,column=2)
        nameLabel=Label(detailF,text="Even Name:", height=3).grid(row=16, column=1)
        eDate = Entry(detailF, width=100, textvariable=nameInput).grid(row=16, column=2)        
        detailLabel=Label(detailF,text="Even Detail:", height=1).grid(row=17, column=1)
        eDetail = Entry(detailF, width=100,textvariable=detailInput).grid(row=17, column=2)         
        spacing2=Label(detailF,pady=20).grid(row=18,column=1)
        bSave=Button(detailF,text="Save",command=lambda : openingClass.SaveB(detailF,hourInput,minuteInput)).grid(row=20,column=5)        
        bCancel=Button(detailF,text="Cancel",command= openingClass.Home).grid(row=20,column=7)
        lHour=Label(detailF, text="  24-based hour:").grid(row=16,column=3)
        sbHour=Entry(detailF,textvariable=hourInput).grid(row=16,column=4)
        lMinute=Label(detailF,text="  Minute:").grid(row=17,column=3)
        sbMinute=Entry(detailF,textvariable=minuteInput).grid(row=17,column=4)
        
    def Tdate(self,a):
        today =datetime.timestamp(datetime.now()) + a*86400
        rtoday=date.fromtimestamp(today)
        return rtoday.day
    def fNext(self):
        global dfDay
        print(dfDay/7)
        dfDay=dfDay+7
        global dateF
        if dfDay==0:
            bToday=Button(dateF,height=1,width=5,bg="white", font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+0)*86400).day)).grid(row=5,column=5)
        else:
            bToday=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+0)*86400).day),command=lambda : openingClass.pushIn(0)).grid(row=5,column=5)
        bPlus1=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+1)*86400).day),command=lambda : openingClass.pushIn(1)).grid(row=5,column=6)
        bPlus2=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+2)*86400).day),command=lambda : openingClass.pushIn(2)).grid(row=5,column=7)
        bPlue3=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+3)*86400).day),command=lambda : openingClass.pushIn(3)).grid(row=5,column=8)
        bMinus1=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - (-dfDay+1)*86400).day),command=lambda : openingClass.pushIn(-1)).grid(row=5,column=4)
        bMinus2=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - (-dfDay+2)*86400).day),command=lambda : openingClass.pushIn(-2)).grid(row=5,column=3)
        bMinus3=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - (-dfDay+3)*86400).day),command=lambda : openingClass.pushIn(-3)).grid(row=5,column=2)
        bNext=Button(dateF,text="Next", command=self.fNext).grid(row=5, column=9)
        bBack=Button(dateF,text="Back", command=self.fBack).grid(row=5, column=1)
                #title
        mToday=Label(dateF,pady=3,width=15,text=str(mName[date.fromtimestamp(datetime.timestamp(datetime.now())+86400*(dfDay)).month]+" "+str(date.fromtimestamp(datetime.timestamp(datetime.now())+86400*dfDay).year))).grid(row=3, column=5)
        lToday=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())])).grid(row=4, column=5)        
        lPlus1=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+1])).grid(row=4, column=6)
        lPlus2=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+2])).grid(row=4, column=7)
        lPlue3=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+3])).grid(row=4, column=8)
        lMinus1=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-1])).grid(row=4, column=4)
        lMinus2=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-2])).grid(row=4, column=3)
        lMinus3=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-3])).grid(row=4, column=2)

    def fBack(self):
        global dfDay
        print(dfDay/7)
        dfDay=dfDay-7
        global dateF
        if dfDay==0:
            bToday=Button(dateF,height=1,width=5, font=("arial", 28),bg="white",text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+0)*86400).day)).grid(row=5,column=5)
        else:
            bToday=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+0)*86400).day),command=lambda : openingClass.pushIn(0)).grid(row=5,column=5)
        bPlus1=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+1)*86400).day),command=lambda : openingClass.pushIn(1)).grid(row=5,column=6)
        bPlus2=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+2)*86400).day),command=lambda : openingClass.pushIn(2)).grid(row=5,column=7)
        bPlue3=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) + (dfDay+3)*86400).day),command=lambda : openingClass.pushIn(3)).grid(row=5,column=8)
        bMinus1=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - (-dfDay+1)*86400).day),command=lambda : openingClass.pushIn(-1)).grid(row=5,column=4)
        bMinus2=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - (-dfDay+2)*86400).day),command=lambda : openingClass.pushIn(-2)).grid(row=5,column=3)
        bMinus3=Button(dateF,height=1,width=5, font=("arial", 28),text=str(date.fromtimestamp(datetime.timestamp(datetime.now()) - (-dfDay+3)*86400).day),command=lambda : openingClass.pushIn(-3)).grid(row=5,column=2)
        bNext=Button(dateF,text="Next", command=self.fNext).grid(row=5, column=9)
        bBack=Button(dateF,text="Back", command=self.fBack).grid(row=5, column=1)
        #title
        mToday=Label(dateF,pady=3,width=15,text=str(mName[date.fromtimestamp(datetime.timestamp(datetime.now())+86400*(dfDay)).month]+" "+str(date.fromtimestamp(datetime.timestamp(datetime.now())+86400*dfDay).year))).grid(row=3, column=5)
        lToday=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())])).grid(row=4, column=5)        
        lPlus1=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+1])).grid(row=4, column=6)
        lPlus2=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+2])).grid(row=4, column=7)
        lPlue3=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())+3])).grid(row=4, column=8)
        lMinus1=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-1])).grid(row=4, column=4)
        lMinus2=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-2])).grid(row=4, column=3)
        lMinus3=Label(dateF,pady=3,width=15,text=str(dName[date.weekday(datetime.now())-3])).grid(row=4, column=2)

if path.exists("data.project"):
    print("exists")
    pass
else:
    print("non")
    f = open("data.project", "w+")
    f.close()
openC=openingClass(root)
root.mainloop()
