from tkinter import Button
from typing import Callable

from ..config import BACKGROUND_COLOR


class ActionButton:
    button: Button

    def __init__(
        self,
        text: str,
        width: int,
        grid_row: int,
        grid_column: int,
        event_handler: Callable[[], None],
        grid_columnspan: int = 1,
    ) -> None:

        button = Button(
            text=text,
            width=width,
            command=event_handler,
            highlightbackground=BACKGROUND_COLOR,
            takefocus=0,
        )
        button.grid(
            row=grid_row,
            column=grid_column,
            columnspan=grid_columnspan,
        )

        self.button = button
