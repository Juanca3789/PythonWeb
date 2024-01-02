import reflex as rx

import pyWEB.styles.styles as styles
from pyWEB.styles.styles import Size


def link_button(title: str, body: str,  url: str, img: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=img,
                    width = Size.DEFAULT.value,
                    height = Size.DEFAULT.value,
                    margin_left= Size.SMALL.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style,
                            margin_top= "0px !important"),
                    align_items= "start"
                ),
                spacing= Size.MEDIUM.value
            )
        ),
        href= url,
        is_external= True,
        width= "100%"
    )