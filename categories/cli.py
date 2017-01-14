"""
categories
Usage:
  categories rebuild
  categories render <category_id>
"""

from docopt import docopt
from inspect import getmembers, isclass


def main():
    import categories.commands
    options = docopt(__doc__)
    for (k, v) in options.items():
        if hasattr(categories.commands, k) and v:
            module = getattr(categories.commands, k)
            categories.commands = getmembers(module, isclass)
            command = [command[1] for command in categories.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
