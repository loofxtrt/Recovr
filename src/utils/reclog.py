from rich.console import Console
from rich.text import Text
import re

console = Console()

def parse_styles(text, inherited_styles=None):
    if inherited_styles is None:
        inherited_styles = []

    result = Text()
    last_pos = 0

    pattern = re.compile(r"(b?)<((?:[^<>]|b<[^>]+>)+)>([a-zA-Z]*)")

    for m in pattern.finditer(text):
        start, end = m.span()

        if start > last_pos:
            segment = text[last_pos:start]
            style = " ".join(inherited_styles) if inherited_styles else ""
            result.append(segment, style=style)

        bold_flag    = (m.group(1) == "b")
        inner_raw    = m.group(2)
        suffix_style = m.group(3)

        combined = inherited_styles.copy()
        if bold_flag:
            combined.append("bold")
        if suffix_style:
            combined.append(suffix_style)

        inner_text = parse_styles(inner_raw, combined)
        result += inner_text

        last_pos = end

    if last_pos < len(text):
        tail = text[last_pos:]
        style = " ".join(inherited_styles) if inherited_styles else ""
        result.append(tail, style=style)

    return result

def info(label=None, message=None):
    log(category="info", label=label, message=message)

def log(category="info", label=None, message=None):
    category = category.upper()
    output = Text()

    # sempre ocupa 12 caracteres
    output.append(f"{category:<12}", style="default")

    label_text = Text()
    if label:
        label_text = parse_styles(label, inherited_styles=["green"])
        output += label_text

    # alinha a message para a coluna X (p.ex. 44)
    if message:
        col_target = 46
        current_width = len(f"{category:<12}") + label_text.cell_len
        padding = max(1, col_target - current_width)  # sempre pelo menos 1 espaço
        output.append(" " * padding)

        output += parse_styles(message)

    console.print(output)