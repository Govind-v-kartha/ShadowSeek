from colorama import Fore, Style, init
from ..core.version import load_local_version


version, version_type = load_local_version()
init(autoreset=True)
C_RED = Fore.RED + Style.BRIGHT
C_CYAN = Fore.CYAN + Style.BRIGHT
C_GREEN = Fore.GREEN + Style.BRIGHT
C_WHITE = Fore.WHITE + Style.BRIGHT
C_YELLOW = Fore.YELLOW + Style.BRIGHT
C_MAGENTA = Fore.MAGENTA + Style.BRIGHT

BANNER_ASCII = (
    C_CYAN
    + "   _____ _                 _                     _    \n"
    + "  / ____| |               | |                   | |   \n"
    + " | (___ | |__   __ _  __| | _____      _____  ___| | __\n"
    + "  \\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / / __|/ _ \\ |/ /\n"
    + "  ____) | | | | (_| | (_| | (_) \\ V  V /\\__ \\  __/   < \n"
    + " |_____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/ |___/\\___|_|\\_\\ "
    + C_WHITE
    + f"Version: {version}\n"
    + "                                                       "
    + C_GREEN
    + "Creator: govind"
    + Style.RESET_ALL
)


def print_banner():
    print(BANNER_ASCII)


if __name__ == "__main__":
    print_banner()
