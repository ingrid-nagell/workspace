import tkinter as tk
from tkinter import StringVar, messagebox
from datetime import datetime
import csv
from matplotlib.pyplot import axis
import pandas as pd
from tabulate import tabulate

BG_COLOR = "#EBF0FA"
BUTTON_COLOR = '#BAC3D9'
PASSORD_PATH = 'C:\\Users\\G020772\\data\\bsf\\passord.txt'
TITTEL = "Registrer data"
FONT_TEXT = ('Trebuchet MS', 10)
FONT_NOTE = ('Trebuchet MS', 8)
LOGO_PATH = 'gjensidige_logo.png'
PATH = 'C:\\Users\\G020772\\data\\bsf\\bsf_tilbudsdata.csv'

###########################
'''
TO DO: Sjekk om data finnes fra før og hvis ja, overskriv
'''
###########################

class MainFrame(tk.Tk):
    """
    Klasse som bygger et tkinter Frame objekt, som igjen oppretter alle 
    sider i applikasjonen, sidekontroller, funksjonalitet, osv.
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Registrer data")
       # self.titlefont = tkfont.Font(familiy ='Verdana', size= 12)
        
        container = tk.Frame(bg='green')
        container.config(bg='green')
        container.grid(row=0, column=0, sticky='nsew')
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.bruker_id = tk.StringVar()

        self.frames = {}
        for p in {LoginPage, RegisterPage}:
            page_name = p.__name__
            frame = p(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[page_name] = frame
        
        self.up_frame('LoginPage')


    def up_frame(self, page_name):
        page = self.frames[page_name]
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
        user = user.upper()
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
        global PATH
        passord = self.get_passwords()
        user = self.bruker_id.get()
        if mnd != '' and aar != '' and ant != '':
            data_entry = [passord[user][1], user, aar, mnd, ant]
            if messagebox.askokcancel(title=TITTEL, message=f"Ønsker du å registrere følgende data for {user}?\n\nAntall: {ant}\nMåned: {mnd}\nÅr: {aar}"):
                with open(PATH, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data_entry)
                    # Sjekk om data for mnd + aar finnes fra før
                    # Hvis ja, skal overskrive?
        else:
            messagebox.showinfo(title=TITTEL, message=f"Data mangler.")


    def access_data(self):
        global PATH
        user = self.bruker_id.get().upper()
        try:
            df = pd.read_csv(PATH, header=None).rename(columns = {0:'id', 1:'user', 2:'år', 3:'måned', 4:'antall'})
        except:
            messagebox.showinfo(title=TITTEL, message="Ingen data er registrert på denne brukeren.")
        else:
            df = df[df['user'] == user]  ##Drop id col, sorter etter år, måned descending
            df = df.drop(['id', 'user'], axis=1).reset_index(drop=True)
            messagebox.showinfo(title=TITTEL, 
                            message=f"Det er registrert følgende tilbud for {user}:\n\n{tabulate(df, headers='keys', tablefmt='simple', showindex=False)}")


class LoginPage(tk.Frame):
    '''
    Klasse som bygger logg inn-siden, hvor brukeren logger inn med forhåndsregistrert brukernavn og passord.
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG_COLOR)
        self.controller = controller
        
        # --- Header msg ---
        title_lbl = tk.Label(self, text=f"Logg inn for å registrere tilbudsdata:", font=FONT_TEXT, bg=BG_COLOR)
        title_lbl.grid(row=0, column=1, columnspan=2, pady=15, padx=20)

        # --- User name entry ---
        user_lbl = tk.Label(self, text="Brukernavn: ", font=FONT_TEXT, bg=BG_COLOR)
        user_lbl.grid(row=1, column=1, sticky='e', padx=20)

        self.user_entry = tk.Entry(self, width=25, font=FONT_TEXT)
        self.user_entry.focus()
        self.user_entry.grid(row=1, column=2, columnspan=2)

        # --- Password entry ---
        pw_label = tk.Label(self, text="Passord: ", font=FONT_TEXT, bg=BG_COLOR)
        pw_label.grid(row=2, column=1, sticky='e', padx=20)

        self.pw_entry = tk.Entry(self, width=25, show="*", font=FONT_TEXT)
        self.pw_entry.grid(row=2, column=2, columnspan=2, padx=10)

        # --- Log in button
        login_button = tk.Button(self, text='Logg inn', font=FONT_TEXT, activebackground='white', 
                                cursor='hand2', bg=BUTTON_COLOR,
                                command=lambda: controller.check_password(self.user_entry.get(), self.pw_entry.get()))
        login_button.grid(row=3, column=1, columnspan=3, pady=15)
        
        # --- Information msg ---
        info_text = tk.Label(self, text="Ny bruker eller glemt passord.\nSend oss en epost <lenke>", 
                            font=FONT_NOTE, compound='center', bg=BG_COLOR)
        info_text.grid(row=4, column=1, columnspan=3)

        controller.bind('<Return>', lambda event: login_button.invoke())


class RegisterPage(tk.Frame):
    '''
    Klasse som bygger registreringssiden, hvor brukeren kan registrere tilbud og se sine lagrede data.
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG_COLOR)
        self.controller = controller

        # --- Header msg ---
        title_lbl = tk.Label(self, text=f"Her kan du registrere data:", font=FONT_TEXT, bg=BG_COLOR)
        title_lbl.grid(row=0, column=1, columnspan=3, pady=5)

        # --- Month entry --- 
        mnd_lbl = tk.Label(self, text="Måned: ", bg=BG_COLOR, font=FONT_TEXT)
        mnd_lbl.grid(row=1, column=2)
        
        self.mnd_entry = tk.StringVar(self)
        self.mnd_entry.set(datetime.now().month) # default value
        months = [m for m in range(1,13)]

        self.mnd_entry_menu = tk.OptionMenu(self, self.mnd_entry, *months) # Front of menu
        self.mnd_entry_menu.config(font=FONT_TEXT, bg='white', width=10)

        menu = self.nametowidget(self.mnd_entry_menu.menuname)  # Get menu widget.
        menu.config(font=FONT_TEXT, bg='white')  # Set the dropdown menu's font
        
        self.mnd_entry_menu.grid(row=2, column=2)

        # --- Year entry ---
        aar_lbl = tk.Label(self, text="År: ", bg=BG_COLOR, font=FONT_TEXT)
        aar_lbl.grid(row=1, column=3)

        self.aar_entry = tk.Entry(self, width=15, font=FONT_TEXT)
        self.aar_entry.insert('end', '2022')
        self.aar_entry.grid(row=2, column=3, padx=15, pady=15)

        # --- Tilbud entry ---
        tilb_lbl = tk.Label(self, text="Antall tilbud: ", bg=BG_COLOR, font=FONT_TEXT)
        tilb_lbl.grid(row=1, column=1)

        self.tilb_entry = tk.Entry(self, width=15, font=FONT_TEXT)
        self.tilb_entry.grid(row=2, column=1, padx=15, pady=15)
        self.tilb_entry.focus()

        # --- Save entry button ---
        save_button = tk.Button(self, text="Lagre", bg=BUTTON_COLOR, font=FONT_TEXT,
                                command= lambda: controller.save_data(
                                    self.mnd_entry.get(), 
                                    self.aar_entry.get(), 
                                    self.tilb_entry.get()
                                    ))
        save_button.grid(row=4, column=1, padx=15, pady=15)

        # --- View data button ---
        viewdata_button = tk.Button(self, text="Se registrerte data",  bg=BUTTON_COLOR, font=FONT_TEXT, command=lambda: controller.access_data())
        viewdata_button.grid(row=4, column=2, columnspan=3, pady=5)

    
if __name__ == '__main__':
    app = MainFrame()
    app.mainloop()