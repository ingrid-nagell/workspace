import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

BG_COLOR = "lightgray"
PASSORD_PATH = 'passord.txt'
TITTEL = "Registrer data"
FONT_TEXT = ('Trebuchet MS', 10)
FONT_NOTE = ('Trebuchet MS', 8)
LOGO_PATH = 'gjensidige_logo.png'

###########################

class MainFrame(tk.Tk):
    """
    frame objct holding all the different 
    pages, control of pages, functions, etc.
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Registrer data")
        self.geometry("400x400")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)
        self.config(padx=20)
       # self.option_add('*Dialog.msg.font', 'Helvetica 12')
       # self.titlefont = tkfont.Font(familiy ='Verdana', size= 12)
        
        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew')

        self.bruker_id = tk.StringVar()

        self.listing = {}

        for p in {LoginPage, RegisterPage}:
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.listing[page_name] = frame
        
        self.up_frame('LoginPage')
        
    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()

    def get_passwords(self):
        global PASSORD_PATH
        with open(PASSORD_PATH) as f:
            passord = {}
            for line in f:
                user, pw, part = line.split()
                passord[user] = [pw, part]
        return passord
    
    def check_password(self, user, password):
        passord = self.get_passwords()
        if user in passord:
            if password == passord[user][0]:
                self.bruker_id.set(user)
                self.up_frame('RegisterPage')
            else:
                messagebox.showinfo(title=TITTEL, message="Feil passord.")
        else:
            messagebox.showinfo(title=TITTEL, message="Skriv inn gyldig brukernavn.")
            
    def save_data(self, mnd, aar, ant):
        if mnd != '' and aar != '' and ant != '':
            if messagebox.askokcancel(title=TITTEL, message=f"Ønsker du å registrere følgende data for {self.bruker_id.get()}?\n{mnd} {aar} {ant}?"):
                print("HEY")
                #clear entry box for antall tilbud
                # Sjekk om fil finnes fra før:
                    #lag en ny fil med bsf_reg_<partref>
                    # Sjekk om data for mnd + aar finnes fra før
                    # Hvis ja, skal overskrive?
                    # Hvis ikke, lagre data til .csv
        else:
            messagebox.showinfo(title=TITTEL, message="Mangler data")


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        logo_img = Image.open(LOGO_PATH)
        logo_img_rez = logo_img.resize((100,40), Image.ANTIALIAS)
        logo_img_v2 = ImageTk.PhotoImage(logo_img_rez)

        canvas = tk.Canvas(width=60, height=30, highlightthickness=0, bg='white')
        canvas.grid(row=0, column=1)
        canvas_image = canvas.create_image(60, 30, image=logo_img_v2)


        #logo_img_lbl = tk.Label(self, i=logo_img, bg='white', compound='center')#, font=(FONT_NAME, 20, 'bold'))
        #logo_img_lbl.grid(row=0, column=0)

       # title_lbl = tk.Label(self, text=f"Her kan du logge inn:", font=FONT_TEXT)
       # title_lbl.grid(row=0, column=1, columnspan=3, pady=5)

        user_lbl = tk.Label(self, text="Brukernavn: ", font=FONT_TEXT)
        user_lbl.grid(row=1, column=1, columnspan=1)

        self.user_entry = tk.Entry(self)
        self.user_entry.grid(row=1, column=2, columnspan=2)

        pw_label = tk.Label(self, text="Passord: ", font=FONT_TEXT)
        pw_label.grid(row=2, column=1, columnspan=1)

        self.pw_entry = tk.Entry(self)
        self.pw_entry.grid(row=2, column=2, columnspan=2)

        login_button = tk.Button(self, text='Logg inn', font=FONT_TEXT, activebackground='white', cursor='hand2', command=lambda: controller.check_password(self.user_entry.get(), self.pw_entry.get()))
        login_button.grid(row=3, column=2, columnspan=2, pady=15)
        
        pw_text = tk.Label(self, text="Ny bruker eller glemt passord.\nSend oss en epost <lenke>", font=FONT_NOTE, compound='center')
        pw_text.grid(row=4, column=2, columnspan=2)



class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_lbl = tk.Label(self, text=f"Her kan du registrere data:")
        title_lbl.grid(row=0, column=1, columnspan=3, pady=5)

        mnd_lbl = tk.Label(self, text="Måned: ")
        mnd_lbl.grid(row=1, column=1)

        self.mnd_entry = tk.Entry(self)
        self.mnd_entry.grid(row=2, column=1)

        aar_lbl = tk.Label(self, text="År: ")
        aar_lbl.grid(row=1, column=2)

        self.aar_entry = tk.Entry(self)
        self.aar_entry.grid(row=2, column=2)

        tilb_lbl = tk.Label(self, text="Antall tilbud: ")
        tilb_lbl.grid(row=1, column=3)

        self.tilb_entry = tk.Entry(self, )
        self.tilb_entry.grid(row=2, column=3)

        login_button = tk.Button(self, text="Lagre", command= lambda: controller.save_data(self.mnd_entry.get(), self.aar_entry.get(), self.tilb_entry.get()))
        login_button.grid(row=4, column=1, pady=5)

        viewdata_button = tk.Button(self, text="Se registrerte data")
        viewdata_button.grid(row=4, column=2, pady=5)

        quit_button = tk.Button(self, text="Avslutt")
        quit_button.grid(row=4, column=3, pady=5)


if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()