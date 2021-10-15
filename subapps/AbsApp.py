from traitlets.config import Application
from traitlets import Bool, observe, Unicode
import os, sys

flags = {
    'size': (
        {'AbsApp' : {'size' : True}},
        "Print the file size for a file.."
    ),
}

class AbsApp(Application):

    flags = flags
    size = Bool(config=True)

    def start(self):
        super(AbsApp, self).start()

        file = self.extra_args[0]
        if not os.path.isfile(file):
            raise ValueError('The provided path does not point to a valid file.')

        print(os.path.abspath(file))
        
        if self.size:
            print('File size:', os.path.getsize(file), "bytes")

        

        