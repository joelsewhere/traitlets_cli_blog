from traitlets.config import Application
from subapps import (GreetingApp,
                     AbsApp,
                     )

class CLIapp(Application):

    name = 'cli'

    subcommands = dict(

    greet=(
        GreetingApp,
        """
        Prints a greeting!  
        """.strip()
        ),
    abs=(
        AbsApp,
        """
        Print the current working directory.
        """
        ), # New commands are added here
    )

    def start(self) -> None:
        # check: is there a subapp given?
        if self.subapp is None:
            print("No command given (run with --help for options). List of subcommands:\n")
            self.print_subcommands()

        # This starts subapps
        super(CLIapp, self).start()

def main():
    # This is where the command line is parsed
    # https://github.com/ipython/traitlets/blob/f24879c16059b34b89c3fe5cb34cf72001fa9b18/traitlets/config/application.py#L839
    CLIapp.launch_instance()

if __name__ == '__main__':
    main()