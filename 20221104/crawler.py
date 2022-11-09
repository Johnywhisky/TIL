from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The JohnyWhisky's Blog</title></head>
<body><p class="title"><b>The JohnyWhisky's Story</b></p>
<p class="story">Once upon a time there were three little sisters;
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story"> ... </p>
"""

soup = BeautifulSoup(html_doc, "html.parser")

print(soup.prettify())  #
print("title : ", soup.title.text)
print(soup.find("p", "story").text)
