from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     data = file.read()
#
# soup = BeautifulSoup(data,"html.parser")
# h1 = soup.find("h3",class_="heading")
# print(soup.select("p a"))

list_of_test = []

response = requests.get("https://news.ycombinator.com/news")
yc_news = response.text
soup = BeautifulSoup(yc_news, "html.parser")
article_title = soup.title
headings = soup.findAll(name="span", class_="titleline")
article_tlist = []
article_llist = []
print("1")
for heading in headings:
    article_tag = heading.find("a")
    # for article_tag in article_tags:
    article_text = article_tag.getText()
    article_tlist.append(article_text)
    article_link = article_tag.get("href")
    article_llist.append(article_link)

score_tag = soup.findAll(name="span", class_="score")
scores = [int(score.text.split()[0]) for score in score_tag]
print(scores)

index = scores.index(max(scores))
print(article_llist[index])
print(article_tlist[index])


# print(article_tag)
# print(article_text)
# print(article_link)
# for heading in headings:
#     title = heading.getText()
#     print(title)
# #     list_of_test.append((title))
# # print(list_of_test)
# <span class="titleline"><a href="http://paulgraham.com/vb.html">Life Is Short (2016)</a><span class="sitebit comhead">
# (<a href="from?site=paulgraham.com"><span class="sitestr">paulgraham.com</span></a>)</span></span>
