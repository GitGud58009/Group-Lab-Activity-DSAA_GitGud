import tkinter as tk
from tkinter import simpledialog, ttk, messagebox
from datetime import datetime, timedelta
import os

from tkcalendar import *
from tkinter import*

from tkinter import PhotoImage
from PIL import Image, ImageTk
#from PIL import ImageTk, Image # use this to import more image file type like jpeg, etc.

from tkinter.messagebox import showinfo
import statistics
from collections import Counter
import math
#                   ----   HOME WINDOW CONFIGURATION   -----
Win = Tk()
Win.title("REMINDER")

# Setting window size
Window_Width = 900
Window_Height = 600

# calculate coordination of screen and window form
positionRight = int(Win.winfo_screenwidth() / 2 - Window_Width / 2)
positionDown = int(Win.winfo_screenheight() / 2 - Window_Height / 2)

# Set window in center screen.          --> resulting to    HomeWin.geometry("900x600,+n+n")
Win.geometry(str(Window_Width) + "x" + str(Window_Height) + "+" + str(positionRight) + "+" + str(positionDown))
# -----------------------------------------------------------------------------------------
# Just put r before your normal string. It converts a normal string to a raw string:
# place the images in the same folder as the python file
#home_icon = Image.open(r"Home_Icon.png")
#mmw_icon = Image.open(r"MMW_ICON.png")
#pfe_icon = Image.open(r"PFE_ICON.png")
#back_icon = Image.open(r"BACK_ICON.svg.png")
#questionMark_icon = Image.open(r"QuestionMark_Icon.png")
#lozano_pic = Image.open(r"LOZANO.png")
#tabobo_pic = Image.open(r"TABOBO.png")
#delasalas_pic = Image.open(r"DELASALAS.jpg")
#guzman_pic = Image.open(r"GUZMAN.png")
#salino_pic = Image.open(r"SALINO.png")

# to resize image
# ANTI-ALIAS is deprecated and will be removed in Pillow 10 (2023-07-01). Use LANCZOS or Resampling.LANCZOS instead.
#resized_home_icon = home_icon.resize((50, 50), Image.LANCZOS)
#resized_mmw_icon = mmw_icon.resize((100, 100), Image.LANCZOS)
#resized_pfe_icon = pfe_icon.resize((500, 200), Image.LANCZOS)
#resized_back_icon = back_icon.resize((50, 50), Image.LANCZOS)
#resized_questionMark_Icon = questionMark_icon.resize((50, 50), Image.LANCZOS)
#resized_lozano_pic = lozano_pic.resize((125, 125), Image.LANCZOS)
#resized_tabobo_pic = tabobo_pic.resize((125, 125), Image.LANCZOS)
#resized_delasalas_pic = delasalas_pic.resize((125, 125), Image.LANCZOS)
#resized_guzman_pic = guzman_pic.resize((125, 125), Image.LANCZOS)
#resized_salino_pic = salino_pic.resize((125, 125), Image.LANCZOS)



#HOME_ICON = ImageTk.PhotoImage(resized_home_icon)
#MMW_ICON = ImageTk.PhotoImage(resized_mmw_icon)
#PFE_ICON = ImageTk.PhotoImage(resized_pfe_icon)
#BACK_ICON = ImageTk.PhotoImage(resized_back_icon)
#INST_ICON = ImageTk.PhotoImage(resized_questionMark_Icon)
#LOZANO_PIC = ImageTk.PhotoImage(resized_lozano_pic)
#TABOBO_PIC = ImageTk.PhotoImage(resized_tabobo_pic)
#DELASALAS_PIC = ImageTk.PhotoImage(resized_delasalas_pic)
#GUZMAN_PIC = ImageTk.PhotoImage(resized_guzman_pic)
#SALINO_PIC = ImageTk.PhotoImage(resized_salino_pic)

var = tk.IntVar()
style = ttk.Style()

