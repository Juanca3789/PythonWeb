import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Carlos Clavijo",
            height = "40px"
        ),
        position = "sticky",
        bg = "blue",
        padding_x = "15px",
        padding_y = "10px",
        z_index = "999"
    )