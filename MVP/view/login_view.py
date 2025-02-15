import customtkinter as ctk
from MVP.presenter.login_presenter import LoginPRESENTER
from CTkMessagebox import CTkMessagebox


class LoginVIEW(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.LoginPRESENTER = LoginPRESENTER(self)

        self.title("Вход в систему")
        self.geometry('300x150')

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2)

        self.username_label = ctk.CTkLabel(self, text = 'Логин:')
        self.username_label.grid(row = 0, column = 0)

        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.grid(row = 0, column = 1)

        self.password_label = ctk.CTkLabel(self, text = 'Пароль:')
        self.password_label.grid(row = 1, column = 0)

        self.password_entry = ctk.CTkEntry(self, show = '*')
        self.password_entry.grid(row = 1, column = 1)

        self.login_button = ctk.CTkButton(self, text = 'Войти', command = self.login)
        self.login_button.grid(row = 2, column = 0, columnspan = 2, pady = 18)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.LoginPRESENTER.login(username, password):
            print("Вы успешно авторизовались!")

    def show_message(self, message):
        CTkMessagebox(title = 'info', message = message)