def StartPage():
    global frame
    global startpage_image
    global loginbutton

    frame = Frame(Win, width=900, height=600, bg="white")
    frame.place(x=0, y=0)

    # Open image with Pillow and convert to PhotoImage
    pil_image = Image.open(r"rsz_startpagelast.png")
    startpage_image = ImageTk.PhotoImage(pil_image)

    canvas = Canvas(frame, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=startpage_image)

    # Increase font size for the label
    #lblUN = Label(frame, text="Username:", font=("Arial", 24))
    #lblUN.place(x=450, y=100)

    # Load PNG image for button
    loginbutton = PhotoImage(file=r"LOGIN2.png")
    # Create a transparent button with text
    custom_button = Button(frame, image=loginbutton, command=login, bd=0, compound=CENTER, padx=0, pady=0)
    custom_button.place(x=530, y=220)

    global entUN
    entUN = Entry(frame, font=("Arial", 18))
    entUN.place(x=530, y=170)

    #btnLogIn = Button(frame, text="Log in", command=login, bg="white", font=("Arial", 18, "bold"))
    #btnLogIn.place(x=440, y=220)

def SignOut():
    response = messagebox.askyesno("Confirmation", "Are you sure you want to sign out?")
    if response:
        StartPage()

def Home():
    global homepage_image
    global signoutbutton
    global billbutton
    global TDLbutton
    global ABTbutton

    frame_Home = Frame(Win, width=900, height=600, bg="white")
    frame_Home.place(x=0, y=0)

    pil2_image = Image.open(r"rsz_homepage.png")
    homepage_image = ImageTk.PhotoImage(pil2_image)

    canvas = Canvas(frame_Home, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=homepage_image)

    #btnSignOut = Button(frame_Home, text="Sign Out", command=SignOut, bd=0, bg="gray", font=("Arial", 12, "bold"))
    #btnSignOut.place(x=750, y=500)
    signoutbutton = PhotoImage(file=r"LOGOUT2.png")
    btnSignOut = Button(frame_Home, image=signoutbutton, command=SignOut, bd=0, compound=CENTER, padx=0, pady=0)
    btnSignOut.place(x=730, y=475)

    #btnBill = Button(frame_Home, text="Bills", command=BILL, width=20, height=5, font=("Arial", 20, "bold"), bg="lightblue")
    #btnBill.place(x=60, y=100)
    billbutton = PhotoImage(file=r"BILL2.png")
    btnBill = Button(frame_Home, image=billbutton, command=BILL, bd=0, compound=CENTER, padx=0, pady=0)
    btnBill.place(x=70, y=100)

    #btnTDL = Button(frame_Home, text="To-do List", command=TDL, width=20, height=5, font=("Arial", 20, "bold"), bg="lightgreen")
    #btnTDL.place(x=490, y=100)
    TDLbutton = PhotoImage(file=r"TDL2.png")
    btnTDL = Button(frame_Home, image=TDLbutton, command=TDL, bd=0, compound=CENTER, padx=0, pady=0)
    btnTDL.place(x=490, y=100)

    #btnABT = Button(frame_Home, text="About", command=ABT, width=5, height=2, font=("Arial", 14, "bold"), bg="lightcoral")
    #btnABT.place(x=60, y=475)
    ABTbutton = PhotoImage(file=r"ABT2.png")
    btnABT = Button(frame_Home, image=ABTbutton, command=ABT, bd=0, compound=CENTER, padx=0, pady=0)
    btnABT.place(x=70, y=475)

def login():
    global username
    username = entUN.get()
    try:
        if username:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            Home()
            frame.destroy()
            # Additional sign-in logic can be added here
        else:
            messagebox.showwarning("Warning", "Please enter a username before signing in.")
    except:
        messagebox.showwarning("Warning", "Please enter a username before signing in.")

