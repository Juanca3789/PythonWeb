import reflex as rx

import pyWEB.styles.styles as styles
from pyWEB.components.footer import footer
from pyWEB.components.navbar import navbar
from pyWEB.styles.styles import Size as Size
from pyWEB.views.header.header import header
from pyWEB.views.links.links import links


class State(rx.State):
    pass

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

app = rx.App(
    style= styles.BASE_STYLE
)
app.add_page(index)
app.compile()