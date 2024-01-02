import reflex as rx

import pyWEB.styles.styles as styles
from pyWEB.styles.styles import Size


def link_icon(url: str, img: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=img
        ),
        is_external= True,
        href= url
    )