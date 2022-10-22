from cgitb import html
from bs4 import BeautifulSoup

import requests

r = requests.get('https://gitlab.gnome.org/GNOME?sort=stars_desc')

# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)

html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

with open("output.html", "w") as f:
    f.write(html_doc)

