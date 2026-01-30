import os, time, sys, random
from colorama import Fore, Style, init

init() # Initialize Colorama for cross-platform ANSI escape code interpretation

def glitch_print(s, base_delay=0.0004):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(base_delay + random.uniform(-0.0003, 0.0008))
    print()

def mini_commandcraft_intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.003)
    
    art = [
"  ██████╗ ██████╗ ███╗   ███╗███╗   ███╗ █████╗ ███╗   ██╗██████╗   ██████╗ ██████╗  █████╗ ███████╗████████╗",
" ██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔══██╗████╗  ██║██╔══██╗ ██╔════╝ ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝",
" ██║     ██║   ██║██╔████╔██║██╔████╔██║███████║██╔██╗ ██║██   ██║ ██║      ██████╔╝███████║█████╗     ██║   ",
" ██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║ ██║      ██╔══██╗██╔══██║██╔══╝     ██║   ",
" ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║██████╔╝ ╚██████╗ ██║  ██║██║  ██║██║        ██║   ",
"  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   ",
    ]
    
    print(Fore.BLUE, end="") # Set color to blue for the art
    for line in art:
        glitch_print(line)
        time.sleep(0.007 if "COMMANDCRAFT" in line else 0.003)
    print(Style.RESET_ALL, end="") # Reset color after the art