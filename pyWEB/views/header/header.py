import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Carlos Clavijo", size="xl"),
        rx.text("@carlosc_3578"),
        rx.text("WEB creada por Juan Carlos Clavijo"),
        rx.text("""Esta pagina web fue creada gracias al curso de python para
                web de @mouredev utilizando el framework Reflex""")
    )