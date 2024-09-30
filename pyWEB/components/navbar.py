import reflex as rx

import pyWEB.styles.styles as Styles
from pyWEB.styles.colors import Color, TextColor
from pyWEB.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "REFLEX ",
            rx.text(
                "APP",
                color = TextColor.FOOTER.value,
                as_= "span"
            ),
            color= TextColor.HEADER.value,
            style=Styles.navbar_title_style
        ),
        position = "sticky",
        bg = Color.SECONDARY.value,
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        top = "0",
        z_index = "999"
    )