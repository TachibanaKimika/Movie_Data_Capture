import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class Logger:
    def __init__(self):
        self.prefixes = {
            'debug': Fore.BLUE   + 'DEBUG' + Fore.RESET,
            'info': Fore.GREEN   + 'INFO' + Fore.RESET,
            'warn': Fore.YELLOW  + 'WARN' + Fore.RESET,
            'error': Fore.RED    + 'ERROR' + Fore.RESET,
            'success': Fore.CYAN + 'SUCCESS' + Fore.RESET
        }

    def _log(self, level, *args):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{self.prefixes[level]}] {timestamp}', *args)

    def info(self, *args):
        self._log('info', *args)

    def warn(self, *args):
        self._log('warn', *args)

    def error(self, *args):
        self._log('error', *args)

    def success(self, *args):
        self._log('success', *args)

    def debug(self, *args):
        self._log('debug', *args)

logger = Logger()
