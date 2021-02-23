from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import model



class Movie:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x820")
        self.root.title("Online Hotel Booking System")
        root.resizable(False, False)
        self.root.config(bg="orange")


        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.address = StringVar()
        self.roomnumber = StringVar()
        self.search_txt = StringVar()
        self.sort = StringVar()
        self.search_by = StringVar()

        # Frames
        MainFrame = Frame(self.root, bg="light grey", width=1350, height=750)
        MainFrame.grid()

        self.TFrame = Label(MainFrame, font=('Arial', 41), text="ONLINE HOTEL BOOKING SYSTEM", bg="black", fg="orange",
                            anchor="w")
        self.TFrame.place(x=0, y=35, relwidth=1)

        frm1 = LabelFrame(self.root, text="Costumer Details", font=("times new roman", 17, "bold"),
                          fg="black", bg="powder blue")
        frm1.place(x=3, y=96, width=993, height=125)

        f_name = Label(frm1, text="Full Name:", fg="Black", font=("times new roman", 19, "bold"))
        f_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        self.ef_name = Entry(frm1, textvariable=self.name, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.ef_name.place(x=125, y=10)

        c_number = Label(frm1, text="Contact Number:", fg="black", font=("times new roman", 19, "bold"))
        c_number.place(x=313, y=10)

        self.e_Contact = Entry(frm1, textvariable=self.contact, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.e_Contact.place(x=470, y=10)

        e_address = Label(frm1, text="Email Address:", fg="black", font=("times new roman", 19, "bold"))
        e_address.place(x=655, y=10)

        self.entry_e = Entry(frm1, textvariable=self.email, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.entry_e.place(x=800, y=10)

        Gender = Label(frm1, text="Gender", fg="black", font=("times new roman", 19, "bold"))
        Gender.place(x=22, y=55)

        self.combo_gender = ttk.Combobox(frm1, textvariable=self.gender, font=("times new roman", 18, "bold"),
                                         state='readonly')
        self.combo_gender['values'] = ("Male", "Female", "Other")
        self.combo_gender.place(x=98, y=55)

        c_address = Label(frm1, text=" Address :", fg="black", font=("times new roman", 19, "bold"))
        c_address.place(x=312, y=55)

        self.e_address = Entry(frm1, textvariable=self.address, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.e_address.place(x=412, y=55)

        r_number = Label(frm1, text=" Room Number :", fg="black", font=("times new roman", 19, "bold"))
        r_number.place(x=612, y=55)

        self.rno_entry = Entry(frm1, textvariable=self.roomnumber, font=("times new roman", 16, "bold"), relief=GROOVE)
        self.rno_entry.place(x=762, y=55)

        BFrame = Frame(MainFrame, bd=2, width=1344, height=70, padx=18, pady=10, bg="orange", relief=RIDGE)
        BFrame.place(x=4, y=222)

        self.btnadd = Button(BFrame, text="Add ", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.adddata)
        self.btnadd.grid(row=0, column=0)

        self.update = Button(BFrame, text="Update", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.updata)
        self.update.grid(row=0, column=1)

        self.btnclc = Button(BFrame, text="Clear", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.clear)
        self.btnclc.grid(row=0, column=2)

        self.btndel = Button(BFrame, text="Delete", font=('Arial', 18, 'bold'), width=10, height=1, bd=4, bg="orange",
                             command=self.deletedata)
        self.btndel.grid(row=0, column=3)

        sFrame = Frame(MainFrame, bd=2, width=300, height=60, padx=18, pady=10, bg="orange", relief=RIDGE)
        sFrame.place(x=650, y=222)

        # sort

        self.bsort = Button(sFrame, text=" Sort ", fg="black", font=("times new roman", 18, "bold"),
                            command=self.sorted)
        self.bsort.place(x=190, y=1)

        self.combo_sort = ttk.Combobox(sFrame, textvariable=self.sort, font=("times new roman", 19, "bold"),
                                       state='readonly', width=15)
        self.combo_sort['values'] = ("RoomNo")
        self.combo_sort.place(x=3, y=1)

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="powderblue")
        Detail_Frame.place(x=5, y=289, width=990, height=530)

        lbl_search = Label(Detail_Frame, text="Search By", bg="powderblue", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=10, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("times new roman", 18, "bold"),
                                    state='readonly')
        combo_search['values'] = ("Name", "Room Number")
        combo_search.grid(row=0, column=1)

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, font=("times new roman", 17, "bold"),
                           relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        self.searchbtn = Button(Detail_Frame, text="Search ", bg="orange", fg="black", width=16, pady=5,
                                command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        self.showallbtn = Button(Detail_Frame, text="Show All", bg="orange", fg="black", width=16, pady=5).grid(row=0,
                                                                                                                column=4,
                                                                                                                padx=10,
                                                                                                                pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        Table_Frame.place(x=10, y=70, width=965, height=450)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.hotel_table = ttk.Treeview(Table_Frame,
                                        columns=("name", "address", "email", "gender", "number", "RoomNumber"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hotel_table.xview)
        scroll_y.config(command=self.hotel_table.yview)

        self.hotel_table.heading("name", text="Full Name")
        self.hotel_table.heading("address", text="address")
        self.hotel_table.heading("email", text="Email")
        self.hotel_table.heading("gender", text="Gender")
        self.hotel_table.heading("number", text="Phone number")
        self.hotel_table.heading("RoomNumber", text="Room Number")
        self.hotel_table['show'] = 'headings'

        self.hotel_table.column("name", width=100)
        self.hotel_table.column("address", width=100)
        self.hotel_table.column("email", width=100)
        self.hotel_table.column("gender", width=100)
        self.hotel_table.column("number", width=100)
        self.hotel_table.pack(fill=BOTH, expand=1)

        self.fetch_data()
        self.hotel_table.bind("<ButtonRelease-1>", self.get_cursor)

    def sorted(self):
        pass

    def get_cursor(self, ev):
        pass

    def fetch_data(self):
        pass

    def adddata(self):
        pass

    def clear(self):
        pass

    def clcdata(self):
        pass

    def deletedata(self):
        pass

    def updata(self):
        pass

    def mergesort(self):
        pass

    def binary_search_name(self):
        pass

    def binary_room_number(self):
        pass

    def search_data(self):
        pass

    def btnclc(self):
        pass


if __name__ == '__main__':
    root = Tk()
    datbase = Movie(root)
    root.mainloop()