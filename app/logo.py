from tkinter import Canvas, PhotoImage

from .config import BACKGROUND_COLOR


class Logo:
    canvas: Canvas
    background: PhotoImage

    def __init__(
        self,
        grid_row: int,
        grid_column: int,
        grid_columnspan: int,
    ) -> None:
        canvas = Canvas(
            width=200,
            height=200,
            background=BACKGROUND_COLOR,
            highlightthickness=0,
        )

        self.background = PhotoImage(file="assets/logo.png")
        canvas.create_image(100, 100, image=self.background)

        canvas.grid(
            row=grid_row,
            column=grid_column,
            columnspan=grid_columnspan,
        )

        self.canvas = canvas
