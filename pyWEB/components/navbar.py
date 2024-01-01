import reflex as rx

from pyWEB.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Carlos Clavijo"
        ),
        position = "sticky",
        bg = "lightgray",
        padding_x = Size.DEFAULT.value,
        padding_y = Size.SMALL.value,
        top = "0",
        z_index = "999"
    )