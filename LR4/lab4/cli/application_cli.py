from __future__ import annotations
from typing import List, Tuple, Callable

import getopt
import sys

from lab4.cli.command_handler import CommandHandler
from lab4.cli.exceptions import ParsingEexception
from lab4.core.controller import Controller
from lab4.core.exceptions import *

class ApplicationCLI:

    _controller: Controller = None
    _handlers: List[CommandHandler] = None
    _root_handler: Callable[[None], None] = None


    def __init__(self, controller: Controller) -> None:
        self._handlers = list()
        self._controller = controller

    def start(self) -> None:
        '''
        Application startup.
        '''
        self.args = self._get_user_entered_agruments()

        if not self.args:
            if self._root_handler is not None:
                self._root_handler()

        for argument, value in self.args:
            for handler in self._handlers:
                if handler.is_expecting(argument):
                    try:
                        handler.handle(controller=self._controller,value=value)
                    except NoCardException:
                        print("Вставьте карту")
                        exit(0)
                    except NoPincodeException:
                        print("Введите пинкод")
                        exit(0)
                    except WrongCardException:
                        print("Карта не найдена")
                        exit(0)
                    except WrongPincodeException:
                        print("Пин код неверный")
                        exit(0)
                    except InsufficientFoundsException:
                        print("Для это операции у вас недостаточно средств")
                        exit(0)
                    except InputFormatException as err:
                        print(f"Ошибка ввода: {str(err)}")
                    except ParsingEexception as err:
                        print(f"Ошибка ввода: {str(err)}")
                    except PhoneFormatException as err:
                        print(f"Ошибка ввода: {str(err)}")
                        

    def _get_user_entered_agruments(self) -> List[Tuple[str, str]]:
        short_flags, long_flags = self._get_handlers_expected_flags()

        try:
            arguments, values = getopt.getopt(
                sys.argv[1:],
                short_flags,
                long_flags
            )

        except getopt.error as err:
            print(str(err))
            exit()

        return arguments

    def _get_handlers_expected_flags(self) -> Tuple[str, List[str]]:
        short_flags = list()
        long_flags = list()

        for handler in self._handlers:
            short, long = handler.get_expected_flags()
            short_flags.append(short)
            long_flags.append(long)

        # getopt accepts shorts flags as str, long flags as list
        return (''.join(short_flags), long_flags)

    def add_handler(self, handler: CommandHandler):
        '''
        Provides the application with a handler
        '''
        self._handlers.append(handler)

    def add_root_handler(self, root_handler: Callable[[None], None]) -> None:
        '''
        Called if there are no arguments from the user
        '''
        self._root_handler = root_handler
