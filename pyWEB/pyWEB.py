import reflex as rx

from pyWEB.components.footer import footer
from pyWEB.components.navbar import navbar
from pyWEB.views.header.header import header
from pyWEB.views.links.links import links


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )

app = rx.App()
app.add_page(index)
app.compile()