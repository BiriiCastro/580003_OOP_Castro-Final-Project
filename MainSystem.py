from tkinter import *  # import functions of tkinter
from PIL import ImageTk, Image  # for accessing image
import messagebox  # to show messageboxes
from datetime import datetime  # for date and time
from dateutil import relativedelta  # for the validity of the receipt: so i can add 1 year for the current datetime
import random  # for randomization
import josetorasakana  # for info of Movie1
import jujutsu  # for info of Movie2
import kiminonawa  # for info of Movie3
import suizo  # for info of Movie4
import koe  # for info of Movie5
import tenki  # for info of Movie6
import data  # for data inside data.py


# to open movie 1
def open_jose():
    josetorasakana.JoseMovie()


# to open movie 2
def open_jujutsu():
    jujutsu.JjkMovie()


# to open movie 3
def open_namae():
    kiminonawa.NamaeMovie()


# to open movie 4
def open_suizo():
    suizo.SuizoMovie()


# to open movie 5
def open_koe():
    koe.KoeMovie()


# to open movie 6
def open_tenki():
    tenki.TenkiMovie()


class Main:
    def __init__(self):
        # to access data
        self.data = data
        # header
        self.frame_header = Frame(main_window)
        self.frame_header.grid(row=0, column=0, sticky="nsew")
        self.frame_header.configure(background="black")

        self.banner = Image.open("AI-chan.png")
        self.banner_size = self.banner.resize((400, 100), Image.LANCZOS)
        self.img0 = ImageTk.PhotoImage(self.banner_size)
        self.lbl0 = Button(self.frame_header, image=self.img0, bg="black", activebackground="black", bd=0)
        self.lbl0.configure(state="active", relief=SUNKEN)
        self.lbl0.grid(row=0, column=0, columnspan=6, pady=5)

        self.line = Label(self.frame_header, text="Movies", bg="#1FBB28", fg="white")
        self.line.grid(row=1, column=0, columnspan=6, pady=2, ipadx=530)

        # body
        self.body_frame = Frame(main_window, bg="black")
        self.body_frame.grid(row=2, column=0, pady=15, ipadx=10)

        self.movie1 = Image.open("Jose.jpg")
        self.movie1_size = self.movie1.resize((93, 131), Image.LANCZOS)
        self.img1 = ImageTk.PhotoImage(self.movie1_size)
        self.lbl11 = Button(self.body_frame, image=self.img1, bg="black", activebackground="black", anchor=W, bd=0,
                            command=open_jose)
        self.lbl11.grid(row=0, column=0, rowspan=3, padx=20, ipadx=10, ipady=10)
        self.lbl21 = Button(self.body_frame, text=f"{data.Movies[0]}", anchor=W, bg="black", fg="#1FBB28",
                            activebackground="black", activeforeground="#1FBB28",
                            font=("California FB", 12), bd=0, command=open_jose)
        self.lbl21.grid(row=0, column=1, padx=10, sticky="s")
        self.lbl31 = Label(self.body_frame, text="Genre: Drama, Romance", anchor=W, bg="black", fg="white")
        self.lbl31.grid(row=1, column=1, padx=10, sticky="n", rowspan=2)
        self.lbl41 = Label(self.body_frame, text=f"${data.Prices[0]}", font=("Open Sans", 15), bg="black", fg="yellow")
        self.lbl41.grid(row=0, column=2)
        self.spinbox1 = Spinbox(self.body_frame, from_=0, to=100, width=5, font=("Open Sans", 12))
        self.spinbox1.grid(row=1, column=2, padx=15)

        self.movie2 = Image.open("jjk.jpg_large")
        self.movie2_size = self.movie2.resize((93, 131), Image.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.movie2_size)
        self.lbl12 = Button(self.body_frame, image=self.img2, bg="black", activebackground="black", anchor=W, bd=0,
                            command=open_jujutsu)
        self.lbl12.grid(row=3, column=0, rowspan=3, padx=20, ipadx=10, ipady=10)
        self.lbl22 = Button(self.body_frame, text=f"{data.Movies[1]}", anchor=W, bg="black", fg="#1FBB28",
                            activebackground="black", activeforeground="#1FBB28",
                            font=("California FB", 12), bd=0, command=open_jujutsu)
        self.lbl22.grid(row=3, column=1, padx=5, sticky="s")
        self.lbl32 = Label(self.body_frame, text=" Genre: Action, Fantasy ", anchor=W, bg="black", fg="white")
        self.lbl32.grid(row=4, column=1, padx=5, sticky="n", rowspan=2)
        self.lbl42 = Label(self.body_frame, text=f"${data.Prices[1]}", font=("Open Sans", 15), bg="black", fg="yellow")
        self.lbl42.grid(row=3, column=2)
        self.spinbox2 = Spinbox(self.body_frame, from_=0, to=100, width=5, font=("Open Sans", 12))
        self.spinbox2.grid(row=4, column=2, padx=15)

        self.movie3 = Image.open("kimi-no-na-wa.jpg")
        self.movie3_size = self.movie3.resize((93, 131), Image.LANCZOS)
        self.img3 = ImageTk.PhotoImage(self.movie3_size)
        self.lbl13 = Button(self.body_frame, image=self.img3, bg="black", activebackground="black", anchor=W, bd=0,
                            command=open_namae)
        self.lbl13.grid(row=7, column=0, rowspan=3, padx=20, ipadx=10, ipady=10)
        self.lbl23 = Button(self.body_frame, text=f"{data.Movies[2]}", anchor=W, bg="black", fg="#1FBB28",
                            activebackground="black", activeforeground="#1FBB28",
                            font=("California FB", 12), bd=0, command=open_namae)
        self.lbl23.grid(row=7, column=1, padx=5, sticky="s")
        self.lbl33 = Label(self.body_frame, text="Genre: Drama, Romance", anchor=W, bg="black", fg="white")
        self.lbl33.grid(row=8, column=1, padx=5, sticky="n", rowspan=2)
        self.lbl43 = Label(self.body_frame, text=f"${data.Prices[2]}", font=("Open Sans", 15), bg="black", fg="yellow")
        self.lbl43.grid(row=7, column=2)
        self.spinbox3 = Spinbox(self.body_frame, from_=0, to=100, width=5, font=("Open Sans", 12))
        self.spinbox3.grid(row=8, column=2, padx=15)

        self.movie4 = Image.open("Suizo.jpg")
        self.movie4_size = self.movie4.resize((93, 131), Image.LANCZOS)
        self.img4 = ImageTk.PhotoImage(self.movie4_size)
        self.lbl14 = Button(self.body_frame, image=self.img4, bg="black", activebackground="black", anchor=W, bd=0,
                            command=open_suizo)
        self.lbl14.grid(row=0, column=3, rowspan=3, padx=20, ipadx=10, ipady=10)
        self.lbl24 = Button(self.body_frame, text=f"{data.Movies[3]}", anchor=W, bg="black", fg="#1FBB28",
                            activebackground="black", activeforeground="#1FBB28",
                            font=("California FB", 12), bd=0, command=open_suizo)
        self.lbl24.grid(row=0, column=4, padx=5, sticky="s")
        self.lbl34 = Label(self.body_frame, text="Genre: Drama, Romance", anchor=W, bg="black", fg="white")
        self.lbl34.grid(row=1, column=4, padx=5, sticky="n", rowspan=2)
        self.lbl44 = Label(self.body_frame, text=f"${data.Prices[3]}", font=("Open Sans", 15), bg="black", fg="yellow")
        self.lbl44.grid(row=0, column=5)
        self.spinbox4 = Spinbox(self.body_frame, from_=0, to=100, width=5, font=("Open Sans", 12))
        self.spinbox4.grid(row=1, column=5, padx=15)

        self.movie5 = Image.open("koe-no-katachi.jpg")
        self.movie5_size = self.movie5.resize((93, 131), Image.LANCZOS)
        self.img5 = ImageTk.PhotoImage(self.movie5_size)
        self.lbl15 = Button(self.body_frame, image=self.img5, bg="black", activebackground="black", anchor=W, bd=0,
                            command=open_koe)
        self.lbl15.grid(row=3, column=3, rowspan=3, padx=20, ipadx=10, ipady=10)
        self.lbl25 = Button(self.body_frame, text=f"{data.Movies[4]}", anchor=W, bg="black", fg="#1FBB28",
                            activebackground="black", activeforeground="#1FBB28",
                            font=("California FB", 12), bd=0, command=open_koe)
        self.lbl25.grid(row=3, column=4, padx=5, sticky="s")
        self.lbl35 = Label(self.body_frame, text="Genre: Drama, Shonen", anchor=W, bg="black", fg="white")
        self.lbl35.grid(row=4, column=4, padx=5, sticky="n", rowspan=2)
        self.lbl45 = Label(self.body_frame, text=f"${data.Prices[4]}", font=("Open Sans", 15), bg="black", fg="yellow")
        self.lbl45.grid(row=3, column=5)
        self.spinbox5 = Spinbox(self.body_frame, from_=0, to=100, width=5, font=("Open Sans", 12))
        self.spinbox5.grid(row=4, column=5, padx=15)

        self.movie6 = Image.open("Tenki.jpg")
        self.movie6_size = self.movie6.resize((93, 131), Image.LANCZOS)
        self.img6 = ImageTk.PhotoImage(self.movie6_size)
        self.lbl16 = Button(self.body_frame, image=self.img6, bg="black", activebackground="black", anchor=W, bd=0,
                            command=open_tenki)
        self.lbl16.grid(row=7, column=3, rowspan=3, padx=20, ipadx=10, ipady=10)
        self.lbl26 = Button(self.body_frame, text=f"{data.Movies[5]}", anchor=W, bg="black", fg="#1FBB28",
                            activebackground="black", activeforeground="#1FBB28",
                            font=("California FB", 12), bd=0, command=open_tenki)
        self.lbl26.grid(row=7, column=4, padx=5, sticky="s")
        self.lbl36 = Label(self.body_frame, text="Genre: Drama, Romance, Fantasy", anchor=W, bg="black", fg="white")
        self.lbl36.grid(row=8, column=4, padx=5, sticky="n", rowspan=2)
        self.lbl46 = Label(self.body_frame, text=f"${data.Prices[5]}", font=("Open Sans", 15), bg="black", fg="yellow")
        self.lbl46.grid(row=7, column=5)
        self.spinbox6 = Spinbox(self.body_frame, from_=0, to=100, width=5, font=("Open Sans", 12))
        self.spinbox6.grid(row=8, column=5, padx=15)

        self.exit_button = Button(main_window, text="Exit", width=12, bg="grey",
                                  activebackground="grey",
                                  font=("California FB", 15), fg="white", activeforeground="white",
                                  command=exit_window)
        self.exit_button.place(x=100, y=630)

        self.order_button = Button(main_window, text="Order Now", width=12, bg="#1FBB28",
                                   activebackground="#1FBB28",
                                   font=("California FB", 15), fg="white", activeforeground="white",
                                   command=self.get_spinbox_value)
        self.order_button.place(x=850, y=630)

    def get_spinbox_value(self):
        data.Quantity.append(float(self.spinbox1.get()))
        data.Quantity.append(float(self.spinbox2.get()))
        data.Quantity.append(float(self.spinbox3.get()))
        data.Quantity.append(float(self.spinbox4.get()))
        data.Quantity.append(float(self.spinbox5.get()))
        data.Quantity.append(float(self.spinbox6.get()))
        Cart()


