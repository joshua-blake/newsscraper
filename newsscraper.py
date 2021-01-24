from requests_html import HTMLSession
from tkinter import *
import webbrowser
root = Tk()
root.title("News Search")
root.config(bg="white")


session = HTMLSession()
r = session.get('https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en')
r.html.render(sleep=1)
articles = r.html.find("article")

search = Entry(root, bg="white", borderwidth=1, relief="solid", width=50)
search.grid(column=0, row=0)
search_icon = PhotoImage(file ="C:/Users/joshb/Future/python/search.png")
search_button = Button(root, image=search_icon, command=lambda: search_news(), bd = 0, bg="white")
search_button.grid(column=1, row=0, sticky="w")

current = Label(root, text="Current Stories", font=("Helvetica", 20), bg="white")
current.grid(column=0, pady=5, row=1, padx = 10)
news_frame = Frame(root, bg="white")
news_frame.grid()
initial_articles = []
for item in articles:
  try:
    news_item = item.find('h3', first=True)
    news_title = news_item.text
    news_link = news_item.absolute_links
    article={
      "link":news_link,
      "title":news_title
    }
    initial_articles.append(article)
  except:
    pass

buttons = [('btn'+str(t), t) for t in range(len(initial_articles))]
r = 0
for (b, t) in buttons:
  xtt = r
  rx = Button(news_frame, text=initial_articles[xtt]['title'], font="Helvetica", bg="white", borderwidth=1, relief="solid", command= lambda x=t: opener(initial_articles, x))
  rx.grid(column=0, sticky="w", pady=5, padx=5)
  r=r+1
print(len(buttons))
searched_articles = []
def search_news():
  query = search.get()
  finds = session.get(f"https://news.google.com/search?q={query}&hl=en-GB&gl=GB&ceid=GB%3Aen")
  finds.html.render(sleep=1)
  articles = finds.html.find("article")
  searched_articles = []
  for article in articles:
    try:
      article_item = article.find("h3", first=True)
      article_title = article_item.text
      article_link = article_item.absolute_links
      search_news = {
        'title': article_title,
        'link': article_link
      }
      searched_articles.append(search_news)
    except:
      pass
  for widget in news_frame.winfo_children():
    widget.destroy()
  searched_buttons = [('btn'+str(t), t) for t in range(len(initial_articles))]
  r = 0
  for (b, t) in searched_buttons:
    xtt = r
    rx = Button(news_frame, text=searched_articles[xtt]['title'], font="Helvetica", bg="white", borderwidth=1, relief="solid", command= lambda x=t: opener(searched_articles, x))
    rx.grid(column=0, sticky="w", pady=5, padx=5)
    r=r+1
  print(searched_articles)

def opener(lister, linkse):
  link = lister[linkse]['link']
  final_link = str(link)[2:-2]
  webbrowser.open_new(final_link)


root.mainloop()