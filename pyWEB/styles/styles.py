from enum import Enum

import reflex as rx

from .colors import Color, TextColor
from .fonts import Font

# Constantes
MAX_WIDTH = "40%"

#sizes
class Size(Enum):
    ZERO = "0em"
    MIN = "0.2em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"

# Styles

BASE_STYLE = {
    "font_family" : Font.DEFAULT.value,
    "background_color" : Color.BACKGROUND.value,
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        "background_color" : Color.PRIMARY.value,
        "color" : TextColor.BODY.value,
        "white_space": "normal",
        "text_align" : "start"
    },
    rx.link: {
        "text_decoration" : "none",
        "_hover" : {}
    }
}

navbar_title_style = dict(
    font_family = Font.PIXEL.value,
    font_size = Size.LARGE.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color = TextColor.HEADER.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

title_style = dict(
    font_family = Font.TITLE.value,
    width = "100%",
    padding = Size.SMALL.value
)