def BILL():
    def update_time():
        current_time = datetime.now()
        date_str = current_time.strftime("%Y-%m-%d")
        time_str = current_time.strftime("%I:%M:%S %p")

        date_label.config(text=date_str)
        time_label.config(text=time_str)

        Win.after(1000, update_time)

        # Check for overdue bills every minute
        if current_time.second == 0:
            check_overdue_bills()

    def selectDate():
        global due_date_str
        global bill_name
        due_date_str = myCal.get_date()
        return due_date_str

    def calendar():
        global myCal
        myCal = Calendar(frame_BILL, setmode='day', date_pattern='YYYY-MM-DD')
        myCal.place(relx=0.5, rely=0.5, anchor="center")
        openCal = Button(frame_BILL, text="Select Date", command=lambda: var.set(1))
        openCal.place(relx=0.5, rely=0.7, anchor="center")
        openCal.wait_variable(var)
        myCal.destroy()
        openCal.destroy()

    def add_bill():
        bill_name = simpledialog.askstring("Input", "Enter Bill Name:")
        calendar()
        due_date_str = selectDate()
        price_str = simpledialog.askstring("Input", "Enter Price:")
        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            days_until_due = (due_date - datetime.now()).days

            price = float(price_str)

            # Check if due date is in the future and price is non-negative
            if days_until_due < 0:
                messagebox.showerror("Error", "Due date should be in the future.")
                return
            elif price < 0:
                messagebox.showerror("Error", "Price should be a non-negative value.")
                return

        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input. Please enter a valid date and price.")
            return

        bill_tree.insert("", "end", values=(bill_name, due_date_str, price_str, days_until_due))

        # Update total due
        total_due = calculate_total_due()
        total_due_label.config(text=f"Total Due: ₱{total_due:.2f}")

        # Check for overdue bills after adding a new bill
        check_overdue_bills()

        # Save the updated data
        save_data()

    def mark_as_paid():
        selected_item = bill_tree.selection()
        if selected_item:
            bill_tree.delete(selected_item)

            # Update total due
            total_due = calculate_total_due()
            total_due_label.config(text=f"Total Due: ₱{total_due:.2f}")

            # Save the updated data
            save_data()

    def calculate_total_due():
        total_due = 0.0
        for item in bill_tree.get_children():
            price_str = bill_tree.item(item, 'values')[2]
            try:
                total_due += float(price_str)
            except ValueError:
                pass
        return total_due

    def check_overdue_bills():
        current_time = datetime.now()
        for item in bill_tree.get_children():
            due_date_str = bill_tree.item(item, 'values')[1]
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

            # If the due date has passed and the bill is not marked as paid, update its appearance
            if current_time > due_date and item not in bill_tree.selection():
                bill_tree.item(item, tags=('overdue',))
            else:
                bill_tree.item(item, tags=())

    def save_data():
        data = []
        for item in bill_tree.get_children():
            values = bill_tree.item(item, 'values')
            data.append(",".join(map(str, values)))

        with open(username + "bill_data.txt", "w") as file:  # open file for user
            file.write("\n".join(data))

    def load_data():
        try:
            with open(username + "bill_data.txt", "r") as file:  # open file for user
                for line in file:
                    values = line.strip().split(",")
                    bill_tree.insert("", "end", values=values)

            # Update total due after loading data
            total_due = calculate_total_due()
            total_due_label.config(text=f"Total Due: ₱{total_due:.2f}")

            # Check for overdue bills after loading data
            check_overdue_bills()

        except FileNotFoundError:
            # Handle the case where the file doesn't exist yet
            pass

    global billimage
    global homebutton
    global addbutton
    global deletebutton

    frame_BILL = Frame(Win, width=900, height=600, bg="white")
    frame_BILL.place(x=0, y=0)

    pil4_image = Image.open(r"billpage3.png")
    billimage = ImageTk.PhotoImage(pil4_image)

    canvas = Canvas(frame_BILL, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=billimage)

    date_label = Label(frame_BILL, font=("Helvetica", 18,))
    date_label.place(relx=0.63, rely=0.145, anchor="w")

    time_label = Label(frame_BILL, font=("Helvetica", 18))
    time_label.place(relx=0.63, rely=0.25, anchor="w")

    #add_bill_button = Button(frame_BILL, text="Add Bill", command=add_bill, font=("Arial", 12, "bold"))
    #add_bill_button.place(relx=0.02, rely=0.2, anchor="w")
    addbutton = PhotoImage(file=r"add3.png")
    btnadd = Button(frame_BILL, image=addbutton, command=add_bill, bd=0, compound=CENTER, padx=0, pady=0)
    btnadd.place(x=60, y=215)

    #paid_button = Button(frame_BILL, text="Paid", command=mark_as_paid, font=("Arial", 12, "bold"))
    #paid_button.place(relx=0.02, rely=0.28, anchor="w")
    deletebutton = PhotoImage(file=r"delete3.png")
    btndelete = Button(frame_BILL, image=deletebutton, command=mark_as_paid, bd=0, compound=CENTER, padx=0, pady=0)
    btndelete.place(x=60, y=335)

    columns = ("Bill Name", "Due Date", "Price", "Days Until Due")
    bill_tree = ttk.Treeview(frame_BILL, columns=columns, show="headings")

    for col in columns:
        bill_tree.heading(col, text=col)
        bill_tree.column(col, width=130)

    scrollbar = ttk.Scrollbar(frame_BILL, orient="vertical", command=bill_tree.yview)
    bill_tree.configure(yscrollcommand=scrollbar.set)
    bill_tree.place(relx=0.677, rely=0.585, anchor="center")
    scrollbar.place(relx=0.95, rely=0.55, anchor="center")

    total_due_label = Label(frame_BILL, text="₱0.00", font=("Helvetica", 24))
    total_due_label.place(relx=0.91, rely=0.88, anchor="e")

    homebutton = PhotoImage(file=r"rsz_homebutton3.png")
    btnhome = Button(frame_BILL, image=homebutton, command=Home, bd=0, compound=CENTER, padx=0, pady=0)
    btnhome.place(x=60, y=480)

    update_time()
    check_overdue_bills()
    load_data()  # Load saved data when the app starts

