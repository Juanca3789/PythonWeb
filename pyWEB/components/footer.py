import datetime

import reflex as rx


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(f"2005 - {datetime.date.today().year} Footer con ", 
                rx.span(
                    rx.link("Enlace",
                            href= "http://localhost:3000")))
    )