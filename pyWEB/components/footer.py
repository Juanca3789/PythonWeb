import datetime

import reflex as rx

from pyWEB.styles.colors import TextColor
from pyWEB.styles.styles import Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.text(f"2005 - {datetime.date.today().year} Footer con ",
                rx.span(
                    rx.link("Enlace",
                            href= "http://localhost:3000"),
                            color=TextColor.FOOTER.value),
                font_size = Size.MEDIUM.value),
        margin_y=Size.MEDIUM.value
    )