#----------------------------------------------------------------------------------------------------------------------
def TDL():
    global tdlimage

    frame_TDL = Frame(Win, width=900, height=600, bg="white")
    frame_TDL.place(x=0, y=0)

    pil3_image = Image.open(r"rsz_ttdlpage2.png")
    tdlimage = ImageTk.PhotoImage(pil3_image)

    canvas = Canvas(frame_TDL, width=900, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=tdlimage)

    class Node:
        def __init__(self, data, due_datetime=None):
            self.data = data
            self.due_datetime = due_datetime
            self.next = None

    class TodoList:
        def __init__(self):
            self.head = None
            self.file_path = username + "todo_list.txt"

            # Load tasks from the file on initialization
            self.load_tasks()

        def add_task(self, task, due_datetime=None):
            new_task = Node(task, due_datetime)
            new_task.next = self.head
            self.head = new_task

            # Save tasks to the file after adding a new task
            self.save_tasks()
            self.sort_tasks_by_due_date()

        def display_tasks(self):
            current = self.head
            tasks = []
            while current:
                tasks.append((current.data, current.due_datetime))
                current = current.next
            return tasks

        def remove_task(self, task):
            current = self.head
            previous = None

            while current and current.data != task:
                previous = current
                current = current.next

            if current is not None:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                # Save tasks to the file after removing a task
                self.save_tasks()
            self.sort_tasks_by_due_date()

        def save_tasks(self):
            with open(self.file_path, 'w') as file:
                current = self.head
                while current:
                    file.write(f"{current.data},{current.due_datetime}\n")
                    current = current.next

        def load_tasks(self):
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    tasks = file.read().splitlines()
                    for task in reversed(tasks):
                        task_data, due_datetime = task.split(',')
                        self.add_task(task_data, due_datetime)

        def sort_tasks_by_due_date(self):
            sorted_tasks = sorted(self.display_tasks(),
                                  key=lambda x: datetime.strptime(x[1] or "9999-12-31 23:59", "%Y-%m-%d %H:%M"))
            return sorted_tasks

        def calculate_remaining_time(self, due_datetime):
            if due_datetime:
                due_datetime_obj = datetime.strptime(due_datetime, "%Y-%m-%d %H:%M")
                current_datetime = datetime.now()
                remaining_time = due_datetime_obj - current_datetime
                return max(remaining_time, timedelta())
            return None

        def is_past_due_date(self, due_datetime):
            if due_datetime:
                due_datetime_obj = datetime.strptime(due_datetime, "%Y-%m-%d %H:%M")
                return due_datetime_obj < datetime.now()
            return False

    class TodoListGUI:
        def __init__(self, master):
            self.master = master
            self.master.title("Todo List")

            self.todo_list = TodoList()

            global addbutton
            global deletebutton
            global homebutton

            # Check for past due tasks during initialization
            past_due_tasks = self.get_past_due_tasks()
            if past_due_tasks:
                self.display_past_due_notification(past_due_tasks)

            self.task_entry = Entry(self.master, width=30)
            #self.task_entry.pack(pady=10)

            self.due_date_entry = Entry(self.master, width=15)
            #self.due_date_entry.pack(pady=10)
            self.due_date_entry.insert(0, "YYYY-MM-DD HH:MM")

            #add_button = Button(self.master, text="Add Task", command=self.add_task, width=40, height=7)
            #add_button.place(x=50, y=150)
            addbutton = PhotoImage(file=r"add3.png")
            btnadd = Button(frame_TDL, image=addbutton, command=self.add_task, bd=0, compound=CENTER, padx=0, pady=0)
            btnadd.place(x=60, y=200)

            #remove_button = Button(self.master, text="Remove Task", command=self.remove_task, width=40, height=7)
            #remove_button.place(x=50, y=275)
            deletebutton = PhotoImage(file=r"delete3.png")
            btndelete = Button(frame_TDL, image=deletebutton, command=self.add_task, bd=0, compound=CENTER, padx=0, pady=0)
            btndelete.place(x=60, y=330)

            #btnHome = Button(self.master, text="Home", command=Home, bd=0, bg="white", font=("Arial", 12, "bold"))
            #btnHome.place(x=20, y=550)
            homebutton = PhotoImage(file=r"rsz_homebutton3.png")
            btnhome = Button(frame_TDL, image=homebutton, command=Home, bd=0, compound=CENTER, padx=0,pady=0)
            btnhome.place(x=60, y=470)

            # Treeview to display tasks

            self.tree = ttk.Treeview(self.master, columns=('Tasks', 'Due Date', 'Remaining Time'), show='headings', height=18)
            style.configure("Treeview.Heading", font = (None, 12))
            self.tree.heading('Tasks', text='Tasks')
            self.tree.heading('Due Date', text='Due Date')
            self.tree.heading('Remaining Time', text='Remaining Time')
            #self.tree.pack(pady=10)
            self.tree.place(x=407, y=140)
            self.tree.column(0, width="200")#
            self.tree.column(1, width="125")#
            self.tree.column(2, width="125")#


            # Load tasks into the Treeview on initialization
            self.load_tasks_to_tree()
            self.master.after(1000, self.update_remaining_time)

        def selectDate(self):
            global due_date_str
            global bill_name
            due_date_str = myCal.get_date()
            return due_date_str

        def calendar(self):
            global myCal
            myCal = Calendar(self.master, setmode='day', date_pattern='YYYY-MM-DD')
            myCal.place(x=350, y=100)
            openCal = Button(self.master, text="Select Date", command=lambda: var.set(1))
            openCal.place(x=425, y=300)
            openCal.wait_variable(var)
            myCal.destroy()
            openCal.destroy()

        def get_past_due_tasks(self):
            past_due_tasks = [task[0] for task in self.todo_list.display_tasks() if
                              self.todo_list.is_past_due_date(task[1])]
            return past_due_tasks

        def display_past_due_notification(self, past_due_tasks):
            notification_message = "The following tasks are past their due date:\n\n"
            notification_message += "\n".join(past_due_tasks)
            messagebox.showinfo("Past Due Tasks", notification_message)

        def add_task(self):
            task = simpledialog.askstring("Input", "Enter Task:")
            self.calendar()
            due_date = self.selectDate()

            Hour_Min = simpledialog.askstring("Input", "Enter Hour and Minute (HH:MM)")
            due_date = due_date + " " + Hour_Min
            if task:
                self.todo_list.add_task(task, due_date)
                self.task_entry.delete(0, tk.END)
                self.due_date_entry.delete(0, tk.END)
                self.due_date_entry.insert(0, "YYYY-MM-DD HH:MM")
                self.load_tasks_to_tree()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
            self.sort_tasks()

        def display_tasks(self):
            tasks = self.todo_list.display_tasks()
            if tasks:
                task_list = "\n".join(
                    [f"{task[0]} - Due Date: {task[1]} - Remaining Time: {self.get_remaining_time_text(task[1])}" for
                     task in tasks])
                messagebox.showinfo("Tasks", task_list)
            else:
                messagebox.showinfo("Tasks", "No tasks in the list.")

        def remove_task(self):
            selected_item = self.tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a task to remove.")
                return

            task_data, due_datetime, remaining_time = self.tree.item(selected_item, 'values')
            if task_data:
                self.todo_list.remove_task(task_data)
                self.load_tasks_to_tree()
            else:
                messagebox.showwarning("Warning", "Please select a valid task to remove.")
            self.sort_tasks()

        def sort_tasks(self):
            sorted_tasks = self.todo_list.sort_tasks_by_due_date()
            # Clear existing items in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            for task in sorted_tasks:
                remaining_time_text = self.get_remaining_time_text(task[1])
                self.tree.insert('', 'end', values=(task[0], task[1], remaining_time_text))

        def load_tasks_to_tree(self):
            # Clear existing items in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            tasks = self.todo_list.display_tasks()
            for task in tasks:
                remaining_time_text = self.get_remaining_time_text(task[1])
                self.tree.insert('', 'end', values=(task[0], task[1], remaining_time_text))
            self.sort_tasks()

        def get_remaining_time_text(self, due_datetime):
            remaining_time = self.todo_list.calculate_remaining_time(due_datetime)
            if remaining_time is not None:
                if remaining_time.total_seconds() <= 0:
                    return "Past Due Date"
                days, seconds = divmod(remaining_time.total_seconds(), 86400)
                hours, seconds = divmod(seconds, 3600)
                minutes, seconds = divmod(seconds, 60)
                return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes"
            return None

        def update_remaining_time(self):
            # Update the remaining time in the Treeview every second
            for item_id in self.tree.get_children():
                task_data, due_datetime, _ = self.tree.item(item_id, 'values')
                remaining_time_text = self.get_remaining_time_text(due_datetime)
                self.tree.item(item_id, values=(task_data, due_datetime, remaining_time_text))

            # Schedule the next update
            self.master.after(1000, self.update_remaining_time)

    TodoListGUI(Win)

