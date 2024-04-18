from tkinter import *
from tkinter import ttk
import sqlite3

c = sqlite3.connect("Student.db")
curses = c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS Student"
               "(ID INTEGER, NAME VARCHAR(20), AGE INTEGER, DOB VARCHAR(8), GENDER VARCHAR(20), CITY VARCHAR(20))")
c.commit()
c.close()
print("TABLE CREATED")


class Student:
    def __init__(self, main):
        self.main = main
        self.TFrame = Frame(self.main, height=50, width=1200, background="yellow", bd=2, relief=GROOVE)
        self.TFrame.pack()
        self.Title = Label(self.TFrame, text="STUDENT MANAGEMENT SYSTEM", font="times 20 bold", width=1200, bg="yellow")
        self.Title.pack()

#FRAME1>>>>>>
        self.Frame_1 = Frame(self.main, height=530, width=400, bd=2, relief=GROOVE, bg="yellow")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.propagate(False)

        Label(self.Frame_1, text="STUDENT DETAILS", background="yellow", font="times, 12 bold").place(x=20, y=20)

        self.Id = Label(self.Frame_1, text="ID:", background="yellow", font="times 12 bold")                    #ID
        self.Id.place(x=40, y=60)
        self.Id_Entry = Entry(self.Frame_1, width=40)
        self.Id_Entry.place(x=150, y=60)

        self.Name = Label(self.Frame_1, text="NAME:", background="yellow", font="times 12 bold")                #NAME
        self.Name.place(x=40, y=100)
        self.Name_Entry = Entry(self.Frame_1, width=40)
        self.Name_Entry.place(x=150, y=100)

        self.Age = Label(self.Frame_1, text="AGE:", background="yellow", font="times 12 bold")                  #AGE
        self.Age.place(x=40, y=140)
        self.Age_Entry = Entry(self.Frame_1, width=40)
        self.Age_Entry.place(x=150, y=140)

        self.DOB = Label(self.Frame_1, text="DOB:", background="yellow", font="times 12 bold")                  #DOB
        self.DOB.place(x=40, y=180)
        self.DOB_Entry = Entry(self.Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=180)

        self.Gender = Label(self.Frame_1, text="GENDER:", background="yellow", font="times 12 bold")            #GENDER
        self.Gender.place(x=40, y=220)
        self.Gender_Entry = Entry(self.Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=220)

        self.City = Label(self.Frame_1, text="CITY:", background="yellow", font="times 12 bold")                #CITY
        self.City.place(x=40, y=260)
        self.City_Entry = Entry(self.Frame_1, width=40)
        self.City_Entry.place(x=150, y=260)

#BUTTONS>>>>>>
        self.Button_Frame = Frame(self.Frame_1, height=250, width=250, background="yellow", relief=GROOVE, bd=2)
        self.Button_Frame.place(x=80, y=300)

        self.Add = Button(self.Button_Frame, text="Add", width=25,  font="times 12 bold", command=self.add)
        self.Add.pack()

        self.Delete = Button(self.Button_Frame, text="Delete", width=25, font="times 12 bold", command=self.delete)
        self.Delete.pack()

        self.Clear = Button(self.Button_Frame, text="Clear", width=25, font="times 12 bold", command=self.clear)
        self.Clear.pack()

        self.Update = Button(self.Button_Frame, text="Update", width=25, font="times 12 bold", command=self.update)
        self.Update.pack()

#FRAME2>>>>>
        self.Frame_2 = Frame(self.main, height=550, width=800, bd=2, relief=GROOVE, bg="yellow")
        self.Frame_2.pack(side=RIGHT)

        self.tree = ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings", height=25)

        self.tree.column("#1", anchor=CENTER, width=70)
        self.tree.heading("#1", text="ID")

        self.tree.column("#2", anchor=CENTER, width=170)
        self.tree.heading("#2", text="NAME")

        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="DOB")

        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="AGE")

        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="GENDER")

        self.tree.column("#6", anchor=CENTER, width=225)
        self.tree.heading("#6", text="CITY")

        self.tree.insert("", index=0, values=(1, "Vishaal", 18, "26/08/2000", "Male", "Madurai"))

        self.tree.pack()

#FUNCTION>>>
    def add(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        c =sqlite3.connect("Student.db")
        curses = c.cursor()
        curses.execute("INSERT INTO Student(ID, NAME, AGE, DOB, GENDER, CITY) VALUES(?, ?, ?, ?, ?, ?)",
                       (id, name, age, dob, gender, city))
        c.commit()
        c.close()
        print("VALUE INSERTED SUCCESSFULLY")
        self.tree.insert("", index=0, values=(id, name, age, dob, gender, city))

    def delete(self):
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        print(selected_item)
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("DELETE FROM Student WHERE ID={}".format(selected_item))
        print("VALUE DELETED SUCCESSFULLY")
        c.commit()
        c.close()
        self.tree.delete(item)

    def clear(self):
        self.Id_Entry.delete(0, END)
        self.Name_Entry.delete(0, END)
        self.Age_Entry.delete(0, END)
        self.DOB_Entry.delete(0, END)
        self.Gender_Entry.delete(0, END)
        self.City_Entry.delete(0, END)

    def update(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        c = sqlite3.connect("Student.db")
        cursor = c.cursor()
        cursor.execute("UPDATE Student SET ID=?, NAME=?, AGE=?, DOB=?, GENDER=?, CITY=? WHERE ID=?",
                       (selected_item, name, age, dob, gender, city, selected_item))
        c.commit()
        c.close()
        print("VALUE UPDATED SUCCESSFULLY")
        self.tree.item(item, values=(id,  name, age, dob, gender, city))


main = Tk()
main.title("STUDENT MANAGEMENT SYSTEM")
main.resizable(False, False)
main.geometry("1200x600")

Student(main)
main.mainloop()
