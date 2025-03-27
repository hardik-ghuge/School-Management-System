from tkinter import * 
import tkinter.messagebox as messagebox
import mysql.connector as mysql
root = Tk()
root.title("School Management System")
root.geometry("400x400")
#####################################Admin Submit Button##################################################
def adminsubmitbutton():
    name = stname.get()
    iid = stuid.get()
    phy = stuphy.get()
    chem = stuchem.get()
    math = stumath.get()
    if(name == "" or iid == "" or phy == "" or chem == "" or math == ""):
        messagebox.showerror("All Fields Required","All Data Is Necessary For Inserting")
    else:
        conn = mysql.connect(host="localhost",username="root",password="dbpass",database="dbname")
        cursor = conn.cursor()
        cursor.execute("insert into studata values('"+ name + "' , '" + iid + "' , '" + phy + "','"+chem+"','"+math+"')")
        cursor.execute("commit")
        messagebox.showinfo("Data Entered Successfully","Data Has Been Successfully Entered Into The Data Base")
#####################################Admin Window#########################################################
def adminlogin():
    usr = user.get()
    pwd = passs.get()
    if(usr == "" or pwd == ""):
        messagebox.showerror("All Fields Required","Username & Password Both Required For Login")
    else:
        conn = mysql.connect(host="localhost",username="root",password="hardikghuge23",database="collegeproject")
        cursor = conn.cursor()
        fpwd = "select pwd from admins where admin = '"+ user.get() +"'"
        cursor.execute(fpwd)
        result=cursor.fetchone()
        input_tuple = result
        password = input_tuple[0]
        password_str = str(password)
        if password_str != pwd:
            messagebox.showerror("Invalid Credentials","Password or Username is incorrect")
        else:
            messagebox.showinfo("Login Successful","You've Successfully Logged In as Admin")
            t1=Toplevel()
            t1.geometry("450x450")
            t1.title("Admin Window")
            Label(t1,text="Enter Student Data Below").place(x=180,y=10)
            Label(t1,text="Enter Student Name").place(x=10,y=50)
            Label(t1,text="Enter Student ID").place(x=10,y=90)
            Label(t1,text="Physics Marks").place(x=10,y=130)
            Label(t1,text="Chemistry Marks").place(x=10,y=170)
            Label(t1,text="Maths Marks").place(x=10,y=210)
            global stname,stuid,stuphy,stuchem,stumath
            stname = StringVar()
            stuid = IntVar()
            stuphy = StringVar()
            stuchem = StringVar()
            stumath = StringVar()
            Entry(t1,textvariable=stname).place(x=130,y=50)
            stuid = Entry(t1)
            stuid.place(x=130,y=90)
            Entry(t1,textvariable=stuphy).place(x=130,y=130)
            Entry(t1,textvariable=stuchem).place(x=130,y=170)
            Entry(t1,textvariable=stumath).place(x=130,y=210)
            Button(t1,text="Enter Into DB",bg="red",fg="white",command=adminsubmitbutton).place(x=180,y=250)
            t1.mainloop()
            cursor.close()
            conn.close()

######################################Student Login############################################################
def studentlogin():
    stu = user.get()
    idd = passs.get()
    if ( idd ==" " or stu ==""):
        messagebox.showerror("All Fields Required","Oops Looks like something is missing for Login")
    else:
        conn = mysql.connect(host="localhost",username="root",password="hardikghuge23",database="collegeproject")
        cursor = conn.cursor()
        query = ("SELECT * FROM studata WHERE name = %s AND id = %s")
        cursor.execute(query,(stu,idd))
        result = cursor.fetchall()
        for data in result:
            messagebox.showinfo("Your Result Is As Follows",
                                    f"Student Name: {data[0]}\n"
                                    f"Student Id: {data[1]}\n"
                                    f"Physics Marks: {data[2]}\n"
                                    f"Chemistry Marks: {data[3]}\n"
                                    f"Maths Marks: {data[4]}")
        cursor.close()
        conn.close()
#########################################MAIN SCREEN#########################################################
Label(root,text="Username").place(x=30,y=30)
user = StringVar()
username = Entry(root,textvariable=user).place(x=100,y=30)
Label(root,text="Password").place(x=30,y=60)
passs = StringVar()
password = Entry(root,textvariable=passs,show="*").place(x=100,y=60)
Button(root,text="Admin Login",fg="cyan",bg="black",command=adminlogin).place(x=120,y=100)
Button(root,text="Student Login",fg="Red",bg="#90EE90",command=studentlogin).place(x=120,y=140)
Label(root,text="In Case Of Student Login Enter",bg="red",fg="white",font="Helvetica 14 bold").place(x=65,y=200)
Label(root,text="ID in place of Password",bg="red",fg="white",font="Helvetica 14 bold").place(x=95,y=230)
root.mainloop()
