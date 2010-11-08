import re

class Senses:
    parse_messages = re.compile(' \s+')
    def __init__(self, ohno):
        self.ohno = ohno
    
    def update(self):
        self.ohno.logger.senses('Updating senses..')

        messages = ''
        while True:
            data = self.ohno.client.receive()
            self.ohno.framebuffer.feed(data)

            messages += self.ohno.framebuffer.get_topline()

            if '--More--' in messages:
                messages = messages.replace('--More--', '  ')
                self.ohno.client.send(' ')
            else:
                break

        messages = Senses.parse_messages.split(messages.strip(' '))
        self.ohno.logger.senses('All messages: ' + ', '.join(map(repr, messages)))

        self.ohno.hero.update()
        self.ohno.dungeon.update()