def exit_window():
    response = messagebox.askyesno(title="Exit", message="Do you want to Exit?")
    if response:
        main_window.destroy()


class Cart:
    def __init__(self):
        self.data = data

        self.cart_window = Toplevel()
        self.cart_window.geometry("1090x700+200+15")
        self.cart_window.resizable(width=False, height=False)
        self.cart_window.title("Order Now")
        self.cart_window.config(bg="black")
        self.cart_window.grab_set()

        # header
        self.frame_header = Frame(self.cart_window)
        self.frame_header.grid(row=0, column=0, sticky="nsew")
        self.frame_header.configure(background="black")

        banner = Image.open("AI-chan.png")
        banner_size = banner.resize((400, 100), Image.LANCZOS)
        img0 = ImageTk.PhotoImage(banner_size)
        lbl0 = Button(self.frame_header, image=img0, bg="black", activebackground="black", bd=0,
                      command=self.cart_window.destroy)
        lbl0.configure(state="active", relief=SUNKEN)
        lbl0.grid(row=0, column=0, columnspan=6, pady=5)

        line = Label(self.frame_header, text="My Cart", bg="#1FBB28", fg="white")
        line.grid(row=1, column=0, columnspan=6, pady=2, ipadx=529)

        # body
        self.cart_frame = Frame(self.cart_window, bg="black")
        self.cart_frame.grid(row=2, column=0, pady=15, ipadx=10)

        self.title1 = Label(self.cart_frame, text="Movies", font=("California FB", 20), bg="black", fg="#1FBB28")
        self.title1.grid(row=0, column=0, ipadx=230, pady=10)
        self.title2 = Label(self.cart_frame, text="Quantity", font=("California FB", 20), bg="black", fg="#1FBB28")
        self.title2.grid(row=0, column=1, ipadx=50, pady=10)
        self.title3 = Label(self.cart_frame, text="Price", font=("California FB", 20), bg="black", fg="#1FBB28")
        self.title3.grid(row=0, column=2, ipadx=50, pady=10)

        if self.data.Quantity[0] != 0:
            self.movie1 = Label(self.cart_frame, text=f"{self.data.Movies[0]}", font=("California FB", 15), bg="black",
                                fg="white")
            self.movie1.grid(row=1, column=0, pady=10)
            self.movie1 = Label(self.cart_frame, text=f"x{self.data.Quantity[0]}", font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie1.grid(row=1, column=1, pady=10)
            self.movie1 = Label(self.cart_frame, text=f"${(self.data.Quantity[0] * data.Prices[0]):.2f}",
                                font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie1.grid(row=1, column=2, pady=10)

        if self.data.Quantity[1] != 0:
            self.movie2 = Label(self.cart_frame, text=f"{self.data.Movies[1]}", font=("California FB", 15), bg="black",
                                fg="white")
            self.movie2.grid(row=2, column=0, pady=10)
            self.movie2 = Label(self.cart_frame, text=f"x{self.data.Quantity[1]}", font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie2.grid(row=2, column=1, pady=10)
            self.movie2 = Label(self.cart_frame, text=f"${(self.data.Quantity[1] * data.Prices[1]):.2f}",
                                font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie2.grid(row=2, column=2, pady=10)

        if self.data.Quantity[2] != 0:
            self.movie3 = Label(self.cart_frame, text=f"{self.data.Movies[2]}", font=("California FB", 15), bg="black",
                                fg="white")
            self.movie3.grid(row=3, column=0, pady=10)
            self.movie3 = Label(self.cart_frame, text=f"x{self.data.Quantity[2]}", font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie3.grid(row=3, column=1, pady=10)
            self.movie3 = Label(self.cart_frame, text=f"${(self.data.Quantity[2] * data.Prices[2]):.2f}",
                                font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie3.grid(row=3, column=2, pady=10)

        if self.data.Quantity[3] != 0:
            self.movie4 = Label(self.cart_frame, text=f"{self.data.Movies[3]}", font=("California FB", 15), bg="black",
                                fg="white")
            self.movie4.grid(row=4, column=0, pady=10)
            self.movie4 = Label(self.cart_frame, text=f"x{self.data.Quantity[3]}", font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie4.grid(row=4, column=1, pady=10)
            self.movie4 = Label(self.cart_frame, text=f"${(self.data.Quantity[3] * data.Prices[3]):.2f}",
                                font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie4.grid(row=4, column=2, pady=10)

        if self.data.Quantity[4] != 0:
            self.movie5 = Label(self.cart_frame, text=f"{self.data.Movies[4]}", font=("California FB", 15), bg="black",
                                fg="white")
            self.movie5.grid(row=5, column=0, pady=10)
            self.movie5 = Label(self.cart_frame, text=f"x{self.data.Quantity[4]}", font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie5.grid(row=5, column=1, pady=10)
            self.movie5 = Label(self.cart_frame, text=f"${(self.data.Quantity[4] * data.Prices[4]):.2f}",
                                font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie5.grid(row=5, column=2, pady=10)

        if self.data.Quantity[5] != 0:
            self.movie6 = Label(self.cart_frame, text=f"{self.data.Movies[5]}", font=("California FB", 15), bg="black",
                                fg="white")
            self.movie6.grid(row=6, column=0, pady=10)
            self.movie6 = Label(self.cart_frame, text=f"x{self.data.Quantity[5]}", font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie6.grid(row=6, column=1, pady=10)
            self.movie6 = Label(self.cart_frame, text=f"${(self.data.Quantity[5] * data.Prices[5]):.2f}",
                                font=("California FB", 15),
                                bg="black",
                                fg="white")
            self.movie6.grid(row=6, column=2, pady=10)

        self.total_label = Label(self.cart_frame, text=f"Total:", font=("California FB", 20), bg="black", fg="yellow")
        self.total_label.grid(row=7, column=1, pady=20)

        self.total_price = Label(self.cart_frame,
                                 text=f"${sum([self.data.Quantity[i] * self.data.Prices[i] for i in range(6)]):.2f}",
                                 font=("California FB", 20), bg="black", fg="yellow")
        self.total_price.grid(row=7, column=2, pady=20)

        self.back_button = Button(self.cart_window, text="Back", width=12, bg="grey",
                                  activebackground="grey",
                                  font=("California FB", 15), fg="white", activeforeground="white",
                                  command=self.back_to_main_window)
        self.back_button.place(x=100, y=630)

        self.confirm_button = Button(self.cart_window, text="Confirm", width=12, bg="#1FBB28",
                                     activebackground="#1FBB28",
                                     font=("California FB", 15), fg="white", activeforeground="white",
                                     command=open_receipt)
        self.confirm_button.place(x=850, y=630)

        self.cart_window.mainloop()

    def back_to_main_window(self):
        self.data.Quantity = []
        self.cart_window.destroy()


def open_receipt():
    if sum([data.Quantity[i] for i in range(6)]) > 0:
        Payment()
    else:
        data.Quantity = []
        messagebox.showerror(title="Error", message="Please order something to continue")


def validate_card_number(new_value):
    if not new_value:
        return True
    try:
        int(new_value)
        if len(new_value) <= 16:
            return True
    except ValueError:
        pass
    return False


def validate_cvv(new_value):
    if not new_value:
        return True
    try:
        int(new_value)
        if len(new_value) <= 4:
            return True
    except ValueError:
        pass
    return False


class Payment:
    def __init__(self):
        self.data = data

        self.month_options = ["January", "February", "March", "April", "May", "June",
                              "July", "August", "September", "October", "November", "December"]
        self.year_options = [str(year) for year in range(2023, 2035)]

        self.payment_window = Toplevel()
        self.payment_window.geometry("1090x700+200+15")
        self.payment_window.resizable(width=False, height=False)
        self.payment_window.title("Tenki no Ko")
        self.payment_window.config(bg="black")
        self.payment_window.grab_set()

        # header
        self.frame_header = Frame(self.payment_window)
        self.frame_header.grid(row=0, column=0, sticky="nsew", columnspan=6)
        self.frame_header.configure(background="black")

        self.banner = Image.open("AI-chan.png")
        self.banner_size = self.banner.resize((400, 100), Image.LANCZOS)
        self.img0 = ImageTk.PhotoImage(self.banner_size)
        self.lbl0 = Button(self.frame_header, image=self.img0, bg="black", activebackground="black", bd=0,
                           command=self.payment_window.destroy)
        self.lbl0.configure(state="active", relief=SUNKEN)
        self.lbl0.grid(row=0, column=0, columnspan=6, pady=5)

        self.line = Label(self.frame_header, text="Payment Method", bg="#1FBB28", fg="white")
        self.line.grid(row=1, column=0, columnspan=6, pady=2, ipadx=501)

        self.frame_body_left = Frame(self.payment_window)
        self.frame_body_left.grid(row=1, column=0, pady=20, rowspan=6, sticky="nsew")
        self.frame_body_left.configure(background="black")

        self.total_label = Button(self.frame_body_left,
                                  text=f"Total: ${sum([self.data.Quantity[i] * self.data.Prices[i] for i in range(6)]):.2f}",
                                  font=("California FB", 25), bd=0, bg="yellow", activebackground="yellow", fg="black",
                                  activeforeground="black", width=13)
        self.total_label.configure(state="active", relief=SUNKEN)
        self.total_label.grid(row=0, column=0, pady=20)

        self.cash_button = Button(self.frame_body_left, text="Cash", font=("California FB", 25), bd=0, bg="green",
                                  activebackground="green", fg="white", activeforeground="black", width=10,
                                  command=self.show_cash)
        self.cash_button.grid(row=1, column=0, pady=10)

        self.card_button = Button(self.frame_body_left, text="Card", font=("California FB", 25), bd=0, bg="green",
                                  activebackground="green", fg="white", activeforeground="black", width=10,
                                  command=self.show_card)
        self.card_button.grid(row=2, column=0, pady=10)

        self.frame_body_right = Frame(self.payment_window)
        self.frame_body_right.grid(row=1, column=1, columnspan=5, pady=20, sticky="nsew")
        self.frame_body_right.configure(background="black")

        self.right_label = Label(self.frame_body_right, text="Select Payment Method",
                                 font=("California FB", 25, "bold"),
                                 bg="black", fg="#1FBB28")
        self.right_label.pack(side=BOTTOM)

        self.back_button = Button(self.payment_window, text="Back", width=12, bg="grey",
                                  activebackground="grey",
                                  font=("California FB", 15), fg="white", activeforeground="white",
                                  command=self.back_to_cart_window)
        self.back_button.place(x=100, y=630)

        self.payment_window.mainloop()

    def show_cash(self):
        for widget in self.frame_body_right.winfo_children():
            widget.destroy()

        label1 = Label(self.frame_body_right, text="Please Click 'Print' and Proceed to\n"
                                                   "the Counter after Printing", font=("California FB", 25, "bold"),
                       bg="black", fg="#1FBB28")
        label1.pack(side=BOTTOM, pady=100)

        confirm_button = Button(self.payment_window, text="Print", width=12, bg="#1FBB28",
                                activebackground="#1FBB28",
                                font=("California FB", 15), fg="white", activeforeground="white",
                                command=self.go_to_receipt)
        confirm_button.place(x=850, y=630)

    def show_card(self):
        for widget in self.frame_body_right.winfo_children():
            widget.destroy()

        title_label = Label(self.frame_body_right, text="Please Input all Information",
                            font=("California FB", 25, "bold"), bg="black", fg="#1FBB28")
        title_label.grid(row=0, column=0, columnspan=6, sticky="nsew", ipadx=10)
        self.name_label = Label(self.frame_body_right, text="Cardholder Name", font=("California FB", 15), width=20,
                                bg="black", fg="#1FBB28")
        self.name_label.grid(row=1, column=0, pady=20, padx=30)
        self.name_entry = Entry(self.frame_body_right, font=("California FB", 15), width=25)
        self.name_entry.grid(row=1, column=1, padx=10, columnspan=2)

        self.card_number_label = Label(self.frame_body_right, text="Card Number", font=("California FB", 15), width=20,
                                       bg="black", fg="#1FBB28")
        self.card_number_label.grid(row=2, column=0, pady=20, padx=30)
        self.card_number_entry = Entry(self.frame_body_right, font=("California FB", 15), width=25)
        self.card_number_entry.config(validate="key")
        self.card_number_entry.config(
            validatecommand=(self.card_number_entry.register(validate_card_number), "%P"))
        self.card_number_entry.grid(row=2, column=1, padx=10, columnspan=2)

        self.month_var = StringVar()
        self.year_var = StringVar()
        self.now = datetime.now()
        self.month_var.set(self.now.strftime("%B"))
        self.year_var.set(self.now.strftime("%Y"))

        self.card_exp_month_label = Label(self.frame_body_right, text="Expiry Month", font=("California FB", 15),
                                          width=15, bg="black", fg="#1FBB28")
        self.card_exp_month_label.grid(row=3, column=0, padx=5, pady=20)
        self.month_option_menu = OptionMenu(self.frame_body_right, self.month_var, *self.month_options)
        self.month_option_menu.grid(row=3, column=0, padx=5, columnspan=3)

        self.card_exp_year_label = Label(self.frame_body_right, text="Expiry Year", font=("California FB", 15),
                                         width=15,
                                         bg="black", fg="#1FBB28")
        self.card_exp_year_label.grid(row=3, column=2, padx=5, pady=20)
        self.year_option_menu = OptionMenu(self.frame_body_right, self.year_var, *self.year_options)
        self.year_option_menu.grid(row=3, column=3, padx=5, columnspan=2)

        self.cvv_label = Label(self.frame_body_right, text="CVV", font=("California FB", 15), width=20,
                               bg="black", fg="#1FBB28")
        self.cvv_label.grid(row=4, column=0, pady=20, padx=30)
        self.cvv_entry = Entry(self.frame_body_right, font=("California FB", 15), width=25)
        self.cvv_entry.config(validate="key")
        self.cvv_entry.config(validatecommand=(self.cvv_entry.register(validate_cvv), "%P"))
        self.cvv_entry.grid(row=4, column=1, columnspan=2)

        confirm_button = Button(self.payment_window, text="Confirm", width=12, bg="#1FBB28",
                                activebackground="#1FBB28",
                                font=("California FB", 15), fg="white", activeforeground="white",
                                command=self.validate_fields)
        confirm_button.place(x=850, y=630)

    def back_to_cart_window(self):
        self.payment_window.destroy()

    def validate_fields(self):
        name = self.name_entry.get()
        card_number = self.card_number_entry.get()
        cvv = self.cvv_entry.get()

        if name == "" or card_number == "" or cvv == "":
            messagebox.showwarning("Error", "Please enter all required information")
        else:
            Receipt()

    def go_to_receipt(self):
        Receipt()


class Receipt:
    def __init__(self):
        self.data = data

        self.receipt_window = Toplevel()
        self.receipt_window.geometry("540x790+475+0")
        self.receipt_window.resizable(width=False, height=False)
        self.receipt_window.title("Receipt")
        self.receipt_window.config(bg="black")
        self.receipt_window.grab_set()

        self.frame_header = Frame(self.receipt_window)
        self.frame_header.grid(row=0, column=0, sticky="nsew")
        self.frame_header.configure(background="black")

        self.banner = Image.open("AI-chan.png")
        self.banner_size = self.banner.resize((400, 100), Image.LANCZOS)
        self.img0 = ImageTk.PhotoImage(self.banner_size)
        self.lbl0 = Button(self.frame_header, image=self.img0, bg="black", activebackground="black", bd=0)
        self.lbl0.configure(state="active", relief=SUNKEN)
        self.lbl0.grid(row=0, column=0, columnspan=3, pady=5)

        line = Label(self.frame_header, text="Receipt", bg="#1FBB28", fg="white")
        line.grid(row=1, column=2, pady=2, ipadx=253)

        self.title_label = Label(self.frame_header, text="Please go to CLAIM MONITOR",
                                 font=("California FB", 18, "bold"), bg="black", fg="#1FBB28")
        self.title_label.grid(row=2, column=2, pady=15)

        self.frame_body = Frame(self.receipt_window)
        self.frame_body.grid(row=1, column=0, columnspan=2)
        self.frame_body.configure(background="white")

        self.title_label = Label(self.frame_body, text="CLAIM#", bg="white")
        self.title_label.grid(row=1, column=0, pady=5, padx=20, sticky="w")
        self.address_label = Label(self.frame_body, text=f"{random.randint(100000, 999999)}",
                                   font=("California FB", 30, "bold"), bg="white")
        self.address_label.grid(row=2, column=0, pady=5, padx=20)

        self.frame_body_receipt = Frame(self.receipt_window)
        self.frame_body_receipt.grid(row=3, column=0, columnspan=3, pady=20)
        self.frame_body_receipt.configure(background="white")

        self.title_label = Label(self.frame_body_receipt, text="KissCinema", font=("California FB", 15, "bold"),
                                 bg="white")
        self.title_label.grid(row=0, column=1, pady=5, ipadx=10, sticky="nsew")
        self.address_label = Label(self.frame_body_receipt, text="1234 San Marcelino St.\n"
                                                                 "Ermita, Manila", font=("California FB", 10),
                                   bg="white")
        self.address_label.grid(row=1, column=1, ipadx=10)
        self.reference = Label(self.frame_body_receipt, text=f"Reference no.: {random.randint(100000, 999999)}",
                               bg="white")
        self.reference.grid(row=2, column=0, sticky="nsew", ipadx=20)
        self.date = Label(self.frame_body_receipt, text=f"{datetime.now().strftime('%Y-%m-%d %H:%M')}", bg="white")
        self.date.grid(row=2, column=3, sticky="nsew", ipadx=35)
        self.receipt_title = Label(self.frame_body_receipt, text="---Items---", bg="white")
        self.receipt_title.grid(row=3, column=1)

        if data.Quantity[0] != 0:
            self.movie_receipt_left = Label(self.frame_body_receipt,
                                            text=f"x{self.data.Quantity[0]}{self.data.Movies[0]}", bg="white")
            self.movie_receipt_left.grid(row=4, column=0)
            self.movie_receipt_right = Label(self.frame_body_receipt,
                                             text=f"${(self.data.Quantity[0] * self.data.Prices[0]):.2f}", bg="white")
            self.movie_receipt_right.grid(row=4, column=3)

        if data.Quantity[1] != 0:
            self.movie_receipt_left = Label(self.frame_body_receipt,
                                            text=f"x{self.data.Quantity[1]}{self.data.Movies[1]}", bg="white")
            self.movie_receipt_left.grid(row=5, column=0)
            self.movie_receipt_right = Label(self.frame_body_receipt,
                                             text=f"${(self.data.Quantity[1] * self.data.Prices[1]):.2f}", bg="white")
            self.movie_receipt_right.grid(row=5, column=3)

        if data.Quantity[2] != 0:
            self.movie_receipt_left = Label(self.frame_body_receipt,
                                            text=f"x{self.data.Quantity[2]}{self.data.Movies[2]}", bg="white")
            self.movie_receipt_left.grid(row=6, column=0)
            self.movie_receipt_right = Label(self.frame_body_receipt,
                                             text=f"${(self.data.Quantity[2] * self.data.Prices[2]):.2f}", bg="white")
            self.movie_receipt_right.grid(row=6, column=3)

        if data.Quantity[3] != 0:
            self.movie_receipt_left = Label(self.frame_body_receipt,
                                            text=f"x{self.data.Quantity[3]}{self.data.Movies[3]}", bg="white")
            self.movie_receipt_left.grid(row=7, column=0)
            self.movie_receipt_right = Label(self.frame_body_receipt,
                                             text=f"${(self.data.Quantity[3] * self.data.Prices[3]):.2f}", bg="white")
            self.movie_receipt_right.grid(row=7, column=3)

        if data.Quantity[4] != 0:
            self.movie_receipt_left = Label(self.frame_body_receipt,
                                            text=f"x{self.data.Quantity[4]}{self.data.Movies[4]}", bg="white")
            self.movie_receipt_left.grid(row=8, column=0)
            self.movie_receipt_right = Label(self.frame_body_receipt,
                                             text=f"${(self.data.Quantity[4] * self.data.Prices[4]):.2f}", bg="white")
            self.movie_receipt_right.grid(row=8, column=3)

        if data.Quantity[5] != 0:
            self.movie_receipt_left = Label(self.frame_body_receipt,
                                            text=f"x{self.data.Quantity[5]}{self.data.Movies[5]}", bg="white")
            self.movie_receipt_left.grid(row=9, column=0)
            self.movie_receipt_right = Label(self.frame_body_receipt,
                                             text=f"${(self.data.Quantity[5] * self.data.Prices[5]):.2f}", bg="white")
            self.movie_receipt_right.grid(row=9, column=3)

        self.vat_title = Label(self.frame_body_receipt, text="VAT Amount", bg="white")
        self.vat_title.grid(row=10, column=0)
        self.vat_amount = Label(self.frame_body_receipt, text=f"${self.data.Vat[0]}", bg="white")
        self.vat_amount.grid(row=10, column=3)

        self.receipt_line = Label(self.frame_body_receipt, text="----------", bg="white")
        self.receipt_line.grid(row=11, column=3)

        self.receipt_total_title = Label(self.frame_body_receipt, text=f"Total", bg="white")
        self.receipt_total_title.grid(row=12, column=0)
        self.receipt_total_amount = Label(self.frame_body_receipt,
                                          text=f"${sum([self.data.Quantity[i] * self.data.Prices[i] for i in range(6)] + [self.data.Vat[0]]):.2f}",
                                          bg="white")
        self.receipt_total_amount.grid(row=12, column=3)

        self.space = Label(self.frame_body_receipt, bg="white")
        self.space.grid(row=13, column=1, pady=10)
        self.company_info = Label(self.frame_body_receipt, text="KissAnime.ru", bg="white")
        self.company_info.grid(row=14, column=1)
        self.vat_tin = Label(self.frame_body_receipt, text="VAT REG TIN: 2*0-00*-*38", bg="white")
        self.vat_tin.grid(row=15, column=1)
        self.validity = Label(self.frame_body_receipt,
                              text=f"Valid Until: {(datetime.now() + relativedelta.relativedelta(months=3)).strftime('%Y-%m-%d %H:%M')}",
                              bg="white")
        self.validity.grid(row=16, column=1)

        self.ok_button = Button(self.receipt_window, text="Exit", width=8, font=("California FB", 10), bg="#1FBB28",
                                activebackground="#1FBB28", fg="white", activeforeground="white", bd=0,
                                command=clear_all)
        self.ok_button.place(x=235, y=750)

        self.receipt_window.mainloop()


def clear_all():
    main_window.destroy()


main_window = Tk()
mywin = Main()
main_window.geometry("1090x700+200+15")
main_window.resizable(width=False, height=False)
main_window.title("KissCinema")
main_window.config(bg="black")
main_window.mainloop()
