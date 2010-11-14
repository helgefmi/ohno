import re

class Senses:
    parse_messages = re.compile(' \s+')
    def __init__(self, ohno):
        self.ohno = ohno
    
    def update(self):
        """
        1. Read from the client
        2. Gather messages and press space and goto 1. if we get
           a "--More--" message
        3. TODO: handle menus
        4. Update Hero (stats, position, dlvl, etc)
        5. Update the dungeon (current level)
        6. TODO: Send out signals for the messages, such that various submodules
                 can listen to them and act accordingly.
        """
        self.ohno.logger.senses('Updating senses..')

        messages = ''
        while True:
            data = self.ohno.client.receive()
            self.ohno.framebuffer.feed(data)

            messages += self.ohno.framebuffer.get_topline()

            if '--More--' in messages:
                # double space so we can split on it later
                messages = messages.replace('--More--', '  ')
                # There's more messages in store for us!
                self.ohno.client.send(' ')
            else:
                break

        messages = Senses.parse_messages.split(messages.strip(' '))
        self.ohno.logger.senses('All messages: ' + \
                                ', '.join(map(repr, messages)))

        self.ohno.hero.update()
        self.ohno.dungeon.update()
