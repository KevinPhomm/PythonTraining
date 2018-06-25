import urllib.request
from html.parser import HTMLParser

content = urllib.request.urlopen("https://www.google.fr/").read()

class MyParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs).get("href"))


p = MyParser()

p.feed(str(content))
print(p.links)
