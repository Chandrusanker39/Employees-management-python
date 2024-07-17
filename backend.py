import sqlite3

class database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""CREATE TABLE IF NOT EXISTS employees
        (
        id Integer  Primary key ,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

         #insert function 
        
    def insert(self,name,age,doj,email,gender,contact,address):
               
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()

        #fetch data from db
    def fetch(self):
        self.cur.execute("select * from employees")
        rows=self.cur.fetchall()
        print(rows)
    
        return rows  

        #deleter data from db
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()

        #update data in db

    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",
                         (name,age,doj,email,gender,contact,address,id))
        self.con.commit()

# obj=database("employees.db")
# obj.insert("chandru","23","03/09/2001","chandrushivam@gmail.com","male","9150617849","Earth of Moon")
# # obj.remove("chandru")
# # # obj.update("1","shivam","23","03/09/2001","chandrushivam@gmail.com","male","9150617849","Earth of Moon")
# obj.fetch()