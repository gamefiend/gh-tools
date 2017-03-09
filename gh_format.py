import subprocess
import platform
from colorama import init, Fore, Back, Style
from prettytable import PrettyTable
import os

# initialize colorama
init()

def stty_columns_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return columns

def print_header(header_text, character):
    print (str(header_text).center(int(stty_columns_size()), character))


def header_pound(header_text):
    print_header(header_text, '#')


def header_star(header_text):
    print_header(header_text, '*')


def header_line(header_text):
    print_header(header_text, '-')

def print_display(display_string):
    return (Fore.GREEN + Back.BLACK + Style.BRIGHT +
            display_string + Style.RESET_ALL)

def print_url(url_string):
    return (Fore.BLUE + Back.BLACK + Style.NORMAL +
            url_string + Style.RESET_ALL)

def print_msg(msg_string):
	return (Fore.RED + Back.CYAN + Style.DIM +
            (str(msg_string).center(int(stty_columns_size()), ' ')) + Style.RESET_ALL)

def print_title(title_string):
	return (Fore.BLUE + Back.WHITE + Style.BRIGHT +
            (str(title_string).center(int(stty_columns_size()), ' ')) + Style.RESET_ALL)

def clear():
	subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell = True)

