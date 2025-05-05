from rich.console import Console
from rich.text import Text

console = Console()

default_message = "default"
default_style = "default"

def info(arg1, arg2=None):
    log(category="info", pos1=arg1, pos2=arg2)

def log(category="info", pos1=default_message, pos2=None):
    """
    cria uma mensagem de log
    os argumentos dessa função podem ser passados só como uma string pura: reclog.info("mensagem")
    ou como uma tupla contendo a string da mensagem e a segunda string definindo o estilo: reclog.info(("mensagem", "green bold"))
    o segundo argumento da posição 2 é opcional
    """

    # criar o objeto de texto do rich
    text = Text()

    # categoria
    category = category.upper() # capitalizar a string da categoria
    text.append(f"{category:<12}") # adicionar a categoria no início do log com x espaços de distância da próxima palavra

    # definir se o arg 1 foi passado como uma string pura (só a mensagem)
    # ou se foi passado como uma tupla
    # caso ele não seja uma tupla, retornar o primeiro valor (a mensagem) e usar o estilo padrão
    def resolve(arg):
        if isinstance(arg, tuple):
            return arg[0], arg[1]
        elif isinstance(arg, str):
            return arg, default_style

    msg1, style1 = resolve(pos1)
    text.append(msg1, style=style1)

    # caso o argumento 2 tenha sido passado, também fazer a mesma verificação nele
    if pos2 is not None:
        msg2, style2 = resolve(pos2)
        text.append(" ") # espaço entre o arg1 e o arg2
        text.append(msg2, style=style2)

    console.print(text)
