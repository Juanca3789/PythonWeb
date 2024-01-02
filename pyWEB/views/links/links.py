import reflex as rx

from pyWEB.components.linkbutton import link_button
from pyWEB.components.title import title
from pyWEB.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
        title("Enlaces"),
        link_button("Facebook",
                    "Cuenta personal",
                    "https://www.facebook.com/?locale=es_LA",
                    "icons/facebook.svg"),
        link_button("Instagram",
                    "@carlosC_3578",
                    "https://www.instagram.com/",
                    "icons/instagram.svg"),
        link_button("Twitter",
                    "@carlosC_3578",
                    "https://twitter.com/home?lang=es",
                    "icons/twitter.svg"),
        link_button("LinkedIn",
                    "Cuenta empleo",
                    "https://co.linkedin.com/",
                    "icons/linkedin.svg"),
        width = "100%"
    )