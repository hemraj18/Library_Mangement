
from tkinter import *                # import the Tkinter library where * means every thing from the library
from tkinter import messagebox       # to show the popup message 
from tkinter.ttk import Combobox     # For combobox 
from tkinter.ttk import Treeview     # For Treeview 
import mysql.connector               # To connect the python with MYSQL Database
import datetime

# create a class where we can write our main code
class Library_Managment_System:
    def __init__(self,root):
        self.root = root
        self.root.title("BookEase - Library Managment System")     # title for the window
        self.root.geometry('1550x1000')                            # size of the window

        # ========================VARIABLES===============
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.lateratefine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()




        # this is the title label where the name will be displayed
        labelTitle = Label(self.root, text = "LIBRARY MANAGMENT SYSTEM", font =("times new roman",50,"bold"), bg="lightblue", fg = "dark green", bd=20, relief = RIDGE)
        labelTitle.pack(side=TOP,fill=X,padx=2,pady=6)

        # Frame for the membership information and books details
        frame = Frame(self.root, bd = 12, relief = RIDGE, padx = 20,bg= "light blue")
        frame.place(x=0, y=130,width=1530,height=400 )

        # ================DATA FRAME LEFT===============

        # label frame for the memebership information 
        DataFrameLeft= LabelFrame(frame,text = "Library Membership Information", font =("times new roman",15,"bold"), bg="light blue", fg = "dark green", bd=12,relief = RIDGE)
        DataFrameLeft.place(x=0,y=5,width=860,height=350)

        # LEFT SIDE of the DATA FRAME LEFT
        
        LabelMember = Label(DataFrameLeft,text="Member Type",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelMember.grid(row=0,column=0,sticky=W)
        ComMember = Combobox(DataFrameLeft,textvariable=self.member_var,font=("times new roman",13,"bold"),width=28,state="readonly")
        ComMember["values"] = ["Admin Staff","Student","Lecturer"]
        ComMember.grid(row=0,column=1)

        LabelPRN_No = Label(DataFrameLeft,text="PRN No",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelPRN_No.grid(row=1,column=0,sticky=W)       
        TxtPRN_NO = Entry(DataFrameLeft,textvariable=self.prn_var,font=("times new roman",13,"bold"),width=30)
        TxtPRN_NO.grid(row=1,column=1) 

        LabelID_No = Label(DataFrameLeft,text="ID No",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelID_No.grid(row=2,column=0,sticky=W)       
        TxtID_NO = Entry(DataFrameLeft,textvariable=self.id_var,font=("times new roman",13,"bold"),width=30)
        TxtID_NO.grid(row=2,column=1) 

        LabelFirstName = Label(DataFrameLeft,text="First Name",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelFirstName.grid(row=3,column=0,sticky=W)       
        TxtFirstName = Entry(DataFrameLeft,textvariable=self.firstname_var,font=("times new roman",13,"bold"),width=30)
        TxtFirstName.grid(row=3,column=1) 

        LabelLastName = Label(DataFrameLeft,text="Last Name",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelLastName.grid(row=4,column=0,sticky=W)       
        TxtLastName = Entry(DataFrameLeft,textvariable=self.lastname_var,font=("times new roman",13,"bold"),width=30)
        TxtLastName.grid(row=4,column=1)

        LabelAddress1 = Label(DataFrameLeft,text="City",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelAddress1.grid(row=5,column=0,sticky=W)       
        TxtAddress1 = Entry(DataFrameLeft,textvariable=self.address1_var,font=("times new roman",13,"bold"),width=30)
        TxtAddress1.grid(row=5,column=1)

        LabelAddress2 = Label(DataFrameLeft,text="State",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelAddress2.grid(row=6,column=0,sticky=W)       
        TxtAddress2 = Entry(DataFrameLeft,textvariable=self.address2_var,font=("times new roman",13,"bold"),width=30)
        TxtAddress2.grid(row=6,column=1)

        LabelPostCode = Label(DataFrameLeft,text="Post Code",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelPostCode.grid(row=7,column=0,sticky=W)       
        TxtPostCode = Entry(DataFrameLeft,textvariable=self.postcode_var,font=("times new roman",13,"bold"),width=30)
        TxtPostCode.grid(row=7,column=1)

        LabelMobile_No = Label(DataFrameLeft,text="Mobile No",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelMobile_No.grid(row=8,column=0,sticky=W)       
        TxtMobile_No = Entry(DataFrameLeft,textvariable=self.mobile_var,font=("times new roman",13,"bold"),width=30)
        TxtMobile_No.grid(row=8,column=1)

        # LEFT SIDE of the DATA FRAME LEFT

        LabelBookID = Label(DataFrameLeft,text="Book ID",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelBookID.grid(row=0,column=3,sticky=W)
        TxtBookID = Entry(DataFrameLeft,textvariable=self.bookid_var,font=("times new roman",13,"bold"),width=30)
        TxtBookID.grid(row=0,column=4)

        LabelBookTitle = Label(DataFrameLeft,text="Book Title",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelBookTitle.grid(row=1,column=3,sticky=W)       
        TxtBookTitle = Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("times new roman",13,"bold"),width=30)
        TxtBookTitle.grid(row=1,column=4) 

        LabelAutherName = Label(DataFrameLeft,text="Auther Name",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelAutherName.grid(row=2,column=3,sticky=W)       
        TxtAutherName = Entry(DataFrameLeft,textvariable=self.author_var,font=("times new roman",13,"bold"),width=30)
        TxtAutherName.grid(row=2,column=4) 

        LabelDateBorrowed = Label(DataFrameLeft,text="Date Borrowed",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelDateBorrowed.grid(row=3,column=3,sticky=W)       
        TxtDateBorrowed = Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("times new roman",13,"bold"),width=30)
        TxtDateBorrowed.grid(row=3,column=4) 

        LabelDateDue = Label(DataFrameLeft,text="Date Due",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelDateDue.grid(row=4,column=3,sticky=W)       
        TxtDateDue = Entry(DataFrameLeft,textvariable=self.datedue_var,font=("times new roman",13,"bold"),width=30)
        TxtDateDue.grid(row=4,column=4)

        LabelDaysOnBook = Label(DataFrameLeft,text="Days On Book",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelDaysOnBook.grid(row=5,column=3,sticky=W)       
        TxtDaysOnBook = Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("times new roman",13,"bold"),width=30)
        TxtDaysOnBook.grid(row=5,column=4)

        LabelLateReturnFine = Label(DataFrameLeft,text="Last Return Fine",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelLateReturnFine.grid(row=6,column=3,sticky=W)       
        TxtLateReturnFine = Entry(DataFrameLeft,textvariable=self.lateratefine_var,font=("times new roman",13,"bold"),width=30)
        TxtLateReturnFine.grid(row=6,column=4)

        LabelDateOverDue = Label(DataFrameLeft,text="Date Over Due",font=("times new roman",12),bg="light blue",padx=2,pady=6)
        LabelDateOverDue.grid(row=7,column=3,sticky=W)       
        TxtDateOverDue = Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("times new roman",13,"bold"),width=30)
        TxtDateOverDue.grid(row=7,column=4)

        LabelActualPrice = Label(DataFrameLeft,text="Actual Price",font=("times new roman",13),bg="light blue",padx=2,pady=6)
        LabelActualPrice.grid(row=8,column=3,sticky=W)       
        TxtActualPrice = Entry(DataFrameLeft,textvariable=self.finalprice_var,font=("times new roman",13,"bold"),width=30)
        TxtActualPrice.grid(row=8,column=4)

        # ================DATA FRAME LEFT===============

        # label for the books details

        DataFrameRight= LabelFrame(frame,text = "Book Details", font =("times new roman",12,"bold"), bg="light blue", fg = "dark green", bd=12,relief = RIDGE)
        DataFrameRight.place(x=870,y=5,width=580,height=350)

        self.txt = Text(DataFrameRight,font=("times new roman",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txt.grid(row=0,column=2)

        ListScrollBar = Scrollbar(DataFrameRight)
        ListScrollBar.grid(row=0,column=1,sticky="ns")

        ListBooks = ["Python Crash Course","JavaScript","Head First Java","Learn C","Eloquent JavaScript",
                     "Deep Learning","Introduction to Algorithms","HTML and CSS","You Don't Know JS","Algorithms","Effective Java",
                     "Node.js Design Patterns","Vue.js 2 Cookbook","Pro ASP.NET Core MVC","Computer Networks",
                     "Operating Systems","Artificial Intelligence","Head First Python","Clean Code"  
                     ]
        
        def selectbook(event=''):
            value = str(ListBox.get(ListBox.curselection()))
            x = value
            if x == "Python Crash Course":
                self.bookid_var.set("001")
                self.booktitle_var.set("Python Crash Course")
                self.author_var.set("Henry Due")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.242")

            if x == "JavaScript":
                self.bookid_var.set("002")
                self.booktitle_var.set("JavaScript")
                self.author_var.set("Raley Jai")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.445")

            if x == "Head First Java":
                self.bookid_var.set("003")
                self.booktitle_var.set("Head First Java")
                self.author_var.set("Raley Jai")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.675")

            if x == "Learn C":
                self.bookid_var.set("004")
                self.booktitle_var.set("Learn C")
                self.author_var.set("Sonal Rathod")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.145")

            if x == "Eloquent JavaScript":
                self.bookid_var.set("005")
                self.booktitle_var.set("Eloquent JavaScript")
                self.author_var.set("Jenny Jeffer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.890")

            if x == "Deep Learning":
                self.bookid_var.set("006")
                self.booktitle_var.set("Deep Learning")
                self.author_var.set("R.K Mishra")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.643")

            if x == "Introduction to Algorithms":
                self.bookid_var.set("007")
                self.booktitle_var.set("Introduction to Algorithms")
                self.author_var.set("Joshef Alzer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.144")

            if x == "HTML and CSS":
                self.bookid_var.set("008")
                self.booktitle_var.set("HTML and CSS")
                self.author_var.set("Raley Jai")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.220")

            if x == "You Don't Know JS":
                self.bookid_var.set("009")
                self.booktitle_var.set("You Don't Know JS")
                self.author_var.set("Joshef Alzer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.620")

            if x == "Algorithms":
                self.bookid_var.set("010")
                self.booktitle_var.set("Algorithms")
                self.author_var.set("Sonal Rathod")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.590")

            if x == "Effective Java":
                self.bookid_var.set("011")
                self.booktitle_var.set("Effective Java")
                self.author_var.set("Jenny Jeffer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.120")

            if x == "Node.js Design Patterns":
                self.bookid_var.set("012")
                self.booktitle_var.set("Node.js Design Patterns")
                self.author_var.set("Jenny Jeffer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.2320")

            if x == "Vue.js 2 Cookbook":
                self.bookid_var.set("013")
                self.booktitle_var.set("Vue.js 2 Cookbook")
                self.author_var.set("Joshef Alzer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.3240")

            if x == "Pro ASP.NET Core MVC":
                self.bookid_var.set("014")
                self.booktitle_var.set("Pro ASP.NET Core MVC")
                self.author_var.set("Jenny Jeffer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.632")

            if x == "Computer Networks":
                self.bookid_var.set("015")
                self.booktitle_var.set("Computer Networks")
                self.author_var.set("Raley Jai")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.345")

            if x == "Operating Systems":
                self.bookid_var.set("016")
                self.booktitle_var.set("Operating Systems")
                self.author_var.set("Jenny Jeffer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.540")

            if x == "Artificial Intelligence":
                self.bookid_var.set("017")
                self.booktitle_var.set("Artificial Intelligence")
                self.author_var.set("Jenny Jeffer")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.240")

            if x == "Head First Python":
                self.bookid_var.set("018")
                self.booktitle_var.set("Head First Python")
                self.author_var.set("Raley Jai")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.133")

            if x == "Clean Code":
                self.bookid_var.set("019")
                self.booktitle_var.set("Clean Code")
                self.author_var.set("Sonal Rathod")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.1230")




        ListBox = Listbox(DataFrameRight,font=("times new roman",12,"bold"),width=20,height=16)
        ListBox.bind("<<ListboxSelect>>",selectbook)
        ListBox.grid(row=0,column=0,padx=2,pady=6)
        ListScrollBar.config(command = ListBox.yview)

        for item in ListBooks:
            ListBox.insert(END,item)
        
        # ================BUTTONS FRAME ===============
        FrameButton = Frame(self.root, bd = 12, relief = RIDGE, padx = 20,bg= "light blue")
        FrameButton.place(x=0, y=530,width=1530,height=70 )

        AddButton = Button(FrameButton,text="Add Data",command=self.add_data,bg="red",fg="white",font=("times new roman",12,"bold"),width=26)
        AddButton.grid(row=0,column=0)

        ShowButton = Button(FrameButton,text="Show Data",command=self.ShowData,bg="red",fg="white",font=("times new roman",12,"bold"),width=26)
        ShowButton.grid(row=0,column=1)

        UpdateButton = Button(FrameButton,text="Update",command=self.update,bg="red",fg="white",font=("times new roman",12,"bold"),width=26)
        UpdateButton.grid(row=0,column=2)

        DeleteButton = Button(FrameButton,text="Delete",command=self.delete,bg="red",fg="white",font=("times new roman",12,"bold"),width=26)
        DeleteButton.grid(row=0,column=3)

        ResetButton = Button(FrameButton,text="Reset",command=self.reset,bg="red",fg="white",font=("times new roman",12,"bold"),width=26)
        ResetButton.grid(row=0,column=4)
        
        ExitButton = Button(FrameButton,text="Exit",command=self.exit,bg="red",fg="white",font=("times new roman",12,"bold"),width=26)
        ExitButton.grid(row=0,column=5)

        # ================INFORAMTION FRAME============
        FrameDetails = Frame(self.root, bd = 12, relief = RIDGE, padx = 20,bg= "light blue")
        FrameDetails.place(x=0, y=600,width=1530,height=195 )

        TableFrame = Frame(FrameDetails,bd = 6, relief = RIDGE,bg= "light blue")
        TableFrame.place(x=0, y=2,width=1460,height=168 )

        xscroll = Scrollbar(TableFrame,orient=HORIZONTAL)
        yscroll = Scrollbar(TableFrame,orient=VERTICAL)

        self.LibraryTable = Treeview(TableFrame,columns=("membertype","prnno","id","firstname","lastname",
                                                         "address1","address2","postid","mobile","bookid","booktitle",
                                                         "author","dateborrowed","datedue","days","latereturnfine","dateoverdue",
                                                         "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.LibraryTable.xview)
        yscroll.config(command=self.LibraryTable.yview)

        self.LibraryTable.heading("membertype",text="Member Type")
        self.LibraryTable.heading("prnno",text="PRN No")
        self.LibraryTable.heading("id",text="ID No")
        self.LibraryTable.heading("firstname",text="First Name")
        self.LibraryTable.heading("lastname",text="Last Name")
        self.LibraryTable.heading("address1",text="Address1")
        self.LibraryTable.heading("address2",text="Address2")
        self.LibraryTable.heading("postid",text="Post Id")
        self.LibraryTable.heading("mobile",text="Mobile No")
        self.LibraryTable.heading("bookid",text="Book Id")
        self.LibraryTable.heading("booktitle",text="Book Title")
        self.LibraryTable.heading("author",text="Author")
        self.LibraryTable.heading("dateborrowed",text="Date Borrowed")
        self.LibraryTable.heading("datedue",text="Date Due")
        self.LibraryTable.heading("days",text="Days")
        self.LibraryTable.heading("latereturnfine",text="Late Return Fine")
        self.LibraryTable.heading("dateoverdue",text="Date Over Due")
        self.LibraryTable.heading("finalprice",text="Final Price")

        self.LibraryTable["show"]= "headings"
        self.LibraryTable.pack(fill=BOTH,expand=1)
        
        self.LibraryTable.column("membertype",width=100)
        self.LibraryTable.column("prnno",width=100)
        self.LibraryTable.column("id",width=100)
        self.LibraryTable.column("firstname",width=100)
        self.LibraryTable.column("lastname",width=100)
        self.LibraryTable.column("address1",width=100)
        self.LibraryTable.column("address2",width=100)
        self.LibraryTable.column("postid",width=100)
        self.LibraryTable.column("mobile",width=100)
        self.LibraryTable.column("bookid",width=100)
        self.LibraryTable.column("booktitle",width=100)
        self.LibraryTable.column("author",width=100)
        self.LibraryTable.column("dateborrowed",width=100)
        self.LibraryTable.column("datedue",width=100)
        self.LibraryTable.column("days",width=100)
        self.LibraryTable.column("latereturnfine",width=100)
        self.LibraryTable.column("dateoverdue",width=100)
        self.LibraryTable.column("finalprice",width=100)
        
        self.fetchdata()
        self.LibraryTable.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database='LMS')
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get()
                                                                                                              ))
        conn.commit()
        self.fetchdata()
        conn.close()

        messagebox.showinfo("Success","Member Data is Successfully Entered")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database='LMS')
        my_cursor = conn.cursor()
        my_cursor.execute("update library set member=%s,id=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postcode=%s,mobile=%s,bookid=%s,booktitle=%s,author=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,lateratefine=%s,dateoverdue=%s,finalprice=%s where prn=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                              ))
        conn.commit()
        self.fetchdata()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member Data is Successfully Updated")


    def fetchdata(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database='LMS')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.LibraryTable.delete(*self.LibraryTable.get_children())
            for i in rows:
                self.LibraryTable.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row = self.LibraryTable.focus()
        content = self.LibraryTable.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])



    def ShowData(self):
        self.txt.insert(END,"Member Type\t\t"+self.member_var.get()+'\n')
        self.txt.insert(END,"PRN No\t\t"+self.prn_var.get()+'\n')
        self.txt.insert(END,"ID No\t\t"+self.id_var.get()+'\n')
        self.txt.insert(END,"First Name\t\t"+self.firstname_var.get()+'\n')
        self.txt.insert(END,"Last Name\t\t"+self.lastname_var.get()+'\n')
        self.txt.insert(END,"Address1\t\t"+self.address1_var.get()+'\n')
        self.txt.insert(END,"Address2\t\t"+self.address2_var.get()+'\n')
        self.txt.insert(END,"Post Code\t\t"+self.postcode_var.get()+'\n')
        self.txt.insert(END,"Mobile No\t\t"+self.mobile_var.get()+'\n')
        self.txt.insert(END,"Book Id\t\t"+self.bookid_var.get()+'\n')
        self.txt.insert(END,"Boook Title\t\t"+self.booktitle_var.get()+'\n')
        self.txt.insert(END,"Auther\t\t"+self.author_var.get()+'\n')
        self.txt.insert(END,"Date Borrowed\t\t"+self.dateborrowed_var.get()+'\n')
        self.txt.insert(END,"Date Due\t\t"+self.datedue_var.get()+'\n')
        self.txt.insert(END,"Days on Book\t\t"+self.daysonbook_var.get()+'\n')
        self.txt.insert(END,"Late Rate Fine\t\t"+self.lateratefine_var.get()+'\n')
        self.txt.insert(END,"Date Over Due\t\t"+self.dateoverdue_var.get()+'\n')
        self.txt.insert(END,"Final Price\t\t"+self.finalprice_var.get()+'\n')

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txt.delete('1.0',END)

    def exit(self):
        if messagebox.askyesno(title="quit", message="Do you want to quit?"):
            self.root.destroy()

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error","First Select the member")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database='LMS')
            my_cursor = conn.cursor()
            my_cursor.execute("delete from library where prn = %s",(self.prn_var.get(),))

            conn.commit()
            self.fetchdata()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member Data is Successfully Deleted")


if __name__ == '__main__':
    root = Tk()
    obj = Library_Managment_System(root)
    root.mainloop()