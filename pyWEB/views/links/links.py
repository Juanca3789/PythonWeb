import reflex as rx

from pyWEB.components.linkbutton import link_button
from pyWEB.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces"),
        link_button("Facebook",
                    "Cuenta personal",
                    "https://www.facebook.com/?locale=es_LA"),
        link_button("Instagram",
                    "@carlosC_3578",
                    "https://www.instagram.com/"),
        link_button("Twitter",
                    "@carlosC_3578",
                    "https://twitter.com/home?lang=es"),
        link_button("LinkedIn",
                    "Cuenta empleo",
                    "https://co.linkedin.com/"),
        width = "100%"
    )