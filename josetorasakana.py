from tkinter import *
from PIL import ImageTk, Image
import data


def JoseMovie():
    windows = Toplevel()
    windows.geometry("540x690+475+20")
    windows.resizable(width=False, height=False)
    windows.title("Jose to Tora to Sakana-tachi")
    windows.config(bg="black")
    windows.grab_set()

    # header
    frame_header = Frame(windows)
    frame_header.grid(row=0, column=0, sticky="nsew")
    frame_header.configure(background="black")

    banner = Image.open("AI-chan.png")
    banner_size = banner.resize((400, 100), Image.LANCZOS)
    img0 = ImageTk.PhotoImage(banner_size)
    lbl0 = Button(frame_header, image=img0, bg="black", activebackground="black", bd=0, command=windows.destroy)
    lbl0.configure(state="active", relief=SUNKEN)
    lbl0.grid(row=0, column=0, columnspan=2, pady=5)

    line = Label(frame_header, text=f"{data.Movies[0]}", bg="#1FBB28", fg="white")
    line.grid(row=1, column=0, pady=2, ipadx=203)

    # body
    frame_body = Frame(windows)
    frame_body.grid(row=1, column=0, sticky="nsew")
    frame_body.configure(background="black")

    movie_image = Image.open("Jose.jpg")
    movie_size = movie_image.resize((210, 297), Image.LANCZOS)
    img1 = ImageTk.PhotoImage(movie_size)
    lbl1 = Label(frame_body, image=img1, bd=0, bg="black")
    lbl1.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)

    lbl2 = Label(frame_body, text="Synopsis:", font=("", 10), bg="black", fg="white")
    lbl2.grid(row=2, column=0, sticky="nw", ipady=15, padx=15)
    lbl3 = Label(frame_body,
                 text="Tsuneo is a university student, and Josee is a young girl who has rarely gone out of the\n"
                      "house by herself due to her being unable to walk. The two meet when Tsuneo finds Josee's\n"
                      "grandmother taking her out for a morning walk.", justify="center", bg="black", fg="white")
    lbl3.grid(row=3, column=0, columnspan=2, sticky="s", ipady=10, padx=25)

    lbl4 = Label(frame_body, text="Alternative Title: Jose, the Tiger and the Fish\n\n"
                                  "Aired: December 25, 2020\n\n"
                                  "Studio: Bones\n\n"
                                  "Source: Novel\n\n"
                                  "Genres: Drama, Romance\n\n"
                                  "Duration 1hr. 38 min.\n\n"
                                  "Rating: PG-13", justify="left", bg="black", fg="white")
    lbl4.grid(row=1, column=1, sticky="w")

    lbl5 = Button(frame_body, text="Back", width=8, font=("California FB", 10), bg="grey",
                  activebackground="grey", fg="white", activeforeground="white", bd=0,
                  command=windows.destroy)
    lbl5.grid(row=4, column=0, columnspan=2, sticky="s", padx=25, pady=40)

    windows.mainloop()
