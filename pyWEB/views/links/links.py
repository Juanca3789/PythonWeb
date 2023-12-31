import reflex as rx

from pyWEB.components.linkbutton import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button("Facebook", "https://www.facebook.com/?locale=es_LA"),
        link_button("Instagram", "https://www.instagram.com/"),
        link_button("Twitter", "https://twitter.com/home?lang=es"),
        link_button("LinkedIn", "https://co.linkedin.com/")
    )