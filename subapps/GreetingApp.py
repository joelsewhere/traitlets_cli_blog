from traitlets.config import Application
from traitlets import Unicode

aliases = {
    "greeting": "GreetingApp.greeting",
    "name": "GreetingApp.name",
    "punctuation": "GreetingApp.punctuation"
}

class GreetingApp(Application):

    # Traitlets specific variables
    # `name` and `description` can be used to autogenerate documentation
    name = "GreetingApp"
    description = """
    This app prints "Hello, World!" when activated.

    This app has the configuration arguments `--greeting`, `--name`, and `--punctuation.
    These arguments allow you to change the printed sentence.

    Example:

    COMMAND: python CLIApp.py greet --greeting=Hi there
    OUTPUT: "Hi there, World!"
    """

    # `alias` allows you to easily map command line arguments
    # to the configuration settings of the actual code.
    aliases = aliases

    # GreetingApp variables
    greeting = Unicode("Hello").tag(config=True)
    name = Unicode("World").tag(config=True)
    punctuation = Unicode("!").tag(config=True)

    def start(self):
        # Activate the `Application.start` method to parse
        # the command line
        super(GreetingApp, self).start()

        # Run GreetingApp code
        print(self.greeting + ", " + self.name + self.punctuation)