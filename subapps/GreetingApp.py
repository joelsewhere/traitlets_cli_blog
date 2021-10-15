from traitlets.config import Application
from traitlets import Unicode

aliases = {
    'greeting': 'GreetingApp.greeting',
    'name': 'GreetingApp.name',
    'punctuation': 'GreetingApp.punctuation'
}


class GreetingApp(Application):

    greeting = Unicode('Hello').tag(config=True)
    name = Unicode('World').tag(config=True)
    punctuation = Unicode('!').tag(config=True)


    aliases = aliases

    def start(self):
        super(GreetingApp, self).start()
        print(self.greeting + ', ' + self.name + self.punctuation)