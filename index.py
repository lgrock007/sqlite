import sqlite3
print("\n")
print("""
          
          DATABASE MANAGEMENT SYSTEM USING CRUD OPERATION
          
            """)
class database:
    def __init__(self,db):
        try:
            self.con = sqlite3.connect(db)
            self.c = self.con.cursor()
            self.c.execute("""
                     CREATE TABLE IF NOT EXISTS DATAS (
                      ID INTEGER PRIMARY KEY,
                      Name TEXT NOT NULL,
                      Age INTEGER NOT NULL,
                      Gender TEXT NOT NULL,
                      Address TEXT NOT NULL,
                      Contact TEXT NOT NULL,
                      Mail TEXT NOT NULL   
                     )  
                         """)
            self.con.commit()
            print('Table Loaded Successfully...')
        except Exception as e :
            print('Error Occured',e)
            
    def insert_record(self):
        name = input("Enter the Name: ")
        age = input('Enter the AGE: ')
        gender = input('Enter the Gender: ')
        address = input('Enter the Address: ')
        contact = input('Enter the contact: ')
        mail = input('Enter the Mail: ')
        
        sql =   '''
                    INSERT INTO DATAS VALUES(NULL,?,?,?,?,?,?)
                '''        
        self.c.execute(sql,(name,age,gender,address,contact,mail))        
        self.con.commit()
        print('Record Added Successfully...')
        
    def fetch_record(self):
        sql =   '''
                SELECT * FROM DATAS
                '''
        self.c.execute(sql)
        data = self.c.fetchall()
        print('\n')
        print('List of Records')
        print('---------------')
        for records in data:
            print(records)
        
    def update_record(self):
        print('1.Name')
        print('2.Age')
        print('3.Gender')
        print('3.Address')
        print('5.Contact')
        print('6.Mail')
        option = int(input("Which Field You want to Update?"))
        ID = input('Enter Your ID:')
        if option == 1:
            name = input("Enter the Name: ")
            sql =   '''
                    UPDATE DATAS SET Name = ?  where ID = ? 
                '''
            self.c.execute(sql,(name,ID))
            self.con.commit()
            obj.fetch_record()
            print('\n')
            print('Updated Name Successfully')
        
        elif option == 2:
            age = input("Enter the Age: ")
            sql =   '''
                    UPDATE DATAS SET Age = ?  where ID = ? 
                    '''
            self.c.execute(sql,(age,ID))
            self.con.commit()
            obj.fetch_record()
            print('\n')
            print('Updated Age Successfully')
        
        elif option == 3:
            gender = input("Enter the Gender: ")
            sql =   '''
                    UPDATE DATAS SET Gender = ?  where ID = ? 
                    '''
            self.c.execute(sql,(gender,ID))
            self.con.commit()
            obj.fetch_record()
            print('\n')
            print('Updated Gender Successfully')
        
        elif option == 4:
            address = input("Enter the Address: ")
            sql =   '''
                    UPDATE DATAS SET Address = ?  where ID = ? 
                    '''
            self.c.execute(sql,(address,ID))
            self.con.commit()
            obj.fetch_record()
            print('\n')
            print('Updated Address Successfully')
        
        elif option == 5:
            contact = input("Enter the Contact: ")
            sql =   '''
                    UPDATE DATAS SET Contact = ?  where ID = ? 
                    '''
            self.c.execute(sql,(contact,ID))
            self.con.commit()
            obj.fetch_record()
            print('\n')
            print('Updated Contact Successfully')
        
        elif option == 6:
            mail = input("Enter the Mail: ")
            sql =   '''
                    UPDATE DATAS SET Mail = ?  where ID = ? 
                    '''
            self.c.execute(sql,(mail,ID))
            self.con.commit()
            obj.fetch_record()
            print('\n')
            print('Updated Mail Successfully')
            
        else:
            print("Invalid Selection")

    def delete_record(self):
        ID = int(input('Enter the ID which you want to delete: '))
        sql =   '''
                    DELETE FROM DATAS WHERE ID=?
                '''
        self.c.execute(sql,(ID,))
        self.con.commit()
        obj.fetch_record()
        print('\n')
        print("Successfully Deleted the Data.")
obj = database('sqlite.db')


while True :
    print("\n")
    print("1)INSERT RECORD")
    print("2)FETCH RECORD")
    print("3)UPDATE RECORD")
    print("4)DELETE RECORD")
    print('\n')
    print('Press 0 to exit')
    print('\n')
    
    choice = int(input("Enter Your Choice: "))
    
    if choice == 1 :
        obj.insert_record()
    elif choice == 2:
        obj.fetch_record()
    elif choice == 3:
        obj.update_record()
    elif choice == 4:
        obj.delete_record()
    
    else :
        quit()