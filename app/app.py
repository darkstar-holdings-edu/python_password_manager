from tkinter import Tk

from .config import BACKGROUND_COLOR

from .logo import Logo
from .components import ActionButton, TextBox

APP_NAME = "Password Manager"


class App(Tk):
    logo: Logo
    website_textbox: TextBox
    username_textbox: TextBox
    password_textbox: TextBox
    generate_button: ActionButton
    add_button: ActionButton

    def __init__(self) -> None:
        super().__init__()

        self.title(APP_NAME)
        self.config(padx=25, pady=25, background=BACKGROUND_COLOR)

        self._init_ui()

    def _init_ui(self):
        self.logo = Logo(
            grid_row=0,
            grid_column=0,
            grid_columnspan=3,
        )

        self.website_textbox = TextBox(
            label_text="Website:",
            label_grid_row=1,
            label_grid_column=0,
            box_width=42,
            box_grid_row=1,
            box_grid_column=1,
            box_grid_columnspan=2,
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

    def generate_button_handler(self):
        print("Generate Clicked!")

    def add_button_handler(self):
        print("Add Clicked!")
