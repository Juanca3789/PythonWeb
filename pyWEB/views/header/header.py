import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Joe Biden", size="xl"),
    )