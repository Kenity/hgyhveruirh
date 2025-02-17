from MVP.cogs.config import errors
import re


class findErrors:
    def __init__(self, login_view):
        self.login_view = login_view

    def check_login_entry(self, text):
        special_chars = re.escape("!,@,#,$,%,^,&,*,(,),+,=,`,~,\",',<,>,?,/,[,],{,},,,")
        pattern = f"[{special_chars}]"

        if text == "" or text == " ":
            self.login_view.show_message(errors[0])
            return False

        elif ' ' in text:
            self.login_view.show_message(errors[1])
            return False

        elif re.search(r'[а-яА-ЯёЁ]', text):
            self.login_view.show_message(errors[2])
            return False

        elif re.search(pattern, text):
            self.login_view.show_message(errors[3])
            return False

        else: return True

    def check_password_entry(self, text):
        special_chars = re.escape("!,@,#,$,%,^,&,*,(,),+,=,`,~,\",',<,>,?,/,[,],{,},,,")
        pattern = f"[{special_chars}]"

        if text == "" or text == " ":
            self.login_view.show_message(errors[4])
            return False

        elif ' ' in text:
            self.login_view.show_message(errors[5])
            return False

        elif re.search(r'[а-яА-ЯёЁ]', text):
            self.login_view.show_message(errors[6])
            return False

        elif re.search(pattern, text):
            self.login_view.show_message(errors[7])
            return False

        else: return True