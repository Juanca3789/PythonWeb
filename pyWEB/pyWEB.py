import reflex as rx


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.text("Hola Mundo", color = "blue")

app = rx.App()
app.add_page(index)
app.compile()