# -------------------------------------------------------------------------------

def ABT():
    frame_ABT = Frame(Win, width=900, height=600, bg="white")
    frame_ABT.place(x=0, y=0)

    btnHome = Button(frame_ABT, text="Home", command=Home, bd=0, bg="white") #add image = ?
    btnHome.place(x=850, y=570)

    lblTitle = Label(frame_ABT, text="FINAL OUTPUT ", font=("Helvetica", 30), bg="white").place(x=325, y=50)
    lblTitle2 = Label(frame_ABT, text="DATA STRUCTURES & ALGORITHMS LAB", font=("Helvetica", 20),
                     bg="white").place(x=210, y=125)
    lblTitle3 = Label(frame_ABT, text="58009 WF 10:30AM - 1:30PM\nEngr. Maria Rizette H. Sayo", font=("Helvetica", 15),
                      bg="white").place(x=340, y=175)
    lblInfo = Label(frame_ABT, text="This application is composed of multiple calculators useful for\nMathemathics in the Modern World and Physics for Engineers", font=("Helvetica", 15), pady=10,
                     bg="white").place(x=200, y=250)
    lblTitle4 = Label(frame_ABT, text="PROPONENTS", font=("Helvetica", 20),
                      bg="white").place(x=375, y=350)
    lblLozano_pic = Label(frame_ABT,  bd=0).place(x=90, y=400) #add image = ?
    lblTabobo_pic = Label(frame_ABT,  bd=0).place(x=245, y=400) #add image = ?
    lblDelasalas_pic = Label(frame_ABT,  bd=0).place(x=400, y=400) #add image = ?
    lblGuzman_pic = Label(frame_ABT, bd=0).place(x=555, y=400) #add image = ?
    lblSalino_pic = Label(frame_ABT, bd=0).place(x=710, y=400) #add image = ?


    lblLozano_name = Label(frame_ABT, text="Christian Jhomel Despi", font=("Helvetica", 8), bg="white").place(x=85, y=530)
    lblTabobo_name = Label(frame_ABT, text="Juan Miguel Ferreras", font=("Helvetica", 8), bg="white").place(x=240,y=530)
    lblDelasalas_name = Label(frame_ABT, text="Gilmore Floyd Lozano", font=("Helvetica", 8), bg="white").place(x=395,y=530)
    lblGuzman_name = Label(frame_ABT, text="Jan Mathew Mendoza", font=("Helvetica", 8), bg="white").place(x=550, y=530)
    lblSalino_name = Label(frame_ABT, text="Darielle Angela Valero", font=("Helvetica", 8), bg="white").place(x=705, y=530)
StartPage()
Win.mainloop()