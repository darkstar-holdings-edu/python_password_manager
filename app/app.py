from tkinter import Tk, messagebox
import random
import string
import json

from .config import BACKGROUND_COLOR
from .logo import Logo
from .components import ActionButton, TextBox

APP_NAME = "Password Manager"
DATA_FILENAME = "data.json"

ALLOWED_CHARS = string.ascii_letters + string.punctuation
PASSWORD_SIZE = 22
NL = "\n"

PasswordData = dict[str, dict[str, str]]


class App(Tk):
    logo: Logo
    website_textbox: TextBox
    username_textbox: TextBox
    password_textbox: TextBox
    generate_button: ActionButton
    add_button: ActionButton
    search_button: ActionButton
    password_data: PasswordData

    def __init__(self) -> None:
        super().__init__()

        self.title(APP_NAME)
        self.config(padx=50, pady=50, background=BACKGROUND_COLOR)

        self.password_data = self.load_data()
        self._init_ui()

    def _init_ui(self) -> None:
        self.logo = Logo(
            grid_row=0,
            grid_column=0,
            grid_columnspan=3,
        )

        self.website_textbox = TextBox(
            label_text="Website:",
            label_grid_row=1,
            label_grid_column=0,
            box_width=23,
            box_grid_row=1,
            box_grid_column=1,
            box_grid_columnspan=1,
        )

        self.search_button = ActionButton(
            text="Search",
            width=12,
            grid_row=1,
            grid_column=2,
            event_handler=self.search_button_handler,
        )

        self.username_textbox = TextBox(
            label_text="Email/Username:",
            label_grid_row=2,
            label_grid_column=0,
            box_width=42,
            box_grid_row=2,
            box_grid_column=1,
            box_grid_columnspan=2,
        )

        self.password_textbox = TextBox(
            label_text="Password:",
            label_grid_row=3,
            label_grid_column=0,
            box_width=23,
            box_grid_row=3,
            box_grid_column=1,
        )

        self.generate_button = ActionButton(
            text="Generate Password",
            width=12,
            grid_row=3,
            grid_column=2,
            event_handler=self.generate_button_handler,
        )

        self.add_button = ActionButton(
            text="Add",
            width=35,
            grid_row=4,
            grid_column=1,
            grid_columnspan=2,
            event_handler=self.add_button_handler,
        )

        self.website_textbox.set_focus()

    def generate_button_handler(self) -> None:
        self.password_textbox.clear_text()

        password = "".join(random.choice(ALLOWED_CHARS) for _ in range(PASSWORD_SIZE))
        self.password_textbox.entry.insert(0, password)

        self.clipboard_clear()
        self.clipboard_append(password)

    def add_button_handler(self) -> None:
        if self.is_form_valid():
            self.save_form()

    def search_button_handler(self) -> None:
        website = self.website_textbox.get_text()

        try:
            data = self.password_data[website.lower()]
        except KeyError:
            messagebox.showerror(
                title="Not Found",
                message="There were no credentials found!",
            )

        else:
            messagebox.showinfo(
                title="Found Password",
                message=(
                    f"This website has the following credentials:\n\n"
                    f"Username: {data['username']}\n"
                    f"Password: {data['password']}\n"
                ),
            )

    def is_form_valid(self) -> bool:
        invalid_fields: list[str] = []

        if not len(self.website_textbox.get_text()):
            invalid_fields.append("Website")

        if not len(self.username_textbox.get_text()):
            invalid_fields.append("Email/Username")

        if not len(self.password_textbox.get_text()):
            invalid_fields.append("Password")

        if len(invalid_fields):
            messagebox.showerror(
                title="Invalid Fields",
                message=(
                    f"The following fields are not valid:\n\n"
                    f"{NL.join(invalid_fields)}"
                ),
            )

            self.website_textbox.set_focus()

            return False

        return True

    def load_data(self) -> PasswordData:
        try:
            with open("data.json", "r") as file:
                data: PasswordData = json.load(file)

        except (json.JSONDecodeError, FileNotFoundError):
            data = {}

        return data

    def save_form(self) -> None:
        website = self.website_textbox.get_text()
        username = self.username_textbox.get_text()
        password = self.password_textbox.get_text()

        entry: PasswordData = {
            website.lower(): {
                "username": username,
                "password": password,
            },
        }

        self.password_data.update(entry)

        with open("data.json", "w") as file:
            json.dump(self.password_data, file)

        self.clear_form()
        messagebox.showinfo(
            message="Your password has been saved successfully.",
            title="Save Successful",
        )

    def clear_form(self) -> None:
        self.website_textbox.clear_text()
        self.username_textbox.clear_text()
        self.password_textbox.clear_text()
