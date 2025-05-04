from rich.console import Console
from rich.text import Text
import re

console = Console()

default_message = "default"
default_style = "default"

def info(arg1, arg2=None):
    log(category="info", pos1=arg1, pos2=arg2)

def log(category="info", pos1="default", pos2=None):
    text = Text()

    category = category.upper() # capitalizar a string da categoria
    text.append(f"{category:<12}") # adicionar a categoria no início do log com x espaços de distância da próxima palavra

    def resolve(arg):
        if isinstance(arg, tuple):
            return arg[0], arg[1]
        elif isinstance(arg, str):
            return arg, default_style

    msg1, style1 = resolve(pos1)
    text.append(msg1, style=style1)

    if pos2 is not None:
        msg2, style2 = resolve(pos2)
        text.append(" ")
        text.append(msg2, style=style2)

    console.print(text)
