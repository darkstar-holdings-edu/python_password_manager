from tkinter import END, Entry, Label

from ..config import (
    BACKGROUND_COLOR,
    BOX_FONT,
    BUTTON_HIGHLIGHT_BACKGROUND,
    BUTTON_HIGHLIGHT_COLOR,
    FONT_COLOR,
    LABEL_FONT,
)


class TextBox:
    label: Label
    entry: Entry

    def __init__(
        self,
        label_text: str,
        label_grid_row: int,
        label_grid_column: int,
        box_width: int,
        box_grid_row: int,
        box_grid_column: int,
        label_grid_columnspan: int = 1,
        box_grid_columnspan: int = 1,
    ) -> None:
        super().__init__()

        label = Label(
            text=label_text,
            background=BACKGROUND_COLOR,
            foreground=FONT_COLOR,
            font=LABEL_FONT,
            pady=5,
            justify="right",
        )

        entry = Entry(
            width=box_width,
            background=BACKGROUND_COLOR,
            font=BOX_FONT,
            foreground=FONT_COLOR,
            highlightthickness=1,
            highlightbackground=BUTTON_HIGHLIGHT_BACKGROUND,
            highlightcolor=BUTTON_HIGHLIGHT_COLOR,
        )

        label.grid(
            row=label_grid_row,
            column=label_grid_column,
            columnspan=label_grid_columnspan,
        )
        entry.grid(
            row=box_grid_row,
            column=box_grid_column,
            columnspan=box_grid_columnspan,
        )

        self.label = label
        self.entry = entry

    def set_focus(self) -> None:
        self.entry.focus()

    def get_text(self) -> str:
        return self.entry.get()

    def clear_text(self) -> None:
        return self.entry.delete(0, END)
