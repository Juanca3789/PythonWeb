import reflex as rx

import pyWEB.styles.styles as styles
from pyWEB.components.footer import footer
from pyWEB.components.navbar import navbar
from pyWEB.styles.styles import Size as Size
from pyWEB.views.header import header
from pyWEB.views.links import links


@rx.page(title= "WEB Reflex")
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width = "100%",
                margin_y = Size.BIG.value
            )
        ),
        footer()
    )