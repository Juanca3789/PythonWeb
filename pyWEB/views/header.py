import reflex as rx

import pyWEB.styles.colors as cols
from pyWEB.components.link_icon import link_icon
from pyWEB.styles.fonts import Font
from pyWEB.styles.styles import Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                    fallback="C",
                    size="xl",
                    variant= "solid",
                    color_scheme= "orange"
            ),
            rx.vstack(
                rx.heading(
                    "@carlosc_3578",
                    size="xl",
                    font_family= Font.TITLE.value
                ),
                rx.text(
                    "WEB creada por Juan Carlos Clavijo",
                    font_size = Size.MEDIUM.value,
                    margin= "0px !important"
                ),
                rx.hstack(
                    link_icon("https://reflex.dev/", "icons/r-solid.svg"),
                    link_icon("https://chakra-ui.com/", "icons/bolt-solid.svg"),
                    spacing= Size.MEDIUM.value
                ),
                align_items="start",
                spacing= Size.MIN.value
            ),
            spacing= Size.MEDIUM.value
        ),
        rx.text(
            """Esta pagina web fue creada gracias al curso de python para
                web de @mouredev utilizando el framework Reflex""",
            font_size= Size.MEDIUM.value
        ),
        spacing= Size.MEDIUM.value,
        align_items="start"
    )