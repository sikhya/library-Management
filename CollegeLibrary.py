class library:
    def __init__(self, book,stdName):
        self.Book = book
        self.name = stdName

    def displayBook(self):
        print("\nAvailable book in library shown as below:")
        for b in self.Book:
            print("  # "+ b)
        
    def checkStudent(self):
        print("\nStudent name of issued book in library:")
        query4 ="select * from issuedbooks"
        cursor.execute(query4)
        result = cursor.fetchall()
        for b in result:
            print(" \t# " + b[0] + " : " +b[1] + " : "+ b[2] + " - " + b[3] )
    
    
    def borrowBook(self, bookName, nm):
        issueDay=date.today()
        thirtyDay = issueDay + timedelta(days=30) 
        if bookName in self.Book:
            print(f"You have been issued {bookName} book")
            self.Book.remove(bookName)
            self.name[nm]=bookName
            query = "delete from books where name ='"+bookName+"'"
            cursor.execute(query)
            mydb.commit()
            query1 = "insert into issuedbooks(student_name, book_name, issued_date, return_date) values('"+nm+"', '"+bookName+"', '"+str(issueDay)+"','"+str(thirtyDay)+"')"
            cursor.execute(query1)
            mydb.commit()
            return True
        else:
            print(f"\nSorry, {bookName} this book is either not available or has already issued someone else. Please wait until the  book  is available.")
            return False
    
    def returnBook(self, bookName):
        self.Book.append(bookName) 
        query3 ="insert into books(name) values('"+bookName+"')"
        cursor.execute(query3)
        mydb.commit()
        query2 = "delete from issuedbooks where book_name='"+bookName+"'"
        cursor.execute(query2)
        mydb.commit()
        print("\nThank you for returning this book! Hope you enjoyed reading it.")

    def addBook(self):
        entryBook = True
        while entryBook:
            nm = input("\nEnter book name or press q for complete book entry: ")
            if nm != "q":
                query = "insert into books(name) values('"+nm+"')"
                cursor.execute(query)
                mydb.commit()
                self.Book.append(nm)
            elif nm == "q":
                entryBook = False
        print("\nSuccessfully added new book.")


        
class student:
    def requestBook(self):
        self.book = input("\nPlease enter the book name you want to borrow: ")
        return self.book

    def nameStudent(self):
        nameStd = input("Enter student name: ")
        return nameStd

    def returnBook(self):
        self.book = input("\nPlease enter the book name you want to return: ")
        return self.book

if __name__ == "__main__":
    import mysql.connector
    from mysql.connector import Error
    from datetime import date, timedelta
    mydb = mysql.connector.connect(host = "localhost", user = "root", port = 3306, passwd = "", database = "collegelibrary")
    cursor = mydb.cursor()
    query = "select name from books"
    cursor.execute(query)
    result = cursor.fetchall()
    l=[]
    for row in result:
        l.append(row[0])
    issuedBook = {}
    studentLibrary = library(l, issuedBook)
    Student = student()
    msg = '''\n 
            ------Welcome To College Library------

                    Please choose an option:
                    1. List all the book
                    2. Issued book
                    3. Request a book
                    4. Return a book
                    5. Add a new book
                    6. Exit the library
    '''
    while True:
        print("\n----------------------------------------------------------------------")
        print(msg)
        a = int(input("Enter a choice: "))
        if a == 1:
            studentLibrary.displayBook()
        elif a == 2:
            studentLibrary.checkStudent()
        elif a == 3:
            studentLibrary.borrowBook(Student.requestBook(),Student.nameStudent())
        elif a == 4:
            studentLibrary.returnBook(Student.returnBook())
        elif a == 5:
            studentLibrary.addBook()
        elif a == 6:    
            print("\nThanks for choosing College Library. Have a great day.\n")
            exit()
        else:
            print("\nInvalid choice!")


   
