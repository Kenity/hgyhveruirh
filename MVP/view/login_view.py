import customtkinter as ctk
from MVP.presenter.login_presenter import LoginPRESENTER
from CTkMessagebox import CTkMessagebox
from MVP.cogs.check_entry_on_errors import findErrors


class LoginVIEW(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.LoginPRESENTER = LoginPRESENTER(self)
        self.findErrors = findErrors(self)

        self.title("Вход в систему")
        self.geometry('300x150')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('resource/theme/breeze.json')

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2)

        self.username_label = ctk.CTkLabel(self, text = 'Логин:')
        self.username_label.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.username_entry.bind("<Button-1>", self.entry_username_click)

        self.password_label = ctk.CTkLabel(self, text = 'Пароль:')
        self.password_label.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.password_entry = ctk.CTkEntry(self, show = '*')
        self.password_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.password_entry.bind("<Button-1>", self.entry_password_click)

        self.login_button = ctk.CTkButton(self, text = 'Войти', command = self.login)
        self.login_button.grid(row = 2, column = 0, columnspan = 2, pady = 18)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.findErrors.check_login_entry(username):pass
        else: self.username_entry.configure(border_color = 'red')

        if self.findErrors.check_password_entry(password):pass
        else: self.password_entry.configure(border_color = 'red')


        if self.LoginPRESENTER.login(username, password):
            print("Вы успешно авторизовались!")

    def entry_username_click(self, event):
        print(self.username_entry._border_color)
        if self.username_entry._border_color == 'red':
            self.username_entry.configure(border_color = '#546063')

    def entry_password_click(self, event):
        if self.password_entry._border_color == 'red':
            self.password_entry.configure(border_color = '#546063')

    def show_message(self, message):
        CTkMessagebox(title = 'info', message = message)


