from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.MESSAGES = []
        self.inP = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'p':
            self.inP = True

    def handle_endtag(self, tag):
        if tag.lower() == 'p':
            self.inP = False

    def handle_data(self, data):
        if self.inP == True:
            self.MESSAGES.append(data)
