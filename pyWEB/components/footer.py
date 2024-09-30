import datetime

import reflex as rx

from pyWEB.styles.colors import TextColor
from pyWEB.styles.styles import Size


def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(src="favicon.ico"),
            rx.text(f"2005 - {datetime.date.today().year} Footer con ",
                    rx.text(
                        rx.link(
                            "Enlace",
                            href= "http://localhost:3000"
                        ),
                        color=TextColor.FOOTER.value,
                        as_= "span"
                    ),
                    font_size = Size.MEDIUM.value),
            margin_y=Size.MEDIUM.value,
            align= "center"
        )
    )