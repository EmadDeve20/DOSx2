from termcolor import colored

class FontColors:
    """
        List of Colors to print message
    """
    red = lambda text: colored(text, "red")
    blue = lambda text: colored(text, "blue")
    green = lambda text: colored(text, "green")
    yellow = lambda text: colored(text, "yellow")
