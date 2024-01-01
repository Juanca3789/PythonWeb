from enum import Enum

import reflex as rx

# Constantes
MAX_WIDTH = "60%"

#sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"

# Styles

BASE_STYLE = {
    rx.Button: {
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value
    },
    rx.Link: {
        "text_decoration" : "none",
        "_hover" : {}
    }
}

button_title_style = dict(
    font_size = Size.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

title_style = dict(
    size="lg",
    width = "100%",
    padding = Size.SMALL.value
)