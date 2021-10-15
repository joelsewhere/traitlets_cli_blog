from traitlets.config import Application
from textwrap import dedent
from subapps import (GreetingApp,
                     AbsApp,
                     )

class CLIapp(Application):

    name = 'cli'

    subcommands = dict(
        greet=(GreetingApp,
        dedent("""
        Prints a greeting!  
        """).strip()
    ),
    abs=(
        AbsApp,
        dedent("""
        Print the current working directory.
        """)

    ))

    def start(self) -> None:
        # check: is there a subapp given?
        if self.subapp is None:
            print("No command given (run with --help for options). List of subcommands:\n")
            self.print_subcommands()

        # This starts subapps
        super(CLIapp, self).start()

def main():
    CLIapp.launch_instance()

if __name__ == '__main__':
    main()