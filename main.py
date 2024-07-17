from tkinter import *
from tkinter import ttk
from backend import database
from tkinter import messagebox
db=database("employees.db")

root=Tk()
root.title("Shivem management system")
root.geometry("1366x768+0+0")
root.config(bg="#2c3e50")
# root.state("zoomed")
name=StringVar()
age=StringVar()
doj=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()
address=StringVar()


#entier frame
entrie_frame=Frame(root,bg="#535c68")
entrie_frame.pack(side=TOP,fill=X)
title=Label(entrie_frame,text="Shivam management system",font=("calibri",18,"bold"),bg="#2c3e50",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lalname=Label(entrie_frame,text="Name" ,font=("calibri",15))
lalname.grid(row=1,column=0 ,sticky="w")
txtname=Entry(entrie_frame,textvariable=name,font=("calibri",15),width=20)
txtname.grid(row=1 ,column=1 ,sticky="w",padx=5)

lblage=Label(entrie_frame,text="Age" ,font=("calibri",14))
lblage.grid(row=1,column=2 ,padx=15,pady=20 ,sticky="w")
txtage=Entry(entrie_frame,textvariable=age,font=("calibri",15),width=20)
txtage.grid(row=1,column=3 ,sticky="w")

laldoj=Label(entrie_frame,text="doj" ,font=("calibri",14))
laldoj.grid(row=1,column=4 ,padx=15,pady=20 ,sticky="w")
txtdoj=Entry(entrie_frame,textvariable=doj,font=("calibri",15),width=20)
txtdoj.grid(row=1 ,column=5 ,sticky="w")

lalemail=Label(entrie_frame,text="Gmail" ,font=("calibri",14))
lalemail.grid(row=2,column=0,pady=20,sticky="w")
txtemail=Entry(entrie_frame,textvariable=email,font=("calibri",15),width=20)
txtemail.grid(row=2 ,column=1 ,sticky="w")

lalgender=Label(entrie_frame,text="Gender",font=("calibri",14))
lalgender.grid(row=2,column=2,sticky="w",padx=10)
combogender=ttk.Combobox(entrie_frame,font=("calibri" ,15),width=20,textvariable=gender,state="readonly")
combogender['values']=["Male","Female"]
combogender.grid(row=2, column=3, padx=15,pady=20, sticky="w")


lalcontact=Label(entrie_frame,text="contact" ,font=("calibri",14))
lalcontact.grid(row=2,column=4,padx=15,pady=20 ,sticky="w")
txtcontact=Entry(entrie_frame,textvariable=contact,font=("calibri",15),width=20)
txtcontact.grid(row=2 ,column=5 ,sticky="w")

lbladdress=Label(entrie_frame,text="Address" ,font=("calibri",14))
lbladdress.grid(row=3,column=0,sticky="w")
txtaddress=Text(entrie_frame ,width=85 ,height=5 ,font=("calibri",14))
txtaddress.grid(row=4,columnspan=4,sticky="w")


def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    # print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaddress.delete(1.0,END)
    txtaddress.insert(END,row[7])
    
def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
        
        
def add_shivam():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or  txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Plice fill all the data")
        return
    db.insert(txtname.get(),txtage.get(),txtdoj.get(),txtemail.get(),combogender.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("DATA INSERT SUCCESSFULLLY")   
    clearall()
    displayall()
    
    
def update_shivam():
    if txtname.get()=="" or txtage.get()=="" or txtdoj.get()=="" or txtemail.get()=="" or combogender.get()=="" or  txtcontact.get()=="" or txtaddress.get(1.0,END)=="":
        messagebox.showerror("Error in input","Plice fill all the data")
        return
    db.update(row[0],txtname.get(),txtage.get(),txtdoj.get(),txtemail.get(),combogender.get(),txtcontact.get(),txtaddress.get(1.0,END))
    messagebox.showinfo("DATA Update SUCCESSFULLLY")   
    clearall()
    displayall()
    
    
def delete_shivam():
    db.remove(row[0])
    clearall()
    displayall()
    
    
def clearall():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    address.set("")
    txtaddress.delete(1.0,END)
    
    

btn_frame=Frame(entrie_frame,bg="#535c68")
btn_frame.grid(row=5,column=0,pady=10)

btnadd=Button(btn_frame,command=add_shivam,text="add data" ,width=10,font=("calibri",14,"bold"),fg="white",bg="#16a885",bd=0).grid(row=0,column=0)

btnupdate=Button(btn_frame,command=update_shivam, text="update data",width=10,font=("calibri",14,"bold"),fg="white",bd=0,bg="#2988b9").grid(row=0,column=1,padx=10)

btndelete=Button(btn_frame,command=delete_shivam, text="delete data",width=10,font=("calibri",14,"bold"),fg="white",bd=0,bg="#c8392b").grid(row=0,column=2,padx=10)

btnclear=Button(btn_frame,command=clearall, text="clear data",width=10,font=("calibri",14,"bold"),fg="white",bd=0,bg="#f39c12").grid(row=0,column=3,padx=10)

#table frame

tree_frame=Frame(root,bg="#ecf8f1")
tree_frame.place(x=8,y=450,width=1500,height=4000)
style=ttk.Style()
style.configure("mystyle.Treeview",font=('calibri',18),rowheight=40 )
style.configure("mystyle.Treeview.Heading",font=("claibri",12))

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="Id")
tv.column("1",width=10)

tv.heading("2",text="name")
tv.column("2",width=10)

tv.heading("3",text="age")
tv.column("3",width=10)

tv.heading("4",text="doj")
tv.column("4",width=10)

tv.heading("5",text="gmail")
tv.column("5",width=10)

tv.heading("6",text="gender")
tv.column("6",width=10)

tv.heading("7",text="contact")
tv.column("7",width=10)

tv.heading("8",text="address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)


displayall()
root.mainloop()